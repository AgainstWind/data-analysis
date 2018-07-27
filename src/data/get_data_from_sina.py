import urllib3

'''
create_table_stock_sina.sql
'''

def sinaStockUrl(pageNum):
    print('pageNum : ' + str(pageNum))
    rows = 10
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'
    url += 'page=' + str(pageNum)
    url += '&num=' + str(rows)
    url += '&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=init'
    print(url)
    return url


def sinaStockData(url):
    http = urllib3.PoolManager()
    stockDataResponse = http.request('GET',url)
    return stockDataResponse.data



if __name__=='__main__':
    for i in range(1,5,1):
        url = sinaStockUrl(i)
        stock_data = sinaStockData(url)
        print(stock_data)

