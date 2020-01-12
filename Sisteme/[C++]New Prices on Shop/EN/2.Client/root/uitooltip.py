#Find
def SetShopItem(self, slotIndex):

#Find in 
else:
	self.AppendPrice(price)
	
#Replace

		else:
			if item.IsAntiFlag(item.ANTIFLAG_SHOP_SECONDARY):
				self.miktar(price)
			elif item.IsAntiFlag(item.ANTIFLAG_SHOP_TRIPLE):
				self.miktar2(price)
			else:
				self.AppendPrice(price)
#Find

	def AppendPrice(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
#Add

	def miktar(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE_NEW  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
		
	def miktar2(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE_NEW_2  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))