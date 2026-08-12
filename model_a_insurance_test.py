"""
Model A v5: Clean Insurance Hypothesis Test
=============================================
Direct analogue of Tilman's Cedar Creek biodiversity experiments.

Design:
- Each "plot" is a group with a fixed set of cultural strategies
- Environment fluctuates via random walk + shocks
- No group selection — just track how each plot performs over time
- Measure: mean output, output variance, minimum output, time stressed

This directly tests Yachi & Loreau's insurance hypothesis:
diversity reduces variance without proportionally reducing mean.
"""

import numpy as np
import json

# 12 strategies with different environmental optima
OPTIMA =      [0.08, 0.17, 0.25, 0.33, 0.42, 0.50, 0.58, 0.67, 0.75, 0.83, 0.92, 0.50]
WIDTHS =      [0.15, 0.18, 0.15, 0.12, 0.15, 0.20, 0.15, 0.18, 0.15, 0.12, 0.15, 0.25]
EXTRACTIONS = [0.30, 0.35, 0.25, 0.40, 0.45, 0.40, 0.45, 0.40, 0.35, 0.40, 0.30, 0.60]
COOPS =       [0.40, 0.25, 0.45, 0.35, 0.30, 0.30, 0.25, 0.30, 0.40, 0.45, 0.35, 0.10]
NAMES =       ['Arctic','Desert','Forest','Wetland','Temper','Mediter',
               'River','Coastal','Tropic','Highland','Steppe','Industrial']


def group_output(strategy_indices, env_state, protocol=None):
    """
    Total output of a group given current environment.
    Each strategy contributes proportional to its niche match.
    
    This IS the Tilman mechanism: in a diverse group, some strategy
    always matches the current conditions reasonably well.
    In a monoculture, if conditions shift away from the optimum,
    output drops dramatically.
    """
    total = 0
    n = len(strategy_indices)
    for si in strategy_indices:
        niche_match = np.exp(-((env_state - OPTIMA[si])**2) / (2 * WIDTHS[si]**2))
        ext = EXTRACTIONS[si]
        coop = COOPS[si]
        if protocol:
            ext = min(ext, protocol.get('max_ext', 1.0))
            coop = max(coop, protocol.get('min_coop', 0.0))
        
        # Output = niche_match * net_extraction / n_strategies
        # Divided by n because resources/attention are split across strategies
        output = niche_match * ext * (1 - coop) / n
        total += output
    return total


def group_extraction_pressure(strategy_indices, env_state, protocol=None):
    """How much extraction pressure does this group put on commons?"""
    total = 0
    n = len(strategy_indices)
    for si in strategy_indices:
        niche_match = np.exp(-((env_state - OPTIMA[si])**2) / (2 * WIDTHS[si]**2))
        ext = EXTRACTIONS[si]
        coop = COOPS[si]
        if protocol:
            ext = min(ext, protocol.get('max_ext', 1.0))
            coop = max(coop, protocol.get('min_coop', 0.0))
        total += niche_match * ext * (1 - coop) / n
    return total


def run_plot(strategy_indices, env_series, protocol=None):
    """
    Run a single "plot" (group) through an environmental time series.
    Track output, resource health.
    """
    resource = 75  # start at 75% of capacity=100
    capacity = 100
    outputs = []
    resources = []
    
    for env in env_series:
        # Group produces
        out = group_output(strategy_indices, env, protocol)
        
        # Scale by resource availability
        res_health = resource / capacity
        actual_out = out * res_health
        outputs.append(actual_out)
        
        # Resource drain
        drain = group_extraction_pressure(strategy_indices, env, protocol) * res_health * capacity * 0.03
        resource = max(0, resource - drain)
        
        # Regeneration
        r = 0.06 * resource * (1 - resource / capacity)
        resource = min(capacity, resource + r)
        
        resources.append(resource / capacity)
    
    return np.array(outputs), np.array(resources)


def generate_environment(steps, volatility, seed=None):
    """Generate an environmental time series."""
    if seed is not None:
        np.random.seed(seed)
    
    env = np.zeros(steps)
    env[0] = 0.5
    
    for t in range(1, steps):
        # Random walk
        env[t] = env[t-1] + np.random.normal(0, volatility)
        
        # Mean reversion (weak)
        env[t] += 0.002 * (0.5 - env[t-1])
        
        # Occasional larger shift
        if np.random.random() < 0.005:
            env[t] += np.random.normal(0, 0.15)
        
        # Rare extreme
        if np.random.random() < 0.002:
            env[t] = np.random.uniform(0, 1)
        
        env[t] = np.clip(env[t], 0, 1)
    
    return env


# ============================================================
# EXPERIMENTAL CONDITIONS
# ============================================================

def make_monoculture_plots(n_plots):
    """Each plot has a single strategy (different ones)."""
    plots = []
    for i in range(n_plots):
        si = i % 12  # cycle through strategies
        plots.append(([si], f'mono_{NAMES[si]}'))
    return plots

def make_diverse_plots(n_strats, n_plots):
    """Each plot has n_strats randomly chosen strategies."""
    plots = []
    for i in range(n_plots):
        np.random.seed(i * 37 + n_strats)
        sis = sorted(np.random.choice(12, n_strats, replace=False).tolist())
        plots.append((sis, f'div{n_strats}_{i}'))
    return plots

def make_protocol_plots(n_strats, n_plots):
    """Diverse plots with protocol."""
    plots = []
    for i in range(n_plots):
        np.random.seed(i * 37 + n_strats)
        sis = sorted(np.random.choice(12, n_strats, replace=False).tolist())
        plots.append((sis, f'proto{n_strats}_{i}'))
    return plots


# ============================================================
# RUN
# ============================================================

VOLS = {'stable': 0.01, 'moderate': 0.03, 'volatile': 0.06, 'crisis': 0.10}
STEPS = 2000
N_ENVS = 20  # number of independent environmental realizations
N_PLOTS_PER_TYPE = 10

PROTOCOL = {'max_ext': 0.45, 'min_coop': 0.15}

print("=" * 70)
print("MODEL A v5: Clean Insurance Hypothesis Test")
print(f"  {N_ENVS} environments × {N_PLOTS_PER_TYPE} plots/type × {STEPS} steps")
print("  Directly analogous to Tilman's Cedar Creek design")
print("=" * 70)

RESULTS = {}

for vn, vol in VOLS.items():
    print(f"\n  {vn.upper()} (volatility={vol}):")
    
    RESULTS[vn] = {}
    
    type_metrics = {
        'Mono (1)': {'outputs': [], 'resources': [], 'variances': [], 'mins': []},
        'Low (3)': {'outputs': [], 'resources': [], 'variances': [], 'mins': []},
        'Med (6)': {'outputs': [], 'resources': [], 'variances': [], 'mins': []},
        'High (12)': {'outputs': [], 'resources': [], 'variances': [], 'mins': []},
        'Proto (6)': {'outputs': [], 'resources': [], 'variances': [], 'mins': []},
    }
    
    # For time series
    type_ts = {k: [] for k in type_metrics}
    type_res_ts = {k: [] for k in type_metrics}
    
    for env_seed in range(N_ENVS):
        env = generate_environment(STEPS, vol, seed=env_seed * 13 + 7)
        
        # Monoculture plots
        mono_plots = make_monoculture_plots(N_PLOTS_PER_TYPE)
        for strats, name in mono_plots:
            out, res = run_plot(strats, env)
            type_metrics['Mono (1)']['outputs'].append(out.mean())
            type_metrics['Mono (1)']['variances'].append(out.var())
            type_metrics['Mono (1)']['mins'].append(out.min())
            type_metrics['Mono (1)']['resources'].append(res.mean())
            type_ts['Mono (1)'].append(out)
            type_res_ts['Mono (1)'].append(res)
        
        # Low diversity (3)
        for strats, name in make_diverse_plots(3, N_PLOTS_PER_TYPE):
            out, res = run_plot(strats, env)
            type_metrics['Low (3)']['outputs'].append(out.mean())
            type_metrics['Low (3)']['variances'].append(out.var())
            type_metrics['Low (3)']['mins'].append(out.min())
            type_metrics['Low (3)']['resources'].append(res.mean())
            type_ts['Low (3)'].append(out)
            type_res_ts['Low (3)'].append(res)
        
        # Medium diversity (6)
        for strats, name in make_diverse_plots(6, N_PLOTS_PER_TYPE):
            out, res = run_plot(strats, env)
            type_metrics['Med (6)']['outputs'].append(out.mean())
            type_metrics['Med (6)']['variances'].append(out.var())
            type_metrics['Med (6)']['mins'].append(out.min())
            type_metrics['Med (6)']['resources'].append(res.mean())
            type_ts['Med (6)'].append(out)
            type_res_ts['Med (6)'].append(res)
        
        # High diversity (all 12)
        for _ in range(N_PLOTS_PER_TYPE):
            out, res = run_plot(list(range(12)), env)
            type_metrics['High (12)']['outputs'].append(out.mean())
            type_metrics['High (12)']['variances'].append(out.var())
            type_metrics['High (12)']['mins'].append(out.min())
            type_metrics['High (12)']['resources'].append(res.mean())
            type_ts['High (12)'].append(out)
            type_res_ts['High (12)'].append(res)
        
        # Protocol + diversity
        for strats, name in make_diverse_plots(6, N_PLOTS_PER_TYPE):
            out, res = run_plot(strats, env, protocol=PROTOCOL)
            type_metrics['Proto (6)']['outputs'].append(out.mean())
            type_metrics['Proto (6)']['variances'].append(out.var())
            type_metrics['Proto (6)']['mins'].append(out.min())
            type_metrics['Proto (6)']['resources'].append(res.mean())
            type_ts['Proto (6)'].append(out)
            type_res_ts['Proto (6)'].append(res)
    
    # Summarize
    print(f"    {'Type':<12} {'Mean Out':>10} {'Variance':>12} {'Min Out':>10} "
          f"{'Resources':>10} {'CV':>8}")
    print(f"    {'-'*62}")
    
    for tname in type_metrics:
        m = type_metrics[tname]
        mean_out = np.mean(m['outputs'])
        mean_var = np.mean(m['variances'])
        mean_min = np.mean(m['mins'])
        mean_res = np.mean(m['resources'])
        # Coefficient of variation across plots
        cv = np.std(m['outputs']) / (mean_out + 1e-10)
        
        print(f"    {tname:<12} {mean_out:>10.5f} {mean_var:>12.7f} {mean_min:>10.6f} "
              f"{mean_res:>10.4f} {cv:>8.3f}")
        
        # Downsample time series
        ds = 20
        ts_arr = np.array(type_ts[tname])
        res_arr = np.array(type_res_ts[tname])
        
        RESULTS[vn][tname] = {
            'mean_output': float(mean_out),
            'mean_variance': float(mean_var),
            'mean_min': float(mean_min),
            'mean_resource': float(mean_res),
            'cv': float(cv),
            'ts_out_mean': ts_arr.mean(axis=0)[::ds].tolist(),
            'ts_res_mean': res_arr.mean(axis=0)[::ds].tolist(),
        }
    
    # Insurance effect
    mono_var = np.mean(type_metrics['Mono (1)']['variances'])
    for tname in ['Low (3)', 'Med (6)', 'High (12)', 'Proto (6)']:
        div_var = np.mean(type_metrics[tname]['variances'])
        reduction = (1 - div_var / (mono_var + 1e-12)) * 100
        RESULTS[vn][tname]['var_reduction_vs_mono'] = float(reduction)
    
    print(f"\n    Insurance effect (variance reduction vs monoculture):")
    for tname in ['Low (3)', 'Med (6)', 'High (12)', 'Proto (6)']:
        r = RESULTS[vn][tname].get('var_reduction_vs_mono', 0)
        print(f"      {tname}: {r:+.1f}%")


# ============================================================
# SUMMARY
# ============================================================

print("\n\n" + "=" * 80)
print("INSURANCE HYPOTHESIS RESULTS")
print("Does diversity reduce output variance? (Tilman analogue)")
print("=" * 80)

print(f"\n{'Vol':<10} {'Metric':<15}", end="")
for t in ['Mono (1)', 'Low (3)', 'Med (6)', 'High (12)', 'Proto (6)']:
    print(f" {t:>10}", end="")
print()
print("-" * 75)

for vn in VOLS:
    for metric in ['mean_output', 'mean_variance', 'mean_min', 'mean_resource']:
        label = metric.replace('mean_', '')
        print(f"{vn:<10} {label:<15}", end="")
        for t in ['Mono (1)', 'Low (3)', 'Med (6)', 'High (12)', 'Proto (6)']:
            v = RESULTS[vn][t][metric]
            if 'variance' in metric:
                print(f" {v:>10.6f}", end="")
            else:
                print(f" {v:>10.5f}", end="")
        print()
    
    # Variance reduction
    print(f"{vn:<10} {'var_red%':<15}", end="")
    print(f" {'—':>10}", end="")
    for t in ['Low (3)', 'Med (6)', 'High (12)', 'Proto (6)']:
        r = RESULTS[vn][t].get('var_reduction_vs_mono', 0)
        print(f" {r:>+9.1f}%", end="")
    print()
    print()


# ============================================================
# KEY FINDING
# ============================================================

print("=" * 80)
print("KEY FINDING:")
crisis_mono_var = RESULTS['crisis']['Mono (1)']['mean_variance']
crisis_high_var = RESULTS['crisis']['High (12)']['mean_variance']
crisis_proto_var = RESULTS['crisis']['Proto (6)']['mean_variance']
crisis_red_high = RESULTS['crisis']['High (12)'].get('var_reduction_vs_mono', 0)
crisis_red_proto = RESULTS['crisis']['Proto (6)'].get('var_reduction_vs_mono', 0)

print(f"  Under CRISIS conditions:")
print(f"    Monoculture output variance:     {crisis_mono_var:.7f}")
print(f"    High Diversity output variance:   {crisis_high_var:.7f}  ({crisis_red_high:+.1f}%)")
print(f"    Protocol+Diversity variance:      {crisis_proto_var:.7f}  ({crisis_red_proto:+.1f}%)")

stable_mono_var = RESULTS['stable']['Mono (1)']['mean_variance']
stable_high_var = RESULTS['stable']['High (12)']['mean_variance']
stable_red = RESULTS['stable']['High (12)'].get('var_reduction_vs_mono', 0)

print(f"\n  Under STABLE conditions:")
print(f"    Monoculture output variance:     {stable_mono_var:.7f}")
print(f"    High Diversity output variance:   {stable_high_var:.7f}  ({stable_red:+.1f}%)")

print(f"\n  The insurance effect {'STRENGTHENS' if abs(crisis_red_high) > abs(stable_red) else 'WEAKENS'} under stress.")
print("=" * 80)


with open('/home/claude/model_a_v5.json', 'w') as f:
    json.dump(RESULTS, f)

# Copy source
import shutil
shutil.copy('/home/claude/model_a_v5.py', '/mnt/user-data/outputs/model_a_insurance_test.py')

print("\nDone. Results saved.")
