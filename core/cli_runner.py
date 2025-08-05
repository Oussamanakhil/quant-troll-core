# === 🧠 Stored Execution Rules ===
# - CLI interface to run strategies quickly
# - Used for quick backtests, tuning, or paper trades

import argparse
import pandas as pd
from strategies.rsi_reversal import rsi_reversal_strategy
from core.paper_trader import paper_trade

parser = argparse.ArgumentParser(description="QuantTroll CLI Strategy Runner")
parser.add_argument("--strategy", type=str, default="rsi", help="Strategy to run")
parser.add_argument("--file", type=str, default="data/btc_ohlcv.csv", help="Data file path")

args = parser.parse_args()

df = pd.read_csv(args.file, index_col=0, parse_dates=True)

if args.strategy == "rsi":
    signals = rsi_reversal_strategy(df)
    results = paper_trade(signals)
    print("✅ Finished RSI backtest.")
    print(results.tail())
