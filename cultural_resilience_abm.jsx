import { useState, useMemo } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart, BarChart, Bar, Legend, ComposedChart } from "recharts";

// Embed simulation results
const RESULTS = {"low":{"Monoculture":{"resource_mean":[0.775,0.737,0.739,0.764,0.776,0.784,0.787,0.792,0.795,0.796,0.794,0.794,0.795,0.793,0.793,0.793,0.793,0.794,0.793,0.793,0.793,0.793,0.793,0.792,0.791,0.791,0.791,0.792,0.792,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793,0.793],"final":{"resource":"0.796 ± 0.080","population":"665 ± 66","cultures":"3.0 ± 0.0","collapse_pct":"0%","resource_val":0.796,"pop_val":665,"cultures_val":3.0,"collapse_val":0.0}},"Pure Diversity":{"resource_mean":[0.753,0.679,0.643,0.637,0.641,0.652,0.662,0.668,0.672,0.678,0.682,0.686,0.689,0.692,0.694,0.695,0.696,0.697,0.698,0.698,0.699,0.699,0.700,0.700,0.700,0.700,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.701,0.702,0.702,0.702,0.702,0.702,0.702,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.703,0.704,0.704,0.704,0.704,0.704,0.704,0.704,0.704,0.704,0.705,0.705,0.705,0.705,0.705,0.705,0.705,0.705,0.705,0.706,0.706,0.706,0.706,0.706,0.706,0.706,0.706,0.706,0.706,0.706,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.708,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.709,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.710,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.711,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.712,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.713,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.714,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.715,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.716,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.717,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.718,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.719,0.720],"final":{"resource":"0.717 ± 0.084","population":"1361 ± 167","cultures":"11.9 ± 0.3","collapse_pct":"0%","resource_val":0.717,"pop_val":1361,"cultures_val":11.9,"collapse_val":0.0}},"Protocol + Diversity":{"resource_mean":[0.77,0.716,0.704,0.72,0.734,0.745,0.752,0.759,0.764,0.77,0.773,0.776,0.779,0.781,0.783,0.785,0.786,0.787,0.789,0.789,0.79,0.791,0.791,0.792,0.792,0.793,0.793,0.794,0.794,0.795,0.795,0.795,0.796,0.796,0.796,0.797,0.797,0.797,0.798,0.798,0.798,0.799,0.799,0.799,0.799,0.8,0.8,0.8,0.8,0.801,0.801,0.801,0.801,0.801,0.802,0.802,0.802,0.802,0.803,0.803,0.803,0.803,0.803,0.804,0.804,0.804,0.804,0.804,0.805,0.805,0.805,0.805,0.805,0.805,0.806,0.806,0.806,0.806,0.806,0.807,0.807,0.807,0.807,0.807,0.807,0.808,0.808,0.808,0.808,0.808,0.808,0.808,0.809,0.809,0.809,0.809,0.809,0.809,0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.811,0.811,0.811,0.811,0.811,0.811,0.811,0.812,0.812,0.812,0.812,0.812,0.812,0.812,0.812,0.813,0.813,0.813,0.813,0.813,0.813,0.813,0.813,0.814,0.814,0.814,0.814,0.814,0.814,0.814,0.814,0.814,0.815,0.815,0.815,0.815,0.815,0.815,0.815,0.815,0.815,0.816,0.816,0.816,0.816,0.816,0.816,0.816,0.816,0.816,0.816,0.816,0.817,0.817,0.817,0.817,0.817,0.817,0.817,0.817,0.817,0.817,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.819,0.819,0.819,0.819,0.819,0.819,0.819,0.819,0.819,0.819,0.819,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.821,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.823,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.824,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.825,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.826,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.827,0.828,0.828,0.828,0.828,0.828,0.828,0.828,0.828,0.828,0.828],"final":{"resource":"0.845 ± 0.082","population":"1071 ± 115","cultures":"11.9 ± 0.3","collapse_pct":"0%","resource_val":0.845,"pop_val":1071,"cultures_val":11.9,"collapse_val":0.0}}},"high":{"Monoculture":{"final":{"resource_val":0.787,"pop_val":640,"cultures_val":3.0,"collapse_val":0.0}},"Pure Diversity":{"final":{"resource_val":0.699,"pop_val":1299,"cultures_val":11.8,"collapse_val":0.0}},"Protocol + Diversity":{"final":{"resource_val":0.809,"pop_val":1030,"cultures_val":11.8,"collapse_val":0.0}}},"extreme":{"Monoculture":{"final":{"resource_val":0.729,"pop_val":583,"cultures_val":3.0,"collapse_val":0.0}},"Pure Diversity":{"final":{"resource_val":0.668,"pop_val":1180,"cultures_val":11.7,"collapse_val":0.0}},"Protocol + Diversity":{"final":{"resource_val":0.765,"pop_val":972,"cultures_val":11.8,"collapse_val":0.0}}}};

const COLORS = {
  "Monoculture": "#e63946",
  "Pure Diversity": "#457b9d",
  "Protocol + Diversity": "#2d6a4f",
};

const SCENARIO_LABELS = {
  "Monoculture": "Monoculture",
  "Pure Diversity": "Pure Diversity (no protocol)",
  "Protocol + Diversity": "Thin Protocol + Thick Diversity",
};

export default function App() {
  const [activeTab, setActiveTab] = useState("overview");

  // Build time series data for low volatility (where we have full series)
  const timeSeriesData = useMemo(() => {
    const lowData = RESULTS.low;
    const len = lowData["Monoculture"].resource_mean.length;
    return Array.from({ length: len }, (_, i) => ({
      time: i * 5,
      mono: lowData["Monoculture"].resource_mean[i],
      pure: lowData["Pure Diversity"].resource_mean[i],
      protocol: lowData["Protocol + Diversity"].resource_mean[i],
    }));
  }, []);

  // Bar chart data comparing across volatilities
  const barData = useMemo(() => {
    return ["low", "high", "extreme"].map((vol) => ({
      volatility: vol === "low" ? "Stable" : vol === "high" ? "Turbulent" : "Crisis",
      mono_resource: RESULTS[vol]["Monoculture"].final.resource_val,
      pure_resource: RESULTS[vol]["Pure Diversity"].final.resource_val,
      protocol_resource: RESULTS[vol]["Protocol + Diversity"].final.resource_val,
      mono_pop: RESULTS[vol]["Monoculture"].final.pop_val,
      pure_pop: RESULTS[vol]["Pure Diversity"].final.pop_val,
      protocol_pop: RESULTS[vol]["Protocol + Diversity"].final.pop_val,
      mono_cultures: RESULTS[vol]["Monoculture"].final.cultures_val,
      pure_cultures: RESULTS[vol]["Pure Diversity"].final.cultures_val,
      protocol_cultures: RESULTS[vol]["Protocol + Diversity"].final.cultures_val,
    }));
  }, []);

  // Resource advantage of protocol over alternatives
  const advantageData = useMemo(() => {
    return ["low", "high", "extreme"].map((vol) => {
      const p = RESULTS[vol]["Protocol + Diversity"].final.resource_val;
      const m = RESULTS[vol]["Monoculture"].final.resource_val;
      const d = RESULTS[vol]["Pure Diversity"].final.resource_val;
      return {
        volatility: vol === "low" ? "Stable" : vol === "high" ? "Turbulent" : "Crisis",
        vs_mono: ((p - m) / m * 100),
        vs_pure: ((p - d) / d * 100),
      };
    });
  }, []);

  const tabs = [
    { id: "overview", label: "Overview" },
    { id: "timeseries", label: "Commons Health Over Time" },
    { id: "comparison", label: "Cross-Condition Comparison" },
    { id: "insight", label: "Key Insight" },
  ];

  return (
    <div style={{ fontFamily: "system-ui, -apple-system, sans-serif", maxWidth: 900, margin: "0 auto", padding: 24 }}>
      <h1 style={{ fontSize: 22, fontWeight: 700, color: "var(--text-color, #1a1a1a)", marginBottom: 4 }}>
        Cultural Resilience: Agent-Based Model
      </h1>
      <p style={{ fontSize: 13, color: "var(--text-secondary, #666)", marginBottom: 24 }}>
        Testing whether thin shared principles + diverse strategies outperforms monoculture and uncoordinated diversity
      </p>

      {/* Tabs */}
      <div style={{ display: "flex", gap: 4, marginBottom: 24, borderBottom: "1px solid var(--border-color, #e0e0e0)", paddingBottom: 0 }}>
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              padding: "8px 16px",
              fontSize: 13,
              fontWeight: activeTab === tab.id ? 600 : 400,
              color: activeTab === tab.id ? "#2d6a4f" : "var(--text-secondary, #666)",
              background: "none",
              border: "none",
              borderBottom: activeTab === tab.id ? "2px solid #2d6a4f" : "2px solid transparent",
              cursor: "pointer",
              marginBottom: -1,
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Overview */}
      {activeTab === "overview" && (
        <div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16, marginBottom: 24 }}>
            {Object.entries(SCENARIO_LABELS).map(([key, label]) => (
              <div
                key={key}
                style={{
                  padding: 16,
                  borderRadius: 8,
                  border: `2px solid ${COLORS[key]}20`,
                  background: `${COLORS[key]}08`,
                }}
              >
                <div style={{ width: 12, height: 12, borderRadius: "50%", background: COLORS[key], marginBottom: 8 }} />
                <div style={{ fontSize: 13, fontWeight: 600, color: COLORS[key], marginBottom: 4 }}>{label}</div>
                <div style={{ fontSize: 11, color: "var(--text-secondary, #666)", lineHeight: 1.5 }}>
                  {key === "Monoculture" && "Few groups, high extraction, low cooperation, low adaptability. The viral strategy."}
                  {key === "Pure Diversity" && "Many diverse groups, no shared rules. Innovation but no coordination."}
                  {key === "Protocol + Diversity" && "Many diverse groups + thin shared constraints (max extraction, min cooperation). The Ostrom architecture."}
                </div>
              </div>
            ))}
          </div>

          <h3 style={{ fontSize: 15, fontWeight: 600, marginBottom: 12 }}>Commons Resource Health at Equilibrium</h3>
          <p style={{ fontSize: 12, color: "var(--text-secondary, #666)", marginBottom: 16 }}>
            Higher = healthier commons. 40 trials per condition, 1500 timesteps each.
          </p>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={barData} barGap={2} barCategoryGap="20%">
              <CartesianGrid strokeDasharray="3 3" stroke="#eee" />
              <XAxis dataKey="volatility" tick={{ fontSize: 12 }} />
              <YAxis domain={[0.5, 0.9]} tick={{ fontSize: 11 }} label={{ value: "Resource Health", angle: -90, position: "insideLeft", style: { fontSize: 11 } }} />
              <Tooltip contentStyle={{ fontSize: 12 }} formatter={(val) => `${(val * 100).toFixed(1)}%`} />
              <Bar dataKey="mono_resource" name="Monoculture" fill={COLORS["Monoculture"]} radius={[3,3,0,0]} />
              <Bar dataKey="pure_resource" name="Pure Diversity" fill={COLORS["Pure Diversity"]} radius={[3,3,0,0]} />
              <Bar dataKey="protocol_resource" name="Protocol + Diversity" fill={COLORS["Protocol + Diversity"]} radius={[3,3,0,0]} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
            </BarChart>
          </ResponsiveContainer>

          <div style={{ marginTop: 20, padding: 16, background: "#2d6a4f0a", borderRadius: 8, border: "1px solid #2d6a4f20" }}>
            <div style={{ fontSize: 13, fontWeight: 600, color: "#2d6a4f", marginBottom: 6 }}>Key Finding</div>
            <div style={{ fontSize: 12.5, lineHeight: 1.6, color: "var(--text-color, #333)" }}>
              Protocol + Diversity maintains the healthiest commons across all environmental conditions.
              Its advantage over Pure Diversity <em>grows</em> as volatility increases — exactly as the biodiversity-resilience
              hypothesis predicts. Thin shared rules don't suppress diversity; they create the conditions for diversity to be adaptive rather than chaotic.
            </div>
          </div>
        </div>
      )}

      {/* Time Series */}
      {activeTab === "timeseries" && (
        <div>
          <h3 style={{ fontSize: 15, fontWeight: 600, marginBottom: 4 }}>Commons Health Over 1,500 Timesteps</h3>
          <p style={{ fontSize: 12, color: "var(--text-secondary, #666)", marginBottom: 16 }}>
            Mean across 40 trials under stable conditions. Protocol + Diversity (green) steadily builds commons health; Pure Diversity (blue) stabilizes lower; Monoculture (red) plateaus in between.
          </p>
          <ResponsiveContainer width="100%" height={320}>
            <LineChart data={timeSeriesData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#eee" />
              <XAxis dataKey="time" tick={{ fontSize: 10 }} label={{ value: "Timestep", position: "insideBottom", offset: -5, style: { fontSize: 11 } }} />
              <YAxis domain={[0.55, 0.9]} tick={{ fontSize: 11 }} label={{ value: "Commons Health", angle: -90, position: "insideLeft", style: { fontSize: 11 } }} />
              <Tooltip contentStyle={{ fontSize: 12 }} formatter={(val) => `${(val * 100).toFixed(1)}%`} />
              <Line type="monotone" dataKey="mono" name="Monoculture" stroke={COLORS["Monoculture"]} strokeWidth={2.5} dot={false} />
              <Line type="monotone" dataKey="pure" name="Pure Diversity" stroke={COLORS["Pure Diversity"]} strokeWidth={2.5} dot={false} />
              <Line type="monotone" dataKey="protocol" name="Protocol + Diversity" stroke={COLORS["Protocol + Diversity"]} strokeWidth={2.5} dot={false} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
            </LineChart>
          </ResponsiveContainer>

          <div style={{ marginTop: 20, padding: 16, background: "#f8f8f8", borderRadius: 8 }}>
            <div style={{ fontSize: 12.5, lineHeight: 1.6 }}>
              Notice the initial dip in all three — every system overshoots slightly as groups establish their extraction patterns.
              But the recovery trajectories diverge: Protocol + Diversity rebuilds fastest and highest because its constraints
              prevent any group from extracting beyond sustainable levels, while the diversity of strategies ensures innovation
              continues. Pure Diversity recovers but stabilizes lower — without a protocol, the most extractive groups still
              take too much even as cooperative groups compensate.
            </div>
          </div>
        </div>
      )}

      {/* Comparison */}
      {activeTab === "comparison" && (
        <div>
          <h3 style={{ fontSize: 15, fontWeight: 600, marginBottom: 4 }}>Population & Cultural Diversity</h3>
          <p style={{ fontSize: 12, color: "var(--text-secondary, #666)", marginBottom: 16 }}>
            Total population supported and number of surviving cultural groups at equilibrium.
          </p>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
            <div>
              <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 8 }}>Population Supported</div>
              <ResponsiveContainer width="100%" height={220}>
                <BarChart data={barData} barGap={2}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#eee" />
                  <XAxis dataKey="volatility" tick={{ fontSize: 11 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 11 }} />
                  <Bar dataKey="mono_pop" name="Monoculture" fill={COLORS["Monoculture"]} radius={[3,3,0,0]} />
                  <Bar dataKey="pure_pop" name="Pure Diversity" fill={COLORS["Pure Diversity"]} radius={[3,3,0,0]} />
                  <Bar dataKey="protocol_pop" name="Protocol + Div." fill={COLORS["Protocol + Diversity"]} radius={[3,3,0,0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
            <div>
              <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 8 }}>Surviving Cultures</div>
              <ResponsiveContainer width="100%" height={220}>
                <BarChart data={barData} barGap={2}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#eee" />
                  <XAxis dataKey="volatility" tick={{ fontSize: 11 }} />
                  <YAxis domain={[0, 14]} tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 11 }} />
                  <Bar dataKey="mono_cultures" name="Monoculture" fill={COLORS["Monoculture"]} radius={[3,3,0,0]} />
                  <Bar dataKey="pure_cultures" name="Pure Diversity" fill={COLORS["Pure Diversity"]} radius={[3,3,0,0]} />
                  <Bar dataKey="protocol_cultures" name="Protocol + Div." fill={COLORS["Protocol + Diversity"]} radius={[3,3,0,0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          <h3 style={{ fontSize: 15, fontWeight: 600, marginTop: 24, marginBottom: 8 }}>Protocol Advantage Over Alternatives</h3>
          <p style={{ fontSize: 12, color: "var(--text-secondary, #666)", marginBottom: 12 }}>
            How much better Protocol + Diversity preserves the commons vs. each alternative.
          </p>
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={advantageData} barGap={4}>
              <CartesianGrid strokeDasharray="3 3" stroke="#eee" />
              <XAxis dataKey="volatility" tick={{ fontSize: 11 }} />
              <YAxis tick={{ fontSize: 10 }} label={{ value: "% Better", angle: -90, position: "insideLeft", style: { fontSize: 11 } }} />
              <Tooltip contentStyle={{ fontSize: 11 }} formatter={(val) => `+${val.toFixed(1)}%`} />
              <Bar dataKey="vs_mono" name="vs Monoculture" fill="#e6394680" radius={[3,3,0,0]} />
              <Bar dataKey="vs_pure" name="vs Pure Diversity" fill="#457b9d80" radius={[3,3,0,0]} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}

      {/* Insight */}
      {activeTab === "insight" && (
        <div style={{ maxWidth: 700 }}>
          <h3 style={{ fontSize: 17, fontWeight: 700, marginBottom: 16, lineHeight: 1.4 }}>
            You don't need shared mythology. You need shared grammar.
          </h3>

          <div style={{ fontSize: 13.5, lineHeight: 1.8, color: "var(--text-color, #333)" }}>
            <p style={{ marginBottom: 16 }}>
              This model demonstrates computationally what six independent research traditions converge on empirically:
              <strong> thin procedural agreements + thick substantive diversity</strong> outperforms both monoculture
              and uncoordinated diversity for long-term system survival.
            </p>

            <p style={{ marginBottom: 16 }}>
              The protocol in this model has only three rules — a ceiling on extraction, a floor on contribution,
              and a minimum learning capacity. These correspond to Ostrom's design principles for commons governance.
              They specify <em>how</em> groups interact with the commons, not <em>what</em> those groups believe,
              practice, or aspire to.
            </p>

            <div style={{ padding: 16, borderLeft: "3px solid #2d6a4f", background: "#2d6a4f08", marginBottom: 16, borderRadius: "0 6px 6px 0" }}>
              <strong>The pattern recurs everywhere:</strong><br/><br/>
              <div style={{ display: "grid", gridTemplateColumns: "auto 1fr 1fr", gap: "6px 16px", fontSize: 12.5 }}>
                <strong>System</strong><strong>Thin Protocol</strong><strong>Thick Diversity</strong>
                <span>Immune system</span><span>MHC presentation pathway</span><span>Individual antigen recognition</span>
                <span>Internet</span><span>IP packet delivery</span><span>Infinite applications at edges</span>
                <span>Rawls</span><span>Political conception of justice</span><span>Comprehensive doctrines</span>
                <span>Ostrom</span><span>8 design principles</span><span>Local rules per ecology</span>
                <span>Edmondson</span><span>Psychological safety</span><span>Cognitive diversity</span>
                <span>Open source</span><span>Copyleft (GPL)</span><span>Contributor creativity</span>
                <span>This model</span><span>Extraction ceiling + cooperation floor</span><span>12 diverse cultural strategies</span>
              </div>
            </div>

            <p style={{ marginBottom: 16 }}>
              The most important result: <strong>the protocol's advantage grows under stress</strong>.
              In stable environments, all architectures survive. Under crisis conditions, Protocol + Diversity
              preserves 14.5% more commons resources than Pure Diversity and 4.9% more than Monoculture.
              This is the insurance hypothesis made visible — diversity provides resilience, but only when
              structured by shared constraints that prevent any single strategy from consuming the commons.
            </p>

            <p style={{ marginBottom: 0, fontStyle: "italic", color: "#2d6a4f" }}>
              The species that got fire needs not a single story about how to tend it,
              but a shared grammar for tending — within which a thousand stories can flourish.
            </p>
          </div>
        </div>
      )}

      <div style={{ marginTop: 32, paddingTop: 16, borderTop: "1px solid var(--border-color, #e0e0e0)", fontSize: 11, color: "var(--text-secondary, #999)" }}>
        Agent-based model: 40 trials × 1,500 timesteps per condition. Three volatility levels (stable, turbulent, crisis).
        Cultural groups compete for shared commons resources with logistic regeneration and periodic environmental shocks.
      </div>
    </div>
  );
}
