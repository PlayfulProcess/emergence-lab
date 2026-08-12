"""
Model A v4: Group-Level Competition Under Environmental Perturbation
=====================================================================
Instead of strategies competing WITHIN a group (where competitive
exclusion dominates), we model GROUPS competing with each other,
where groups differ in their internal cultural diversity.

This directly implements cultural group selection (Boyd & Richerson)
and tests the Tilman insurance hypothesis at the group level.

Design:
- 20 groups, each with a shared commons
- Groups have 1, 3, 6, or 12 internal cultural strategies  
- Environment fluctuates; different strategies match different conditions
- Group output = sum of strategy outputs (niche-weighted)
- Groups with higher output grow; lower output groups shrink
- Periodically, successful groups "bud" and failing groups die

The question: do diverse groups outperform monoculture groups
across varying environmental volatility?
"""

import numpy as np
import json

# ============================================================
# STRATEGIES: each has an environmental optimum
# ============================================================

# 12 strategies spanning the environmental niche space [0,1]
STRAT_OPTIMA = [0.08, 0.17, 0.25, 0.33, 0.42, 0.50, 0.58, 0.67, 0.75, 0.83, 0.92, 0.50]
STRAT_WIDTHS = [0.15, 0.18, 0.15, 0.12, 0.15, 0.20, 0.15, 0.18, 0.15, 0.12, 0.15, 0.30]
STRAT_EXTRACTIONS = [0.3, 0.35, 0.25, 0.4, 0.45, 0.5, 0.55, 0.5, 0.35, 0.4, 0.3, 0.65]
STRAT_COOPERATIONS = [0.4, 0.25, 0.45, 0.35, 0.3, 0.35, 0.25, 0.3, 0.4, 0.45, 0.2, 0.1]
STRAT_NAMES = ['Arctic','Desert','Forest','Wetland','Temperate','Mediter',
               'River','Coastal','Tropical','Highland','Steppe','Industrial']


def niche_fitness(strat_idx, env_state):
    """How well does this strategy match the current environment?"""
    opt = STRAT_OPTIMA[strat_idx]
    w = STRAT_WIDTHS[strat_idx]
    return np.exp(-((env_state - opt)**2) / (2 * w**2))


class Group:
    """A cultural group with internal strategy diversity."""
    
    def __init__(self, strategy_indices, resource=100, protocol=None):
        self.strats = list(strategy_indices)
        self.n_strats = len(self.strats)
        # Equal internal allocation
        self.weights = np.ones(self.n_strats) / self.n_strats
        self.resource = resource
        self.capacity = 100
        self.protocol = protocol
        self.alive = True
        self.output_history = []
    
    def produce(self, env_state):
        """
        Group output = sum of strategy contributions.
        Each strategy contributes proportional to its niche match
        and its resource extraction, weighted by group allocation.
        
        This is the Tilman mechanism: diverse groups have higher average
        output because some strategy always matches the current conditions.
        """
        if not self.alive or self.resource < 1:
            self.alive = False
            return 0
        
        total_output = 0
        total_extraction = 0
        total_contribution = 0
        res_health = self.resource / self.capacity
        
        for j, si in enumerate(self.strats):
            nf = niche_fitness(si, env_state)
            ext = STRAT_EXTRACTIONS[si]
            coop = STRAT_COOPERATIONS[si]
            
            if self.protocol:
                ext = min(ext, self.protocol.get('max_ext', 1.0))
                coop = max(coop, self.protocol.get('min_coop', 0.0))
            
            # Strategy output: niche_match * extraction * resource_availability
            output = nf * ext * res_health * self.weights[j]
            total_output += output
            
            extraction = output
            contribution = extraction * coop
            total_extraction += extraction
            total_contribution += contribution
        
        # Update group resource
        net_drain = (total_extraction - total_contribution) * self.capacity * 0.05
        self.resource = max(0, self.resource - net_drain)
        
        # Regeneration
        r = 0.08 * self.resource * (1 - self.resource / self.capacity)
        self.resource = min(self.capacity, self.resource + r)
        
        if self.resource < 1:
            self.alive = False
        
        self.output_history.append(total_output)
        return total_output
    
    def diversity(self):
        if self.n_strats <= 1:
            return 0
        return float(-np.sum(self.weights * np.log(self.weights + 1e-12)))
    
    @property
    def recent_output(self):
        if len(self.output_history) < 10:
            return np.mean(self.output_history) if self.output_history else 0
        return np.mean(self.output_history[-50:])


def run_competition(n_mono, n_low, n_high, n_proto, env_vol, steps=3000, protocol=None):
    """
    Run group competition.
    Groups are assigned different diversity levels.
    Environment fluctuates. Groups produce output.
    Every 100 steps: weakest group dies, strongest group buds.
    """
    groups = []
    labels = []
    
    # Monoculture groups (single strategy, chosen to be the generalist)
    for _ in range(n_mono):
        si = np.random.choice(12)  # random single strategy
        groups.append(Group([si]))
        labels.append('mono')
    
    # Low diversity (3 strategies)
    for _ in range(n_low):
        sis = sorted(np.random.choice(12, 3, replace=False))
        groups.append(Group(sis))
        labels.append('low')
    
    # High diversity (6 strategies)
    for _ in range(n_high):
        sis = sorted(np.random.choice(12, 6, replace=False))
        groups.append(Group(sis))
        labels.append('high')
    
    # Protocol + high diversity (6 strategies with constraints)
    proto = {'max_ext': 0.45, 'min_coop': 0.15}
    for _ in range(n_proto):
        sis = sorted(np.random.choice(12, 6, replace=False))
        groups.append(Group(sis, protocol=proto))
        labels.append('proto')
    
    N = len(groups)
    env_state = 0.5
    
    history = {
        'env': [],
        'mono_res': [], 'low_res': [], 'high_res': [], 'proto_res': [],
        'mono_count': [], 'low_count': [], 'high_count': [], 'proto_count': [],
        'mono_output': [], 'low_output': [], 'high_output': [], 'proto_output': [],
    }
    
    for t in range(steps):
        # Environment fluctuation (random walk)
        env_state += np.random.normal(0, env_vol)
        env_state = np.clip(env_state, 0, 1)
        
        # Occasional larger shift
        if np.random.random() < 0.008:
            env_state += np.random.normal(0, 0.2)
            env_state = np.clip(env_state, 0, 1)
        
        # Rare extreme event
        if np.random.random() < 0.003:
            env_state = np.random.uniform(0, 1)
            for g in groups:
                if g.alive:
                    g.resource *= 0.7
        
        # All groups produce
        outputs = []
        for g in groups:
            if g.alive:
                outputs.append(g.produce(env_state))
            else:
                outputs.append(0)
        
        # Group selection every 100 steps
        if t > 0 and t % 100 == 0:
            alive_indices = [i for i in range(N) if groups[i].alive]
            if len(alive_indices) >= 2:
                # Find weakest and strongest
                recent = [(i, groups[i].recent_output) for i in alive_indices]
                recent.sort(key=lambda x: x[1])
                
                weakest_idx = recent[0][0]
                strongest_idx = recent[-1][0]
                
                # Weakest dies, replaced by copy of strongest
                groups[weakest_idx].alive = False
                new_group = Group(
                    groups[strongest_idx].strats[:],
                    resource=80,
                    protocol=groups[strongest_idx].protocol
                )
                groups[weakest_idx] = new_group
                labels[weakest_idx] = labels[strongest_idx]
        
        # Record
        history['env'].append(env_state)
        
        for label_name in ['mono', 'low', 'high', 'proto']:
            idxs = [i for i in range(N) if labels[i] == label_name and groups[i].alive]
            if idxs:
                history[f'{label_name}_res'].append(np.mean([groups[i].resource / groups[i].capacity for i in idxs]))
                history[f'{label_name}_output'].append(np.mean([outputs[i] for i in idxs]))
            else:
                history[f'{label_name}_res'].append(0)
                history[f'{label_name}_output'].append(0)
            history[f'{label_name}_count'].append(len(idxs))
    
    return history, labels


# ============================================================
# EXPERIMENTS
# ============================================================

VOLS = {'stable': 0.01, 'moderate': 0.03, 'volatile': 0.06, 'crisis': 0.10}
TRIALS = 40
STEPS = 3000

print("=" * 70)
print("MODEL A v4: Group Competition with Cultural Diversity")
print(f"  {TRIALS} trials × {STEPS} steps × {len(VOLS)} volatilities")
print(f"  20 groups: 5 mono, 5 low-div, 5 high-div, 5 protocol+div")
print("=" * 70)

ALL = {}

for vn, vol in VOLS.items():
    print(f"\n  {vn.upper()} (vol={vol}):")
    ALL[vn] = {}
    
    # Track final group type counts across trials
    final_counts = {'mono': [], 'low': [], 'high': [], 'proto': []}
    final_resources = {'mono': [], 'low': [], 'high': [], 'proto': []}
    final_outputs = {'mono': [], 'low': [], 'high': [], 'proto': []}
    
    all_ts = {'mono_res': [], 'low_res': [], 'high_res': [], 'proto_res': [],
              'mono_count': [], 'low_count': [], 'high_count': [], 'proto_count': []}
    
    for trial in range(TRIALS):
        np.random.seed(trial * 71 + 3)
        hist, labels = run_competition(5, 5, 5, 5, vol, STEPS)
        
        for lt in ['mono', 'low', 'high', 'proto']:
            final_counts[lt].append(hist[f'{lt}_count'][-1])
            final_resources[lt].append(hist[f'{lt}_res'][-1])
            final_outputs[lt].append(hist[f'{lt}_output'][-1])
            all_ts[f'{lt}_res'].append(hist[f'{lt}_res'])
            all_ts[f'{lt}_count'].append(hist[f'{lt}_count'])
    
    ds = 10
    for lt in ['mono', 'low', 'high', 'proto']:
        arr_res = np.array(all_ts[f'{lt}_res'])
        arr_cnt = np.array(all_ts[f'{lt}_count'], dtype=float)
        
        ALL[vn][lt] = {
            'count_mean': float(np.mean(final_counts[lt])),
            'count_std': float(np.std(final_counts[lt])),
            'res_mean': float(np.mean(final_resources[lt])),
            'output_mean': float(np.mean(final_outputs[lt])),
            'survived_pct': float(np.mean([1 if c > 0 else 0 for c in final_counts[lt]])) * 100,
            'ts_res': arr_res.mean(axis=0)[::ds].tolist(),
            'ts_count': arr_cnt.mean(axis=0)[::ds].tolist(),
        }
    
    # Print
    print(f"    {'Type':<15} {'Final Count':>12} {'Resources':>12} {'Output':>12} {'Survived':>10}")
    print(f"    {'-'*61}")
    for lt in ['mono', 'low', 'high', 'proto']:
        d = ALL[vn][lt]
        print(f"    {lt:<15} {d['count_mean']:>10.1f}±{d['count_std']:.1f} "
              f"{d['res_mean']:>11.3f} {d['output_mean']:>11.4f} {d['survived_pct']:>9.0f}%")
    
    # Who dominates?
    counts = {lt: ALL[vn][lt]['count_mean'] for lt in ['mono','low','high','proto']}
    dominant = max(counts, key=counts.get)
    total = sum(counts.values())
    print(f"    → {dominant.upper()} dominates with {counts[dominant]/total*100:.0f}% of groups")


# ============================================================
# SUMMARY TABLE
# ============================================================

print("\n\n" + "=" * 80)
print("FINAL GROUP COUNT BY TYPE (out of 20 groups)")
print("Started: 5 mono, 5 low-div, 5 high-div, 5 protocol+div")
print("Cultural group selection: weakest group replaced by copy of strongest every 100 steps")
print("=" * 80)

print(f"\n{'Volatility':<12}", end="")
for lt in ['mono', 'low', 'high', 'proto']:
    print(f" {lt:>10}", end="")
print(f" {'dominant':>12}")
print("-" * 70)

for vn in VOLS:
    print(f"{vn:<12}", end="")
    best_lt = ''
    best_val = 0
    for lt in ['mono', 'low', 'high', 'proto']:
        v = ALL[vn][lt]['count_mean']
        print(f" {v:>10.1f}", end="")
        if v > best_val:
            best_val = v
            best_lt = lt
    print(f" {best_lt:>12}")


# ============================================================
# SAVE
# ============================================================

with open('/home/claude/model_a_v4.json', 'w') as f:
    json.dump(ALL, f)

print("\nResults saved.")
