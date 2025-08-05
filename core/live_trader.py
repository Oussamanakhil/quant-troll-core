import os
import requests
import pandas as pd
from dotenv import load_dotenv

# 🔐 Load Alpaca keys from .env
load_dotenv()
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}


def submit_order(symbol, qty, side, type="market", time_in_force="gtc"):
    """
    Submit a market order to Alpaca.
    """
    url = f"{ALPACA_BASE_URL}/v2/orders"
    order = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    response = requests.post(url, json=order, headers=HEADERS)

    if response.status_code == 200:
        print(f"✅ Order submitted: {side.upper()} {qty} {symbol}")
    else:
        print(f"❌ Order failed: {response.status_code} - {response.text}")


def place_orders_from_signals(df, symbol="BTCUSD", capital=1000):
    """
    Reads a DataFrame with a 'position' column and submits live orders.
    - 1 = Long (BUY)
    - -1 = Short (SELL)
    - 0 = Flat (no action)
    """
    last_position = 0
    qty = 1  # 🧠 TODO: replace with size logic from capital and price

    for i in range(1, len(df)):
        current_pos = df.iloc[i]['position']
        prev_pos = df.iloc[i - 1]['position']

        if current_pos != prev_pos:
            if current_pos == 1:
                submit_order(symbol, qty, "buy")
            elif current_pos == -1:
                submit_order(symbol, qty, "sell")
            # else: hold


