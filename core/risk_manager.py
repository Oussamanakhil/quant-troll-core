# 🛡️ Quant Troll Risk Manager

# === 🧠 Stored Execution Rules ===
# - Calculates position size based on risk % and stop loss
# - Tracks max drawdown from equity high watermark
# - Enforces max daily loss limit before disabling strategy
# - Reusable by paper_trader, live_trader, and strategy evaluation

def calculate_position_size(capital, entry_price, stop_loss_price, risk_percent):
    risk_amount = capital * (risk_percent / 100)
    stop_distance = abs(entry_price - stop_loss_price)
    if stop_distance == 0:
        return 0
    qty = risk_amount / stop_distance
    return round(qty, 6)


def check_portfolio_drawdown(current_equity, high_watermark, max_drawdown_percent):
    drawdown = (high_watermark - current_equity) / high_watermark * 100
    return drawdown > max_drawdown_percent


def is_max_daily_loss_hit(daily_pnl, max_loss_threshold):
    return daily_pnl <= -abs(max_loss_threshold)
