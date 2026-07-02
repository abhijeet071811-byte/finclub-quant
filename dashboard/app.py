import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Portfolio Simulator",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Portfolio Simulator Dashboard")
st.markdown("---")

# ----------------------------
# Load Data
# ----------------------------
equity_curve = pd.read_csv("storage/equity_curve.csv")
trades = pd.read_csv("storage/trades.csv")
portfolio = pd.read_csv("storage/portfolio.csv")

# ----------------------------
# Calculate Metrics
# ----------------------------

initial_value = equity_curve["Portfolio Value"].iloc[0]
final_value = equity_curve["Portfolio Value"].iloc[-1]

total_return = ((final_value-initial_value)/initial_value)*100

daily_returns = equity_curve["Portfolio Value"].pct_change().dropna()

volatility = daily_returns.std()

sharpe = 0

if volatility != 0:
    sharpe = (daily_returns.mean()/volatility)

rolling_max = equity_curve["Portfolio Value"].cummax()

drawdown = (equity_curve["Portfolio Value"]-rolling_max)/rolling_max

max_drawdown = drawdown.min()*100

# Win Rate

profits=[]

buy_price=None
qty=None

for _,row in trades.iterrows():

    if row["Action"]=="BUY":
        buy_price=row["Price"]
        qty=row["Quantity"]

    elif row["Action"]=="SELL":
        profits.append((row["Price"]-buy_price)*qty)

if len(profits)>0:
    win_rate=100*sum(p>0 for p in profits)/len(profits)
else:
    win_rate=0

# ----------------------------
# Top Metrics
# ----------------------------

col1,col2,col3,col4=st.columns(4)

col1.metric(
    "Portfolio Value",
    f"₹{final_value:,.2f}"
)

col2.metric(
    "Total Return",
    f"{total_return:.2f}%"
)

col3.metric(
    "Sharpe Ratio",
    f"{sharpe:.2f}"
)

col4.metric(
    "Max Drawdown",
    f"{max_drawdown:.2f}%"
)

st.markdown("")

col5,col6,col7=st.columns(3)

col5.metric(
    "Volatility",
    f"{volatility:.5f}"
)

col6.metric(
    "Win Rate",
    f"{win_rate:.2f}%"
)

col7.metric(
    "Total Trades",
    len(profits)
)

st.markdown("---")

# ----------------------------
# Equity Curve
# ----------------------------

st.subheader("📊 Portfolio Equity Curve")

equity_curve["Date"]=pd.to_datetime(equity_curve["Date"])
equity_curve=equity_curve.set_index("Date")

st.line_chart(equity_curve["Portfolio Value"])

st.markdown("---")

# ----------------------------
# Portfolio Holdings
# ----------------------------

st.subheader("💼 Current Portfolio")

st.dataframe(
    portfolio,
    use_container_width=True
)

st.markdown("---")

# ----------------------------
# Trade History
# ----------------------------

st.subheader("📜 Trade History")

st.dataframe(
    trades,
    use_container_width=True
)

st.markdown("---")

# ----------------------------
# Daily Returns
# ----------------------------

st.subheader("📈 Daily Returns")

returns_df=pd.DataFrame(
    {
        "Daily Return":daily_returns
    }
)

st.bar_chart(returns_df)