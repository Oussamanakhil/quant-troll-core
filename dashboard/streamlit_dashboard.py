# 📊 Quant Troll Streamlit Dashboard

# === 🧠 Stored Execution Rules ===
# - Pulls trade logs from logs/trade_logs.csv
# - Plots equity curve, signal distribution, trade stats
# - Reusable for both backtest and live mode
# - Must be run with: streamlit run dashboard/streamlit_dashboard.py

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🧌 Quant Troll Dashboard")

# Load logs
log_path = "logs/trade_logs.csv"
if not os.path.exists(log_path):
    st.warning("No trade logs found at logs/trade_logs.csv.")
    st.stop()

df = pd.read_csv(log_path, parse_dates=["timestamp"])

# Equity Curve
st.subheader("📈 Equity Curve")
df["equity"] = df["pnl"].cumsum()
st.line_chart(df.set_index("timestamp")["equity"])

# PnL Stats
st.subheader("📊 PnL Stats")
st.dataframe(df[["symbol", "side", "pnl"]].describe())

# Signal Distribution
st.subheader("📍 Trade Signal Distribution")
st.bar_chart(df["side"].value_counts())

# Recent Trades
st.subheader("🧾 Recent Executions")
st.dataframe(df.tail(10))
