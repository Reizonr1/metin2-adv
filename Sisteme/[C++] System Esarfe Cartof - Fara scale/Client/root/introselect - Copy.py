""""""
#1) Search: hair = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_HAIR)
#2) Make a new line and paste:
			acce = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_ACCE)
""""""

""""""
#1) Search: self.MakeCharacter(index, id, name, race, form, hair)
#2) Delete this line and paste:
				self.MakeCharacter(index, id, name, race, form, hair, acce)
""""""

""""""
#1) Search: def MakeCharacter(self, index, id, name, race, form, hair):
#2) Delete their function and paste:
	def MakeCharacter(self, index, id, name, race, form, hair, acce):
		if 0 == id:
			return
		
		chr.CreateInstance(index)
		chr.SelectInstance(index)
		chr.SetVirtualID(index)
		chr.SetNameString(name)
		
		chr.SetRace(race)
		chr.SetArmor(form)
		chr.SetHair(hair)
		chr.SetAcce(acce)
		chr.Refresh()
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)
		chr.SetRotation(0.0)
""""""