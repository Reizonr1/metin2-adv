##Search for:
class TextLine(Window):
##Down on:
	def __init__(self):
##Replace it with:
	def __init__(self, font = None):
##and down on:
		self.SetFontName(localeInfo.UI_DEF_FONT)
##replace it with:
		if font == None:
			self.SetFontName(localeInfo.UI_DEF_FONT)
		else:
			self.SetFontName(font)