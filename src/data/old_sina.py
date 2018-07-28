import urllib.request
import re
import pymysql
import time

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
    # http://www.cnblogs.com/sysu-blackbear/p/3629420.html
    stockDataResponse = urllib.request.urlopen(url)
    stockData = stockDataResponse.read()
    # stockData = stockDataResponse.decode('utf8')
    stockData = stockData.decode('gbk')
    # stockData = stockData.decode('gb2312')

    print(stockData)

    return stockData


def dbStore(str_stocks):
    print(type(str_stocks))

    stocks = re.findall("\[(.*?)\]", str_stocks)
    stocks = re.findall("{(.*?)}", stocks[0])

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='stock', charset='utf8')
    # 创建游标
    cursor = conn.cursor()

    for i in range(0, len(stocks)):
        print('No.' + str(i))
        properties = stocks[i].split(',')
        #         print( properties )
        #         print( type( properties ))
        effect_rows = insertDb(properties, cursor)
    #         time.sleep(1)

    # 提交，不然无法保存新建或者修改的数据
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return effect_rows


def insertDb(properties, cursor):
    arr_values = []
    arr_columns = []

    for j in range(0, len(properties)):
        #         print( 'propertie['+ str(j)+']: ' + properties[j] )
        #         key_value = properties[j].split(':')
        #         print( key_value[0] + ' -> ' + key_value[1] )
        key = properties[j][:properties[j].find(':')]
        value = properties[j][properties[j].find(':') + 1:]
        value = value.replace('"', '')
        #         print( key + ' -> ' + value )
        #         sql += '"' + value + '"'
        arr_columns.append('`' + key + '`')
        #         arr_columns.append( key )
        arr_values.append('"' + value + '"')

    sql = 'insert into stock_sina '
    sql = sql + ' ( ' + ','.join(arr_columns) + ' ) VALUES ( ' + ','.join(arr_values) + ' ) '

    print(sql)

    effect_row = cursor.execute(sql)

    return effect_row


for i in range(1, 9999):

    print(time.strftime('%H:%M', time.localtime(time.time())))

    url = sinaStockUrl(pageNum=i)
    stockData = sinaStockData(url=url)
    if (stockData == 'null'):
        break
    effect_rows = dbStore(str_stocks=stockData)
    time.sleep(3)

print('finished.')