import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017,8,1)
# end = datetime.date.today()
end = datetime.datetime(2017,12,30)
stock = web.DataReader("AAPL","iex-tops",start,end)
print(stock)
print("----------------------------------------------------")
print(stock.tail(5))
print(stock.describe())