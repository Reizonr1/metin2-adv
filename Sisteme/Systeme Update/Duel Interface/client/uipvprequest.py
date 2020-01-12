import ui
import net
import wndMgr
import playerSettingModule
import progressbar

class PVPRequestDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Title 			= 0
		self.RequesterName  = 0
		self.DuelText 		= 0
		self.CharacterIcon  = 0
		self.AcceptButton   = 0
		self.DenyButton		= 0
		self.Level			= 0
		self.VID			= 0
		self.Name 			= ""
		self.progressBar    = None
		
		self.FACE_IMAGE_DICT = {
			playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
			playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
			playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
			playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
			playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
			playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
			playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
			playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
		}

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		PythonScriptLoader = ui.PythonScriptLoader()
		PythonScriptLoader.LoadScriptFile(self, "uiscript/pvprequestdialog.py")
		
		self.AcceptButton = self.GetChild("ApplyButton")
		self.AcceptButton.SetEvent(ui.__mem_func__(self.ApplyRequest))
		
		self.DenyButton = self.GetChild("DenyButton")
		self.DenyButton.SetEvent(ui.__mem_func__(self.DenyRequest))

		self.Title = self.GetChild("Title")
		self.GetChild("TitleBar").SetCloseEvent(self.DenyRequest)
		
		self.RequesterName = self.GetChild("RequesterName")
		self.GetChild("TitleBar").SetCloseEvent(self.DenyRequest)
		
		self.DuelText = self.GetChild("DuelText")
		self.GetChild("TitleBar").SetCloseEvent(self.DenyRequest)
		
		self.CharacterIcon = self.GetChild("CharacterIcon")
		self.GetChild("TitleBar").SetCloseEvent(self.DenyRequest)
		
		self.progressBar = progressbar.ProgressBar()
		self.progressBar.SetParent(self)
		self.progressBar.SetPosition(56, 67)
		self.progressBar.SetSize(133, 11)
	
	def OpenDialog(self, Name, Level, VID, Race):
		self.Name  = Name
		self.Level = int(Level)
		self.VID   = int(VID)
		self.Race  = int(Race)
		
		self.RequesterName.SetText("  " + Name + " - Lv " + str(Level))
		self.DuelText.SetText("  Duelloyu kabul ediyor musun?") #You agree to duel?
		
		self.CharacterIcon.LoadImage(self.FACE_IMAGE_DICT[self.Race])
		
		self.progressBar.Show()
		self.Show()
		
		self.progressBar.SetWorking(TRUE)
		self.progressBar.SetCallbackEvent(ui.__mem_func__(self.DenyRequest))
		
	def DenyRequest(self):
		net.SendChatPacket("/deny_pvp %d" % (self.VID))
		self.Hide()
		
	def ApplyRequest(self):
		net.SendChatPacket("/pvp %d" % (self.VID))
		self.Hide()
				
	def Close(self):
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()
		self.Title 			= 0
		self.RequesterName  = 0
		self.CharacterIcon  = 0
		self.AcceptButton   = 0
		self.DuelText 		= 0
		self.Level			= 0
		self.Name 			= ""
		self.progressBar    = None

