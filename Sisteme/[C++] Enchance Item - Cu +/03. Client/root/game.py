""""""
#1) Search: self.serverCommander.SAFE_RegisterCallBack(serverCommandItem[0], serverCommandItem[1])
#2) After this make a new line and paste:
		if app.ENABLE_NEW_ENCHANT_ATTR:
			self.serverCommander.SAFE_RegisterCallBack("EnchantAttr_open", self.__OpenEnchantAttr)
""""""

""""""
#1) Search: def BINARY_ServerCommand_Run(self, line):
#2) Before this a new line and paste:
	if app.ENABLE_NEW_ENCHANT_ATTR:
		def __OpenEnchantAttr(self, cell):
			if self.interface:
				new_cell = int(cell.split("#")[1])
				attrType0 = int(cell.split("#")[2])
				attrValue0 = int(cell.split("#")[3])
				attrType1 = int(cell.split("#")[4])
				attrValue1 = int(cell.split("#")[5])
				attrType2 = int(cell.split("#")[6])
				attrValue2 = int(cell.split("#")[7])
				attrType3 = int(cell.split("#")[8])
				attrValue3 = int(cell.split("#")[9])
				attrType4 = int(cell.split("#")[10])
				attrValue4 = int(cell.split("#")[11])
				new_attrSlot = [
									[attrType0, attrValue0],
									[attrType1, attrValue1],
									[attrType2, attrValue2],
									[attrType3, attrValue3],
									[attrType4, attrValue4],
				]
				
				self.interface.OpenEnchantAttrWindow(new_cell, new_attrSlot)
""""""