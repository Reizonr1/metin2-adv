#Bul

def AskBuyItem(self, slotPos):

#İçindeki
itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))

#Değiştir

			if item.IsAntiFlag(item.ANTIFLAG_SHOP_SECONDARY):
				itemBuyQuestionDialog.SetText(localeInfo.BLACK_AL(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))
			elif item.IsAntiFlag(item.ANTIFLAG_SHOP_TRIPLE):
				itemBuyQuestionDialog.SetText(localeInfo.BLACK_AL2(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))
			else:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToGoldString(itemPrice)))