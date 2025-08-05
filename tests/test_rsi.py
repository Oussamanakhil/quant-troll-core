# === 🧠 Stored Execution Rules ===
# - Must pass for every repo release (CI/CD safe)
# - Strategy must return 'position' column
# - Backtest must generate non-empty results
# - Sharpe must not be NaN or infinite

import pandas as pd
import numpy as np
from strategies.rsi_reversal import rsi_reversal_strategy
from core.paper_trader import paper_trade

def test_rsi_strategy():
    df = pd.read_csv("data/btc_ohlcv.csv", index_col=0, parse_dates=True)
    signals = rsi_reversal_strategy(df)
    assert "position" in signals.columns, "Missing 'position' in signals"
    assert not signals["position"].isnull().all(), "Empty positions"

def test_rsi_backtest():
    df = pd.read_csv("data/btc_ohlcv.csv", index_col=0, parse_dates=True)
    signals = rsi_reversal_strategy(df)
    results = paper_trade(signals)
    assert not results.empty, "Backtest returned empty"
    sharpe = results["pnl"].mean() / (results["pnl"].std() + 1e-9)
    assert np.isfinite(sharpe), "Sharpe ratio is not finite"
