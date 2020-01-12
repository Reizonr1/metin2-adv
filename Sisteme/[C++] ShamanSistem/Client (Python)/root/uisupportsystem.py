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
import uiToolTip


AFFECT_DICT = {
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
	}
	
	
def checkdiv(n):
	x = str(n/10.0)
	if len(x) > 3:
		return str(x)[0:3]
	return str(x)

def pointop(n):
	t = int(n)
	if t / 10 < 1:
		return "0."+n
	else:		
		return n[0:len(n)-1]+"."+n[len(n)-1:]
		
class SupportMainGui(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self, y):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignLeft()
			textLine.SetOutline()
			textLine.Show()
			self.y = y
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 60 + self.y)

	def __init__(self, vnum = 0):
		ui.ScriptWindow.__init__(self)
		self.vnum = vnum
		self.__LoadWindow()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		constInfo.SUPPORTGUI = 0
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE	

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/supportinformationwindow.py")
		except:
			import exception
			exception.Abort("supportinformationwindow.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("board")
			self.boardclose = self.GetChild("CloseButton")
			
			self.slotimage = self.GetChild("SlotSupportImage")
			self.supportname = self.GetChild("SupportsName")
			self.speciality = self.GetChild("SpecialityValue")
			
			self.suppexp = self.GetChild("UpBringing_Support_EXP_Gauge_Board")
			self.tooltipexp = []
			for i in range(0,4):
				self.tooltipexp.append(self.TextToolTip(15*i))
				self.tooltipexp[i].Hide()
						
			self.supportlvl = self.GetChild("LevelValue")
			self.combSlot = self.GetChild("CombSlot")
			self.petexpa = self.GetChild("UpBringing_Support_EXPGauge_01")
			self.petexpb = self.GetChild("UpBringing_Support_EXPGauge_02")
			self.petexpc = self.GetChild("UpBringing_Support_EXPGauge_03")
			self.petexpd = self.GetChild("UpBringing_Support_EXPGauge_04")
			self.petexppages = []			
			self.petexppages.append(self.petexpa)
			self.petexppages.append(self.petexpb)
			self.petexppages.append(self.petexpc)
			self.petexppages.append(self.petexpd)
			
			for exp in self.petexppages:
				exp.SetSize(0, 0)
			
			self.supportint = self.GetChild("SupportIntValue")
			self.SetDefaultInfo()
			self.boardclose.SetEvent(ui.__mem_func__(self.Close,))
			self.combSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))

		except:
			import exception
			exception.Abort("PetInformationWindow.LoadWindow.BindObject")

	def SetDefaultInfo(self):
		self.supportname.SetText("")
		self.speciality.SetText("")
		self.supportlvl.SetText("")
		self.supportint.SetText("")
		
		self.slotimage.ClearSlot(0)
		for i in xrange(4):
			self.combSlot.ClearSlot(i)
		self.SetExperience(0,0)

	def SetImageSlot(self, vnum):
		self.slotimage.SetItemSlot(0, int(vnum), 0)
		self.slotimage.SetAlwaysRenderCoverButton(0, True)
	
	def SetName(self, name , name2):
		real_name = name + name2
		self.supportname.SetText(real_name)
	
	def SetLevel(self, level):
		self.supportlvl.SetText(level)
		
	def SetSpeciality(self, speciality):
		self.speciality.SetText(speciality)
		
	def SetInt(self, ints):
		self.supportint.SetText(ints +"%")
			
	def SetExperience(self, expm, exptot):
		expm = int(expm)
		exptot = int(exptot)
		
		if exptot > 0:	
			totalexp = exptot
			totexpm = int(float(totalexp) / 100 * 100 )
			totexpi = totalexp - totexpm
			expmp =  float(expm) / totexpm * 100
		else:
			totalexp = 0
			totexpm = 0
			totexpi = 0
			expmp =  0
			
		
		curPoint = int(min(expm, totexpm))
		curPoint = int(max(expm, 0))
		maxPoint = int(max(totexpm, 0))
		
		maxPointi = int(max(totexpi, 0))

		quarterPoint = maxPoint / 4
		quarterPointi = maxPointi 
		FullCount = 0

		if 0 != quarterPoint:
			FullCount = min(4, curPoint / quarterPoint)

		for i in xrange(3):
			self.petexppages[i].Hide()
			
		self.petexppages[3].Hide()

		for i in xrange(FullCount):
			self.petexppages[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.petexppages[i].Show()

		if 0 != quarterPoint:
			if FullCount < 4:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.petexppages[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.petexppages[FullCount].Show()
			
		#####
		self.tooltipexp[0].SetText("Experience : %d of %d" % (expm, totexpm))
		self.tooltipexp[1].SetText("Experience : %.2f%%" % expmp)
	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			targetIndex = player.GetItemIndex(attachedSlotPos)
			if attachedSlotType != player.SLOT_TYPE_INVENTORY:
				return
				
			mouseModule.mouseController.DeattachObject()
				
			item.SelectItem(targetIndex)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			itemVnum = player.GetItemIndex(attachedSlotPos)
			if itemType != item.ITEM_TYPE_COSTUME:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT3)
				return
				
			if app.ENABLE_SASH_SYSTEM:
				if itemSubType == item.COSTUME_TYPE_SASH:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "<Support System> You can not put this item!")
					return
				
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Support System> You can not put this item. Your support is male!")
				return
				
			self.combSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
	
			if selectedSlotPos == 1:
				net.SendChatPacket("/support_system %s" % (str(itemVnum)))
			else:
				net.SendChatPacket("/support_system_d %s" % (str(itemVnum)))
					
			for i in xrange(4):
				self.combSlot.ClearSlot(i)
			
	def OnUpdate(self):
		if TRUE == self.suppexp.IsIn():
			for i in range(0,4):				
				self.tooltipexp[i].Show()
		else:
			for i in range(0,4):				
				self.tooltipexp[i].Hide()
	