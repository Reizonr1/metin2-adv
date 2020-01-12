*uiAffectShower.py

Find - Bul:
class HorseImage(ui.ExpandedImageBox):

Add it upper - Üstüne ekle:
class CPlayTime(ui.ExpandedImageBox):
	FILE_PATH = "locale/tr/ui/playtime/"
	
	FILE_DICT = {
		00 : FILE_PATH+"B-1.dds",
		10 : FILE_PATH+"Y-3.dds",
		15 : FILE_PATH+"Y-2.dds",
		20 : FILE_PATH+"Y-1.dds",
		25 : FILE_PATH+"G-3.dds",
		35 : FILE_PATH+"G-2.dds",
		40 : FILE_PATH+"G-1.dds",
	}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)
		
		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

	def CalcPlayTime(self, start_time):
		start_time = int(start_time)
		if not start_time:
			return 0
		elif start_time <= 10:
			return 00
		elif start_time > 10 and start_time <= 30:
			return 10
		elif start_time > 30 and start_time <= 60:
			return 15
		elif start_time > 60 and start_time <= 90:
			return 20
		elif start_time > 90 and start_time <= 120:
			return 25
		elif start_time > 120 and start_time <= 150:
			return 35
		elif start_time >= 180:
			return 40
		else:
			return 0
	
	def ConvertMin(self, x):
		while int(x) >= 60:
			x = x - 60
		return x
	
	def SetPlayTime(self, time):
		self.toolTip.ClearToolTip()

		if int(time) == 0:
			self.__AppendText("Kisa bir suredir aktifsin") # You're active a short time
		elif int(time) > 60:
			self.__AppendText("%s saat" % (str(int(time) / 60))) # %s hour
			self.__AppendText("%s dakikadir aktifsin" % (str(self.ConvertMin(time)))) # %s minute you are active
		else:
			self.__AppendText("%s dakikadir aktifsin" % (str(time))) # You are active from %s minute

		try:
			fileName=self.FILE_DICT[self.CalcPlayTime(time)]
		except KeyError:
			import exception
			exception.Abort("PlayTime(time=%d, calctime=%d) - KeyError" % (int(time), int(self.CalcPlayTime(time))))

		try:
			self.LoadImage(fileName)
		except:
			import exception
			exception.Abort("PlayTime(time=%d, calctime=%d) - LoadError %s" % (int(time), int(self.CalcPlayTime(time))))

		self.SetScale(0.7, 0.7)
	
	def OnUpdatePlayTime(self, time):
		self.SetPlayTime(time)
	
	def __AppendText(self, text):
		self.toolTip.AppendTextLine(text)
		self.toolTip.ResizeToolTip()

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()
		

		
Arat ve sil - Find and remove:
		self.serverPlayTime=0
		self.clientPlayTime=0
		

		
Find - Bul:
self.lovePointImage=None

Add it under- Altýna ekle:
self.playTimeImage=None

/ TEKRAR /
Find - Bul:
self.lovePointImage=None

Add it under- Altýna ekle:
self.playTimeImage=None

http://puu.sh/kmxiu/5ee5aaf1b9.png



Find - Bul:
def SetPlayTime(self, playTime):

Fonksiyonu komple deðiþtir - Change function with this:
	def SetPlayTime(self, playTime):
		image = CPlayTime()
		image.SetParent(self)
		image.SetPlayTime(playTime)
		image.Show()

		self.playTimeImage=image
		self.__ArrangeImageList()
		
	def OnUpdatePlayTime(self, play_time):
		if self.playTimeImage:
			self.playTimeImage.OnUpdatePlayTime(play_time)

	
http://puu.sh/kmxlH/843c61e9c2.png




Find - Bul:
		if self.horseImage:
			width+=self.IMAGE_STEP
			
Add it under- Altýna ekle:
		if self.playTimeImage:
			width+=self.IMAGE_STEP
			
Find - Bul:
		if self.horseImage:
			self.horseImage.SetPosition(xPos, 0)
			xPos += self.IMAGE_STEP
			
Add it under- Altýna ekle:
		if self.playTimeImage:
			self.playTimeImage.SetPosition(xPos, 0)
			xPos += self.IMAGE_STEP		
			
http://puu.sh/kmxpp/9208362463.png