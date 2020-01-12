Search for:
	self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
down write:
	self.costume				= GetObject("costume")
Search for:
	wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))
down write:
	self.costume.SetEvent(ui.__mem_func__(self.__costume))
Search for:
	def RefreshCostumeSlot
Down this function put:
	def __costume(self):
		constInfo.costume = 1
		event.QuestButtonClick(int(constInfo.QUEST_INDEX_06))
		net.SendQuestInputStringPacket(str(constInfo.costume))