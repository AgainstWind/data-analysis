-- postgres
CREATE TABLE stock_sina (
	 symbol   char(50)  ,
	 code   char(50)  ,
	 name   char(50)  ,
	 trade   char(50)  ,
	 pricechange   char(50)  ,
	 changepercent   char(50)  ,
	 buy   char(50)  ,
	 sell   char(50)  ,
	 settlement   char(50)  ,
	 open   char(50)  ,
	 high   char(50)  ,
	 low   char(50)  ,
	 volume   char(50)  ,
	 amount   char(50)  ,
	 ticktime   char(50)  ,
	 per   char(50)  ,
	 pb   char(50)  ,
	 mktcap   char(50)  ,
	 nmc   char(50)  ,
	 turnoverratio   char(50)  ,
	 id SERIAL primary key
	);