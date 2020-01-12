## Search for:
	def __init__(self, layer = "UI"):
		self.clickEvent = None
		self.hWnd = None
		self.parentWindow = 0
		self.onMouseLeftButtonUpEvent = None
		self.RegisterWindow(layer)
		self.Hide()

## Add (Under):
		if app.ENABLE_SEND_TARGET_INFO:
			self.mouseLeftButtonDownEvent = None
			self.mouseLeftButtonDownArgs = None
			self.mouseLeftButtonUpEvent = None
			self.mouseLeftButtonUpArgs = None
			self.mouseLeftButtonDoubleClickEvent = None
			self.mouseRightButtonDownEvent = None
			self.mouseRightButtonDownArgs = None
			self.moveWindowEvent = None
			self.renderEvent = None
			self.renderArgs = None

			self.overInEvent = None
			self.overInArgs = None

			self.overOutEvent = None
			self.overOutArgs = None

			self.baseX = 0
			self.baseY = 0

			self.SetWindowName("NONAME_Window")

## Search for:
	def GetWindowName(self):
		return wndMgr.GetName(self.hWnd)

	def SetParent(self, parent):
		wndMgr.SetParent(self.hWnd, parent.hWnd)

## Add (Under & Replace SetParent Function with this):
	if app.ENABLE_SEND_TARGET_INFO:
		def SetParent(self, parent):
			if parent:
				wndMgr.SetParent(self.hWnd, parent.hWnd)
			else:
				wndMgr.SetParent(self.hWnd, 0)
	
		def SetAttachParent(self, parent):
			wndMgr.SetAttachParent(self.hWnd, parent.hWnd)
	else:
		def SetParent(self, parent):
			wndMgr.SetParent(self.hWnd, parent.hWnd)

## Search for On (class Window(object):):
	def Hide(self):
		wndMgr.Hide(self.hWnd)

## Add (Under)
	if app.ENABLE_SEND_TARGET_INFO:
		def SetVisible(self, is_show):
			if is_show:
				self.Show()
			else:
				self.Hide()

## Search for:
	def GetLocalPosition(self):
		return wndMgr.GetWindowLocalPosition(self.hWnd)

## Add (Under):
	if app.ENABLE_SEND_TARGET_INFO:
		def GetLeft(self):
			x, y = self.GetLocalPosition()
			return x
	
		def GetGlobalLeft(self):
			x, y = self.GetGlobalPosition()
			return x
	
		def GetTop(self):
			x, y = self.GetLocalPosition()
			return y
	
		def GetGlobalTop(self):
			x, y = self.GetGlobalPosition()
			return y
	
		def GetRight(self):
			return self.GetLeft() + self.GetWidth()
	
		def GetBottom(self):
			return self.GetTop() + self.GetHeight()

## Search for:
	def GetRect(self):
		return wndMgr.GetWindowRect(self.hWnd)

## Add (Under):
	if app.ENABLE_SEND_TARGET_INFO:
		def SetLeft(self, x):
			wndMgr.SetWindowPosition(self.hWnd, x, self.GetTop())

## Search for:
	def SetCenterPosition(self, x = 0, y = 0):
		self.SetPosition((wndMgr.GetScreenWidth() - self.GetWidth()) / 2 + x, (wndMgr.GetScreenHeight() - self.GetHeight()) / 2 + y)

## Add (Under):
	if app.ENABLE_SEND_TARGET_INFO:
		def SavePosition(self):
			self.baseX = self.GetLeft()
			self.baseY = self.GetTop()
	
		def UpdatePositionByScale(self, scale):
			self.SetPosition(self.baseX * scale, self.baseY * scale)

## Search for:
	def IsIn(self):
		return wndMgr.IsIn(self.hWnd)

## Add (Under):
	if app.ENABLE_SEND_TARGET_INFO:
		def IsInPosition(self):
			xMouse, yMouse = wndMgr.GetMousePosition()
			x, y = self.GetGlobalPosition()
			return xMouse >= x and xMouse < x + self.GetWidth() and yMouse >= y and yMouse < y + self.GetHeight()
	
		def SetMouseLeftButtonDownEvent(self, event, *args):
			self.mouseLeftButtonDownEvent = event
			self.mouseLeftButtonDownArgs = args
	
		def OnMouseLeftButtonDown(self):
			if self.mouseLeftButtonDownEvent:
				apply(self.mouseLeftButtonDownEvent, self.mouseLeftButtonDownArgs)

## Search for:
	def SetOnMouseLeftButtonUpEvent(self, event):
		self.onMouseLeftButtonUpEvent = ev

## Add (Replace the whole function of SetOnMouseLeftButtonUpEvent with this):
	if app.ENABLE_SEND_TARGET_INFO:
		def SetMouseLeftButtonUpEvent(self, event, *args):
			self.mouseLeftButtonUpEvent = event
			self.mouseLeftButtonUpArgs = args
	else:
		def SetOnMouseLeftButtonUpEvent(self, event):
			self.onMouseLeftButtonUpEvent = ev

	if app.ENABLE_SEND_TARGET_INFO:
		def SetMouseLeftButtonDoubleClickEvent(self, event):
			self.mouseLeftButtonDoubleClickEvent = event
	
		def OnMouseLeftButtonDoubleClick(self):
			if self.mouseLeftButtonDoubleClickEvent:
				self.mouseLeftButtonDoubleClickEvent()
	
		def SetMouseRightButtonDownEvent(self, event, *args):
			self.mouseRightButtonDownEvent = event
			self.mouseRightButtonDownArgs = args
	
		def OnMouseRightButtonDown(self):
			if self.mouseRightButtonDownEvent:
				apply(self.mouseRightButtonDownEvent, self.mouseRightButtonDownArgs)
	
		def SetMoveWindowEvent(self, event):
			self.moveWindowEvent = event
	
		def OnMoveWindow(self, x, y):
			if self.moveWindowEvent:
				self.moveWindowEvent(x, y)
	
		def SAFE_SetOverInEvent(self, func, *args):
			self.overInEvent = __mem_func__(func)
			self.overInArgs = args
	
		def SetOverInEvent(self, func, *args):
			self.overInEvent = func
			self.overInArgs = args
	
		def SAFE_SetOverOutEvent(self, func, *args):
			self.overOutEvent = __mem_func__(func)
			self.overOutArgs = args
	
		def SetOverOutEvent(self, func, *args):
			self.overOutEvent = func
			self.overOutArgs = args
	
		def OnMouseOverIn(self):
			if self.overInEvent:
				apply(self.overInEvent, self.overInArgs)
	
		def OnMouseOverOut(self):
			if self.overOutEvent:
				apply(self.overOutEvent, self.overOutArgs)
	
		def SAFE_SetRenderEvent(self, event, *args):
			self.renderEvent = __mem_func__(event)
			self.renderArgs = args
	
		def ClearRenderEvent(self):
			self.renderEvent = None
			self.renderArgs = None
	
		def OnRender(self):
			if self.renderEvent:
				apply(self.renderEvent, self.renderArgs)

## Search for:
class CandidateListBox(ListBoxEx):

## Add (Before):
if app.ENABLE_SEND_TARGET_INFO:
	class ListBoxExNew(Window):
		class Item(Window):
			def __init__(self):
				Window.__init__(self)

				self.realWidth = 0
				self.realHeight = 0

				self.removeTop = 0
				self.removeBottom = 0

				self.SetWindowName("NONAME_ListBoxExNew_Item")

			def __del__(self):
				Window.__del__(self)

			def SetParent(self, parent):
				Window.SetParent(self, parent)
				self.parent=proxy(parent)

			def SetSize(self, width, height):
				self.realWidth = width
				self.realHeight = height
				Window.SetSize(self, width, height)

			def SetRemoveTop(self, height):
				self.removeTop = height
				self.RefreshHeight()

			def SetRemoveBottom(self, height):
				self.removeBottom = height
				self.RefreshHeight()

			def SetCurrentHeight(self, height):
				Window.SetSize(self, self.GetWidth(), height)

			def GetCurrentHeight(self):
				return Window.GetHeight(self)

			def ResetCurrentHeight(self):
				self.removeTop = 0
				self.removeBottom = 0
				self.RefreshHeight()

			def RefreshHeight(self):
				self.SetCurrentHeight(self.GetHeight() - self.removeTop - self.removeBottom)

			def GetHeight(self):
				return self.realHeight

		def __init__(self, stepSize, viewSteps):
			Window.__init__(self)

			self.viewItemCount=10
			self.basePos=0
			self.baseIndex=0
			self.maxSteps=0
			self.viewSteps = viewSteps
			self.stepSize = stepSize
			self.itemList=[]

			self.scrollBar=None

			self.SetWindowName("NONAME_ListBoxEx")

		def __del__(self):
			Window.__del__(self)

		def IsEmpty(self):
			if len(self.itemList)==0:
				return 1
			return 0

		def __CheckBasePos(self, pos):
			self.viewItemCount = 0

			start_pos = pos

			height = 0
			while height < self.GetHeight():
				if pos >= len(self.itemList):
					return start_pos == 0
				height += self.itemList[pos].GetHeight()
				pos += 1
				self.viewItemCount += 1
			return height == self.GetHeight()

		def SetBasePos(self, basePos, forceRefresh = TRUE):
			if forceRefresh == FALSE and self.basePos == basePos:
				return

			for oldItem in self.itemList[self.baseIndex:self.baseIndex+self.viewItemCount]:
				oldItem.ResetCurrentHeight()
				oldItem.Hide()

			self.basePos=basePos

			baseIndex = 0
			while basePos > 0:
				basePos -= self.itemList[baseIndex].GetHeight() / self.stepSize
				if basePos < 0:
					self.itemList[baseIndex].SetRemoveTop(self.stepSize * abs(basePos))
					break
				baseIndex += 1
			self.baseIndex = baseIndex

			stepCount = 0
			self.viewItemCount = 0
			while baseIndex < len(self.itemList):
				stepCount += self.itemList[baseIndex].GetCurrentHeight() / self.stepSize
				self.viewItemCount += 1
				if stepCount > self.viewSteps:
					self.itemList[baseIndex].SetRemoveBottom(self.stepSize * (stepCount - self.viewSteps))
					break
				elif stepCount == self.viewSteps:
					break
				baseIndex += 1

			y = 0
			for newItem in self.itemList[self.baseIndex:self.baseIndex+self.viewItemCount]:
				newItem.SetPosition(0, y)
				newItem.Show()
				y += newItem.GetCurrentHeight()

		def GetItemIndex(self, argItem):
			return self.itemList.index(argItem)

		def GetSelectedItem(self):
			return self.selItem

		def GetSelectedItemIndex(self):
			return self.selItemIdx

		def RemoveAllItems(self):
			self.itemList=[]
			self.maxSteps=0

			if self.scrollBar:
				self.scrollBar.SetPos(0)

		def RemoveItem(self, delItem):
			self.maxSteps -= delItem.GetHeight() / self.stepSize
			self.itemList.remove(delItem)

		def AppendItem(self, newItem):
			if newItem.GetHeight() % self.stepSize != 0:
				import dbg
				dbg.TraceError("Invalid AppendItem height %d stepSize %d" % (newItem.GetHeight(), self.stepSize))
				return

			self.maxSteps += newItem.GetHeight() / self.stepSize
			newItem.SetParent(self)
			self.itemList.append(newItem)

		def SetScrollBar(self, scrollBar):
			scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
			self.scrollBar=scrollBar

		def __OnScroll(self):
			self.SetBasePos(int(self.scrollBar.GetPos()*self.__GetScrollLen()), FALSE)

		def __GetScrollLen(self):
			scrollLen=self.maxSteps-self.viewSteps
			if scrollLen<0:
				return 0

			return scrollLen

		def __GetViewItemCount(self):
			return self.viewItemCount

		def __GetItemCount(self):
			return len(self.itemList)

		def GetViewItemCount(self):
			return self.viewItemCount

		def GetItemCount(self):
			return len(self.itemList)

## Search for On (class ThinBoard(Window):):
	def __del__(self):
		Window.__del__(self)

## Add (Under):
	if app.ENABLE_SEND_TARGET_INFO:
		def ShowCorner(self, corner):
			self.Corners[corner].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideCorners(self, corner):
			self.Corners[corner].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def ShowLine(self, line):
			self.Lines[line].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideLine(self, line):
			self.Lines[line].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())
