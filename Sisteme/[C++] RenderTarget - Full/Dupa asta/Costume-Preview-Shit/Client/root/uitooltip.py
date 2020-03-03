Adaugi
	
import renderTarget
	
	
cauţi
	def __del__(self):
		ToolTip.__del__(self)
		
adaugi mai jos

	def CanViewRendering(self):
		race = player.GetRace()
		job = chr.RaceToJob(race)
		if not self.ANTI_FLAG_DICT.has_key(job):
			return False

		if item.IsAntiFlag(self.ANTI_FLAG_DICT[job]):
			return False

		sex = chr.RaceToSex(race)
		
		MALE = 1
		FEMALE = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			return False

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			return False

		return True

	def CanViewRenderingSex(self):
		race = player.GetRace()
		sex = chr.RaceToSex(race)
		
		MALE = 1
		FEMALE = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			return False

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			return False

		return True
		
		
cauţi:
	def __AdjustMaxWidth(self, attrSlot, desc):

Adaugi mai sus:

	def __ModelPreview(self, Vnum, test, model):
		if constInfo.DISABLE_MODEL_PREVIEW == 1:
			return

		RENDER_TARGET_INDEX = 1

		self.ModelPreviewBoard = ui.ThinBoard()
		self.ModelPreviewBoard.SetParent(self)
		self.ModelPreviewBoard.SetSize(190+10, 210+30)
		self.ModelPreviewBoard.SetPosition(-202, 0)
		self.ModelPreviewBoard.Show()

		self.ModelPreview = ui.RenderTarget()
		self.ModelPreview.SetParent(self.ModelPreviewBoard)
		self.ModelPreview.SetSize(190, 210)
		self.ModelPreview.SetPosition(5, 22)
		self.ModelPreview.SetRenderTarget(RENDER_TARGET_INDEX)
		self.ModelPreview.Show()

		self.ModelPreviewText = ui.TextLine()
		self.ModelPreviewText.SetParent(self.ModelPreviewBoard)
		self.ModelPreviewText.SetFontName(self.defFontName)
		self.ModelPreviewText.SetPackedFontColor(grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0))
		self.ModelPreviewText.SetPosition(0, 5)
		self.ModelPreviewText.SetText("Vizualizare")
		self.ModelPreviewText.SetOutline()
		self.ModelPreviewText.SetFeather(False)
		self.ModelPreviewText.SetWindowHorizontalAlignCenter()
		self.ModelPreviewText.SetHorizontalAlignCenter()
		self.ModelPreviewText.Show()
		renderTarget.SetBackground(RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(RENDER_TARGET_INDEX, model)
		if test == 2:
			renderTarget.SetArmor(RENDER_TARGET_INDEX, Vnum)
		else:
			renderTarget.SetHair(RENDER_TARGET_INDEX, Vnum)
			
	def __ModelPreviewClose(self):
		RENDER_TARGET_INDEX = 1

		if self.ModelPreviewBoard:
			self.ModelPreviewBoard.Hide()
			self.ModelPreview.Hide()
			self.ModelPreviewText.Hide()

			self.ModelPreviewBoard = None
			self.ModelPreview = None
			self.ModelPreviewText = None

			renderTarget.SetVisibility(RENDER_TARGET_INDEX, False)	
	
	def __ItemGetRace(self):
		race = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 9
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 1
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 2
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA):
			race = 3

		sex = chr.RaceToSex(player.GetRace())
		MALE = 1
		FEMALE = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			race = player.GetRace() + 4

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			race = player.GetRace()

		if race == 0:
			race = player.GetRace()

		if race == 9:
			race = 0

		return race
		
		
cauţi
class ItemToolTip(ToolTip):

deasupra lui 
	CHARACTER_NAMES = ( 

		
adaugi:

	ModelPreviewBoard = None
	ModelPreview = None
	ModelPreviewText = None
	
	
cauţi_
	### Hair Preview Image ###

adaugi mai sus 
		self.__ModelPreviewClose()

cauţi 
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, win

şi adaugi la urmă 
		sloboz = 1

Linia, arătând aşa.
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, window_type = player.INVENTORY, slotIndex = -1, transmutation = -1,  sloboz = 1):


Cauţi:
		### Armor ###
		elif item.ITEM_TYPE_ARMOR == itemType:
			self.__AppendLimitInformation()


sub:
			self.__AppendAttributeInformation(attrSlot)


adaugi:

			if sloboz != 0 and itemSubType == 0:
				itemTransmutedVnum = player.GetItemTransmutation(slotIndex)
				if itemTransmutedVnum:
					self.__ModelPreview(itemTransmutedVnum, 2, self.__ItemGetRace())	
				else:
					self.__ModelPreview(itemVnum, 2, self.__ItemGetRace())	

cauţi
		elif 0 != isCostumeItem:


modifici funcţia cu


		elif 0 != isCostumeItem:
			self.__AppendLimitInformation()
			MountVnum = item.GetValue(3)
			if sloboz != 0:
				if isCostumeHair:
					if itemVnum >= 45003 and itemVnum <= 45400:
						itemTransmutedVnum = player.GetItemTransmutation(slotIndex)
						if itemTransmutedVnum:
							item.SelectItem(itemTransmutedVnum)
							self.__ModelPreview(item.GetValue(3), 1, self.__ItemGetRace())
							item.SelectItem(itemVnum)
						else:
							self.__ModelPreview(item.GetValue(3), 1, self.__ItemGetRace())
				else:
					if itemVnum >= 41003 and itemVnum <= 42000:
						itemTransmutedVnum = player.GetItemTransmutation(slotIndex)
						if itemTransmutedVnum:
							self.__ModelPreview(itemTransmutedVnum, 2, self.__ItemGetRace())
						else:
							self.__ModelPreview(itemVnum, 2, self.__ItemGetRace())


