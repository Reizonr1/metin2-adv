#search in this file:
	BUTTON_DRAGON_SOUL = 0

#add after:
	BUTTON_PET_GUI = 1

#search in this file:
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL] = self.GetChild("DragonSoulButton")
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL].SetParent(self)

#add after:
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_PET_GUI] = self.GetChild("PetGuiButton")
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_PET_GUI].SetParent(self)
