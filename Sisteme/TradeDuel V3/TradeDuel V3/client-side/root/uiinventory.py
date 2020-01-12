import gameInfo
import event
import localegame
import uiitemineduello

class InventoryWindow(ui.ScriptWindow):

	def __init__(self):
		self.iteminevs = uiitemineduello.itemineduello()

	## Fonksiyonlarýn içine eklenecekler!!! ##
	
	def OnDetachMetinFromItem(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.OnCloseQuestionDialog()
			return

	def OpenPickMoneyDialog(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			return

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if srcItemSlotPos in uiitemineduello.ItemSlot:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
			return

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		if srcSlotPos in uiitemineduello.ItemSlot:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_KULLANAMASSIN)
			return

	def __SendUseItemPacket(self, slotPos):
		if slotPos in uiitemineduello.ItemSlot:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_KULLANAMASSIN)
			return

	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		if srcSlotPos in uiitemineduello.ItemSlot:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
			return


	def __SellItem(self, itemSlotPos):
		if itemSlotPos in uiitemineduello.ItemSlot:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
			return

	def SelectItemSlot(self, itemSlotIndex):
			if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
				mouseModule.mouseController.DeattachObject()
				return
				
			if player.GetItemIndex(attachedSlotPos) == 71084 or player.GetItemIndex(attachedSlotPos) == 71085:
				if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
					mouseModule.mouseController.DeattachObject()
					return
