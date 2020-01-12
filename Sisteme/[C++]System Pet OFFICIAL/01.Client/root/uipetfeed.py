import os
import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import localeInfo
import constInfo
import ime
import wndMgr

class PetFeedWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.arryfeed = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
		self.__LoadWindow()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)
			
	def Close(self):
		for x in range(len(self.arryfeed)):
			self.arryfeed[x] = -1
			self.petslot.ClearSlot(x)
			self.petslot.RefreshSlot()
		self.Hide()
		constInfo.FEEDWIND = 0
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetFeedWindow.py")
		except:
			import exception
			exception.Abort("PetFeedWindow.LoadWindow.LoadObject")
			
		try:
			self.petfeed = self.GetChild("board")
			self.closebtn = self.GetChild("PetFeed_TitleBar")
			self.petslot = self.GetChild("FeedItemSlot")
			self.feedbtn = self.GetChild("FeedButton")
			
			##PetSlot
			
			self.petslot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.petslot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
			self.petslot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			self.petslot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
			
			##Event secondari
			
			self.feedbtn.SetEvent(ui.__mem_func__(self.SendPetItem))
			self.closebtn.SetCloseEvent(self.Close)
			
			
		except:
			import exception
			exception.Abort("PetFeedWindow.LoadWindow.BindObject")
	
	def SelectEmptySlot(self, selectedSlotPos):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "Empty"+str(selectedSlotPos))		

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			if attachedItemCount > 1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Non e' possibile inserire oggetti sovrapposti")
				return
			if attachedItemCount == 1:
				attachedItemCount = 0
				
			if player.SLOT_TYPE_INVENTORY == attachedSlotType and not attachedSlotPos in self.arryfeed:
				itemCount = player.GetItemCount(attachedSlotPos)
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				self.arryfeed[selectedSlotPos] = attachedSlotPos
				self.petslot.SetItemSlot(selectedSlotPos, attachedItemIndex, attachedItemCount)

			mouseModule.mouseController.DeattachObject()
	
	def SelectItemSlot(self, itemSlotIndex):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Select"+str(itemSlotIndex))
		self.arryfeed[itemSlotIndex] = -1
		self.petslot.ClearSlot(itemSlotIndex)
		self.petslot.RefreshSlot()
	
	def UseItemSlot(self, slotIndex):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Select"+str(slotIndex))
		
	def SendPetItem(self):
		for i in range(len(self.arryfeed)):
			if self.arryfeed[i] != -1:
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "Oggetto inviato in pos"+str(i))
				net.SendChatPacket("/cubepetadd add %d %d" % (i, self.arryfeed[i]))
		net.SendChatPacket("/feedcubepet %d" % (constInfo.FEEDWIND))
		for x in range(len(self.arryfeed)):
			self.arryfeed[x] = -1
			self.petslot.ClearSlot(x)
			self.petslot.RefreshSlot()
		


