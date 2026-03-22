"""
Fetch 6 months of institutional fund flow data:
  - Taiwan 三大法人 market total (via FinMind free API)
  - QQQ & TAIEX price data (via yfinance)
Saves everything to ./data/ as CSV files.
"""

import requests
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

START_DATE = "2025-09-22"
END_DATE   = "2026-03-21"

FINMIND_URL = "https://api.finmindtrade.com/api/v4/data"


# ──────────────────────────────────────────────
# 1. Taiwan 三大法人 – market total (FinMind)
# ──────────────────────────────────────────────

INVESTOR_MAP = {
    "Foreign_Investor":    "foreign",
    "Investment_Trust":    "trust",
    "Dealer_self":         "dealer_self",
    "Dealer_Hedging":      "dealer_hedge",
    "Foreign_Dealer_Self": "foreign_dealer",
}

def fetch_taiwan_institutional() -> pd.DataFrame:
    params = {
        "dataset":    "TaiwanStockTotalInstitutionalInvestors",
        "start_date": START_DATE,
        "end_date":   END_DATE,
    }
    resp = requests.get(FINMIND_URL, params=params, timeout=20)
    resp.raise_for_status()
    raw = resp.json()
    if raw.get("msg") != "success":
        raise RuntimeError(f"FinMind error: {raw.get('msg')}")

    df = pd.DataFrame(raw["data"])
    df["date"] = pd.to_datetime(df["date"])
    df["net"] = df["buy"] - df["sell"]

    # Pivot so each investor type is a column
    pivot = df.pivot_table(index="date", columns="name", values="net", aggfunc="sum")
    pivot.columns = [INVESTOR_MAP.get(c, c) for c in pivot.columns]

    # Aggregate to 三大法人 categories (values are in TWD)
    pivot["foreign_net"]  = pivot.get("foreign", 0) + pivot.get("foreign_dealer", 0)
    pivot["trust_net"]    = pivot.get("trust", 0)
    pivot["dealer_net"]   = pivot.get("dealer_self", 0) + pivot.get("dealer_hedge", 0)
    pivot["total_institutional_net"] = pivot["foreign_net"] + pivot["trust_net"] + pivot["dealer_net"]

    result = pivot[["foreign_net", "trust_net", "dealer_net", "total_institutional_net"]].copy()
    # Convert from TWD → 億元 (100M TWD) for readability
    result = result / 1e8
    result = result.reset_index().sort_values("date")
    return result


# ──────────────────────────────────────────────
# 2. Price data – TAIEX + QQQ (yfinance)
# ──────────────────────────────────────────────

def fetch_prices() -> pd.DataFrame:
    end_plus1 = (datetime.strptime(END_DATE, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    frames = {}
    for name, ticker in {"TAIEX": "^TWII", "QQQ": "QQQ"}.items():
        raw = yf.download(ticker, start=START_DATE, end=end_plus1,
                          progress=False, auto_adjust=True)
        close = raw["Close"]
        if hasattr(close, "columns"):     # MultiIndex → flatten
            close = close.iloc[:, 0]
        close = close.copy()
        close.name = name
        frames[name] = close

    prices = pd.concat(frames.values(), axis=1)
    prices.index.name = "date"
    prices = prices.reset_index()
    prices["date"] = pd.to_datetime(prices["date"]).dt.tz_localize(None)
    return prices


# ──────────────────────────────────────────────
# 3. Main
# ──────────────────────────────────────────────

if __name__ == "__main__":
    print("Fetching Taiwan 三大法人 data (FinMind)...")
    tw = fetch_taiwan_institutional()
    tw_path = os.path.join(OUTPUT_DIR, "taiwan_institutional_flows.csv")
    tw.to_csv(tw_path, index=False)
    print(f"  {len(tw)} rows → {tw_path}")

    print("Fetching price data (TAIEX + QQQ)...")
    prices = fetch_prices()
    pr_path = os.path.join(OUTPUT_DIR, "prices.csv")
    prices.to_csv(pr_path, index=False)
    print(f"  {len(prices)} rows → {pr_path}")

    print("Merging datasets...")
    tw["date"] = pd.to_datetime(tw["date"])
    merged = prices.merge(tw, on="date", how="left")
    merged_path = os.path.join(OUTPUT_DIR, "combined.csv")
    merged.to_csv(merged_path, index=False)
    print(f"  {len(merged)} rows → {merged_path}")

    print("\nDone! Files in ./data/")
    print(merged.tail(5).to_string(index=False))
