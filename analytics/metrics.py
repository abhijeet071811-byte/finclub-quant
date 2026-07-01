import math
import pandas as pd
class Metrics:

    @staticmethod
    def calculate_total_return(equity_curve):

        if equity_curve.empty:
            return 0

        initial_value = equity_curve["Portfolio Value"].iloc[0]
        final_value = equity_curve["Portfolio Value"].iloc[-1]

        return ((final_value - initial_value) / initial_value) * 100

    @staticmethod
    def calculate_daily_returns(equity_curve):
        
        return equity_curve["Portfolio Value"].pct_change().dropna()

    @staticmethod
    def calculate_volatility(daily_returns):
        
        return_mean=daily_returns.mean()
        k=len(daily_returns)
        sum=0
        
        for i in range(k):
            sum+=(daily_returns.iloc[i]-return_mean)**2
        
        volatilities = math.sqrt(sum/(k-1))
        
        return volatilities

    @staticmethod
    def calculate_sharpe_ratio(daily_returns,risk_free_rate=0):
        
        volatility = Metrics.calculate_volatility(daily_returns)

        if volatility == 0:
            return 0

        average_return = daily_returns.mean()
        daily_rf = risk_free_rate / 252

        sharpe = (average_return - daily_rf) / volatility

        return sharpe


    @staticmethod
    def calculate_max_drawdown(equity_curve):

        portfolio_values = equity_curve["Portfolio Value"]

        peak = portfolio_values.iloc[0]
        max_drawdown = 0
        drawdown=0

        running_peak = equity_curve["Portfolio Value"].cummax()

        drawdowns = (equity_curve["Portfolio Value"] - running_peak) / running_peak
        max_drawdown = abs(drawdowns.min()) * 100
            
        return max_drawdown * 100
            



    # @staticmethod
    # def calculate_win_rate(trades):
    #     ...

    # @staticmethod
    # def calculate_average_profit(trades):
    #     ...

    # @staticmethod
    # def calculate_profit_factor(trades):
    #     ...