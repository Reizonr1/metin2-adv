Ýmportlarýn arasýna aþþaðýdakini ekleyin ;

import uiOfflineShopBuilder

Aþþaðýdaki kodu arat ;

	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()

Yukardaki kod bloðunu komple aþþaðýdaki ile deðiþtirin ;

	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()
		uiOfflineShopBuilder.UpdateADBoard()
