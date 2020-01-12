#Search 
import debugInfo
#Add After
import uipetsystem

#search
		self.targetBoard = uiTarget.TargetBoard()
		self.targetBoard.SetWhisperEvent(ui.__mem_func__(self.interface.OpenWhisperDialog))
		self.targetBoard.Hide()

#add After:
		
		self.petmain = uipetsystem.PetSystemMain()
		self.petmini = uipetsystem.PetSystemMini()

#Search:
		self.ClearDictionary()

#Add After:
		self.petmain.Close()
		self.petmini.Close()

#Search:

		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()

#Add After:
		onClickKeyDict[app.DIK_P] = lambda: self.OpenPetMainGui()

#Search:
			"WarUC"					: self.__GuildWar_UpdateMemberCount,
			"test_server"			: self.__EnableTestServerFlag,
			"mall"			: self.__InGameShop_Show,

#ADd After:
			"PetEvolution"			: self.SetPetEvolution,
			"PetName"				: self.SetPetName,
			"PetLevel"				: self.SetPetLevel,
			"PetDuration"			: self.SetPetDuration,
			"PetBonus"				: self.SetPetBonus,
			"PetSkill"				: self.SetPetskill,
			"PetIcon"				: self.SetPetIcon,
			"PetExp"				: self.SetPetExp,
			"PetUnsummon"			: self.PetUnsummon,
			"OpenPetIncubator"		: self.OpenPetIncubator,
			
#Search:
	# PRIVATE_SHOP_PRICE_LIST
	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)	
	# END_OF_PRIVATE_SHOP_PRICE_LIST

#Add After:
	def SetPetEvolution(self, evo):
		petname = ["Cucciolo", "Selvaggio", "Coraggioso", "Eroico"]
		self.petmain.SetEvolveName(petname[int(evo)])
	
	def SetPetName(self, name):
		if len(name) > 1 and name != "":
			self.petmini.Show()
		self.petmain.SetName(name)
	
	def SetPetLevel(self, level):
		self.petmain.SetLevel(level)
	
	def SetPetDuration(self, dur, durt):
		if int(durt) > 0:
			self.petmini.SetDuration(dur, durt)
		self.petmain.SetDuration(dur, durt)
	
	def SetPetBonus(self, hp, dif, sp):
		self.petmain.SetHp(hp)
		self.petmain.SetDef(dif)
		self.petmain.SetSp(sp)
		
	def SetPetskill(self, slot, idx, lv):
		if int(lv) > 0:
			self.petmini.SetSkill(slot, idx, lv)
		self.petmain.SetSkill(slot, idx, lv)
		self.affectShower.BINARY_NEW_AddAffect(5400+int(idx),int(constInfo.LASTAFFECT_POINT)+1,int(constInfo.LASTAFFECT_VALUE)+1, 0)
		if int(slot)==0:
			constInfo.SKILL_PET1=5400+int(idx)
		if int(slot)==1:
			constInfo.SKILL_PET2=5400+int(idx)
		if int(slot)==2:
			constInfo.SKILL_PET3=5400+int(idx)

	def SetPetIcon(self, vnum):
		if int(vnum) > 0:
			self.petmini.SetImageSlot(vnum)
		self.petmain.SetImageSlot(vnum)
		
	def SetPetExp(self, exp, expi, exptot):
		if int(exptot) > 0:
			self.petmini.SetExperience(exp, expi, exptot)
		self.petmain.SetExperience(exp, expi, exptot)
		
	def PetUnsummon(self):
		self.petmini.SetDefaultInfo()
		self.petmini.Close()
		self.petmain.SetDefaultInfo()
		self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET1),0)
		self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET2),0)
		self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET3),0)
		constInfo.SKILL_PET1 = 0
		constInfo.SKILL_PET2 = 0
		constInfo.SKILL_PET3 = 0
	
	def OpenPetMainGui(self):
		self.petmain.Show()
		self.petmain.SetTop()
		
	
	def OpenPetIncubator(self, pet_new = 0):
		import uipetincubatrice
		self.petinc = uipetincubatrice.PetSystemIncubator(pet_new)
		self.petinc.Show()
		self.petinc.SetTop()
		
	def OpenPetMini(self):
		self.petmini.Show()
		self.petmini.SetTop()
		
	def OpenPetFeed(self):
		
		self.feedwind = uipetfeed.PetFeedWindow()
		self.feedwind.Show()
		self.feedwind.SetTop()

	def Gift_Show(self):
		if constInfo.PET_MAIN == 0:
			self.petmain.Show()
			constInfo.PET_MAIN =1
			self.petmain.SetTop()
		else:
			self.petmain.Hide()
			constInfo.PET_MAIN =0

