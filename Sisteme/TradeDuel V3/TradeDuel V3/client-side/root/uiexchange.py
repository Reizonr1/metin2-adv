import localegame
import gameInfo
import uiitemineduello

DUELLO_YAPAMASSIN = 0

class ExchangeDialog(ui.ScriptWindow):

	def OpenDialog(self):
		global DUELLO_YAPAMASSIN
		DUELLO_YAPAMASSIN = 0

	def SelectOwnerEmptySlot(self, SlotIndex):
				if SrcSlotNumber in uiitemineduello.ItemSlot:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
					mouseModule.mouseController.DeattachObject()
					return

	def OnUpdate(self):
		global DUELLO_YAPAMASSIN
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			if DUELLO_YAPAMASSIN == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_TICARET_YAPAMASSIN)
				net.SendExchangeExitPacket()	
				DUELLO_YAPAMASSIN = 1