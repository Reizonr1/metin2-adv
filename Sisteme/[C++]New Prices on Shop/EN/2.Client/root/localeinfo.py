#Find
"NOT_ENOUGH_MONEY" : SHOP_NOT_ENOUGH_MONEY,
#Add
"YOKDA_AMINA_GOYACAM" : MONEY_1__,
"PARAN_YOK_OC" : MONEY_2__,

#Find
elif IsEUROPE() and not IsWE_KOREA() and not IsYMIR():
#İçinde
	def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemPrice )
			
#Add

	def BLACK_AL(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return DO_YOU_BUY_NEW_1_2 % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return DO_YOU_BUY_NEW_1 % ( buyItemName, buyItemPrice )
	def BLACK_AL2(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return DO_YOU_BUY_NEW_2_2 % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return DO_YOU_BUY_NEW_2 % ( buyItemName, buyItemPrice )