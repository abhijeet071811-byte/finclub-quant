from storage.storage import Storage
from analytics.metrics import Metrics

def get_summary():

    equity_curve = Storage.load_equity_curve()

    trades = Storage.load_trades()

    daily_returns = Metrics.calculate_daily_returns(equity_curve)

        
    summary = {
        "Total Return": Metrics.calculate_total_return(equity_curve),
        "Volatility": Metrics.calculate_volatility(daily_returns),
        "Sharpe": Metrics.calculate_sharpe_ratio(daily_returns),
        "Max Drawdown": Metrics.calculate_max_drawdown(equity_curve),
        "Win Rate": Metrics.calculate_win_rate(trades),
    }
    return summary
