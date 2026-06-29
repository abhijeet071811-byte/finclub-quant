from data.download import download_stock
from strategies.sma_crossover import SMACrossover
from portfolio.portfolio import Portfolio
from Execution.Executor import Executor

ticker = "RELIANCE.NS"

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

print("\nPortfolio Summary")
print("-" * 40)
print("Cash:", portfolio.cash)
print("Holdings:", portfolio.holdings)
print("Portfolio Value:", portfolio.portfolio_value(current_prices))
print("Trade History:")

for trade in portfolio.trade_history:
    print(trade)