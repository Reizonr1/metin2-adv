import dbg,grp
import ui,uiCommon,localeInfo

class _ui:
	###################################################################################################################
	# BOARD
	###################################################################################################################
	def Board(self, parent, moveable, x, y, width, heigh):
		tmpBoard = ui.Board()
		
		if parent:
			tmpBoard.SetParent(parent)
		
		if moveable:
			tmpBoard.AddFlag('movable')
			tmpBoard.AddFlag('float')
		
		tmpBoard.SetSize(width, heigh)
		tmpBoard.SetPosition(x, y)

		tmpBoard.Show()
		return tmpBoard
	
	def ThinBoard(self, parent, moveable, x, y, width, heigh):
		tmpThinboard = ui.ThinBoard()
		
		if parent:
			tmpThinboard.SetParent(parent)
		
		if moveable:
			tmpThinboard.AddFlag('movable')
			tmpThinboard.AddFlag('float')
		
		tmpThinboard.SetSize(width, heigh)
		tmpThinboard.SetPosition(x, y)

		tmpThinboard.Show()
		return tmpThinboard

	def BoardWithTitleBar(self, parent, moveable, x, y, width, heigh, title, closeevent):
		tmpTitleBoard = ui.BoardWithTitleBar()
		
		if parent:
			tmpTitleBoard.SetParent(parent)
		
		if moveable:
			tmpTitleBoard.AddFlag('movable')
			tmpTitleBoard.AddFlag('float')
		
		tmpTitleBoard.SetSize(width, heigh)
		tmpTitleBoard.SetPosition(x, y)
		tmpTitleBoard.SetTitleName(title)
		tmpTitleBoard.SetCloseEvent(closeevent)

		tmpTitleBoard.Show()
		return tmpTitleBoard
	
	###################################################################################################################
	# BUTTON
	###################################################################################################################
	def BasicButton(self, parent, buttonName, x, y, func):
		tmpButton = ui.Button()
		
		if parent:
			tmpButton.SetParent(parent)
		
		tmpButton.SetPosition(x, y)
		tmpButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
		tmpButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
		tmpButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')

		tmpButton.SetText(buttonName)
		
		tmpButton.SetEvent(func)
		tmpButton.Show()
		return tmpButton
	
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		tmpButtonFormatted = ui.Button()
		
		if parent:
			tmpButtonFormatted.SetParent(parent)
		
		tmpButtonFormatted.SetPosition(x, y)
		tmpButtonFormatted.SetUpVisual(UpVisual)
		tmpButtonFormatted.SetOverVisual(OverVisual)
		tmpButtonFormatted.SetDownVisual(DownVisual)
		
		tmpButtonFormatted.SetText(buttonName)
		tmpButtonFormatted.SetToolTipText(tooltipText)
		
		tmpButtonFormatted.SetEvent(func)
		tmpButtonFormatted.Show()
		return tmpButtonFormatted
	
	def RadioButton(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		tmpRadioButton = ui.RadioButton()
		
		if parent:
			tmpRadioButton.SetParent(parent)
		
		tmpRadioButton.SetPosition(x, y)
		
		tmpRadioButton.SetEvent(func)
		tmpRadioButton.SetUpVisual(UpVisual)
		tmpRadioButton.SetOverVisual(OverVisual)
		tmpRadioButton.SetDownVisual(DownVisual)
		
		tmpRadioButton.SetText(buttonName)
		tmpRadioButton.SetToolTipText(tooltipText)
		
		tmpRadioButton.SetEvent(func)
		tmpRadioButton.Show()
		return tmpRadioButton
	
	def ToggleButton(self, parent, text, tooltiptext, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		tmpToggleButton = ui.ToggleButton()
		
		if parent:
			tmpToggleButton.SetParent(parent)
			
		tmpToggleButton.SetPosition(x, y)
		tmpToggleButton.SetUpVisual(UpVisual)
		tmpToggleButton.SetOverVisual(OverVisual)
		tmpToggleButton.SetDownVisual(DownVisual)
		
		tmpToggleButton.SetText(text)
		tmpToggleButton.SetToolTipText(tooltiptext)
		
		tmpToggleButton.SetToggleUpEvent(funcUp)
		tmpToggleButton.SetToggleDownEvent(funcDown)		
		tmpToggleButton.Show()
		return tmpToggleButton
	
	def DragButton(self, parent, func, UpVisual, OverVisual, DownVisual):
		tmpDragButton = ui.DragButton()

		tmpDragButton.SetParent(parent)
		tmpDragButton.SetMoveEvent(func)
		
		tmpDragButton.SetUpVisual(UpVisual)
		tmpDragButton.SetOverVisual(OverVisual)
		tmpDragButton.SetDownVisual(DownVisual)
		
		tmpDragButton.Show()
		return tmpDragButton
	
	def ResizeableButton(self, parent, x, y, width, heigh, text, tooltiptext, event):
		tmpResizeableButton = ResizeableButton()
		
		if parent:
			tmpResizeableButton.SetParent(parent)
			
		tmpResizeableButton.SetPosition(x, y) 
		tmpResizeableButton.SetSize(width, heigh)
		
		tmpResizeableButton.SetText(text)
		tmpResizeableButton.SetToolTipText(tooltiptext)
		
		tmpResizeableButton.SetEvent(event)
		
		tmpResizeableButton.Show()
		return tmpResizeableButton
	
	###################################################################################################################
	# GENERAL
	###################################################################################################################
	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)
	
	def Box(self, parent, x, y, width, heigh, color):
		tmpBox = ui.Box()
		
		if parent:
			tmpBox.SetParent(parent)
		if color:
			tmpBox.SetColor(color)
		
		tmpBox.SetPosition(x, y)
		tmpBox.SetSize(width, heigh)
		
		tmpBox.Show()
		return tmpBox
	
	def Line(self, parent, x, y, width, heigh, color):
		tmpLine = ui.Line()
		
		if parent:
			tmpLine.SetParent(parent)
		if color:
			tmpLine.SetColor(color)
		
		tmpLine.SetPosition(x, y)
		tmpLine.SetSize(width, heigh)
		
		tmpLine.Show()
		return tmpLine
	
	def TextLine(self, parent, text, x, y):
		tmpText = ui.TextLine()
		
		if parent:
			tmpText.SetParent(parent)
			
		tmpText.SetPosition(x, y)
		tmpText.SetText(text)
		
		tmpText.Show()
		return tmpText
		
	def EditLine(self, parent, text, x, y, width, heigh, max):
		tmpEditLine = ui.EditLine()
		
		if parent:
			tmpEditLine.SetParent(parent)
		
		tmpEditLine.SetSize(width, heigh)
		tmpEditLine.SetPosition(x, y)
		tmpEditLine.SetMax(max)
		tmpEditLine.SetLimitWidth(width)
		tmpEditLine.SetMultiLine()
		tmpEditLine.SetText(text)
		
		tmpEditLine.Show()
		return tmpEditLine
	
	def NumberLine(self, parent, path, number, x, y):
		tmpNumberLine = ui.NumberLine()
		
		if parent:
			tmpNumberLine.SetParent(parent)
			
		tmpNumberLine.SetPosition(x, y)
		tmpNumberLine.SetPath(path)
		tmpNumberLine.SetNumber(number)
		
		tmpNumberLine.Show()
		return tmpNumberLine
		
	def ComboBox(self, parent, text, x, y, width):
		tmpCombo = ComboBox()
		
		if parent:
			tmpCombo.SetParent(parent)
			
		tmpCombo.SetPosition(x, y)
		tmpCombo.SetSize(width, 15)
		
		tmpCombo.SetCurrentItem(text)
		
		tmpCombo.Show()
		return tmpCombo
	
	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		
		if parent:
			gauge.SetParent(parent)
			
		gauge.SetPosition(x, y)
		
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge
	
	###################################################################################################################
	# LIST
	###################################################################################################################

	def ListBox(self, parent, x, y, width, heigh):
		tmpListBox = ui.ListBox()
		
		if parent:
			tmpListBox.SetParent(parent)
		
		tmpListBox.SetPosition(x, y)
		tmpListBox.SetSize(width, heigh)
		
		tmpListBox.Show()
		return tmpListBox
	
	def ListBox2(self, parent, x, y, width, heigh):
		tmpListBox2 = ui.ListBox2()
		
		if parent:
			tmpListBox2.SetParent(parent)
		
		tmpListBox2.SetPosition(x, y)
		tmpListBox2.SetSize(width, heigh)
		
		tmpListBox2.Show()
		return tmpListBox2
	
	def ListBoxEx(self, parent, x, y, width, heigh):
		tmpListBoxEx = ui.ListBoxEx()
		
		if parent:
			tmpListBoxEx.SetParent(parent)
		
		tmpListBoxEx.SetPosition(x, y)
		tmpListBoxEx.SetSize(width, heigh)
		
		tmpListBoxEx.Show()
		return tmpListBoxEx
	
	###################################################################################################################
	# BAR
	###################################################################################################################
	def SlotBar(self, parent, x, y, width, heigh):
		tmpSlotBar = ui.SlotBar()
		
		if parent:
			tmpSlotBar.SetParent(parent)
		
		tmpSlotBar.SetSize(width, heigh)
		tmpSlotBar.SetPosition(x, y)
		
		tmpSlotBar.Show()
		return tmpSlotBar
	
	def Bar(self, parent, x, y, width, heigh):
		tmpBar = ui.Bar()
		
		if parent:
			tmpBar.SetParent(parent)
			
		tmpBar.SetPosition(x, y)
		tmpBar.SetSize(width, heigh)
		
		tmpBar.SetColor(0x77000000)
		
		tmpBar.Show()
		return tmpBar
	
	def Bar3D(self, parent, x, y, width, heigh, color):
		tmpBar3D = ui.Bar3D()
		
		if parent:
			tmpBar3D.SetParent(parent)
		if color:
			tmpBar3D.SetColor(color)
			
		tmpBar3D.SetPosition(x, y)
		tmpBar3D.SetSize(width, heigh)
		
		tmpBar3D.Show()
		return tmpBar3D
	
	def TitleBar(self, parent, x, y, width, color, event):
		tmpTitleBar = ui.TitleBar()
		
		if parent:
			tmpTitleBar.SetParent(parent)
		
		tmpTitleBar.SetPosition(x, y)
		tmpTitleBar.SetCloseEvent(event)
		
		tmpTitleBar.MakeTitleBar(width, color)
		tmpTitleBar.Show()
		return tmpTitleBar
		
	def HorizontalBar(self, parent, x, y, width):
		tmpHorizontalBar = ui.HorizontalBar()
		
		if parent:
			tmpHorizontalBar.SetParent(parent)
		
		tmpHorizontalBar.SetPosition(x, y)
		
		tmpHorizontalBar.Create(width)
		tmpHorizontalBar.Show()
		return tmpHorizontalBar
		
	def SliderBar(self, parent, x, y, width, heigh, event):
		tmpSliderBar = ui.SliderBar()
		
		if parent:
			tmpSliderBar.SetParent(parent)
		
		tmpSliderBar.SetPosition(x, y)
		tmpSliderBar.SetSize(width, heigh)
		tmpSliderBar.SetEvent(event)
		
		tmpSliderBar.Show()
		return tmpSliderBar
	
	def ProgressBar(self, parent, x, y, width, heigh, percentage):
		tmpProgressBar = ProgressBar()
		
		if parent:
			tmpProgressBar.SetParent(parent)
			
		tmpProgressBar.SetPosition(x, y)
		tmpProgressBar.SetSize(width, heigh)
		
		tmpProgressBar.SetPercentage(percentage)
		
		tmpProgressBar.Show()
		return tmpProgressBar
	
	def ScrollBar(self, parent, width, heigh):
		tmpScrollBar = ui.ScrollBar()
		
		if parent:
			tmpScrollBar.SetParent(parent)
			
		tmpScrollBar.SetPosition(width-15, 17)
		tmpScrollBar.SetScrollBarSize(heigh)
		
		tmpScrollBar.Show()
		return tmpScrollBar
	
	###################################################################################################################
	# IMAGE
	###################################################################################################################
	def ImageBox(self, parent, image, x, y):
		tmpImage = ui.ImageBox()
		
		if parent:
			tmpImage.SetParent(parent)
		
		tmpImage.LoadImage(image)
		tmpImage.SetPosition(x, y)
		
		tmpImage.Show()
		return tmpImage
	
	def AniImageBox(self, parent, image, x, y):
		tmpAniImage = ui.AniImageBox()
		
		if parent:
			tmpAniImage.SetParent(parent)
		
		tmpAniImage.AppendImage(image)
		tmpAniImage.SetPosition(x, y)
		
		tmpAniImage.Show()
		return tmpAniImage
	
	def ExpandedImageBox(self, parent, image, x, y, min, max):
		tmpExpImageBox = ui.ExpandedImageBox()
		
		if parent:
			tmpExpImageBox.SetParent(parent)
		
		tmpExpImageBox.LoadImage(image)
		
		tmpExpImageBox.SetPosition(x,y)
		tmpExpImageBox.SetPercentage(min,max)
		
		tmpExpImageBox.Show()
		return tmpExpImageBox
	
	###################################################################################################################
	# SLOT	
	###################################################################################################################
	def SlotWindow(self, parent, x, y, width, heigh, emptyevent, selectItemEvent, itemInEvent, ItemOutEvent):
		tmpSlowWindow = ui.SlotWindow()
		
		if parent:
			tmpSlowWindow.SetParent(parent)
		
		tmpSlowWindow.SetSize(width, heigh)
		tmpSlowWindow.SetPosition(x, y)
		
		tmpSlowWindow.SetSelectEmptySlotEvent(emptyevent)
		tmpSlowWindow.SetSelectItemSlotEvent(selectItemEvent)
		tmpSlowWindow.SetOverInItemEvent(itemInEvent)
		tmpSlowWindow.SetOverOutItemEvent(ItemOutEvent)
		
		tmpSlowWindow.Show()
		return tmpSlowWindow
	
	def GridSlotWindow(self, parent, ItemInEvent, ItemOutEvent, x, y, width, heigh, SlotStartIndex, SlotXCount, SlotYCount, SlotXStep, SlotYStep, SlotXBlank, SlotYBlank):
		tmpGridSlotWindow = ui.GridSlotWindow()
		
		if parent:
			tmpGridSlotWindow.SetParent(parent)
		
		tmpGridSlotWindow.SetSize(width, heigh)
		tmpGridSlotWindow.SetPosition(x, y)
		
		tmpGridSlotWindow.SetOverInItemEvent(ItemInEvent)
		tmpGridSlotWindow.SetOverOutItemEvent(ItemOutEvent)
		tmpGridSlotWindow.ArrangeSlot(SlotStartIndex, SlotXCount, SlotYCount, SlotXStep, SlotYStep, SlotXBlank, SlotYBlank)
		tmpGridSlotWindow.RefreshSlot()
		tmpGridSlotWindow.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		
		tmpGridSlotWindow.Show()
		return tmpGridSlotWindow
	
	###################################################################################################################
	# COMMON	
	###################################################################################################################
	def Popup(self, text, width, acceptevent):
		tmpPopup = uiCommon.PopupDialog()
		
		tmpPopup.SetText(str(text))
		if width: tmpPopup.SetWidth(width)
		if acceptevent: tmpPopup.SetAcceptEvent(acceptevent)
		
		tmpPopup.Open()
		return tmpPopup
	
	def Input(self, text, length, acceptevent, cancelevent):
		tmpInput = uiCommon.InputDialog()
		
		tmpInput.SetTitle(str(text))
		tmpInput.SetMaxLength(length)
		
		if acceptevent: tmpInput.SetAcceptEvent(acceptevent)
		if cancelevent: tmpInput.SetCancelEvent(cancelevent)
		
		tmpInput.Open()
		return tmpInput
	
	def InputDescription(self, text, description,length, acceptevent, cancelevent):
		tmpInputDescription = uiCommon.InputDialogWithDescription()
		
		tmpInputDescription.SetTitle(str(text))
		tmpInputDescription.SetDescription(str(description))
		
		tmpInputDescription.SetMaxLength(length)
		
		if acceptevent: tmpInputDescription.SetAcceptEvent(acceptevent)
		if cancelevent: tmpInputDescription.SetCancelEvent(cancelevent)
		
		tmpInputDescription.Open()
		return tmpInputDescription	
	
	def InputDescription2(self, text, description, description2, length, acceptevent, cancelevent):
		tmpInputDescription2 = uiCommon.InputDialogWithDescription2()
		
		tmpInputDescription2.SetTitle(str(text))
		tmpInputDescription2.SetDescription1(str(description))
		tmpInputDescription2.SetDescription2(str(description2))
		
		tmpInputDescription2.SetMaxLength(length)
		
		if acceptevent: tmpInputDescription2.SetAcceptEvent(acceptevent)
		if cancelevent: tmpInputDescription2.SetCancelEvent(cancelevent)
		
		tmpInputDescription2.Open()
		return tmpInputDescription2
	
	def Question(self, text, width, acceptevent, cancelevent):
		tmpQuestion = uiCommon.QuestionDialog()
		
		tmpQuestion.SetText(str(text))
		if width: tmpQuestion.SetWidth(width)
		
		if acceptevent: tmpQuestion.SAFE_SetAcceptEvent(acceptevent)
		if cancelevent: tmpQuestion.SAFE_SetCancelEvent(cancelevent)
		
		tmpQuestion.Open()
		return tmpQuestion
	
	def Question2(self, text, text2, width, acceptevent, cancelevent):
		tmpQuestion2 = uiCommon.QuestionDialog2()
		
		tmpQuestion2.SetText1(str(text))
		tmpQuestion2.SetText2(str(text2))
		
		if width: tmpQuestion2.SetWidth(width)
		
		if acceptevent: tmpQuestion2.SAFE_SetAcceptEvent(acceptevent)
		if cancelevent: tmpQuestion2.SAFE_SetCancelEvent(cancelevent)
		
		tmpQuestion2.Open()
		return tmpQuestion2
	
	def QuestionWithLimit(self, text, limit, width, acceptevent, cancelevent):
		tmpQuestionWithLimit = uiCommon.QuestionDialogWithTimeLimit()
		
		if width: tmpQuestionWithLimit.SetWidth(width)
		
		if acceptevent: tmpQuestionWithLimit.SAFE_SetAcceptEvent(acceptevent)
		if cancelevent: tmpQuestionWithLimit.SAFE_SetCancelEvent(cancelevent)
		
		tmpQuestionWithLimit.Open(str(text), limit)
		return tmpQuestionWithLimit
	
class ListBoxExItem(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		#self.textLine=self.__CreateTextLine(text[:75])
		self.textLine=self.__CreateTextLine(text)
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 7*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(10, 4)
		textLine.SetText(text)
		textLine.Show()
		return textLine

class ComboBox(ui.Window):

	class ListBoxWithBoard(ui.ListBox):

		def __init__(self, layer):
			ui.ListBox.__init__(self, layer)

		def OnRender(self):
			xRender, yRender = self.GetGlobalPosition()
			yRender -= self.TEMPORARY_PLACE
			widthRender = self.width
			heightRender = self.height + self.TEMPORARY_PLACE*2
			grp.SetColor(ui.BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
			grp.SetColor(ui.DARK_COLOR)
			grp.RenderLine(xRender, yRender, widthRender, 0)
			grp.RenderLine(xRender, yRender, 0, heightRender)
			grp.SetColor(ui.BRIGHT_COLOR)
			grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
			grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

			ui.ListBox.OnRender(self)

	def __init__(self):
		ui.Window.__init__(self)
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.isSelected = FALSE
		self.isOver = FALSE
		self.isListOpened = FALSE
		self.event = lambda *arg: None
		self.enable = TRUE

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetText(localeInfo.UI_ITEM)

		self.listBox = self.ListBoxWithBoard("TOP_MOST")
		self.listBox.SetPickAlways()
		self.listBox.SetParent(self)
		self.listBox.SetEvent(ui.__mem_func__(self.OnSelectItem))
		self.listBox.Hide()

	def __del__(self):
		ui.Window.__del__(self)

	def Destroy(self):
		self.textLine = None
		self.listBox = None

	def SetPosition(self, x, y):
		ui.Window.SetPosition(self, x, y)
		self.x = x
		self.y = y
		self.__ArrangeListBox()

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height
		self.textLine.UpdateRect()
		self.__ArrangeListBox()

	def __ArrangeListBox(self):
		self.listBox.SetPosition(0, self.height + 5)
		self.listBox.SetWidth(self.width)

	def Enable(self):
		self.enable = TRUE

	def Disable(self):
		self.enable = FALSE
		self.textLine.SetText("")
		self.CloseListBox()

	def SetEvent(self, event):
		self.event = event

	def ClearItem(self):
		self.CloseListBox()
		self.listBox.ClearItem()

	def InsertItem(self, index, name):
		self.listBox.InsertItem(index, name)
		self.listBox.ArrangeItem()

	def SetCurrentItem(self, text):
		self.textLine.SetText(text)

	def GetCurrentText(self):
		return self.textLine.GetText()

	def GetCurrentIndex(self):
		return self.listBox.selectedLine
		
	def SelectItem(self, key):
		self.listBox.SelectItem(key)

	def OnSelectItem(self, index, name):
		self.SetCurrentItem(name)
		self.CloseListBox()
		self.event(index)

	def CloseListBox(self):
		self.isListOpened = FALSE
		self.listBox.Hide()

	def OnMouseLeftButtonDown(self):

		if not self.enable:
			return

		self.isSelected = TRUE

	def OnMouseLeftButtonUp(self):

		if not self.enable:
			return

		self.isSelected = FALSE

		if self.isListOpened:
			self.CloseListBox()
		else:
			if self.listBox.GetItemCount() > 0:
				self.isListOpened = TRUE
				self.listBox.Show()
				self.__ArrangeListBox()

	def OnUpdate(self):

		if not self.enable:
			return

		if self.IsIn():
			self.isOver = TRUE
		else:
			self.isOver = FALSE

	def OnRender(self):
		self.x, self.y = self.GetGlobalPosition()
		xRender = self.x
		yRender = self.y
		widthRender = self.width
		heightRender = self.height
		grp.SetColor(ui.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(ui.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.SetColor(ui.BRIGHT_COLOR)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		if self.isOver:
			grp.SetColor(ui.HALF_WHITE_COLOR)
			grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

			if self.isSelected:
				grp.SetColor(ui.WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

class ResizeableButton(ui.Window):
	
	BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
	DARK_COLOR = grp.GenerateColor(0.4, 0.4, 0.4, 1.0)
	
	WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.3)
	HALF_WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.2)
	
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.ButtonText = None
		self.ToolTipText = None
		
		self.isOver = FALSE
		self.isSelected = FALSE
		
		self.width = 0
		self.height = 0		

	def __del__(self):
		ui.Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height
		
	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

	def SetText(self, text):
		if not self.ButtonText:
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.ButtonText = textLine

		self.ButtonText.SetText(text)

	def SetToolTipText(self, text, x=0, y = -19):
		if not self.ToolTipText:		
			toolTip=ui.createToolTipWindowDict["TEXT"]()
			toolTip.SetParent(self)
			toolTip.SetSize(0, 0)
			toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.SetPosition(x + self.GetWidth()/2, y)
			self.ToolTipText=toolTip

		self.ToolTipText.SetText(text)

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Show()

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()
		
	def OnMouseLeftButtonDown(self):
		self.isSelected = TRUE
		
	def OnMouseLeftButtonUp(self):
		self.isSelected = FALSE
		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def OnUpdate(self):
		if self.IsIn():
			self.isOver = TRUE
			self.ShowToolTip()
		else:
			self.isOver = FALSE
			self.HideToolTip()

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		
		widthRender = self.width
		heightRender = self.height
		grp.SetColor(self.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		if self.isOver:
			grp.SetColor(self.HALF_WHITE_COLOR)
			grp.RenderBar(xRender + 2, yRender + 2, self.width - 3, heightRender - 3)

			if self.isSelected:
				grp.SetColor(self.WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 2, self.width - 3, heightRender - 3)

class ProgressBar(ui.Window):

	BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
	DARK_COLOR = grp.GenerateColor(0.4, 0.4, 0.4, 1.0)
	
	PROGRESS_COLOR = grp.GenerateColor(1.0, 0.2, 0.2, 0.4)
	
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.width = 0
		self.height = 0		
		self.percentage = 0
		
		self.textLine = None
		
	def __del__(self):
		ui.Window.__del__(self)
	
	def GetPercentage(self):
		if self.textLine:
			return self.textLine.GetText()[1:]
	
	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetPercentage(self, num):
		if num > 100:
			self.percentage = 100
		elif num < 0:
			self.percentage = 0
		else:
			self.percentage = num
		
		if not self.textLine:		
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine
		
		self.textLine.SetText('%' + str(self.percentage))

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		
		widthRender = self.width
		heightRender = self.height
		grp.SetColor(self.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		grp.SetColor(self.PROGRESS_COLOR)
		grp.RenderBar(xRender + 2, yRender + 2, (self.width - 3) * self.percentage / 100, heightRender - 3)
		

