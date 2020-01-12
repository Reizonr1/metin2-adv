Search:
SHOP_ERROR_DICT = {
	"NOT_ENOUGH_MONEY" : SHOP_NOT_ENOUGH_MONEY,
	"SOLDOUT" : SHOP_SOLDOUT,
	"INVENTORY_FULL" : SHOP_INVENTORY_FULL,
	"INVALID_POS" : SHOP_INVALID_POS,
	"NOT_ENOUGH_MONEY_EX" : SHOP_NOT_ENOUGH_MONEY_EX,
}

Add it under:
if app.ENABLE_OFFLINE_SHOP:
	SHOP_ERROR_DICT.update({
		"NOT_ENOUGH_MONEY_COIN": SHOP_NOT_ENOUGH_MONEY_COIN,
		"NOT_ENOUGH_MONEY_GOLDBAR": SHOP_NOT_ENOUGH_MONEY_GOLDBAR,
		"NOT_ENOUGH_MONEY_WON": SHOP_NOT_ENOUGH_MONEY_WON
	})

https://puu.sh/sgY0O/18be13c139.png

--

Search:
def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
	if buyItemCount > 1 :
		return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemCount, buyItemPrice )
	else:
		return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemPrice )

Add it under:
if app.ENABLE_OFFLINE_SHOP:
	def DO_YOU_BUY_ITEM_NEW(buyItemName, buyItemCount, buyItemPrice = "0", buyItemPriceTwo = "0", buyItemPriceThree = "0", buyItemPriceFour = "0"):
		if buyItemCount > 1:
			return [DO_YOU_BUY_ITEM2_1 % ( buyItemName, buyItemCount ), DO_YOU_BUY_ITEM1_2 % ( buyItemPrice, buyItemPriceTwo, buyItemPriceThree, buyItemPriceFour) ]
		return [DO_YOU_BUY_ITEM1_1 % ( buyItemName ), DO_YOU_BUY_ITEM1_2 % ( buyItemPrice, buyItemPriceTwo, buyItemPriceThree, buyItemPriceFour) ]

https://puu.sh/sgY3w/a471c32972.png
---

Search:
def NumberToSecondaryCoinString(n) :
	if n <= 0:
		return "0 %s" % (MONETARY_UNIT_JUN)

	return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT_JUN)

Add it under:
if app.ENABLE_OFFLINE_SHOP:
	def NumberToPriceString(n, type):
		if n <= 0 :
			return "0 " + str(type)

		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), str(type))

https://puu.sh/sgY5f/6aab917b54.png
