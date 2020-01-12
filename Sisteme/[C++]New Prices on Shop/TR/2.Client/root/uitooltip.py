#Bul
def SetShopItem(self, slotIndex):

#İçindeki 
else:
	self.AppendPrice(price)
	
#Değiştir

		else:
			if item.IsAntiFlag(item.ANTIFLAG_SHOP_SECONDARY):
				self.miktar(price)
			elif item.IsAntiFlag(item.ANTIFLAG_SHOP_TRIPLE):
				self.miktar2(price)
			else:
				self.AppendPrice(price)
#Bul

	def AppendPrice(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
#Ekle

	def miktar(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE_NEW  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
		
	def miktar2(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE_NEW_2  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))