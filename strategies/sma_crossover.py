class SMACrossover:
    def generate_signal(self,data):

        data = data.copy()

        data.columns = data.columns.get_level_values(0)

        data["SMA20"] = data["Close"].rolling(20).mean()
        data["SMA50"] = data["Close"].rolling(50).mean()

        data["Signal"] = (data["SMA20"] > data["SMA50"]).astype(int)

        data["Position"] = 0

        signal_col = data.columns.get_loc("Signal")
        position_col = data.columns.get_loc("Position")

        for i in range(1, len(data)):

            diff = data.iloc[i, signal_col] - data.iloc[i - 1, signal_col]

            if diff == 1:
                data.iloc[i, position_col] = 1

            elif diff == -1:
                data.iloc[i, position_col] = -1

            else :
                data.iloc[i, position_col] = 0
        return data

