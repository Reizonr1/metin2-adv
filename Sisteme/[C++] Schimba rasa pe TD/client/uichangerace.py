'''
Created on Dec 12, 2018
With Eclipse-PyDev module
@author: [RaffaeL]
'''
import ui
import net
import app
import chat
import math
import wndMgr
import serverInfo
import background
import constInfo
import game
import event
import ime
import grp
import uiScriptLocale
import uiCommon
import localeInfo
import snd
import item
import player
import mouseModule
import uichangerace

class ChangeRace(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__MakeWindow()
		self.__MakeBoard()

	def __del__(self):

		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):

		ui.ScriptWindow.Hide(self)

	def OnPressEscapeKey(self):

		self.Close()
		return True

	def Destroy(self):
		self.Hide()

		return True

	def __MakeWindow(self):
		self.SetSize(295, 200)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth()) / 2),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2))
		)
		self.AddFlag("movable")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("movable")
		self.Board.Show()

		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()

		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("|cff80FFFFMeniu-Schimba rasa|h|r")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()

		self.bg0 = ui.ImageBox()
		self.bg0.SetParent(self.Board)
		self.bg0.SetPosition(5, 35)
		self.bg0.LoadImage("change_race/faces/icon_mwarrior.tga")
		self.bg0.Show()

		self.bg1 = ui.ImageBox()
		self.bg1.SetParent(self.Board)
		self.bg1.SetPosition(72, 35)
		self.bg1.LoadImage("change_race/faces/icon_mninja.tga")
		self.bg1.Show()

		self.bg2 = ui.ImageBox()
		self.bg2.SetParent(self.Board)
		self.bg2.SetPosition(142, 35)
		self.bg2.LoadImage("change_race/faces/icon_msura.tga")
		self.bg2.Show()

		self.bg3 = ui.ImageBox()
		self.bg3.SetParent(self.Board)
		self.bg3.SetPosition(212, 35)
		self.bg3.LoadImage("change_race/faces/icon_mshaman.tga")
		self.bg3.Show()

		self.bgtxt0 = ui.TextLine()
		self.bgtxt0.SetParent(self.bg0)
		self.bgtxt0.SetPosition(0,0)
		self.bgtxt0.SetWindowHorizontalAlignCenter()
		self.bgtxt0.SetHorizontalAlignCenter()
		self.bgtxt0.SetText("Razboinic")
		self.bgtxt0.Show()

		self.bgtxt1 = ui.TextLine()
		self.bgtxt1.SetParent(self.bg1)
		self.bgtxt1.SetPosition(0,0)
		self.bgtxt1.SetWindowHorizontalAlignCenter()
		self.bgtxt1.SetHorizontalAlignCenter()
		self.bgtxt1.SetText("Ninja")
		self.bgtxt1.Show()

		self.bgtxt2 = ui.TextLine()
		self.bgtxt2.SetParent(self.bg2)
		self.bgtxt2.SetPosition(0,0)
		self.bgtxt2.SetWindowHorizontalAlignCenter()
		self.bgtxt2.SetHorizontalAlignCenter()
		self.bgtxt2.SetText("Sura")
		self.bgtxt2.Show()

		self.bgtxt3 = ui.TextLine()
		self.bgtxt3.SetParent(self.bg3)
		self.bgtxt3.SetPosition(0,0)
		self.bgtxt3.SetWindowHorizontalAlignCenter()
		self.bgtxt3.SetHorizontalAlignCenter()
		self.bgtxt3.SetText("Shaman")
		self.bgtxt3.Show()

		self.btn0 = ui.Button()
		self.btn0.SetParent(self.Board)
		self.btn0.SetPosition(12,170)
		self.btn0.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn0.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn0.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetText("Alege")
		self.btn0.SetEvent(lambda : self.__choose_war())
		self.btn0.Show()

		self.btn1 = ui.Button()
		self.btn1.SetParent(self.Board)
		self.btn1.SetPosition(82,170)
		self.btn1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetText("Alege")
		self.btn1.SetEvent(lambda : self.__choose_ninja())
		self.btn1.Show()

		self.btn2 = ui.Button()
		self.btn2.SetParent(self.Board)
		self.btn2.SetPosition(152,170)
		self.btn2.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn2.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn2.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn2.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn2.SetText("Alege")
		self.btn2.SetEvent(lambda : self.__choose_sura())
		self.btn2.Show()

		self.btn3 = ui.Button()
		self.btn3.SetParent(self.Board)
		self.btn3.SetPosition(222,170)
		self.btn3.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn3.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn3.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn3.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn3.SetText("Alege")
		self.btn3.SetEvent(lambda : self.__choose_shaman())
		self.btn3.Show()

	def __choose_war(self):
		w = uichangerace.ChangeRace0()
		w.Show()
		ui.ScriptWindow.Hide(self)

	def __choose_ninja(self):
		n = uichangerace.ChangeRace1()
		n.Show()
		ui.ScriptWindow.Hide(self)

	def __choose_sura(self):
		s = uichangerace.ChangeRace2()
		s.Show()
		ui.ScriptWindow.Hide(self)

	def __choose_shaman(self):
		sh = uichangerace.ChangeRace3()
		sh.Show()
		ui.ScriptWindow.Hide(self)

class ChangeRace0(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__MakeWindow()
		self.__MakeBoard()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		ui.ScriptWindow.Hide(self)

	def OnPressEscapeKey(self):
		self.Close()

		return True

	def Destroy(self):
		self.Hide()

		return True

	def __MakeWindow(self):
		self.SetSize(160, 200)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
		)
		self.AddFlag("movable")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("movable")
		self.Board.Show()

		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()

		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("|cff00FFFFAlege sexul|h|r")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()

		self.bg0 = ui.ImageBox()
		self.bg0.SetParent(self.Board)
		self.bg0.SetPosition(5, 35)
		self.bg0.LoadImage("change_race/faces/icon_mwarrior.tga")
		self.bg0.Show()

		self.bg1 = ui.ImageBox()
		self.bg1.SetParent(self.Board)
		self.bg1.SetPosition(75, 35)
		self.bg1.LoadImage("change_race/faces/icon_wwarrior.tga")
		self.bg1.Show()

		self.btn0 = ui.Button()
		self.btn0.SetParent(self.Board)
		self.btn0.SetPosition(12,170)
		self.btn0.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn0.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn0.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetText("Alege")
		self.btn0.SetEvent(lambda : self.__choose_war_m())
		self.btn0.Show()

		self.btn1 = ui.Button()
		self.btn1.SetParent(self.Board)
		self.btn1.SetPosition(82,170)
		self.btn1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetText("Alege")
		self.btn1.SetEvent(lambda : self.__choose_war_f())
		self.btn1.Show()

	def __choose_war_m(self):
		net.SendChatPacket("/change_race 0")
		ui.ScriptWindow.Hide(self)

	def __choose_war_f(self):
		net.SendChatPacket("/change_race 4")
		ui.ScriptWindow.Hide(self)

class ChangeRace1(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__MakeWindow()
		self.__MakeBoard()

	def __del__(self):
		ui.ScriptWindow.__del__(self)


	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		ui.ScriptWindow.Hide(self)

	def OnPressEscapeKey(self):
		self.Close()

		return True

	def Destroy(self):
		self.Hide()

		return True

	def __MakeWindow(self):
		self.SetSize(160, 200)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
		)
		self.AddFlag("movable")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("movable")
		self.Board.Show()

		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()

		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("|cff00FFFFAlege sexul|h|r")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()

		self.bg0 = ui.ImageBox()
		self.bg0.SetParent(self.Board)
		self.bg0.SetPosition(5, 35)
		self.bg0.LoadImage("change_race/faces/icon_mninja.tga")
		self.bg0.Show()

		self.bg1 = ui.ImageBox()
		self.bg1.SetParent(self.Board)
		self.bg1.SetPosition(75, 35)
		self.bg1.LoadImage("change_race/faces/icon_wninja.tga")
		self.bg1.Show()

		self.btn0 = ui.Button()
		self.btn0.SetParent(self.Board)
		self.btn0.SetPosition(12,170)
		self.btn0.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn0.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn0.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetText("Alege")
		self.btn0.SetEvent(lambda : self.__choose_ninja_m())
		self.btn0.Show()

		self.btn1 = ui.Button()
		self.btn1.SetParent(self.Board)
		self.btn1.SetPosition(82,170)
		self.btn1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetText("Alege")
		self.btn1.SetEvent(lambda : self.__choose_ninja_f())
		self.btn1.Show()

	def __choose_ninja_m(self):
		net.SendChatPacket("/change_race 5")
		ui.ScriptWindow.Hide(self)

	def __choose_ninja_f(self):
		net.SendChatPacket("/change_race 1")
		ui.ScriptWindow.Hide(self)

class ChangeRace2(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__MakeWindow()
		self.__MakeBoard()

	def __del__(self):
		ui.ScriptWindow.__del__(self)


	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		ui.ScriptWindow.Hide(self)


	def OnPressEscapeKey(self):
		self.Close()

		return True

	def Destroy(self):
		self.Hide()

		return True

	def __MakeWindow(self):
		self.SetSize(160, 200)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
		)
		self.AddFlag("movable")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("movable")
		self.Board.Show()

		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()

		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("|cff00FFFFAlege sexul|h|r")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()

		self.bg0 = ui.ImageBox()
		self.bg0.SetParent(self.Board)
		self.bg0.SetPosition(5, 35)
		self.bg0.LoadImage("change_race/faces/icon_msura.tga")
		self.bg0.Show()

		self.bg1 = ui.ImageBox()
		self.bg1.SetParent(self.Board)
		self.bg1.SetPosition(75, 35)
		self.bg1.LoadImage("change_race/faces/icon_wsura.tga")
		self.bg1.Show()

		self.btn0 = ui.Button()
		self.btn0.SetParent(self.Board)
		self.btn0.SetPosition(12,170)
		self.btn0.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn0.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn0.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetText("Alege")
		self.btn0.SetEvent(lambda : self.__choose_sura_m())
		self.btn0.Show()

		self.btn1 = ui.Button()
		self.btn1.SetParent(self.Board)
		self.btn1.SetPosition(82,170)
		self.btn1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetText("Alege")
		self.btn1.SetEvent(lambda : self.__choose_sura_f())
		self.btn1.Show()

	def __choose_sura_m(self):
		net.SendChatPacket("/change_race 2")
		ui.ScriptWindow.Hide(self)

	def __choose_sura_f(self):
		net.SendChatPacket("/change_race 6")
		ui.ScriptWindow.Hide(self)

class ChangeRace3(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__MakeWindow()
		self.__MakeBoard()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		ui.ScriptWindow.Hide(self)

	def OnPressEscapeKey(self):
		self.Close()

		return True

	def Destroy(self):
		self.Hide()

		return True

	def __MakeWindow(self):
		self.SetSize(160, 200)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
		)
		self.AddFlag("movable")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("movable")
		self.Board.Show()

		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()

		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("|cff00FFFFAlege sexul|h|r")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()

		self.bg0 = ui.ImageBox()
		self.bg0.SetParent(self.Board)
		self.bg0.SetPosition(5, 35)
		self.bg0.LoadImage("change_race/faces/icon_mshaman.tga")
		self.bg0.Show()

		self.bg1 = ui.ImageBox()
		self.bg1.SetParent(self.Board)
		self.bg1.SetPosition(75, 35)
		self.bg1.LoadImage("change_race/faces/icon_wshaman.tga")
		self.bg1.Show()

		self.btn0 = ui.Button()
		self.btn0.SetParent(self.Board)
		self.btn0.SetPosition(12,170)
		self.btn0.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn0.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn0.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn0.SetText("Alege")
		self.btn0.SetEvent(lambda : self.__choose_shaman_m())
		self.btn0.Show()

		self.btn1 = ui.Button()
		self.btn1.SetParent(self.Board)
		self.btn1.SetPosition(82,170)
		self.btn1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.btn1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.btn1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetDisableVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.btn1.SetText("Alege")
		self.btn1.SetEvent(lambda : self.__choose_shaman_f())
		self.btn1.Show()

	def __choose_shaman_m(self):
		net.SendChatPacket("/change_race 7")
		ui.ScriptWindow.Hide(self)

	def __choose_shaman_f(self):
		net.SendChatPacket("/change_race 3")
		ui.ScriptWindow.Hide(self)