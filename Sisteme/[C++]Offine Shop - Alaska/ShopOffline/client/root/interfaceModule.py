[..]
class Interface(object):
	[..]
	def Init(self):
		[..]
		self.wndGiftBox = None
		
		[..]
		
		
	def __OnClickGiftButton(self):
		if self.wndGameButton:
			if not self.wndGiftBox.IsShow():
				self.wndGiftBox.Open()
			else:
				self.wndGiftBox.Close()

	def ClearGift(self):
		if self.wndGameButton:
			self.wndGameButton.HideGiftButton()
		if self.wndGiftBox:
			self.wndGiftBox.Clear()
			self.wndGiftBox.Refresh()

	def __MakeTaskBar(self):
		[..]
			
		import uiGift
		wndGiftBox=uiGift.GiftDialog()
		wndGiftBox.Hide()
		self.wndGiftBox=wndGiftBox


	def __MakeGameButtonWindow(self):
		[..]
		wndGameButton.SetButtonEvent("GIFT", ui.__mem_func__(self.__OnClickGiftButton))

		self.wndGameButton = wndGameButton

	def Close(self):
		[..]

		if self.wndGiftBox:
			self.wndGiftBox.Clear()
			self.wndGiftBox.Hide()
			self.wndGiftBox.Destroy()
		del self.wndGiftBox
		[..]
		uiChat.DestroyChatInputSetWindow()


	# show GIFT
	def OpenGift(self):
		if self.wndGameButton:
			self.wndGameButton.ShowGiftButton()
	