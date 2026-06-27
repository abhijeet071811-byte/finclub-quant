from data.download import download_stock

data = download_stock("RELIANCE.NS")

print(data.tail())