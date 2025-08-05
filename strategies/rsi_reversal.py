# rsi_reverimport pandas as pd

def rsi_reversal_strategy(df, rsi_period=14, lower_thresh=30, upper_thresh=70):
    """
    RSI Mean Reversion Strategy:
    - Buy when RSI crosses above lower threshold (oversold reversal)
    - Sell when RSI crosses below upper threshold (overbought reversion)
    """
    df = df.copy()
    
    # === RSI Calculation ===
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(rsi_period).mean()
    loss = -delta.where(delta < 0, 0).rolling(rsi_period).mean()
    rs = gain / (loss + 1e-9)
    df['rsi'] = 100 - (100 / (1 + rs))

    # === Signal Logic ===
    df['signal'] = 0
    df.loc[(df['rsi'] > lower_thresh) & (df['rsi'].shift(1) <= lower_thresh), 'signal'] = 1
    df.loc[(df['rsi'] < upper_thresh) & (df['rsi'].shift(1) >= upper_thresh), 'signal'] = -1

    # === Position Column ===
    df['position'] = df['signal'].shift()

    df.dropna(inplace=True)
    return df[['close', 'rsi', 'signal', 'position']]
sal.py - Placeholder for strategies
