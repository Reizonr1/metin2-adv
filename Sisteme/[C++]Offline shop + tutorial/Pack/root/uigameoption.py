�mportlar�n aras�na a��a��dakini ekleyin ;

import uiOfflineShopBuilder

A��a��daki kodu arat ;

	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()

Yukardaki kod blo�unu komple a��a��daki ile de�i�tirin ;

	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()
		uiOfflineShopBuilder.UpdateADBoard()
