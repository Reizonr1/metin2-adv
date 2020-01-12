
Gems system fix



uisystemgems.py aç ve cauta

	def RefreshSlot(self,refresh = False):

schimba complet

	def RefreshSlot(self,refresh = False):
		getItemVNum,getItemCount,setItemVNum=player.GetItemIndex,player.GetItemCount,self.itemSlot.SetItemSlot

		if not refresh:
			for i in xrange(player.STONE_INVENTORY_SLOT_COUNT*3):
				slotNumber = item.STONE_INVENTORY_SLOT_START + i
				itemVNum = getItemVNum(slotNumber)

				if 0 == itemVNum or not item.IsMetin(itemVNum):
					continue

				itemGrade = self.CheckGradeStone(item.GetItemName())
				if itemGrade > "3":
					continue

				#if itemVNum != 50926:
				#	continue

				self.slot_inventario.append(slotNumber)
				self.slot_gui.append(self.slotPos)

				self.slotPos += 1
				if self.slotPos > 54:
					break

		itemCount = len(self.slot_inventario)
		if itemCount < 15:
			self.SetTableSize(3)

		else:
			lineCount = 3
			lineCount += (itemCount - 15) / 5
			if itemCount % 5:
				lineCount += 1
			self.SetTableSize(lineCount)

		count = 0
		for inventoryPos in self.slot_inventario:
			itemVNum = getItemVNum(inventoryPos)
			itemCount = getItemCount(inventoryPos)

			if itemCount <= 1:
				itemCount = 0

			setItemVNum(count, itemVNum, itemCount)
			count += 1
	
		self.itemSlot.RefreshSlot()
		if refresh:
			self.tooltipItem.Hide()