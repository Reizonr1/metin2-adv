uisystem.py aç
#---------------

self.GetChild("cancel_button").SAFE_SetEvent(self.Close)

arat


self.GetChild("arayuz_button").SAFE_SetEvent(self.arayuz)


altýna ekle.
#----------------------------------------------

def __ClickCikButton(self):

arat

	def arayuz(self):
		self.Close()
		try:
			self.k.OpenDialog()
			pass
		except:
			import uiinterfececolor
			self.k = uiinterfececolor.kolorDialog()
			self.k.OpenDialog()
			pass
			
altýna ekle.
#----------------------------------------------
ui.py aç
#----------

from _weakref import proxy

arat

import uiScriptLocale
LOCALE_PATH = uiScriptLocale.WINDOWS_PATH
interfacelist = (
						"d:/ymir work/ui/pattern/Board_Corner_LeftTop.tga",
						"d:/ymir work/ui/pattern/Board_Corner_LeftBottom.tga",
						"d:/ymir work/ui/pattern/Board_Corner_RightTop.tga",
						"d:/ymir work/ui/pattern/Board_Corner_RightBottom.tga",
						"d:/ymir work/ui/pattern/Board_Line_Left.tga",
						"d:/ymir work/ui/pattern/Board_Line_Right.tga",
						"d:/ymir work/ui/pattern/Board_Line_Top.tga",
						"d:/ymir work/ui/pattern/Board_Line_Bottom.tga",
						"d:/ymir work/ui/pattern/TaskBar_Base.tga",
						"d:/ymir work/ui/game/windows/equipment_base.sub",
						"d:/ymir work/ui/equipment_bg_without_ring.tga",
						"d:/ymir work/ui/pattern/titlebar_left.tga",
						"d:/ymir work/ui/pattern/titlebar_center.tga",
						"d:/ymir work/ui/pattern/titlebar_right.tga",
						"d:/ymir work/ui/pattern/Board_Base.tga",
						"d:/ymir work/ui/minimap/minimap.sub",
						LOCALE_PATH+"tab_1.sub",
						LOCALE_PATH+"tab_2.sub",
						LOCALE_PATH+"tab_3.sub",
						LOCALE_PATH+"tab_4.sub",
						LOCALE_PATH+"label_std_item1.sub",
						LOCALE_PATH+"label_std_item2.sub",
						LOCALE_PATH+"label_ext_item1.sub",
						LOCALE_PATH+"label_ext_item2.sub",
						"d:/ymir work/ui/pattern/ThinBoard_Corner_LeftTop.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Corner_LeftBottom.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Corner_RightBottom.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Corner_RightTop.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Line_Left.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Line_Right.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Line_Top.tga",
						"d:/ymir work/ui/pattern/ThinBoard_Line_Bottom.tga",
)


interfacelist2 = []

def zmiengrafike(r,g,b,a):
	for x in interfacelist2:
		if x:
			wndMgr.SetDiffuseColor(x.hWnd, r, g, b, a)

	pass
	

altýna ekle.
#----------------------------------------

locale_tr/systemdialog.py aç
#------------------------------

"name" : "exit_button",

arat

				{
					"name" : "arayuz_button",
					"type" : "button",

					"x" : 10,
					"y" : 247+30,

					"text" : "Renkli Arayüz",
					"text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_02.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_02.sub",
				},
				
				
üstüne ekle.
#----------------------------------------