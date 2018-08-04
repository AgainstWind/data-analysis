import urllib3
import pandas as pd
import psycopg2 as pg
import matplotlib.pyplot as plt
import traceback

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

conn = pg.connect(database="sina_stock", user="yuezht", password="postgres", host='127.0.0.1', port=5432)
cursor = conn.cursor()

def pg_create_db():
    try:
        conn = pg.connect(database="sina_stock", user="yuezht", password="postgres", host='127.0.0.1', port=5432)
        cursor = conn.cursor()
        cursor.execute('create database sina_stock')
    except Exception as e:
        print(e.args)

def pg_insert(item_dicts):
    '''
    :param item_dict:
    :return:
    '''
    for item_dict in item_dicts:
        try:
            sql = 'insert into stock_sina(symbol,code,name,trade,pricechange,changepercent,buy,sell,settlement,open,high,low,' \
                  'volume,amount,ticktime,per,pb,mktcap,nmc,turnoverratio) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',' \
                  '\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');' % (
                  item_dict.get('symbol',None), item_dict.get('code',None), item_dict.get('name',None), item_dict.get('trade',None),
                  item_dict.get('pricechange',None), item_dict.get('changepercent',None), item_dict.get('buy',None),
                  item_dict.get('sell',None), item_dict.get('settlement',None), item_dict.get('open',None), item_dict.get('high',None),
                  item_dict.get('low',None), item_dict.get('volume',None), item_dict.get('amount',None), item_dict.get('ticktime',None),
                  item_dict.get('per',None), item_dict.get('pb',None), item_dict.get('mktcap',None), item_dict.get('nmc',None),
                  item_dict.get('turnoverratio',None))
            print(sql)
            result = cursor.execute(sql)
            print(result)
        except Exception as e:
            print(e)
            # traceback.print_exc()
            #exeception_stack_str = traceback.format_exc()
    conn.commit()



if __name__=='__main__':
    main_df = pd.DataFrame(data=None,columns=data_header,index=['ticktime'])
    for i in range(1,2,1):
        url = sinaStockUrl(i)
        stock_data = sinaStockData(url)
        stock_dict = parse_js(stock_data)
        pg_insert(stock_dict)
        df = pd.DataFrame(stock_dict)
        main_df = main_df.append(df)
    main_df.plot(x=main_df['ticktime'], subplots=True)
    plt.show()
    print(main_df)

