class SMACrossover:
    def generate_signal(self,data):

        data = data.copy()

        data.columns = data.columns.get_level_values(0)

        data["SMA20"] = data["Close"].rolling(20).mean()
        data["SMA50"] = data["Close"].rolling(50).mean()

        data["Signal"] = (data["SMA20"] > data["SMA50"]).astype(int)

        return data

