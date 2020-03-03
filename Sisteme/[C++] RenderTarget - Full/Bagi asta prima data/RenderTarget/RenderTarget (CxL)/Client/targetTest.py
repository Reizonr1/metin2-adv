#Example
import ui
import dbg
import app
import player
import wndMgr
import renderTarget

class Dialog1(ui.Window):
	RENDER_TARGET_INDEX = 1
	def __init__(self):
		ui.Window.__init__(self)
		
		self.max_pos_x = wndMgr.GetScreenWidth()
		self.max_pos_y = wndMgr.GetScreenHeight()
		self.BuildWindow()

	def __del__(self):
		self.Close()
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(445, 429)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Window')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		self.__BuildKeyDict()
		self.comp = Component()
		
		self.chrRenderer =  ui.RenderTarget()
		self.chrRenderer.SetParent(self.Board)
		self.chrRenderer.SetSize(190,210)
		self.chrRenderer.SetPosition(16, 35)
		self.chrRenderer.SetRenderTarget(self.RENDER_TARGET_INDEX)
		self.chrRenderer.Show()

		self.btnSet = self.comp.Button(self.Board, 'Set', '', 92, 384, self.btnSet_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.slotbar_txtModel, self.txtModel = self.comp.EditLine(self.Board, '101', 20, 386, 60, 15, 10)

		renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
		
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, 101)
		
	def MINMAX(self, min, value, max):
		
		if value < min:
			return min
		elif value > max:
			return max
		else:
			return value
		
	def OnUpdate(self):
		x, y = self.GetGlobalPosition()
		
		pos_x = self.MINMAX(0, x, self.max_pos_x)
		pos_y = self.MINMAX(0, y, self.max_pos_y)
		
		self.SetPosition(pos_x, pos_y)
	
	def btnSet_func(self):
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, int(self.txtModel.GetText()))
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
	def OnKeyDown(self, key):
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise
		return TRUE
	
	def OpenWindow(self):
		if self.Board.IsShow():
			renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, False)
			self.Board.Hide()
		else:
			self.Board.Show()
	
	def Close(self):
		renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, False)
		self.Board.Hide()

class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

