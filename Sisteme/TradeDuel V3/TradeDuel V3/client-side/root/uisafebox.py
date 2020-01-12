import uiitemineduello
import localegame
import gameInfo

class SafeboxWindow(ui.ScriptWindow):
	def SelectEmptySlot(self, selectedSlotPos):

		if attachedSlotPos in uiitemineduello.ItemSlot:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
				mouseModule.mouseController.DeattachObject()
				return

	def OnUpdate(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()

class MallWindow(ui.ScriptWindow):

	def OnUpdate(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()