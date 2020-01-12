import net
import snd
import locale
import constInfo
import ui
import uiToolTip
import dbg
import os
import app
import background

class SkyboxSelect(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.LoadMultiSkybox()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
		
	def Destroy(self):
		self.Hide()
		return TRUE
		
	def LoadMultiSkybox(self):
		self.SetSize(108, 370)
		self.Show()
		self.AddFlag('movable')
		self.AddFlag("float")
		self.SetTitleName('Cer')
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)
				
		self.LoadButtons()
		
	def LoadButtons(self):
	
		self.AlchemyHava01 = ui.Button()
		self.AlchemyHava01.SetParent(self)
		self.AlchemyHava01.SetPosition(10, 30)
		self.AlchemyHava01.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava01.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava01.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava01.SetText("Normal")
		self.AlchemyHava01.SetEvent(self.__Skybox_1)
		self.AlchemyHava01.Show()
	
		self.AlchemyHava02 = ui.Button()
		self.AlchemyHava02.SetParent(self)
		self.AlchemyHava02.SetPosition(10, 50)
		self.AlchemyHava02.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava02.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava02.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava02.SetText("Noapte")
		self.AlchemyHava02.SetEvent(self.__Skybox_2)
		self.AlchemyHava02.Show()
		
		self.AlchemyHava03 = ui.Button()
		self.AlchemyHava03.SetParent(self)
		self.AlchemyHava03.SetPosition(10, 80)
		self.AlchemyHava03.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava03.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava03.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava03.SetText("1")
		self.AlchemyHava03.SetEvent(self.__Skybox_3)
		self.AlchemyHava03.Show()
		
		self.AlchemyHava04 = ui.Button()
		self.AlchemyHava04.SetParent(self)
		self.AlchemyHava04.SetPosition(10, 100)
		self.AlchemyHava04.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava04.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava04.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava04.SetText("2")
		self.AlchemyHava04.SetEvent(self.__Skybox_4)
		self.AlchemyHava04.Show()
		
		self.AlchemyHava05 = ui.Button()
		self.AlchemyHava05.SetParent(self)
		self.AlchemyHava05.SetPosition(10, 120)
		self.AlchemyHava05.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava05.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava05.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava05.SetText("3")
		self.AlchemyHava05.SetEvent(self.__Skybox_5)
		self.AlchemyHava05.Show()
		
		self.AlchemyHava06 = ui.Button()
		self.AlchemyHava06.SetParent(self)
		self.AlchemyHava06.SetPosition(10, 140)
		self.AlchemyHava06.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava06.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava06.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava06.SetText("4")
		self.AlchemyHava06.SetEvent(self.__Skybox_6)
		self.AlchemyHava06.Show()
		
		self.AlchemyHava07 = ui.Button()
		self.AlchemyHava07.SetParent(self)
		self.AlchemyHava07.SetPosition(10, 160)
		self.AlchemyHava07.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava07.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava07.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava07.SetText("5")
		self.AlchemyHava07.SetEvent(self.__Skybox_7)
		self.AlchemyHava07.Show()
		
		self.AlchemyHava08 = ui.Button()
		self.AlchemyHava08.SetParent(self)
		self.AlchemyHava08.SetPosition(10, 180)
		self.AlchemyHava08.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava08.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava08.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava08.SetText("6")
		self.AlchemyHava08.SetEvent(self.__Skybox_8)
		self.AlchemyHava08.Show()
		
		self.AlchemyHava09 = ui.Button()
		self.AlchemyHava09.SetParent(self)
		self.AlchemyHava09.SetPosition(10, 200)
		self.AlchemyHava09.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava09.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava09.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava09.SetText("7")
		self.AlchemyHava09.SetEvent(self.__Skybox_9)
		self.AlchemyHava09.Show()
		
		self.AlchemyHava10 = ui.Button()
		self.AlchemyHava10.SetParent(self)
		self.AlchemyHava10.SetPosition(10, 220)
		self.AlchemyHava10.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava10.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava10.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava10.SetText("8")
		self.AlchemyHava10.SetEvent(self.__Skybox_10)
		self.AlchemyHava10.Show()
		
		self.AlchemyHava11 = ui.Button()
		self.AlchemyHava11.SetParent(self)
		self.AlchemyHava11.SetPosition(10, 240)
		self.AlchemyHava11.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava11.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava11.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava11.SetText("9")
		self.AlchemyHava11.SetEvent(self.__Skybox_11)
		self.AlchemyHava11.Show()
		
		self.AlchemyHava12 = ui.Button()
		self.AlchemyHava12.SetParent(self)
		self.AlchemyHava12.SetPosition(10, 260)
		self.AlchemyHava12.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava12.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava12.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava12.SetText("10")
		self.AlchemyHava12.SetEvent(self.__Skybox_12)
		self.AlchemyHava12.Show()
		
		self.AlchemyHava13 = ui.Button()
		self.AlchemyHava13.SetParent(self)
		self.AlchemyHava13.SetPosition(10, 280)
		self.AlchemyHava13.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava13.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava13.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava13.SetText("11")
		self.AlchemyHava13.SetEvent(self.__Skybox_13)
		self.AlchemyHava13.Show()
		
		self.AlchemyHava14 = ui.Button()
		self.AlchemyHava14.SetParent(self)
		self.AlchemyHava14.SetPosition(10, 300)
		self.AlchemyHava14.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava14.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava14.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava14.SetText("12")
		self.AlchemyHava14.SetEvent(self.__Skybox_14)
		self.AlchemyHava14.Show()
		
		self.AlchemyHava15 = ui.Button()
		self.AlchemyHava15.SetParent(self)
		self.AlchemyHava15.SetPosition(10, 320)
		self.AlchemyHava15.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava15.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava15.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava15.SetText("13")
		self.AlchemyHava15.SetEvent(self.__Skybox_15)
		self.AlchemyHava15.Show()
		
		self.AlchemyHava16 = ui.Button()
		self.AlchemyHava16.SetParent(self)
		self.AlchemyHava16.SetPosition(10, 340)
		self.AlchemyHava16.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.AlchemyHava16.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.AlchemyHava16.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.AlchemyHava16.SetText("14")
		self.AlchemyHava16.SetEvent(self.__Skybox_16)
		self.AlchemyHava16.Show()
		
	def __Skybox_1(self):
		background.SetEnvironmentData(0)
		
	def __Skybox_2(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_01)
		background.SetEnvironmentData(1)
		
	def __Skybox_3(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_02)
		background.SetEnvironmentData(1)
		
	def __Skybox_4(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_03)
		background.SetEnvironmentData(1)
		
	def __Skybox_5(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_04)
		background.SetEnvironmentData(1)

	def __Skybox_6(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_05)
		background.SetEnvironmentData(1)

	def __Skybox_7(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_06)
		background.SetEnvironmentData(1)

	def __Skybox_8(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_07)
		background.SetEnvironmentData(1)

	def __Skybox_9(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_08)
		background.SetEnvironmentData(1)

	def __Skybox_10(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_09)
		background.SetEnvironmentData(1)

	def __Skybox_11(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_10)
		background.SetEnvironmentData(1)
		
	def __Skybox_12(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_11)
		background.SetEnvironmentData(1)
		
	def __Skybox_13(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_12)
		background.SetEnvironmentData(1)
		
	def __Skybox_14(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_13)
		background.SetEnvironmentData(1)
		
	def __Skybox_15(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_14)
		background.SetEnvironmentData(1)
		
	def __Skybox_16(self):
		background.RegisterEnvironmentData(1, constInfo.ALCHEMY_SKYBOX_15)
		background.SetEnvironmentData(1)
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
