def load_strategy(name: str):
    if name == "rsi_reversal":
        from strategies.rsi_reversal import RSIStrategy
        return RSIStrategy()
    elif name == "breakout":
        from strategies.breakout import BreakoutStrategy
        return BreakoutStrategy()
