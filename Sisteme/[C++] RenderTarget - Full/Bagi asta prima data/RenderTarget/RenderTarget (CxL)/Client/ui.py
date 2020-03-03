#1.1 Search:
	LIST_BOX_KEY_LIST = ( "width", "height", )

#2.1 Add After:
	RENDER_TARGET_KEY_LIST = ( "index", )

#2.1 Search:
	def LoadElementTitleBar(self, window, value, parentWindow):
	
#2.1 Add above:
	def LoadElementRenderTarget(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.RENDER_TARGET_KEY_LIST):
			return False

		window.SetSize(value["width"], value["height"])
		
		if True == value.has_key("style"):
			for style in value["style"]:
				window.AddFlag(style)
				
		self.LoadDefaultData(window, value, parentWindow)
		
		if value.has_key("index"):
			window.SetRenderTarget(int(value["index"]))

		return True


#3.1 Search:
			elif Type == "button":
			
#3.2 Add ABOVE:
			elif Type == "render_target":	
				parent.Children[Index] = RenderTarget()
				parent.Children[Index].SetParent(parent)
				self.LoadElementRenderTarget(parent.Children[Index], ElementValue, parent)

#4.1 Search:
RegisterToolTipWindow("TEXT", TextLine)

#4.2 Add after:
class RenderTarget(Window):

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		
		self.number = -1

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterRenderTarget(self, layer)
		
	def SetRenderTarget(self, number):
		self.number = number
		wndMgr.SetRenderTarget(self.hWnd, self.number)

