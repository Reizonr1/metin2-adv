import gameInfo
import event
import localegame
import uidice

class InventoryWindow(ui.ScriptWindow):

	## Fonksiyonlarýn içine eklenecekler!!! ##
	
	def OnDetachMetinFromItem(self):
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			self.OnCloseQuestionDialog()
			return

	def OpenPickMoneyDialog(self):
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			return

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if srcItemSlotPos in uidice.ItemSlot:
			return

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		if srcSlotPos in uidice.ItemSlot:
			return
			
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			return

	def __SendUseItemPacket(self, slotPos):
		if slotPos in uidice.ItemSlot:
			return
			
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			return

	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		if srcSlotPos in uidice.ItemSlot:
			return
		

	def __SellItem(self, itemSlotPos):
		if itemSlotPos in uidice.ItemSlot:
			return

	def SelectItemSlot(self, itemSlotIndex):
			if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
				mouseModule.mouseController.DeattachObject()
				return
				
			if player.GetItemIndex(attachedSlotPos) == 71084 or player.GetItemIndex(attachedSlotPos) == 71085:
				if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
					mouseModule.mouseController.DeattachObject()
					return
