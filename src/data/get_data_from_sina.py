import urllib3

'''
create_table_stock_sina.sql
'''
data_header = ['symbol','code','name','trade','pricechange','changepercent','buy','sell','settlement','open','high',
               'low','volume','amount','ticktime','per','pb','mktcap','nmc','turnoverratio' ]

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
    return str(stockDataResponse.data,encoding='gbk')

def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
    return obj

'''
b'[{symbol:"sh600000",code:"600000",name:"\xc6\xd6\xb7\xa2\xd2\xf8\xd0\xd0",trade:"9.990",pricechange:"0.030",
changepercent:"0.301",buy:"9.990",sell:"10.000",settlement:"9.960",open:"9.960",high:"10.040",low:"9.930"
volume:12120067,amount:121060815,ticktime:"15:00:00",per:5.429,pb:0.736,mktcap:29322728.316603,nmc:28075311.983601,
turnoverratio:0.04313}]'
'''


def dict2array(dictt):
    try:
       arry = []
       for key in data_header:
            if key in dictt:
                arry.append(dictt.get(key))
       print(arry)
       return arry
    except Exception as e:
        print(e.args)
        return None





import pandas as pd

if __name__=='__main__':
    main_df = pd.DataFrame(data=None,columns=data_header)
    for i in range(1,2,1):
        url = sinaStockUrl(i)
        stock_data = sinaStockData(url)
        stock_dict = parse_js(stock_data)
        df = pd.DataFrame(stock_dict)
        main_df = main_df.append(df)

    print(main_df)

