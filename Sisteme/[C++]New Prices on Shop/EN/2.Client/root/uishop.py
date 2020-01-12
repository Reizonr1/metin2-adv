#Find

def AskBuyItem(self, slotPos):

#Find in
itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))

#Replace

			if item.IsAntiFlag(item.ANTIFLAG_SHOP_SECONDARY):
				itemBuyQuestionDialog.SetText(localeInfo.BLACK_AL(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))
			elif item.IsAntiFlag(item.ANTIFLAG_SHOP_TRIPLE):
				itemBuyQuestionDialog.SetText(localeInfo.BLACK_AL2(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))
			else:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))