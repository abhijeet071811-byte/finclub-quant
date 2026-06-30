from data.download import download_stock
from strategies.sma_crossover import SMACrossover
from portfolio.portfolio import Portfolio
from Execution.Executor import Executor
from storage.storage import Storage
from analytics.performance import get_summary

from pathlib import Path

Path("storage/equity_curve.csv").unlink(missing_ok=True)
Path("storage/trades.csv").unlink(missing_ok=True)
Path("storage/portfolio.csv").unlink(missing_ok=True)

ticker = "TCS.NS"

# Download Data
data = download_stock(ticker, "6mo")

# Generate Signals
strategy = SMACrossover()
signal_data = strategy.generate_signal(data)

# Create Portfolio
portfolio = Portfolio()

# Execute Trades
executor = Executor()
executor.execute(signal_data, portfolio, ticker)

# Get Latest Price
latest_price = signal_data["Close"].iloc[-1]

current_prices = {
    ticker: latest_price
}

Storage.save_trades(portfolio.trade_history)

portfolio_data = [{
    "Cash": portfolio.cash,
    "Holdings": str(portfolio.holdings)
}]

Storage.save_portfolio(portfolio_data)


print("\nPortfolio Summary")
print("-" * 40)
print("Cash:", portfolio.cash)
print("Holdings:", portfolio.holdings)
print("Portfolio Value:", portfolio.portfolio_value(current_prices))
print("Trade History:")

for trade in portfolio.trade_history:
    print(trade)



summary=get_summary()
print(summary)