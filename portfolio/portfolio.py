import math

class Portfolio:
    def __init__(self, initial_cash=100000, allocation=0.20):
        self.cash = initial_cash
        self.allocation = allocation
        self.holdings = {}
        self.trade_history = []

    def buy(self,price,ticker):
        
        investment=self.cash*self.allocation
        quantity=math.floor(investment / price)

        if quantity == 0:
            return

        self.cash=self.cash-quantity * price
        self.holdings[ticker] = self.holdings.get(ticker, 0) + quantity

        self.trade_history.append({
            "Ticker": ticker,
            "Action": "BUY",
            "Quantity": quantity,
            "Price": price,
        })

    def sell(self, price, ticker):
        if ticker not in self.holdings or self.holdings[ticker] == 0:
            return

        quantity = self.holdings[ticker]

        self.cash += quantity * price
        self.holdings[ticker] = 0

        self.trade_history.append({
            "Ticker": ticker,
            "Action": "SELL",
            "Quantity": quantity,
            "Price": price,
        })

    def portfolio_value(self, current_prices):
        total_value = self.cash

        for ticker, quantity in self.holdings.items():
            if ticker in current_prices:
                total_value += quantity * current_prices[ticker]

        return total_value
