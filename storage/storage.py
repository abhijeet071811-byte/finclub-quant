import pandas as pd
from pathlib import Path
CSV_PATH = Path(__file__).parent / "equity_curve.csv"
class Storage:

    @staticmethod
    def load_portfolio():
        if not Path('storage/portfolio.csv').exists():
            return pd.DataFrame()
        df=pd.read_csv('storage/portfolio.csv')
        return df
    
    @staticmethod
    def save_portfolio(data):
        df=pd.DataFrame(data)
        df.to_csv('storage/portfolio.csv',index=False)

    @staticmethod
    def load_trades():
        if not Path('storage/trades.csv').exists():
            return pd.DataFrame()
        df=pd.read_csv('storage/trades.csv')
        return df
    
    @staticmethod
    def save_trades(data):
        df=pd.DataFrame(data)
        df.to_csv('storage/trades.csv',index=False)

    @staticmethod
    def load_equity_curve():
        if not Path('storage/equity_curve.csv').exists():
            return pd.DataFrame()

        return pd.read_csv('storage/equity_curve.csv')

    @staticmethod
    def save_equity_curve(data):
        df = pd.DataFrame(data)
        df.to_csv('storage/equity_curve.csv', index=False)

    @staticmethod
    def append_equity_curve(date, cash, holdings, total):

        row = pd.DataFrame([{
            "Date": date,
            "Cash": cash,
            "Holdings Value": holdings,
            "Portfolio Value": total
        }])

        row.to_csv(
            CSV_PATH,  
            mode="a",
            header=not CSV_PATH.exists(),
            index=False
        )