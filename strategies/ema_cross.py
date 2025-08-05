import pandas as pd

def ema_cross_strategy(df, fast=10, slow=50):
    """
    EMA Crossover Strategy:
    Buy when fast EMA crosses above slow EMA.
    Sell when fast EMA crosses below slow EMA.
    """
    df = df.copy()
    df['ema_fast'] = df['close'].ewm(span=fast).mean()
    df['ema_slow'] = df['close'].ewm(span=slow).mean()
    
    df['signal'] = 0
    df.loc[df['ema_fast'] > df['ema_slow'], 'signal'] = 1
    df.loc[df['ema_fast'] < df['ema_slow'], 'signal'] = -1
    
    df['position'] = df['signal'].shift()
    df.dropna(inplace=True)
    
    return df[['close', 'ema_fast', 'ema_slow', 'signal', 'position']]
