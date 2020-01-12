## Go at the end of the file and add:

	if app.ENABLE_SHOW_CHEST_DROP:
		def BINARY_AddChestDropInfo(self, chestVnum, pageIndex, slotIndex, itemVnum, itemCount):
			if not constInfo.CHEST_DROP_INFO_DATA.has_key(chestVnum):
				constInfo.CHEST_DROP_INFO_DATA[chestVnum] = {}
				
			if not constInfo.CHEST_DROP_INFO_DATA[chestVnum].has_key(pageIndex):
				constInfo.CHEST_DROP_INFO_DATA[chestVnum][pageIndex] = {}
	
			curList = constInfo.CHEST_DROP_INFO_DATA[chestVnum]
			
			if curList.has_key(pageIndex):
				if curList[pageIndex].has_key(slotIndex):
					if curList[pageIndex][slotIndex][0] == itemVnum and curList[pageIndex][slotIndex][1] == itemCount:
						return

			curList[pageIndex][slotIndex] = [itemVnum, itemCount]
						
		def BINARY_RefreshChestDropInfo(self, chestVnum):
			if self.interface:
				self.interface.RefreshChestDropInfo(chestVnum)