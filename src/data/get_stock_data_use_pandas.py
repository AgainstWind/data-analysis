import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017,12,1)
end = datetime.date.today()
stock = web.DataReader("AAPL","iex-tops",start,end)
print(stock)

