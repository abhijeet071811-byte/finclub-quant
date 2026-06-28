from data.download import download_stock

data = download_stock("RELIANCE.NS","6mo")

data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()

data["Signal"] = (data["SMA20"] > data["SMA50"]).astype(int)

for i in range(len(data["Signal"])):
    if i==0:
        data.loc[i,"Sigout"]="Hold"
    else:
        if (data.loc[i,"Signal"]-data.loc[i-1,"Signal"])==1: 
            data.loc[i,"Sigout"]="Buy"
        elif (data.loc[i,"Signal"]-data.loc[i-1,"Signal"])==-1:
            data.loc[i,"Sigout"]="Sell"
        else :
            data.loc[i,"Sigout"]="Hold"
print(data.loc[data["Sigout"]=="Sell"])