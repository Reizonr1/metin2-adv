#Check this:
import stringCommander

#Add under:
import uisupportsystem

#Check this:

		self.console = consoleModule.ConsoleWindow()
		self.console.BindGameClass(self)
		self.console.SetConsoleSize(wndMgr.GetScreenWidth(), 200)
		self.console.Hide()
		
#Add under:

		self.supportpg = uisupportsystem.SupportMainGui()
		
#Check this:

		self.ClearDictionary()

#Add under:

		self.supportpg.Close()
		
#Check this:

		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()
		
#Add under:

		onClickKeyDict[app.DIK_X] = lambda: self.OpenSupportGui()
		
#Check this:

			"lover_login"			: self.__LoginLover,
			"lover_logout"			: self.__LogoutLover,
			"lover_near"			: self.__LoverNear,
			"lover_far"				: self.__LoverFar,
			"lover_divorce"			: self.__LoverDivorce,
			"PlayMusic"				: self.__PlayMusic,
			
#Add under:

			"SupportLv"					: self.SetSupportLevel,
			"SupportName"				: self.SetSupportName,
			"SupportLeave"				: self.SupportLeave,
			"SupporInt"					: self.SupportInt,
			"SupportExp"				: self.SetSupportExp,
			"SupportIcon"				: self.SetSupportIcon,
			"SupportSpeciality"			: self.SetSupportSpeciality,
			
			
#Add this at the end of file:
	def OpenSupportGui(self):
		if constInfo.SUPPORTGUI == 0:
			self.supportpg.Show()
			self.supportpg.SetTop()
			constInfo.SUPPORTGUI = 1
		else:
			self.supportpg.Close()
			constInfo.SUPPORTGUI = 0
			
	def SetSupportLevel(self, level):
		self.supportpg.SetLevel(level)
		constInfo.SUPPORTLEVEL = int(level)
		
	def SetSupportName(self, name, name2):
		self.supportpg.SetName(name, name2)	
		
	def SupportLeave(self):
		self.supportpg.SetDefaultInfo()
		self.supportpg.Close()
	
	def SupportInt(self , ints):
		self.supportpg.SetInt(ints)
		
	def SetSupportExp(self, exp, exptot):
		if int(exptot) > 0:
			self.supportpg.SetExperience(exp, exptot)
		self.supportpg.SetExperience(exp, exptot)
		
	def SetSupportIcon(self, vnum):
		if int(vnum) > 0:
			self.supportpg.SetImageSlot(vnum)
		self.supportpg.SetImageSlot(vnum)
		
	def SetSupportSpeciality(self,speciality):
		self.supportpg.SetSpeciality(speciality)	
		