			elif Type == "listbox": ## search
	

			## add the this style


			elif Type == "listbox_scroll":
				parent.Children[Index] = ListBox_Scroll()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)


#under to class ListBox
class ListBox_Scroll(ListBox):
	def __init__(self):
		ListBox.__init__(self)
		
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Show()

	def SetSize(self, width, height):
		ListBox.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBox.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBox._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Show()

	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))