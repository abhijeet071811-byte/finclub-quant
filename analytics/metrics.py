class Metrics:

    @staticmethod
    def calculate_total_return(equity_curve):

        if equity_curve.empty:
            return 0

        initial_value = equity_curve["Portfolio Value"].iloc[0]
        final_value = equity_curve["Portfolio Value"].iloc[-1]

        return ((final_value - initial_value) / initial_value) * 100

    # @staticmethod
    # def calculate_daily_returns(equity_curve):
    #     ...

    # @staticmethod
    # def calculate_volatility(daily_returns):
    #     ...

    # @staticmethod
    # def calculate_sharpe_ratio(daily_returns, risk_free_rate=0):
    #     ...

    # @staticmethod
    # def calculate_max_drawdown(equity_curve):
    #     ...

    # @staticmethod
    # def calculate_win_rate(trades):
    #     ...

    # @staticmethod
    # def calculate_average_profit(trades):
    #     ...

    # @staticmethod
    # def calculate_profit_factor(trades):
    #     ...