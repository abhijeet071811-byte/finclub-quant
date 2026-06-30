from storage.storage import Storage

class Executor:

    def execute(self,signal_data,portfolio,ticker):

        signal_col = signal_data.columns.get_loc("Signal")

        close_col = signal_data.columns.get_loc("Close")

        for i in range(1,len(signal_data)):

            prev_signal = signal_data.iloc[i-1,signal_col]

            current_signal = signal_data.iloc[i,signal_col]

            price = signal_data.iloc[i,close_col]

            if prev_signal == 0 and current_signal == 1:

                portfolio.buy(price, ticker)

            elif prev_signal == 1 and current_signal == 0:

                portfolio.sell(price, ticker)
            
            today_value = portfolio.portfolio_value({ticker: price})
            today_date = signal_data.iloc[i]["Date"]

            Storage.append_equity_curve(
                today_date,
                portfolio.cash,
                today_value - portfolio.cash,
                today_value
            )
