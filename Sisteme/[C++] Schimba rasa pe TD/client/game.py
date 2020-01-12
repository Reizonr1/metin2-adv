##Pe tasta F5:

#Cauta 
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		
#si adauga:
		onPressKeyDict[app.DIK_F5]	= lambda : self.__toggleRace()
		
#Cauta:
	def __PressNumKey(self,num):
	
#Si adauga deasupra:
	def __toggleRace(self):
		import uichangerace
		c = uichangerace.ChangeRace()
		c.Show()
