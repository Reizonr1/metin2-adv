import localegame
import gameInfo

class SafeboxWindow(ui.ScriptWindow):
	def SelectEmptySlot(self, selectedSlotPos):

		if attachedSlotPos in uidice.ItemSlot:
				mouseModule.mouseController.DeattachObject()
				return

	def OnUpdate(self):
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			self.Close()

class MallWindow(ui.ScriptWindow):

	def OnUpdate(self):
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			self.Close()