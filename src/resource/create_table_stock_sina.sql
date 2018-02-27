CREATE TABLE `stock_sina` (
	`symbol` VARCHAR(50) NULL DEFAULT NULL,
	`code` VARCHAR(50) NULL DEFAULT NULL,
	`name` VARCHAR(50) NULL DEFAULT NULL,
	`trade` VARCHAR(50) NULL DEFAULT NULL,
	`pricechange` VARCHAR(50) NULL DEFAULT NULL,
	`changepercent` VARCHAR(50) NULL DEFAULT NULL,
	`buy` VARCHAR(50) NULL DEFAULT NULL,
	`sell` VARCHAR(50) NULL DEFAULT NULL,
	`settlement` VARCHAR(50) NULL DEFAULT NULL,
	`open` VARCHAR(50) NULL DEFAULT NULL,
	`high` VARCHAR(50) NULL DEFAULT NULL,
	`low` VARCHAR(50) NULL DEFAULT NULL,
	`volume` VARCHAR(50) NULL DEFAULT NULL,
	`amount` VARCHAR(50) NULL DEFAULT NULL,
	`ticktime` VARCHAR(50) NULL DEFAULT NULL,
	`per` VARCHAR(50) NULL DEFAULT NULL,
	`pb` VARCHAR(50) NULL DEFAULT NULL,
	`mktcap` VARCHAR(50) NULL DEFAULT NULL,
	`nmc` VARCHAR(50) NULL DEFAULT NULL,
	`turnoverratio` VARCHAR(50) NULL DEFAULT NULL,
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`id`)
)
COMMENT='insert into stock_sina  ( `symbol`,`code`,`name`,`trade`,`pricechange`,`changepercent`,`buy`,`sell`,`settlement`,`open`,`high`,`low`,`volume`,`amount`,`ticktime`,`per`,`pb`,`mktcap`,`nmc`,`turnoverratio` ) \r\nVALUES ( "sh600000","600000","浦发银行","12.630","-0.100","-0.786","12.630","12.640","12.730","12.750","12.760","12.610","21138263","267909168","11:11:06","5.254","0.957","37071677.541411","35495053.804437","0.07522" ) \r\n'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=11
;