"""
Backtest: does institutional fund flow predict next-day / next-week returns?
Signals:
  - Taiwan: 外資 (foreign) net flow → TAIEX next-day return
  - US: QQQ weekly return as flow proxy → QQQ next-week return
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT_DIR, exist_ok=True)


def load_data():
    combined = pd.read_csv(os.path.join(DATA_DIR, "combined.csv"), parse_dates=["date"])
    combined = combined.sort_values("date").reset_index(drop=True)
    return combined


def compute_signals(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # ── Taiwan signals ──
    df["taiex_ret_1d"] = df["TAIEX"].pct_change(1).shift(-1) * 100   # next-day return
    df["taiex_ret_5d"] = df["TAIEX"].pct_change(5).shift(-5) * 100   # next-week return

    # Normalise foreign net flow (z-score, 20-day rolling)
    roll = df["foreign_net"].rolling(20)
    df["foreign_net_z"] = (df["foreign_net"] - roll.mean()) / roll.std()

    # Signal: +1 if foreign z > 0, -1 otherwise
    df["signal_foreign"] = np.where(df["foreign_net_z"] > 0, 1, -1)

    # ── QQQ signals ──
    df["qqq_ret_1d"] = df["QQQ"].pct_change(1).shift(-1) * 100
    df["qqq_ret_5d"] = df["QQQ"].pct_change(5).shift(-5) * 100

    qqq_roll = df["total_institutional_net"].rolling(20)
    df["inst_net_z"] = (df["total_institutional_net"] - qqq_roll.mean()) / qqq_roll.std()
    df["signal_inst"] = np.where(df["inst_net_z"] > 0, 1, -1)

    return df


def backtest_signal(df: pd.DataFrame, signal_col: str, return_col: str, label: str):
    valid = df[[signal_col, return_col]].dropna()
    long_returns = valid.loc[valid[signal_col] == 1, return_col]
    short_returns = valid.loc[valid[signal_col] == -1, return_col]

    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    print(f"  Total days:        {len(valid)}")
    print(f"  Long days (net+):  {len(long_returns)}  |  Avg next return: {long_returns.mean():.3f}%")
    print(f"  Short days (net-): {len(short_returns)} |  Avg next return: {short_returns.mean():.3f}%")
    corr = valid[signal_col].corr(valid[return_col])
    print(f"  Signal correlation: {corr:.4f}")

    # Hit rate
    hit_long = (long_returns > 0).mean()
    hit_short = (short_returns < 0).mean()
    print(f"  Long hit rate:  {hit_long:.1%}  |  Short hit rate: {hit_short:.1%}")
    return {
        "label": label,
        "long_avg_ret": long_returns.mean(),
        "short_avg_ret": short_returns.mean(),
        "correlation": corr,
        "long_hit_rate": hit_long,
        "short_hit_rate": hit_short,
    }


def plot_flow_vs_price(df: pd.DataFrame):
    fig, axes = plt.subplots(4, 1, figsize=(14, 16), sharex=False)
    fig.suptitle("Institutional Flows vs Price (Past 6 Months)", fontsize=14, fontweight="bold")

    valid = df.dropna(subset=["TAIEX", "foreign_net"])

    # Panel 1: TAIEX price
    ax1 = axes[0]
    ax1.plot(valid["date"], valid["TAIEX"], color="#1a73e8", linewidth=1.5)
    ax1.set_title("TAIEX Index")
    ax1.set_ylabel("Price (TWD)")
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    # Panel 2: Taiwan 外資 net flow
    ax2 = axes[1]
    colors = ["#d32f2f" if x < 0 else "#388e3c" for x in valid["foreign_net"]]
    ax2.bar(valid["date"], valid["foreign_net"] / 1e4, color=colors, width=1)
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.set_title("Taiwan 外資 Net Flow (億元)")
    ax2.set_ylabel("億元")
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    # Panel 3: QQQ price
    valid_qqq = df.dropna(subset=["QQQ"])
    ax3 = axes[2]
    ax3.plot(valid_qqq["date"], valid_qqq["QQQ"], color="#f57c00", linewidth=1.5)
    ax3.set_title("QQQ Price (USD)")
    ax3.set_ylabel("Price (USD)")
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    # Panel 4: Taiwan total institutional net flow
    ax4 = axes[3]
    colors4 = ["#d32f2f" if x < 0 else "#388e3c" for x in valid["total_institutional_net"]]
    ax4.bar(valid["date"], valid["total_institutional_net"] / 1e4, color=colors4, width=1)
    ax4.axhline(0, color="black", linewidth=0.5)
    ax4.set_title("Taiwan 三大法人合計 Net Flow (億元)")
    ax4.set_ylabel("億元")
    ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    for ax in axes:
        ax.grid(axis="y", linestyle="--", alpha=0.4)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right")

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "flows_vs_price.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"\nChart saved → {path}")


def plot_cumulative_pnl(df: pd.DataFrame):
    valid = df.dropna(subset=["signal_foreign", "taiex_ret_1d"])
    valid = valid.copy()
    valid["strategy_ret"] = valid["signal_foreign"] * valid["taiex_ret_1d"]
    valid["cum_strategy"] = (1 + valid["strategy_ret"] / 100).cumprod() - 1
    valid["cum_taiex"] = (1 + valid["taiex_ret_1d"] / 100).cumprod() - 1

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(valid["date"], valid["cum_strategy"] * 100, label="外資 Flow Signal", linewidth=1.5, color="#1a73e8")
    ax.plot(valid["date"], valid["cum_taiex"] * 100, label="TAIEX Buy & Hold", linewidth=1.5, color="#888", linestyle="--")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_title("Cumulative Return: 外資 Flow Signal vs TAIEX Buy & Hold")
    ax.set_ylabel("Cumulative Return (%)")
    ax.legend()
    ax.grid(linestyle="--", alpha=0.4)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right")
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "cumulative_pnl.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Chart saved → {path}")


def save_summary(results: list):
    summary = pd.DataFrame(results)
    path = os.path.join(OUT_DIR, "backtest_summary.csv")
    summary.to_csv(path, index=False)
    print(f"Summary saved → {path}")


if __name__ == "__main__":
    print("Loading data...")
    df = load_data()
    print(f"  {len(df)} trading days loaded ({df['date'].min().date()} → {df['date'].max().date()})")

    df = compute_signals(df)

    results = []
    results.append(backtest_signal(df, "signal_foreign", "taiex_ret_1d",
                                   "Taiwan 外資 Flow → TAIEX Next-Day Return"))
    results.append(backtest_signal(df, "signal_foreign", "taiex_ret_5d",
                                   "Taiwan 外資 Flow → TAIEX Next-Week Return"))
    results.append(backtest_signal(df, "signal_inst",   "qqq_ret_1d",
                                   "TW 三大法人 Flow → QQQ Next-Day Return"))
    results.append(backtest_signal(df, "signal_inst",   "qqq_ret_5d",
                                   "TW 三大法人 Flow → QQQ Next-Week Return"))

    print("\nGenerating charts...")
    plot_flow_vs_price(df)
    plot_cumulative_pnl(df)
    save_summary(results)

    print("\nAll done! Results in ./output/")
