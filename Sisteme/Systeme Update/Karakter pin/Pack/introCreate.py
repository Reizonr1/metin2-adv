Find - Bul:
self.editCharacterName = getChild("character_name_value")

Add it under- Altına ekle:
self.editCharacterPin = getChild("character_pin_value")

http://puu.sh/jSYLz/e038d68415.png


Find - Bul:
self.editCharacterName.SetReturnEvent(ui.__mem_func__(self.CreateCharacter))
self.editCharacterName.SetEscapeEvent(ui.__mem_func__(self.CancelCreate))

Change - Değiştir:
self.editCharacterName.SetReturnEvent(ui.__mem_func__(self.editCharacterPin.SetFocus))
self.editCharacterName.SetEscapeEvent(ui.__mem_func__(self.CancelCreate))
self.editCharacterPin.SetReturnEvent(ui.__mem_func__(self.CreateCharacter))
self.editCharacterPin.SetEscapeEvent(ui.__mem_func__(self.CancelCreate))	


http://puu.sh/jSYVM/920df7cf8d.png


Find - Bul:
self.editCharacterName.SetText("")

Change - Değiştir:
self.editCharacterName.SetText("")
self.editCharacterPin.SetText("")

http://puu.sh/jSZ6u/fcbeb29b22.png


Find - Bul:
	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE CREATE WINDOW"

		self.editCharacterName.Enable()
		self.dlgBoard.ClearDictionary()
		self.stream=0
		self.shapeButtonList = []
		self.genderButtonList = []
		self.btnCreate = 0
		self.btnCancel = 0
		self.btnPrev = 0
		self.btnNext = 0
		self.btnLeft = 0
		self.btnRight = 0
		self.textBoard = 0
		self.editCharacterName = 0
		self.backGround = None
		
Change - Değiştir:
	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE CREATE WINDOW"

		self.editCharacterName = None
		self.editCharacterPin = None
		self.dlgBoard.ClearDictionary()
		self.stream=0
		self.shapeButtonList = []
		self.genderButtonList = []
		self.btnCreate = 0
		self.btnCancel = 0
		self.btnPrev = 0
		self.btnNext = 0
		self.btnLeft = 0
		self.btnRight = 0
		self.textBoard = 0
		self.backGround = None
		
http://puu.sh/jSZbc/90b662bc93.png


Find - Bul:
self.editCharacterName.SetFocus()
self.editCharacterName.Enable()
		
Change - Değiştir:
self.editCharacterPin.SetFocus()
self.editCharacterName.SetFocus()

http://puu.sh/jSZfy/2a53179a0b.png


Find - Bul:
self.editCharacterName.Disable()

Add it under- Altına ekle:
self.editCharacterPin.Disable()

http://puu.sh/jSZxZ/ac1102ee25.png


Find - Bul:
textName = self.editCharacterName.GetText()
if False == self.__CheckCreateCharacter(textName):
	return
	
Change - Değiştir:
textName = self.editCharacterName.GetText()
if not self.__CheckCreateCharacter(textName):
	return
textPin = self.editCharacterPin.GetText()
if not textPin:
	self.PopupMessage("Pin girin", None) #Enter pin
	return
if not textPin.isdigit():
	self.PopupMessage("Pin sayi olmalidir", None) #Pin only avaible as number
	return
if textPin == 0 or textPin == "0":
	self.PopupMessage("Uygunsuz pin", None) #inappropriate pin
	return	
if len(textPin) > 9:
	self.PopupMessage("Pin 9 karakterden buyuk olamaz", None) # pin can not be larger than 9 character
	return


http://puu.sh/jSZF0/dc8b48b46b.png


Find - Bul:
net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex)

Change - Değiştir:
net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex, int(self.editCharacterPin.GetText()))

http://puu.sh/jSZ1C/8effdc551e.png