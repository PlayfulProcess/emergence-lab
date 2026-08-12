"""
Cultural Resilience ABM v2 — Recalibrated
==========================================
Fixed: extraction/regeneration balance, population dynamics, adaptation rates
"""

import numpy as np
import json

np.random.seed(42)

class CulturalGroup:
    def __init__(self, gid, extraction, cooperation, adaptability, innovation, pop=100):
        self.gid = gid
        self.extraction = np.clip(extraction, 0.05, 0.95)
        self.cooperation = np.clip(cooperation, 0.0, 0.95)
        self.adaptability = np.clip(adaptability, 0.0, 1.0)
        self.innovation = np.clip(innovation, 0.0, 0.2)
        self.pop = pop
        self.alive = True
    
    def step(self, resource_health, protocol=None):
        """Execute one step: extract, contribute, grow, adapt."""
        if not self.alive:
            return 0, 0
        
        # Apply protocol constraints
        eff_extraction = self.extraction
        eff_cooperation = self.cooperation
        if protocol:
            eff_extraction = min(eff_extraction, protocol.get('max_extraction', 1.0))
            eff_cooperation = max(eff_cooperation, protocol.get('min_cooperation', 0.0))
        
        # Extraction scales with population but is moderated by resource health
        # (harder to extract when resources are scarce)
        extract_per_capita = eff_extraction * 0.1 * resource_health
        total_extracted = extract_per_capita * self.pop
        
        # Contribute back
        total_contributed = total_extracted * eff_cooperation
        
        # Net consumption
        net_consumed = total_extracted - total_contributed
        
        # Population growth: logistic, based on per-capita net harvest
        per_cap = net_consumed / max(self.pop, 1)
        # Need a minimum per-capita to sustain; above that, grow; below, shrink
        carrying = 200 * per_cap / 0.05 if per_cap > 0 else 0
        growth_rate = 0.03 * (1 - self.pop / max(carrying, 1)) if carrying > 10 else -0.02
        growth_rate = np.clip(growth_rate, -0.05, 0.04)
        
        self.pop = self.pop * (1 + growth_rate)
        
        if self.pop < 3:
            self.alive = False
            self.pop = 0
        
        # Adapt: if resources are low, reduce extraction (if adaptable)
        if np.random.random() < self.adaptability * 0.05:
            if resource_health < 0.3:
                self.extraction *= (1 - self.adaptability * 0.08)
                self.cooperation = min(0.95, self.cooperation + self.adaptability * 0.03)
            elif resource_health > 0.7:
                self.extraction *= (1 + 0.01)  # slight drift toward more extraction in good times
        
        # Innovate
        if np.random.random() < self.innovation:
            self.extraction = np.clip(self.extraction + np.random.normal(0, 0.015), 0.05, 0.95)
            self.cooperation = np.clip(self.cooperation + np.random.normal(0, 0.015), 0.0, 0.95)
        
        return total_extracted, total_contributed


class World:
    def __init__(self, groups, capacity=5000, regen=0.06, protocol=None, volatility=0.1):
        self.groups = groups
        self.capacity = capacity
        self.resource = capacity * 0.8
        self.regen = regen
        self.protocol = protocol
        self.volatility = volatility
        self.t = 0
        self.history = []
    
    @property
    def health(self):
        return self.resource / self.capacity
    
    def shannon_diversity(self):
        alive = [g for g in self.groups if g.alive]
        if len(alive) <= 1:
            return 0
        total = sum(g.pop for g in alive)
        if total == 0:
            return 0
        props = [g.pop / total for g in alive]
        return -sum(p * np.log(p + 1e-12) for p in props if p > 0)
    
    def step(self):
        self.t += 1
        
        # Environmental shocks
        if np.random.random() < self.volatility * 0.12:
            shock = np.random.beta(2, 5) * 0.4
            self.resource *= (1 - shock)
        # Rare catastrophe
        if np.random.random() < 0.003:
            self.resource *= (1 - np.random.uniform(0.25, 0.55))
        
        alive = [g for g in self.groups if g.alive]
        
        total_extracted = 0
        total_contributed = 0
        
        for g in alive:
            ext, cont = g.step(self.health, self.protocol)
            total_extracted += ext
            total_contributed += cont
        
        # Remove extracted, add contributed
        self.resource = max(0, self.resource - total_extracted + total_contributed)
        
        # Regeneration (logistic)
        regen = self.regen * self.resource * (1 - self.resource / self.capacity)
        self.resource = min(self.capacity, max(0, self.resource + regen))
        
        alive = [g for g in self.groups if g.alive]
        self.history.append({
            'resource': self.health,
            'population': sum(g.pop for g in alive),
            'n_cultures': len(alive),
            'diversity': self.shannon_diversity(),
            'avg_extract': np.mean([g.extraction for g in alive]) if alive else 0,
            'avg_coop': np.mean([g.cooperation for g in alive]) if alive else 0,
        })
    
    def run(self, steps=1500):
        for _ in range(steps):
            self.step()
        return self.history


# ============================================================
# SCENARIOS
# ============================================================

def make_monoculture(vol=0.1):
    """Few groups, all high-extraction, low-cooperation, low-adaptability."""
    groups = [
        CulturalGroup(i, 
                       extraction=0.7 + np.random.normal(0, 0.03),
                       cooperation=0.08 + np.random.normal(0, 0.02),
                       adaptability=0.15,
                       innovation=0.02,
                       pop=160)
        for i in range(3)
    ]
    return World(groups, protocol=None, volatility=vol)


def make_pure_diversity(vol=0.1):
    """Many groups with varied strategies, no shared protocol."""
    groups = [
        CulturalGroup(i,
                       extraction=np.random.uniform(0.15, 0.75),
                       cooperation=np.random.uniform(0.05, 0.55),
                       adaptability=np.random.uniform(0.1, 0.7),
                       innovation=np.random.uniform(0.01, 0.12),
                       pop=40)
        for i in range(12)
    ]
    return World(groups, protocol=None, volatility=vol)


def make_protocol_diversity(vol=0.1):
    """Many diverse groups with thin shared protocol (Ostrom-style)."""
    groups = [
        CulturalGroup(i,
                       extraction=np.random.uniform(0.15, 0.75),
                       cooperation=np.random.uniform(0.05, 0.55),
                       adaptability=np.random.uniform(0.1, 0.7),
                       innovation=np.random.uniform(0.01, 0.12),
                       pop=40)
        for i in range(12)
    ]
    protocol = {
        'max_extraction': 0.45,  # Ceiling on extraction
        'min_cooperation': 0.15, # Floor on contribution back
    }
    return World(groups, protocol=protocol, volatility=vol)


# ============================================================
# RUN
# ============================================================

STEPS = 1500
N_TRIALS = 40

scenarios = {
    'Monoculture': make_monoculture,
    'Pure Diversity': make_pure_diversity,
    'Protocol + Diversity': make_protocol_diversity,
}

volatilities = {
    'low': 0.05,
    'high': 0.25,
    'extreme': 0.5,
}

all_results = {}

for vol_name, vol in volatilities.items():
    print(f"\n{'='*50}")
    print(f"  VOLATILITY: {vol_name.upper()} ({vol})")
    print(f"{'='*50}")
    
    all_results[vol_name] = {}
    
    for sc_name, builder in scenarios.items():
        print(f"  Running {sc_name} ({N_TRIALS} trials)...")
        
        all_histories = []
        for trial in range(N_TRIALS):
            np.random.seed(trial * 137 + 7)
            world = builder(vol=vol)
            hist = world.run(STEPS)
            all_histories.append(hist)
        
        # Aggregate
        keys = ['resource', 'population', 'n_cultures', 'diversity']
        agg = {}
        for key in keys:
            matrix = np.array([[h[key] for h in trial_hist] for trial_hist in all_histories])
            agg[key] = {
                'mean': matrix.mean(axis=0),
                'q25': np.percentile(matrix, 25, axis=0),
                'q75': np.percentile(matrix, 75, axis=0),
            }
        
        # Final state
        final_res = [trial[-1]['resource'] for trial in all_histories]
        final_pop = [trial[-1]['population'] for trial in all_histories]
        final_cul = [trial[-1]['n_cultures'] for trial in all_histories]
        final_div = [trial[-1]['diversity'] for trial in all_histories]
        
        agg['final'] = {
            'resource': f"{np.mean(final_res):.3f} ± {np.std(final_res):.3f}",
            'population': f"{np.mean(final_pop):.0f} ± {np.std(final_pop):.0f}",
            'cultures': f"{np.mean(final_cul):.1f} ± {np.std(final_cul):.1f}",
            'collapse_pct': f"{np.mean([1 if r < 0.05 else 0 for r in final_res])*100:.0f}%",
            'resource_val': float(np.mean(final_res)),
            'pop_val': float(np.mean(final_pop)),
            'cultures_val': float(np.mean(final_cul)),
            'collapse_val': float(np.mean([1 if r < 0.05 else 0 for r in final_res])),
        }
        
        all_results[vol_name][sc_name] = agg
        
        f = agg['final']
        print(f"    Resource: {f['resource']}  |  Pop: {f['population']}  |  "
              f"Cultures: {f['cultures']}  |  Collapse: {f['collapse_pct']}")


# ============================================================
# PRINT SUMMARY TABLE
# ============================================================

print("\n\n" + "=" * 80)
print("COMPLETE RESULTS TABLE")
print("=" * 80)

for vol_name in volatilities:
    print(f"\n  {vol_name.upper()} VOLATILITY:")
    print(f"  {'Scenario':<25} {'Resource':>12} {'Population':>14} {'Cultures':>12} {'Collapse':>10}")
    print(f"  {'-'*73}")
    for sc_name in scenarios:
        f = all_results[vol_name][sc_name]['final']
        print(f"  {sc_name:<25} {f['resource']:>12} {f['population']:>14} "
              f"{f['cultures']:>12} {f['collapse_pct']:>10}")


# ============================================================
# SAVE FOR VISUALIZATION
# ============================================================

def ds(arr, factor=5):
    """Downsample array."""
    return arr[::factor].tolist()

viz = {}
for vol_name in volatilities:
    viz[vol_name] = {}
    for sc_name in scenarios:
        d = all_results[vol_name][sc_name]
        viz[vol_name][sc_name] = {
            'resource_mean': ds(d['resource']['mean']),
            'resource_q25': ds(d['resource']['q25']),
            'resource_q75': ds(d['resource']['q75']),
            'pop_mean': ds(d['population']['mean']),
            'pop_q25': ds(d['population']['q25']),
            'pop_q75': ds(d['population']['q75']),
            'diversity_mean': ds(d['diversity']['mean']),
            'cultures_mean': ds(d['n_cultures']['mean']),
            'final': d['final'],
        }

with open('/home/claude/abm_viz.json', 'w') as f:
    json.dump(viz, f)

print("\nVisualization data saved.")
