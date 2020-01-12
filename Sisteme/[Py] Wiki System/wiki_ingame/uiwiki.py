###########################################################
#					   WikiBoard by .Kori				  #
###########################################################
import ui
import player
import constInfo
import uiScriptLocale
import net
import snd
import app
import mouseModule
import playerSettingModule
import uicharacter
import uiToolTip
import grp
import item
import localeInfo
pos = [[20, 150], [20, 180], [20, 210], [20, 240], [20, 270], [20, 300]]
NavigationTextButton = ["Armas", "Evolução I", "Evolução II", "Mapas", "NPC's", "Informações"]
Face_Icon = ["0", "1", "2", "3", "4", "5", "6"]
WillkommensText = [["Bem-Vindo ao Sistema Wiki do Elusion2"], [" "],  ["Este sistema foi criado principalmente para exclarecimento de dúvidas."], ["Aqui poderás consultar todas as novidades do Elusion2."], ["Em caso de sugestões, duvidas ou erros, deverás consultar a equipa."]]
## Bonus
Bonus1 = [[155, 125], [295, 125], [435, 135], [575, 135], [155, 265], [290, 265], [430, 265], [570, 265]]
BoardPosition = [[110, 100], [250, 100], [390, 100], [530, 100], [110, 230], [250, 230], [390, 230], [530, 230]]
Bonus__Text = [["Espada Rúnica"], ["Lâmina Solar"], ["Lâmina Dente de Dragão"], ["Lâmina Cinco Elementos"], ["Arco de Fénix"], ["Campaínha Dracónica"], ["Leque Dragão"], ["Lorde Dragão"]]
Bonus__Position = [[135, 110], [280, 110], [420, 110], [560, 110], [135, 240], [285, 240], [425, 240], [556, 240]]
Bonus_Image = [["icon/item/00460.tga"], ["icon/item/03190.tga"], ["icon/item/00470.tga"], ["icon/item/01340.tga"], ["icon/item/02370.tga"], ["icon/item/05340.tga"], ["icon/item/07370.tga"], ["icon/item/06090.tga"]]
## Rüstung Uppsystem
RustungUppsystem = [[180, 100], [180, 230], [180, 100], [180, 230]]
RustungButtonPos = [[115, 350], [560, 350]]
RustungButtonBeschreibung = [["Anterior"], ["Seguinte"]]
RustungUberschrift = [["Evolução de Armaduras de Guerreiro"], ["Evolução de Armaduras de Ninja"], ["Evolução de Armaduras de Xamã"], ["Evolução de Armaduras de Sura"]]
RustungUberschriftPosition = [[300, 110], [300, 240], [300, 110], [300, 240]]
Rustung_Icons = [["icon/item/11290.tga", "pfeile.tga"], ["icon/item/12020.tga"], ["icon/item/20000.tga"], ["icon/item/8240.tga"], ["icon/item/11490.tga"], ["icon/item/12030.tga"], ["icon/item/20250.tga"], ["icon/item/8250.tga"], ["icon/item/11890.tga"], ["icon/item/12040.tga"], ["icon/item/20500.tga"], ["icon/item/8270.tga"], ["icon/item/11690.tga"], ["icon/item/12010.tga"], ["icon/item/20750.tga"], ["icon/item/8260.tga"]]
Rustung_IconPos = [[215, 125], [315, 125], [415, 125], [515, 125], [215, 255], [315, 255], [415, 255], [515, 255], [215, 125], [315, 125], [415, 125], [515, 125], [215, 255], [315, 255], [415, 255], [515, 255]]
Rustung_PfeilePos = [[265, 125], [365, 125], [465, 125], [570, 125], [265, 255], [365, 255], [465, 255], [570, 255], [265, 125], [365, 125], [465, 125], [570, 125], [265, 255], [365, 255], [465, 255], [570, 255]]
Notige_Items_Rustung = [["icon/item/money.tga", 20, 170], ["icon/item/71123.tga", 20, 40], ["icon/item/71129.tga", 20, 80], ["icon/item/30509.tga", 20, 40], ["icon/item/30514.tga", 20, 80], ["icon/item/30516.tga", 20, 120], ["icon/item/30512.tga", 20, 40], ["icon/item/30511.tga", 20, 80], ["icon/item/30513.tga", 20, 120]]
## Waffen Uppsystem
WaffenUppText = [["Evolução de Armas de Guerreiro I"], ["Evolução de Armas de Guerreiro II"], ["Evolução de Adagas"], ["Evolução de Arcos"], ["Evolução de Campaínhas"], ["Evolução de Leques"], ["Evolução de Armas de Sura"], [" "]]
WaffenUppTextPos = [[300, 110], [300, 220], [300, 110], [300, 220], [300, 110], [300, 220], [300, 110], [300, 220]]
WaffenButtonText = [["Guerreiro"], ["Ninja"], ["Xamã"], ["Sura"]]
WaffenButtonPos = [[205, 350], [295, 350], [385, 350], [475, 350]]
Waffen_Image = [["icon/item/00140.tga"], ["icon/item/00270.tga"], ["icon/item/00460.tga"], ["icon/item/set_17_sword.tga"], ["icon/item/03130.tga"], ["icon/item/03200.tga"], ["icon/item/03190.tga"], ["icon/item/set_17_spear.tga"], ["icon/item/01100.tga"], ["icon/item/04040.tga"], ["icon/item/01340.tga"], ["icon/item/set_17_knife.tga"], ["icon/item/02140.tga"], ["icon/item/02160.tga"], ["icon/item/02370.tga"], ["icon/item/set_17_bow.tga"], ["icon/item/05100.tga"], ["icon/item/05330.tga"], ["icon/item/05340.tga"], ["icon/item/set_17_bell.tga"], ["icon/item/07140.tga"], ["icon/item/07190.tga"], ["icon/item/07370.tga"], ["icon/item/set_17_range.tga"], ["icon/item/00150.tga"], ["icon/item/00280.tga"], ["icon/item/00470.tga"], ["icon/item/set_17_sword_s.tga"]]
Waffen_IconPos = [[215, 125], [315, 125], [415, 125], [515, 125], [215, 235], [315, 235], [415, 235], [515, 235], [215, 135], [315, 135], [415, 135], [515, 135], [215, 255], [315, 255], [415, 255], [515, 255], [215, 135], [315, 135], [415, 135], [515, 135], [215, 265], [315, 265], [415, 265], [515, 265], [215, 125], [315, 125], [415, 125], [515, 125]]
Notige_Items_Waffen = [["icon/item/money.tga", 20, 170], ["icon/item/25040.tga", 20, 40], ["icon/item/70031.tga", 20, 80], ["icon/item/51001.tga", 20, 120]]
## Run´s
Run_Image = [["run1.tga"], ["run2.tga"], ["run3.tga"]]
Run_ImagePos = [[120, 110], [120, 110], [120, 110]]
Run1 = "TEXTO PARA EDITAR 1"
Run2 = "TEXTO PARA EDITAR 2"
Run3 = "TEXTO PARA EDITAR 3"
Run_Buttons = [["Mapa PvP"], ["Mapa PvM"], ["TESTE"]]
Run_ButtonsPos = [[205, 355], [295, 355], [385, 355]]
Anzahl = [[1], [2], [3]]
## Quests
Quest_Icons = [["uriel.tga", 115, 120], ["bio.tga", 115, 120], ["soon.tga", 115, 120], ["afrau.tga", 115, 120]]
Quest1 = "Texto para editar 1"
Quest2 = "Texto para editar 2"
Quest3 = "Texto para editar 3"
Quest4 = "Texto para editar 4"
QuestButtons = [["Uriel"], ["Biólogo"], ["Sr. Soon"], ["Idosa"]]
QuestButtonsPos = [[205, 360], [295, 360], [385, 360], [475, 360]]
QuestAnzahl = [["1"], ["2"], ["3"], ["4"]]
## FAQ
FAQ_Text = "Informações Importantes:# #Este sistema é aberto automaticamente, clicando na tecla K.# #Para evitar erros, o Sistema Wiki deve ser fechado antes de saíres da conta ou alterares personagem.# #Em caso de dúvidas, erros, ou sugestões, contacta a equipa.# #Com os Melhores Cumprimentos,#A Equipa Elusion2"

FACE_IMAGE_DICT = ["icon/face/warrior_m.tga", "icon/face/warrior_w.tga", "icon/face/assassin_m.tga", "icon/face/assassin_w.tga", "icon/face/sura_m.tga", "icon/face/sura_w.tga", "icon/face/shaman_m.tga", "icon/face/shaman_w.tga", "icon/face/wolfman_m.tga", "icon/face/wolfman_w.tga"]

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName)
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(fileName)
		textLine.SetFontColor(1.0, 1.0, 0.0)
		textLine.Show()
		return textLine
		
class AgeofPlatonWiki(ui.BoardWithTitleBar):
	AFFECT_DICT = {
		item.APPLY_MAX_HP : localeInfo.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : localeInfo.TOOLTIP_MAX_SP,
		item.APPLY_CON : localeInfo.TOOLTIP_CON,
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
		item.APPLY_STR : localeInfo.TOOLTIP_STR,
		item.APPLY_DEX : localeInfo.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : localeInfo.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : localeInfo.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : localeInfo.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : localeInfo.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : localeInfo.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : localeInfo.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : localeInfo.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_PENETRATE_PCT,

		item.APPLY_ATTBONUS_WARRIOR : localeInfo.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : localeInfo.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : localeInfo.TOOLTIP_APPLY_ATTBONUS_MONSTER,

		item.APPLY_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : localeInfo.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : localeInfo.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : localeInfo.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : localeInfo.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : localeInfo.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : localeInfo.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : localeInfo.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : localeInfo.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : localeInfo.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : localeInfo.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : localeInfo.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : localeInfo.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : localeInfo.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : localeInfo.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : localeInfo.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : localeInfo.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : localeInfo.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : localeInfo.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : localeInfo.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : localeInfo.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : localeInfo.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : localeInfo.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : localeInfo.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : localeInfo.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : localeInfo.TOOLTIP_BOW_DISTANCE,
		#item.APPLY_DEF_GRADE : localeInfo.TOOLTIP_DEF_GRADE,
		#item.APPLY_ATT_GRADE : localeInfo.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : localeInfo.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : localeInfo.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : localeInfo.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : localeInfo.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : localeInfo.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : localeInfo.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : localeInfo.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : localeInfo.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_PC_BANG_EXP_BONUS : localeInfo.TOOLTIP_MALL_EXPBONUS_P_STATIC,
		item.APPLY_PC_BANG_DROP_BONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS_P_STATIC,
		item.APPLY_RESIST_WARRIOR : localeInfo.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : localeInfo.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : localeInfo.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : localeInfo.TOOLTIP_APPLY_RESIST_SHAMAN,
#		item.APPLY_MAX_HP_PCT : localeInfo.TOOLTIP_APPLY_MAX_HP_PCT,
#		item.APPLY_MAX_SP_PCT : localeInfo.TOOLTIP_APPLY_MAX_SP_PCT,
#		item.APPLY_ENERGY : localeInfo.TOOLTIP_ENERGY,
	}
	CHARACTER_NAMES = ( 
		localeInfo.TOOLTIP_WARRIOR,
		localeInfo.TOOLTIP_ASSASSIN,
		localeInfo.TOOLTIP_SURA,
		localeInfo.TOOLTIP_SHAMAN 
	)		
	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
	CHARACTER_COUNT = len(CHARACTER_NAMES)
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.SetSize(660, 405)
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.AddFlag('float')
		self.SetTitleName('Elusion2 Wiki')
		self.SetCloseEvent(self.__del__)
		self.Hide()
		self.Buttons = {}
		self.haupttext = {}
		self.Bonusliste = {}
		self.MinniBoard = {}
		self.Bonus_Text = {}
		self.Rustungupp = {}
		self.EinstellungsButton = {}
		self.RustungUberschrift = {}
		self.RustungIcons = {}
		self.Pfeile_Icon = {}
		self.Pfeile_Icon = {}
		self.WaffenuppText = {}
		self.WaffenButtons = {}
		self.WaffenIcon = {}
		self.RunImages = {}
		self.List = {}
		self.RunButtons = {}
		self.Upp_Items_2 = {}
		self.Upp_Items = {}
		self.QuestIcon = {}
		self.Quest_Buttons = {}
		self.Listcc = {}
		Seite = 0
		self.__Load()
		
	def __del__(self):
		self.Hide()
		
	def Destroy(self):
		self.Hide()
		return TRUE
		
	def __Load(self):
		import wiki
		global pos
		global NavigationTextButton
		self.WikiText = []
		posy = 10
		posy2 = 110
		race = net.GetMainActorRace()
		faceImageName = FACE_IMAGE_DICT[race]
		### Charakter Informationen ###
		self.header = ui.ThinBoard()
		self.header.SetParent(self)
		self.header.SetPosition(7, 27)
		self.header.SetSize(646, 80)
		self.header.Show()
		
		self.Face_slot = ui.ImageBox()
		self.Face_slot.SetParent(self.header)
		self.Face_slot.SetPosition(20, 10)
		self.Face_slot.LoadImage("d:/ymir work/ui/game/windows/box_face.sub")
		self.Face_slot.Show()
		
		self.Face_image = ui.ImageBox()
		self.Face_image.SetParent(self.Face_slot)
		self.Face_image.SetPosition(4, 4)
		self.Face_image.LoadImage(faceImageName)
		self.Face_image.Show()
		
		for text in wiki.Wiki1:
			self.Seite1Text = ui.TextLine()
			self.Seite1Text.SetParent(self.header)
			self.Seite1Text.SetPosition(75, posy)
			self.Seite1Text.SetText(str(text).split("#")[0])
			self.Seite1Text.Show()
			self.WikiText.append(self.Seite1Text)
			posy += 11
		### Charakter Informationen END ###
		### Willommens Naricht ###
		for haupt in xrange(len(WillkommensText)):
			self.haupttext[str(haupt)] = ui.TextLine()
			self.haupttext[str(haupt)].SetParent(self)
			self.haupttext[str(haupt)].SetPosition(300, posy2)
			self.haupttext[str(haupt)].SetText(WillkommensText[haupt][0])
			self.haupttext[str(haupt)].Show()
			posy2 += 11
		### Willommens Naricht END ###
		### Navigation ###
		
		self.Thinbordd = ui.ThinBoard()
		self.Thinbordd.SetParent(self)
		self.Thinbordd.SetSize(110, 300)
		self.Thinbordd.SetPosition(7, 102)
		self.Thinbordd.Show()

		for line in xrange(len(pos)):
			self.Buttons[str(line)] = ui.Button()
			self.Buttons[str(line)].SetParent(self)
			self.Buttons[str(line)].SetPosition(pos[line][0], pos[line][1])
			self.Buttons[str(line)].SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub")
			self.Buttons[str(line)].SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub")
			self.Buttons[str(line)].SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub")
			self.Buttons[str(line)].SetText(NavigationTextButton[line])
			self.Buttons[str(line)].SetEvent(lambda arg = line : self.__OnClickButton (arg))
			self.Buttons[str(line)].Show()
		### Navigation END ###
		
		### Bonus Liste ###
		self.toolTiprustung = uiToolTip.ToolTip()
		self.toolTiprustung.ClearToolTip()
		self.toolTiprustung.AutoAppendTextLine("Bonús da Arma+0", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTiprustung.AutoAppendTextLine("")
		self.toolTiprustung.AutoAppendTextLine("Nível Mínimo: 87", grp.GenerateColor(255,185,15, 1.0))
		self.toolTiprustung.AutoAppendTextLine("Valor de Ataque: 153 - 208")
		self.toolTiprustung.AutoAppendTextLine("Valor de Ataque Mágico: 119 - 161 ")
		self.toolTiprustung.AutoAppendTextLine("Rapidez de Ataque: +15%")
		self.toolTiprustung.AutoAppendTextLine("Forte contra Semi-Humanos: +2%")
		self.toolTiprustung.AutoAppendTextLine("Forte contra Monstros: +1&")
		self.toolTiprustung.AutoAppendTextLine("Equipável para:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTiprustung.AutoAppendTextLine("Guerreiro Ninja Sura")
		self.toolTiprustung.AlignHorizonalCenter()
		
		self.toolTipwaffen = uiToolTip.ToolTip()
		self.toolTipwaffen.ClearToolTip()
		self.toolTipwaffen.AutoAppendTextLine("Mögliche Boni für Waffen:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipwaffen.AutoAppendTextLine("")
		self.toolTipwaffen.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipwaffen.AutoAppendTextLine("Esoterische +20% ")
		self.toolTipwaffen.AutoAppendTextLine("Halbmenschen +10% ")
		self.toolTipwaffen.AutoAppendTextLine("Orks +20% ")
		self.toolTipwaffen.AutoAppendTextLine("Teufel +20% ")
		self.toolTipwaffen.AutoAppendTextLine("Tiere +20% ")
		self.toolTipwaffen.AutoAppendTextLine("Untote +20% ")
		self.toolTipwaffen.AutoAppendTextLine("")
		self.toolTipwaffen.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipwaffen.AutoAppendTextLine("Keine")
		self.toolTipwaffen.AutoAppendTextLine("")
		self.toolTipwaffen.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipwaffen.AutoAppendTextLine("10% Chance auf durchbohrenden Treffer")
		self.toolTipwaffen.AutoAppendTextLine("10% Chance auf kritischen Treffer")
		self.toolTipwaffen.AutoAppendTextLine("Vergiftungschance: 8%")
		self.toolTipwaffen.AutoAppendTextLine("Ohnmachtschance: 8%")
		self.toolTipwaffen.AutoAppendTextLine("Verlangsamungschance: 8%")
		self.toolTipwaffen.AutoAppendTextLine("Zaubergeschwindigkeit +20%")
		self.toolTipwaffen.AutoAppendTextLine("Intelligenz +12")
		self.toolTipwaffen.AutoAppendTextLine("Stärke +12")
		self.toolTipwaffen.AutoAppendTextLine("Beweglichkeit +12")
		self.toolTipwaffen.AutoAppendTextLine("Lebenskraft +12")
		self.toolTipwaffen.AlignHorizonalCenter()
		
		self.toolTipschuhe = uiToolTip.ToolTip()
		self.toolTipschuhe.ClearToolTip()
		self.toolTipschuhe.AutoAppendTextLine("Mögliche Boni für Schuhe:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipschuhe.AutoAppendTextLine("")
		self.toolTipschuhe.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipschuhe.AutoAppendTextLine("Keine")
		self.toolTipschuhe.AutoAppendTextLine("")
		self.toolTipschuhe.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipschuhe.AutoAppendTextLine("15% Schwertverteidigung")
		self.toolTipschuhe.AutoAppendTextLine("15% Zweihandverteidigung")
		self.toolTipschuhe.AutoAppendTextLine("15% Dolchverteidigung")
		self.toolTipschuhe.AutoAppendTextLine("15% Glockenverteidigung")
		self.toolTipschuhe.AutoAppendTextLine("15% Fächerverteidigung")
		self.toolTipschuhe.AutoAppendTextLine("15% Pfeilwiderstand")
		self.toolTipschuhe.AutoAppendTextLine("")
		self.toolTipschuhe.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipschuhe.AutoAppendTextLine("10% Chance auf kritischen Treffer")
		self.toolTipschuhe.AutoAppendTextLine("Ohnmachtschance: 8%")
		self.toolTipschuhe.AutoAppendTextLine("Verlangsamungschance: 8%")
		self.toolTipschuhe.AutoAppendTextLine("Max. TP +100 bis +2000")
		self.toolTipschuhe.AutoAppendTextLine("Max. MP +20 bis +80")
		self.toolTipschuhe.AutoAppendTextLine("20% Chance auf EXP Bonus")
		self.toolTipschuhe.AutoAppendTextLine("Angriffsgeschwindigkeit +8%")
		self.toolTipschuhe.AutoAppendTextLine("20% Chance, eine doppelte Menge Yang fallen zu lassen")
		self.toolTipschuhe.AutoAppendTextLine("15% Chance Pfeilangriffen auszuweichen")
		self.toolTipschuhe.AlignHorizonalCenter()
		
		self.toolTipSchilld = uiToolTip.ToolTip()
		self.toolTipSchilld.ClearToolTip()
		self.toolTipSchilld.AutoAppendTextLine("Mögliche Boni für Schilder:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipSchilld.AutoAppendTextLine("")
		self.toolTipSchilld.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipSchilld.AutoAppendTextLine("Esoterische +20%")
		self.toolTipSchilld.AutoAppendTextLine("Halbmenschen +10%")
		self.toolTipSchilld.AutoAppendTextLine("Orks +20%")
		self.toolTipSchilld.AutoAppendTextLine("Teufel +20%")
		self.toolTipSchilld.AutoAppendTextLine("Tiere +20%")
		self.toolTipSchilld.AutoAppendTextLine("Untote +20%")
		self.toolTipSchilld.AutoAppendTextLine("")
		self.toolTipSchilld.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipSchilld.AutoAppendTextLine("Abwehr gegen Ohnmacht")
		self.toolTipSchilld.AutoAppendTextLine("Abwehr gegen Verlangsamung")
		self.toolTipSchilld.AutoAppendTextLine("")
		self.toolTipSchilld.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipSchilld.AutoAppendTextLine("15% Chance, Nahkampftreffer zu reflektieren")
		self.toolTipSchilld.AutoAppendTextLine("15% Chance direkten körperlichen Angriff abzublocken")
		self.toolTipSchilld.AutoAppendTextLine("20% Chance auf EXP Bonus")
		self.toolTipSchilld.AutoAppendTextLine("20% Chance, eine doppelte Menge Yang fallen zu lassen")
		self.toolTipSchilld.AutoAppendTextLine("Intelligenz +12")
		self.toolTipSchilld.AutoAppendTextLine("Stärke +12")
		self.toolTipSchilld.AutoAppendTextLine("Beweglichkeit +12")
		self.toolTipSchilld.AutoAppendTextLine("Lebenskraft +12")
		self.toolTipSchilld.AlignHorizonalCenter()
		
		self.toolTipOhr = uiToolTip.ToolTip()
		self.toolTipOhr.ClearToolTip()
		self.toolTipOhr.AutoAppendTextLine("Mögliche Boni für Ohrringe:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipOhr.AutoAppendTextLine("")
		self.toolTipOhr.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipOhr.AutoAppendTextLine("Esoterische +20%")
		self.toolTipOhr.AutoAppendTextLine("Halbmenschen +10%")
		self.toolTipOhr.AutoAppendTextLine("Orks +20%")
		self.toolTipOhr.AutoAppendTextLine("Teufel +20%")
		self.toolTipOhr.AutoAppendTextLine("Tiere +20%")
		self.toolTipOhr.AutoAppendTextLine("Untote +20%")
		self.toolTipOhr.AutoAppendTextLine("")
		self.toolTipOhr.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipOhr.AutoAppendTextLine("15% Schwertverteidigung")
		self.toolTipOhr.AutoAppendTextLine("15% Zweihandverteidigung")
		self.toolTipOhr.AutoAppendTextLine("15% Dolchverteidigung")
		self.toolTipOhr.AutoAppendTextLine("15% Glockenverteidigung")
		self.toolTipOhr.AutoAppendTextLine("15% Fächerverteidigung")
		self.toolTipOhr.AutoAppendTextLine("15% Pfeilwiderstand")
		self.toolTipOhr.AutoAppendTextLine("")
		self.toolTipOhr.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipOhr.AutoAppendTextLine("10% Chance auf Manaraub")
		self.toolTipOhr.AutoAppendTextLine("5% Giftwiderstand")
		self.toolTipOhr.AutoAppendTextLine("20% Chance, eine doppelte Menge von Gegenständen fallen zu lassen")
		self.toolTipOhr.AutoAppendTextLine("20% Bewegungsgeschwindigkeit")
		self.toolTipOhr.AlignHorizonalCenter()
		
		self.toolTipHelm = uiToolTip.ToolTip()
		self.toolTipHelm.ClearToolTip()
		self.toolTipHelm.AutoAppendTextLine("Mögliche Boni für Helme:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipHelm.AutoAppendTextLine("")
		self.toolTipHelm.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipHelm.AutoAppendTextLine("Esoterische +20%")
		self.toolTipHelm.AutoAppendTextLine("Halbmenschen +10%")
		self.toolTipHelm.AutoAppendTextLine("Orks +20%")
		self.toolTipHelm.AutoAppendTextLine("Teufel +20%")
		self.toolTipHelm.AutoAppendTextLine("Tiere +20%")
		self.toolTipHelm.AutoAppendTextLine("Untote +20%")
		self.toolTipHelm.AutoAppendTextLine("")
		self.toolTipHelm.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipHelm.AutoAppendTextLine("15% Magiewiderstand")
		self.toolTipHelm.AutoAppendTextLine("15% Blitzwiderstand")
		self.toolTipHelm.AutoAppendTextLine("15% Windwiderstand")
		self.toolTipHelm.AutoAppendTextLine("15% Feuerwiderstand")
		self.toolTipHelm.AutoAppendTextLine("")
		self.toolTipHelm.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipHelm.AutoAppendTextLine("Vergiftungschance: 8%")
		self.toolTipHelm.AutoAppendTextLine("Schaden 10% wird von MP absorbiert")
		self.toolTipHelm.AutoAppendTextLine("MP-Regeneration +30%")
		self.toolTipHelm.AutoAppendTextLine("TP-Regeneration +30%")
		self.toolTipHelm.AutoAppendTextLine("Angriffsgeschwindigkeit +8%")
		self.toolTipHelm.AutoAppendTextLine("15% Chance Pfeilangriffen auszuweichen")
		self.toolTipHelm.AlignHorizonalCenter()
		
		self.toolTipKetten = uiToolTip.ToolTip()
		self.toolTipKetten.ClearToolTip()
		self.toolTipKetten.AutoAppendTextLine("Mögliche Boni für Ketten:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipKetten.AutoAppendTextLine("")
		self.toolTipKetten.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipKetten.AutoAppendTextLine("Keine")
		self.toolTipKetten.AutoAppendTextLine("")
		self.toolTipKetten.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipKetten.AutoAppendTextLine("15% Schwertverteidigung")
		self.toolTipKetten.AutoAppendTextLine("15% Zweihandverteidigung")
		self.toolTipKetten.AutoAppendTextLine("15% Dolchverteidigung")
		self.toolTipKetten.AutoAppendTextLine("15% Glockenverteidigung")
		self.toolTipKetten.AutoAppendTextLine("15% Fächerverteidigung")
		self.toolTipKetten.AutoAppendTextLine("15% Pfeilwiderstand")
		self.toolTipKetten.AutoAppendTextLine("")
		self.toolTipKetten.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipKetten.AutoAppendTextLine("Ohnmachtschance: 8%")
		self.toolTipKetten.AutoAppendTextLine("10% Chance auf durchbohrenden Treffer")
		self.toolTipKetten.AutoAppendTextLine("10% Chance auf kritischen Treffer")
		self.toolTipKetten.AutoAppendTextLine("Schaden 10% wird von MP absorbiert")
		self.toolTipKetten.AutoAppendTextLine("10% Chance auf Manaraub")
		self.toolTipKetten.AutoAppendTextLine("Max. TP +100 bis +2000")
		self.toolTipKetten.AutoAppendTextLine("Max. MP +10 bis +200")
		self.toolTipKetten.AutoAppendTextLine("MP-Regeneration +30%")
		self.toolTipKetten.AutoAppendTextLine("TP-Regeneration +30%")
		self.toolTipKetten.AutoAppendTextLine("20% Chance auf EXP Bonus")
		self.toolTipKetten.AutoAppendTextLine("20% Chance, eine doppelte Menge Yang fallen zu lassen")
		self.toolTipKetten.AlignHorizonalCenter()
		
		self.toolTipABand = uiToolTip.ToolTip()
		self.toolTipABand.ClearToolTip()
		self.toolTipABand.AutoAppendTextLine("Mögliche Boni für Armbänder:", uiToolTip.ToolTip.TITLE_COLOR)
		self.toolTipABand.AutoAppendTextLine("")
		self.toolTipABand.AutoAppendTextLine("Stark Gegen:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipABand.AutoAppendTextLine("Esoterische +20%")
		self.toolTipABand.AutoAppendTextLine("Halbmenschen +10%")
		self.toolTipABand.AutoAppendTextLine("Orks +20%")
		self.toolTipABand.AutoAppendTextLine("Teufel +20%")
		self.toolTipABand.AutoAppendTextLine("Tiere +20%")
		self.toolTipABand.AutoAppendTextLine("Untote +20%")
		self.toolTipABand.AutoAppendTextLine("")
		self.toolTipABand.AutoAppendTextLine("Mögliche Widerstände:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipABand.AutoAppendTextLine("15% Magiewiderstand")
		self.toolTipABand.AutoAppendTextLine("15% Blitzwiderstand")
		self.toolTipABand.AutoAppendTextLine("15% Windwiderstand")
		self.toolTipABand.AutoAppendTextLine("15% Feuerwiderstand")
		self.toolTipABand.AutoAppendTextLine("")
		self.toolTipABand.AutoAppendTextLine("Sonstiges:", grp.GenerateColor(255,185,15, 1.0))
		self.toolTipABand.AutoAppendTextLine("10% Chance auf durchbohrenden Treffer")
		self.toolTipABand.AutoAppendTextLine("Schaden 10% wird von TP absorbiert")
		self.toolTipABand.AutoAppendTextLine("10% Chance auf Manaraub")
		self.toolTipABand.AutoAppendTextLine("Max. TP +100 bis +2000 (Bei Armbändern mit Standard TP-Bonus nicht)")
		self.toolTipABand.AutoAppendTextLine("Max. MP +10 bis +80 (Bei Armbändern mit Standard MP-Bonus nicht)")
		self.toolTipABand.AutoAppendTextLine("20% Chance, eine doppelte Menge von Gegenständen fallen zu lassen")
		self.toolTipABand.AlignHorizonalCenter()
		
		for miniboard in xrange(len(BoardPosition)):
			self.MinniBoard[str(miniboard)] = ui.Board()
			self.MinniBoard[str(miniboard)].SetParent(self)
			self.MinniBoard[str(miniboard)].SetSize(120, 110)
			self.MinniBoard[str(miniboard)].SetPosition(BoardPosition[miniboard][0], BoardPosition[miniboard][1])
			self.MinniBoard[str(miniboard)].Hide()
		
		for Bonus in xrange(len(Bonus1)):
			self.Bonusliste[str(Bonus)] = ui.ImageBox()
			self.Bonusliste[str(Bonus)].SetParent(self)
			self.Bonusliste[str(Bonus)].LoadImage(Bonus_Image[Bonus][0])
			self.Bonusliste[str(Bonus)].SetPosition(Bonus1[Bonus][0], Bonus1[Bonus][1])
			self.Bonusliste[str(Bonus)].Hide()
		self.Bonusliste[str(0)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip)
		self.Bonusliste[str(0)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip)
		self.Bonusliste[str(1)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip1)
		self.Bonusliste[str(1)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip1)
		self.Bonusliste[str(2)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip2)
		self.Bonusliste[str(2)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip2)
		self.Bonusliste[str(3)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip3)
		self.Bonusliste[str(3)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip3)
		self.Bonusliste[str(4)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip4)
		self.Bonusliste[str(4)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip4)
		self.Bonusliste[str(5)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip5)
		self.Bonusliste[str(5)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip5)
		self.Bonusliste[str(6)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip6)
		self.Bonusliste[str(6)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip6)
		self.Bonusliste[str(7)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip7)
		self.Bonusliste[str(7)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideToolTip7)
			
		for BonusText in xrange(len(Bonus__Position)):
			self.Bonus_Text[str(BonusText)] = ui.TextLine()
			self.Bonus_Text[str(BonusText)].SetParent(self)
			self.Bonus_Text[str(BonusText)].SetPosition(Bonus__Position[BonusText][0], Bonus__Position[BonusText][1])
			self.Bonus_Text[str(BonusText)].SetText(Bonus__Text[BonusText][0])
			self.Bonus_Text[str(BonusText)].Hide()
		### Rüstungen Seite ###
		for Copy in xrange(len(RustungUppsystem)):
			self.Rustungupp[str(Copy)]  = ui.Board()
			self.Rustungupp[str(Copy)].SetParent(self)
			self.Rustungupp[str(Copy)].SetSize(400, 110)
			self.Rustungupp[str(Copy)].SetPosition(RustungUppsystem[Copy][0], RustungUppsystem[Copy][1])
			self.Rustungupp[str(Copy)].Hide()
		
		for ProfessorDrEnte in xrange(len(RustungButtonPos)):
			self.EinstellungsButton[str(ProfessorDrEnte)] = ui.Button()
			self.EinstellungsButton[str(ProfessorDrEnte)].SetParent(self)
			self.EinstellungsButton[str(ProfessorDrEnte)].SetPosition(RustungButtonPos[ProfessorDrEnte][0], RustungButtonPos[ProfessorDrEnte][1])
			self.EinstellungsButton[str(ProfessorDrEnte)].SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub")
			self.EinstellungsButton[str(ProfessorDrEnte)].SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub")
			self.EinstellungsButton[str(ProfessorDrEnte)].SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub")
			self.EinstellungsButton[str(ProfessorDrEnte)].SetText(RustungButtonBeschreibung[ProfessorDrEnte][0])
			self.EinstellungsButton[str(ProfessorDrEnte)].SetEvent(lambda arg = ProfessorDrEnte : self.__OnKlickRustung (arg))
			self.EinstellungsButton[str(ProfessorDrEnte)].Hide()
			
		for poccix in xrange(len(RustungUppsystem)):
			self.RustungUberschrift[str(poccix)] = ui.TextLine()
			self.RustungUberschrift[str(poccix)].SetParent(self)
			self.RustungUberschrift[str(poccix)].SetPosition(RustungUberschriftPosition[poccix][0], RustungUberschriftPosition[poccix][1])
			self.RustungUberschrift[str(poccix)].SetText(RustungUberschrift[poccix][0])
			self.RustungUberschrift[str(poccix)].Hide()
			
		for Kryter in xrange(len(Rustung_Icons)):
			self.RustungIcons[str(Kryter)] = ui.ImageBox()
			self.RustungIcons[str(Kryter)].SetParent(self)
			self.RustungIcons[str(Kryter)].SetPosition(Rustung_IconPos[Kryter][0], Rustung_IconPos[Kryter][1])
			self.RustungIcons[str(Kryter)].LoadImage(Rustung_Icons[Kryter][0])
			self.RustungIcons[str(Kryter)].Hide()
		self.RustungIcons[str(1)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp)
		self.RustungIcons[str(1)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp)
		self.RustungIcons[str(2)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe2)
		self.RustungIcons[str(2)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe2)
		self.RustungIcons[str(3)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe3)
		self.RustungIcons[str(3)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe3)
		
		self.RustungIcons[str(5)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp)
		self.RustungIcons[str(5)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp)
		self.RustungIcons[str(6)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe2)
		self.RustungIcons[str(6)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe2)
		self.RustungIcons[str(7)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe3)
		self.RustungIcons[str(7)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe3)
		
		self.RustungIcons[str(9)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp)
		self.RustungIcons[str(9)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp)
		self.RustungIcons[str(10)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe2)
		self.RustungIcons[str(10)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe2)
		self.RustungIcons[str(11)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe3)
		self.RustungIcons[str(11)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe3)
		
		self.RustungIcons[str(13)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp)
		self.RustungIcons[str(13)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp)
		self.RustungIcons[str(14)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe2)
		self.RustungIcons[str(14)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe2)
		self.RustungIcons[str(15)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowRustungUpp_Stufe3)
		self.RustungIcons[str(15)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideRustungUpp_Stufe3)
		
		self.UppBoard = ui.ThinBoard()
		self.UppBoard.SetSize(250, 210)
		self.UppBoard.SetParent(self)
		self.UppBoard.SetPosition(665, 120)
		self.UppBoard.AddFlag('float')
		self.UppBoard.Hide()
		
		self.UppText = ui.TextLine()
		self.UppText.SetParent(self.UppBoard)
		self.UppText.SetText("Benötigte Items für diese Rüstung:")
		self.UppText.SetPosition(50, 20)
		self.UppText.Hide()
		##Stufe 1
		self.UppText_Stufe1_1 = ui.TextLine()
		self.UppText_Stufe1_1.SetParent(self.UppBoard)
		self.UppText_Stufe1_1.SetText("Benötigte Drachenschuppen: 3x")
		self.UppText_Stufe1_1.SetPosition(55, 50)
		self.UppText_Stufe1_1.Hide()
		
		self.UppText_Stufe1_2 = ui.TextLine()
		self.UppText_Stufe1_2.SetParent(self.UppBoard)
		self.UppText_Stufe1_2.SetText("Benötigte Drachenkrallen: 4x")
		self.UppText_Stufe1_2.SetPosition(55, 90)
		self.UppText_Stufe1_2.Hide()
		
		self.UppText_Stufe1_3 = ui.TextLine()
		self.UppText_Stufe1_3.SetParent(self.UppBoard)
		self.UppText_Stufe1_3.SetText("Benötigtes Yang: 10.000")
		self.UppText_Stufe1_3.SetPosition(55, 180)
		self.UppText_Stufe1_3.Hide()
		##Stufe 2
		self.UppText_Stufe2_1 = ui.TextLine()
		self.UppText_Stufe2_1.SetParent(self.UppBoard)
		self.UppText_Stufe2_1.SetText("Benötigtes Blaudrachenstahl: 10x")
		self.UppText_Stufe2_1.SetPosition(55, 50)
		self.UppText_Stufe2_1.Hide()
		
		self.UppText_Stufe2_2 = ui.TextLine()
		self.UppText_Stufe2_2.SetParent(self.UppBoard)
		self.UppText_Stufe2_2.SetText("Benötigter  Violetter Stoff: 10x")
		self.UppText_Stufe2_2.SetPosition(55, 90)
		self.UppText_Stufe2_2.Hide()
		
		self.UppText_Stufe2_3 = ui.TextLine()
		self.UppText_Stufe2_3.SetParent(self.UppBoard)
		self.UppText_Stufe2_3.SetText("Benötigtes Antikes Schulterstück: 10x")
		self.UppText_Stufe2_3.SetPosition(55, 130)
		self.UppText_Stufe2_3.Hide()
		
		self.UppText_Stufe2_4 = ui.TextLine()
		self.UppText_Stufe2_4.SetParent(self.UppBoard)
		self.UppText_Stufe2_4.SetText("Benötigtes Yang: 30.000")
		self.UppText_Stufe2_4.SetPosition(55, 180)
		self.UppText_Stufe2_4.Hide()
		## Stufe 3
		self.UppText_Stufe3_1 = ui.TextLine()
		self.UppText_Stufe3_1.SetParent(self.UppBoard)
		self.UppText_Stufe3_1.SetText("Benötigtes Rotdrachenstahl: 10x")
		self.UppText_Stufe3_1.SetPosition(55, 50)
		self.UppText_Stufe3_1.Hide()
		
		self.UppText_Stufe3_2 = ui.TextLine()
		self.UppText_Stufe3_2.SetParent(self.UppBoard)
		self.UppText_Stufe3_2.SetText("Benötigter  Roter Stoff: 10x")
		self.UppText_Stufe3_2.SetPosition(55, 90)
		self.UppText_Stufe3_2.Hide()
		
		self.UppText_Stufe3_3 = ui.TextLine()
		self.UppText_Stufe3_3.SetParent(self.UppBoard)
		self.UppText_Stufe3_3.SetText("Benötigtes Edles Schulterstück: 10x")
		self.UppText_Stufe3_3.SetPosition(55, 130)
		self.UppText_Stufe3_3.Hide()
		
		self.UppText_Stufe3_4 = ui.TextLine()
		self.UppText_Stufe3_4.SetParent(self.UppBoard)
		self.UppText_Stufe3_4.SetText("Benötigtes Yang: 900.000")
		self.UppText_Stufe3_4.SetPosition(55, 180)
		self.UppText_Stufe3_4.Hide()
		
		for UppItems in xrange(len(Notige_Items_Rustung)):
			self.Upp_Items[str(UppItems)] = ui.ImageBox()
			self.Upp_Items[str(UppItems)].SetParent(self.UppBoard)
			self.Upp_Items[str(UppItems)].SetPosition(Notige_Items_Rustung[UppItems][1], Notige_Items_Rustung[UppItems][2])
			self.Upp_Items[str(UppItems)].LoadImage(Notige_Items_Rustung[UppItems][0])
			self.Upp_Items[str(UppItems)].Hide()
			
		### Waffen Seite ###
		self.Waffenupp = ui.Board()
		self.Waffenupp.SetParent(self)
		self.Waffenupp.SetSize(400, 240)
		self.Waffenupp.SetPosition(180, 100)
		self.Waffenupp.Hide()
		
		for UppItems_2 in xrange(len(Notige_Items_Waffen)):
			self.Upp_Items_2[str(UppItems_2)] = ui.ImageBox()
			self.Upp_Items_2[str(UppItems_2)].SetParent(self.UppBoard)
			self.Upp_Items_2[str(UppItems_2)].SetPosition(Notige_Items_Waffen[UppItems_2][1], Notige_Items_Waffen[UppItems_2][2])
			self.Upp_Items_2[str(UppItems_2)].LoadImage(Notige_Items_Waffen[UppItems_2][0])
			self.Upp_Items_2[str(UppItems_2)].Hide()
			
		self.UppText_w = ui.TextLine()
		self.UppText_w.SetParent(self.UppBoard)
		self.UppText_w.SetText("Benötigte Items für diese Waffe:")
		self.UppText_w.SetPosition(50, 20)
		self.UppText_w.Hide()
		## Stufe 1
		self.UppText_Waffen_Stufe1_1 = ui.TextLine()
		self.UppText_Waffen_Stufe1_1.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe1_1.SetText("Benötigte SegenSchriftrollen: 2x")
		self.UppText_Waffen_Stufe1_1.SetPosition(55, 50)
		self.UppText_Waffen_Stufe1_1.Hide()
		
		self.UppText_Waffen_Stufe1_2 = ui.TextLine()
		self.UppText_Waffen_Stufe1_2.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe1_2.SetText("Benötigte Traktat zur Fechtkunst: 1x")
		self.UppText_Waffen_Stufe1_2.SetPosition(55, 90)
		self.UppText_Waffen_Stufe1_2.Hide()
		
		self.UppText_Waffen_Stufe1_3 = ui.TextLine()
		self.UppText_Waffen_Stufe1_3.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe1_3.SetText("Benötigtes Yang: 100.000")
		self.UppText_Waffen_Stufe1_3.SetPosition(55, 180)
		self.UppText_Waffen_Stufe1_3.Hide()
		# Stufe 2
		self.UppText_Waffen_Stufe2_1 = ui.TextLine()
		self.UppText_Waffen_Stufe2_1.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe2_1.SetText("Benötigte Segenschriftrollen: 2x")
		self.UppText_Waffen_Stufe2_1.SetPosition(55, 50)
		self.UppText_Waffen_Stufe2_1.Hide()
		
		self.UppText_Waffen_Stufe2_2 = ui.TextLine()
		self.UppText_Waffen_Stufe2_2.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe2_2.SetText("Benötigte Traktat zur Fechtkunst: 3x")
		self.UppText_Waffen_Stufe2_2.SetPosition(55, 90)
		self.UppText_Waffen_Stufe2_2.Hide()
		
		self.UppText_Waffen_Stufe2_3 = ui.TextLine()
		self.UppText_Waffen_Stufe2_3.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe2_3.SetText("Benötigte Energiesplitter: 100x")
		self.UppText_Waffen_Stufe2_3.SetPosition(55, 130)
		self.UppText_Waffen_Stufe2_3.Hide()
		
		self.UppText_Waffen_Stufe2_4 = ui.TextLine()
		self.UppText_Waffen_Stufe2_4.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe2_4.SetText("Benötigtes Yang: 500.000")
		self.UppText_Waffen_Stufe2_4.SetPosition(55, 180)
		self.UppText_Waffen_Stufe2_4.Hide()
		#Stufe 3
		self.UppText_Waffen_Stufe3_1 = ui.TextLine()
		self.UppText_Waffen_Stufe3_1.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe3_1.SetText("Benötigte Segenschriftrollen: 10x")
		self.UppText_Waffen_Stufe3_1.SetPosition(55, 50)
		self.UppText_Waffen_Stufe3_1.Hide()
		
		self.UppText_Waffen_Stufe3_2 = ui.TextLine()
		self.UppText_Waffen_Stufe3_2.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe3_2.SetText("Benötigte Traktat zur Fechtkunst: 10x")
		self.UppText_Waffen_Stufe3_2.SetPosition(55, 90)
		self.UppText_Waffen_Stufe3_2.Hide()
		
		self.UppText_Waffen_Stufe3_3 = ui.TextLine()
		self.UppText_Waffen_Stufe3_3.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe3_3.SetText("Benötigte Energiesplitter: 200x")
		self.UppText_Waffen_Stufe3_3.SetPosition(55, 130)
		self.UppText_Waffen_Stufe3_3.Hide()
		
		self.UppText_Waffen_Stufe3_4 = ui.TextLine()
		self.UppText_Waffen_Stufe3_4.SetParent(self.UppBoard)
		self.UppText_Waffen_Stufe3_4.SetText("Benötigtes Yang: 1.000.000")
		self.UppText_Waffen_Stufe3_4.SetPosition(55, 180)
		self.UppText_Waffen_Stufe3_4.Hide()
		
		for jauteng in xrange(len(WaffenUppTextPos)):
			self.WaffenuppText[str(jauteng)] = ui.TextLine()
			self.WaffenuppText[str(jauteng)].SetParent(self)
			self.WaffenuppText[str(jauteng)].SetPosition(WaffenUppTextPos[jauteng][0], WaffenUppTextPos[jauteng][1])
			self.WaffenuppText[str(jauteng)].SetText(WaffenUppText[jauteng][0])
			self.WaffenuppText[str(jauteng)].Hide()
			
		for Kori in xrange(len(WaffenButtonPos)):
			self.WaffenButtons[str(Kori)] = ui.Button()
			self.WaffenButtons[str(Kori)].SetParent(self)
			self.WaffenButtons[str(Kori)].SetPosition(WaffenButtonPos[Kori][0], WaffenButtonPos[Kori][1])
			self.WaffenButtons[str(Kori)].SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub")
			self.WaffenButtons[str(Kori)].SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub")
			self.WaffenButtons[str(Kori)].SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub")
			self.WaffenButtons[str(Kori)].SetText(WaffenButtonText[Kori][0])
			self.WaffenButtons[str(Kori)].SetEvent(lambda arg = Kori : self.__OnKlickWaffen (arg))
			self.WaffenButtons[str(Kori)].Hide()
			
		for Mojo in xrange(len(Waffen_IconPos)):
			self.WaffenIcon[str(Mojo)] = ui.ImageBox()
			self.WaffenIcon[str(Mojo)].SetParent(self)
			self.WaffenIcon[str(Mojo)].SetPosition(Waffen_IconPos[Mojo][0], Waffen_IconPos[Mojo][1])
			self.WaffenIcon[str(Mojo)].LoadImage(Waffen_Image[Mojo][0])
			self.WaffenIcon[str(Mojo)].Hide()
		self.WaffenIcon[str(1)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(1)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(2)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(2)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(3)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(3)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(5)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(5)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(6)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(6)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(7)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(7)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(9)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(9)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(10)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(10)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(11)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(11)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(13)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(13)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(14)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(14)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(15)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(15)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(17)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(17)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(18)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(18)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(19)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(19)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(21)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(21)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(22)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(22)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(23)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(23)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
		self.WaffenIcon[str(25)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe1)
		self.WaffenIcon[str(25)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe1)
		self.WaffenIcon[str(26)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe2)
		self.WaffenIcon[str(26)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe2)
		self.WaffenIcon[str(27)].SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowWaffenUpp_Stufe3)
		self.WaffenIcon[str(27)].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideWaffenUpp_Stufe3)
			
		for Epvp in xrange(len(Rustung_Icons)):
			self.Pfeile_Icon[str(Epvp)] = ui.ImageBox()
			self.Pfeile_Icon[str(Epvp)].SetParent(self)
			self.Pfeile_Icon[str(Epvp)].SetPosition(Rustung_PfeilePos[Epvp][0], Rustung_PfeilePos[Epvp][1])
			self.Pfeile_Icon[str(Epvp)].LoadImage(Rustung_Icons[0][1])
			self.Pfeile_Icon[str(Epvp)].Hide()
		### Run´s ###
		for DasSchwarzeT in xrange(len(Run_Image)):
			self.RunImages[str(DasSchwarzeT)] = ui.ImageBox()
			self.RunImages[str(DasSchwarzeT)].SetParent(self)
			self.RunImages[str(DasSchwarzeT)].SetPosition(Run_ImagePos[DasSchwarzeT][0], Run_ImagePos[DasSchwarzeT][1])
			self.RunImages[str(DasSchwarzeT)].LoadImage(Run_Image[DasSchwarzeT][0])
			self.RunImages[str(DasSchwarzeT)].Hide()
		
		self.scroll1 = ui.ScrollBar()
		self.scroll1.SetParent(self)
		self.scroll1.SetPosition(630, 180)
		self.scroll1.SetScrollBarSize(200)
		self.scroll1.Hide()
		
		self.scroll2 = ui.ScrollBar()
		self.scroll2.SetParent(self)
		self.scroll2.SetPosition(630, 180)
		self.scroll2.SetScrollBarSize(200)
		self.scroll2.Hide()
		
		self.scroll3 = ui.ScrollBar()
		self.scroll3.SetParent(self)
		self.scroll3.SetPosition(630, 180)
		self.scroll3.SetScrollBarSize(200)
		self.scroll3.Hide()
		
		for Kori in xrange(len(Anzahl)):
			self.List[str(Kori)] = ui.ListBoxEx()
			self.List[str(Kori)].SetParent(self)
			self.List[str(Kori)].SetSize(500, 200)
			self.List[str(Kori)].SetViewItemCount(9)
			self.List[str(Kori)].SetPosition(130, 180)
			self.List[str(Kori)].Hide()
		
		self.List[str(0)].SetScrollBar(self.scroll1)
		self.List[str(1)].SetScrollBar(self.scroll2)
		self.List[str(2)].SetScrollBar(self.scroll3)
		
		for xy in xrange(len(Run_Buttons)):
			self.RunButtons[str(xy)] = ui.Button()
			self.RunButtons[str(xy)].SetParent(self)
			self.RunButtons[str(xy)].SetPosition(Run_ButtonsPos[xy][0], Run_ButtonsPos[xy][1])
			self.RunButtons[str(xy)].SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub")
			self.RunButtons[str(xy)].SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub")
			self.RunButtons[str(xy)].SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub")
			self.RunButtons[str(xy)].SetText(Run_Buttons[xy][0])
			self.RunButtons[str(xy)].SetEvent(lambda arg = xy : self.__OnKlickRun (arg))
			self.RunButtons[str(xy)].Hide()
		
		Kori_Natur = Run1.split("#")
		for i in Kori_Natur:
			self.List[str(0)].AppendItem(Item(i))
		Kori_Natur_1 = Run2.split("#")
		for ik in Kori_Natur_1:
			self.List[str(1)].AppendItem(Item(ik))
		Kori_Natur_2 = Run3.split("#")
		for xyz in Kori_Natur_2:
			self.List[str(2)].AppendItem(Item(xyz))
		## Quests
		
		for Zitronenlimonade in xrange(len(Quest_Icons)):
			self.QuestIcon[str(Zitronenlimonade)] = ui.ImageBox()
			self.QuestIcon[str(Zitronenlimonade)].SetParent(self)
			self.QuestIcon[str(Zitronenlimonade)].SetPosition(Quest_Icons[Zitronenlimonade][1], Quest_Icons[Zitronenlimonade][2])
			self.QuestIcon[str(Zitronenlimonade)].LoadImage(Quest_Icons[Zitronenlimonade][0])
			self.QuestIcon[str(Zitronenlimonade)].Hide()
			
		for Apfelsaft in xrange(len(QuestButtons)):
			self.Quest_Buttons[str(Apfelsaft)] = ui.Button()
			self.Quest_Buttons[str(Apfelsaft)].SetParent(self)
			self.Quest_Buttons[str(Apfelsaft)].SetPosition(QuestButtonsPos[Apfelsaft][0], QuestButtonsPos[Apfelsaft][1])
			self.Quest_Buttons[str(Apfelsaft)].SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub")
			self.Quest_Buttons[str(Apfelsaft)].SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub")
			self.Quest_Buttons[str(Apfelsaft)].SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub")
			self.Quest_Buttons[str(Apfelsaft)].SetText(QuestButtons[Apfelsaft][0])
			self.Quest_Buttons[str(Apfelsaft)].SetEvent(lambda arg = Apfelsaft : self.__OnKlickBio (arg))
			self.Quest_Buttons[str(Apfelsaft)].Hide()
			
		self.Scrollbar = ui.ScrollBar()
		self.Scrollbar.SetParent(self)
		self.Scrollbar.SetPosition(630, 120)
		self.Scrollbar.SetScrollBarSize(250)
		self.Scrollbar.Hide()
			
		self.Scrollbar1 = ui.ScrollBar()
		self.Scrollbar1.SetParent(self)
		self.Scrollbar1.SetPosition(630, 120)
		self.Scrollbar1.SetScrollBarSize(250)
		self.Scrollbar1.Hide()
			
		self.Scrollbar2 = ui.ScrollBar()
		self.Scrollbar2.SetParent(self)
		self.Scrollbar2.SetPosition(630, 120)
		self.Scrollbar2.SetScrollBarSize(250)
		self.Scrollbar2.Hide()
			
		self.Scrollbar3 = ui.ScrollBar()
		self.Scrollbar3.SetParent(self)
		self.Scrollbar3.SetPosition(630, 120)
		self.Scrollbar3.SetScrollBarSize(250)
		self.Scrollbar3.Hide()
		
		for BirnenSaft in xrange(len(QuestAnzahl)):
			self.Listcc[str(BirnenSaft)] = ui.ListBoxEx()
			self.Listcc[str(BirnenSaft)].SetParent(self)
			self.Listcc[str(BirnenSaft)].SetSize(100, 90)
			self.Listcc[str(BirnenSaft)].SetViewItemCount(12)
			self.Listcc[str(BirnenSaft)].SetPosition(220, 120)
			self.Listcc[str(BirnenSaft)].Hide()
		self.Listcc[str(0)].SetScrollBar(self.Scrollbar)
		self.Listcc[str(1)].SetScrollBar(self.Scrollbar1)
		self.Listcc[str(2)].SetScrollBar(self.Scrollbar2)
		self.Listcc[str(3)].SetScrollBar(self.Scrollbar3)
		
		Kori_Natur_3 = Quest1.split("#")
		for xyz in Kori_Natur_3:
			self.Listcc[str(0)].AppendItem(Item(xyz))
		Kori_Natur_4 = Quest2.split("#")
		for xyzi in Kori_Natur_4:
			self.Listcc[str(1)].AppendItem(Item(xyzi))
		Kori_Natur_5 = Quest3.split("#")
		for xyzg in Kori_Natur_5:
			self.Listcc[str(2)].AppendItem(Item(xyzg))
		Kori_Natur_6 = Quest4.split("#")
		for xyzh in Kori_Natur_6:
			self.Listcc[str(3)].AppendItem(Item(xyzh))
	### FAQ
	
		self.FAQUberschrift = ui.TextLine()
		self.FAQUberschrift.SetParent(self)
		self.FAQUberschrift.SetPosition(120, 110)
		self.FAQUberschrift.SetText("O sistema wiki foi criado principalmente para exclarecimento de dúvidas.")
		self.FAQUberschrift.Hide()
		
		self.ScrollBarFAQ = ui.ScrollBar()
		self.ScrollBarFAQ.SetParent(self)
		self.ScrollBarFAQ.SetPosition(630, 120)
		self.ScrollBarFAQ.SetScrollBarSize(250)
		self.ScrollBarFAQ.Hide()
		
		self.FAQListBox = ui.ListBoxEx()
		self.FAQListBox.SetParent(self)
		self.FAQListBox.SetSize(100, 90)
		self.FAQListBox.SetViewItemCount(12)
		self.FAQListBox.SetPosition(120, 130)
		self.FAQListBox.Hide()
		self.FAQListBox.SetScrollBar(self.ScrollBarFAQ)
		
		Kori_Natur_7 = FAQ_Text.split("#")
		for vplus in Kori_Natur_7:
			self.FAQListBox.AppendItem(Item(vplus))
			
	### Item_ Liste
		self.ItemSearchText = ui.TextLine()
		self.ItemSearchText.SetParent(self)
		self.ItemSearchText.SetDefaultFontName()
		self.ItemSearchText.SetPosition(290, 120)
		self.ItemSearchText.SetFeather()
		self.ItemSearchText.SetText("Suchen:")
		self.ItemSearchText.SetFontColor(1.0, 1.0, 1.0)
		self.ItemSearchText.SetOutline()
		self.ItemSearchText.Hide()

		self.ItemSearchSlotBar = ui.SlotBar()
		self.ItemSearchSlotBar.SetParent(self)
		self.ItemSearchSlotBar.SetSize(190, 18)
		self.ItemSearchSlotBar.SetPosition(360, 120)
		self.ItemSearchSlotBar.Hide()
		
		self.ItemSearchEditline = ui.EditLine()
		self.ItemSearchEditline.SetParent(self.ItemSearchSlotBar)
		self.ItemSearchEditline.SetSize(190, 18)
		self.ItemSearchEditline.SetPosition(10, 0)
		self.ItemSearchEditline.SetMax(25)
		self.ItemSearchEditline.SetFocus()
		self.ItemSearchEditline.SetReturnEvent(ui.__mem_func__(self.SetOrSearch))
		self.ItemSearchEditline.SetTabEvent(ui.__mem_func__(self.SetOrSearch))
		self.ItemSearchEditline.SetNumberMode()
		self.ItemSearchEditline.Hide()
	
		self.SetItemButton = ui.Button()
		self.SetItemButton.SetParent(self)
		self.SetItemButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SetItemButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SetItemButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SetItemButton.SetText("Suchen")
		self.SetItemButton.SetPosition(560, 120)
		self.SetItemButton.SetEvent(self.SetOrSearch)
		self.SetItemButton.Hide()
		
		self.ItemSearchIcon = ui.ExpandedImageBox()
		self.ItemSearchIcon.SetParent(self)
		self.ItemSearchIcon.SetPosition(320, 140)
		self.ItemSearchIcon.Hide()
		
		self.ItemNameText = ui.TextLine()
		self.ItemNameText.SetParent(self)
		self.ItemNameText.SetDefaultFontName()
		self.ItemNameText.SetPosition(365, 140)
		self.ItemNameText.SetFeather()
		self.ItemNameText.SetText("Kein Item")
		self.ItemNameText.SetFontColor(1.0, 1.0, 1.0)
		self.ItemNameText.SetOutline()
		self.ItemNameText.Hide()
		
		self.ItemDescriptionText = ui.TextLine()
		self.ItemDescriptionText.SetParent(self)
		self.ItemDescriptionText.SetDefaultFontName()
		self.ItemDescriptionText.SetPosition(365, 160)
		self.ItemDescriptionText.SetFeather()
		self.ItemDescriptionText.SetText("Keine Informationen verfügbar.")
		self.ItemDescriptionText.SetFontColor(1.0, 1.0, 1.0)
		self.ItemDescriptionText.SetOutline()
		self.ItemDescriptionText.Hide()
		
		self.LevelDescriptionText = ui.TextLine()
		self.LevelDescriptionText.SetParent(self)
		self.LevelDescriptionText.SetDefaultFontName()
		self.LevelDescriptionText.SetPosition(365, 180)
		self.LevelDescriptionText.SetFeather()
		self.LevelDescriptionText.SetText("Level: -")
		self.LevelDescriptionText.SetFontColor(1.0, 1.0, 1.0)
		self.LevelDescriptionText.SetOutline()
		self.LevelDescriptionText.Hide()
		
		self.WeartypesText = ui.TextLine()
		self.WeartypesText.SetParent(self)
		self.WeartypesText.SetDefaultFontName()
		self.WeartypesText.SetPosition(365, 200)
		self.WeartypesText.SetFeather()
		self.WeartypesText.SetText("Guerreiro, Ninja, Sura, Xamã, Lycan")
		self.WeartypesText.SetFontColor(1.0, 1.0, 1.0)
		self.WeartypesText.SetOutline()

		self.AttackOrDefStatText = ui.TextLine()
		self.AttackOrDefStatText.SetParent(self)
		self.AttackOrDefStatText.SetDefaultFontName()
		self.AttackOrDefStatText.SetPosition(365, 220)
		self.AttackOrDefStatText.SetFeather()
		self.AttackOrDefStatText.SetText("Angriffswert: 0")
		self.AttackOrDefStatText.SetFontColor(1.0, 1.0, 1.0)
		self.AttackOrDefStatText.SetOutline()

		self.MagicAttackOrDefStatText = ui.TextLine()
		self.MagicAttackOrDefStatText.SetParent(self)
		self.MagicAttackOrDefStatText.SetDefaultFontName()
		self.MagicAttackOrDefStatText.SetPosition(365, 240)
		self.MagicAttackOrDefStatText.SetFeather()
		self.MagicAttackOrDefStatText.SetText("Magischer Angriffswert: 0")
		self.MagicAttackOrDefStatText.SetFontColor(1.0, 1.0, 1.0)
		self.MagicAttackOrDefStatText.SetOutline()

		self.AttackOrMoveSpeed = ui.TextLine()
		self.AttackOrMoveSpeed.SetParent(self)
		self.AttackOrMoveSpeed.SetDefaultFontName()
		self.AttackOrMoveSpeed.SetPosition(365, 260)
		self.AttackOrMoveSpeed.SetFeather()
		self.AttackOrMoveSpeed.SetText("")
		self.AttackOrMoveSpeed.SetFontColor(1.0, 1.0, 1.0)
		self.AttackOrMoveSpeed.SetOutline()

		self.ItemBonusOne = ui.TextLine()
		self.ItemBonusOne.SetParent(self)
		self.ItemBonusOne.SetDefaultFontName()
		self.ItemBonusOne.SetPosition(365, 280)
		self.ItemBonusOne.SetFeather()
		self.ItemBonusOne.SetText("Bonus 1: -")
		self.ItemBonusOne.SetFontColor(1.0, 1.0, 1.0)
		self.ItemBonusOne.SetOutline()

		self.ItemBonusTwo = ui.TextLine()
		self.ItemBonusTwo.SetParent(self)
		self.ItemBonusTwo.SetDefaultFontName()
		self.ItemBonusTwo.SetPosition(365, 300)
		self.ItemBonusTwo.SetFeather()
		self.ItemBonusTwo.SetText("Bonus 2: -")
		self.ItemBonusTwo.SetFontColor(1.0, 1.0, 1.0)
		self.ItemBonusTwo.SetOutline()

		self.ItemBonusThree = ui.TextLine()
		self.ItemBonusThree.SetParent(self)
		self.ItemBonusThree.SetDefaultFontName()
		self.ItemBonusThree.SetPosition(365, 320)
		self.ItemBonusThree.SetFeather()
		self.ItemBonusThree.SetText("Bonus 3: -")
		self.ItemBonusThree.SetFontColor(1.0, 1.0, 1.0)
		self.ItemBonusThree.SetOutline()
		
		self.fileListBox2 = self.__CreateFileListBox()
		self.LoadFuckingScrollBar()
		self.fileListBox.SetScrollBar(self.ScrollBar)
		self.UpdateFileList()
		
		
	def __CreateFileListBox(self):
		self.fileListBox = ui.ListBoxEx()
		self.fileListBox.SetParent(self)
		self.fileListBox.SetSize(90, 500)
		self.fileListBox.SetPosition(115, 110)
		self.fileListBox.SetViewItemCount(13)
		self.fileListBox.Hide()
		self.fileListBox.SetSelectEvent(self.SetSearchedItem)
	
	def LoadFuckingScrollBar(self):
		self.ScrollBar = ui.ScrollBar()
		self.ScrollBar.SetParent(self)
		self.ScrollBar.SetPosition(260, 110)
		self.ScrollBar.SetScrollBarSize(280)
		self.ScrollBar.Hide()
		
	
	def SetOrSearch(self):
		self.data = str(self.ItemSearchEditline.GetText())
		if self.data.isdigit():
			self.SetItem()
		else:
			self.SearchItem()
		
	def SetItem(self):
		ItemSearchValue = self.data.split()
		ItemSearchValue = int(ItemSearchValue[0])
		item.SelectItem(ItemSearchValue)
		itemIcon = item.GetIconImageFileName()
		self.ItemSearchIcon.LoadImage(itemIcon)
	
		ItemType = item.GetItemType()
		ItemSubType = item.GetItemSubType()
		ItemDescription = item.GetItemDescription()  
		ItemSummary = item.GetItemSummary()
		for i in xrange(0,1):
			(ItemTypeLimit, ItemLevelLimit) = item.GetLimit(i)
			if item.LIMIT_LEVEL == ItemTypeLimit:
				if ItemLevelLimit > 0:
					self.LevelDescriptionText.SetText("Level: -")
				self.LevelDescriptionText.SetText("Level: " + str(ItemLevelLimit))
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.LevelDescriptionText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.LevelDescriptionText.SetPackedFontColor(self.ENABLE_COLOR)
			elif item.LIMIT_STR == ItemTypeLimit:
				if ItemLevelLimit > 0:
					self.LevelDescriptionText.SetText("Stärke: -")
				self.LevelDescriptionText.SetText("Stärke: " + str(ItemLevelLimit))
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.LevelDescriptionText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.LevelDescriptionText.SetPackedFontColor(self.ENABLE_COLOR)
			elif item.LIMIT_DEX == ItemTypeLimit:
				if ItemLevelLimit > 0:
					self.LevelDescriptionText.SetText("Verteidigung: -")
				self.LevelDescriptionText.SetText("Verteidigung: " + str(ItemLevelLimit))
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.LevelDescriptionText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.LevelDescriptionText.SetPackedFontColor(self.ENABLE_COLOR)
			elif item.LIMIT_INT == ItemTypeLimit:
				if ItemLevelLimit > 0:
					self.LevelDescriptionText.SetText("Intelligenz: -")
				self.LevelDescriptionText.SetText("Intelligenz: " + str(ItemLevelLimit))
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.LevelDescriptionText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.LevelDescriptionText.SetPackedFontColor(self.ENABLE_COLOR)
			elif item.LIMIT_CON == ItemTypeLimit:
				if ItemLevelLimit > 0:
					self.LevelDescriptionText.SetText("Vitalität: -")
				self.LevelDescriptionText.SetText("Vitalität: " + str(ItemLevelLimit))
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.LevelDescriptionText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.LevelDescriptionText.SetPackedFontColor(self.ENABLE_COLOR)
			else:
				self.LevelDescriptionText.SetText("Bonus Status non noti")
				self.LevelDescriptionText.SetFontColor(1.0, 1.0, 1.0)				
			
		if str(ItemDescription) != "":
			self.ItemDescriptionText.SetText(ItemDescription)
		elif str(ItemDescription) == "":
			self.ItemDescriptionText.SetText("Keine Informationen verfügbar.")
			
		self.ItemNameText.SetText(str(item.GetItemName()))
			
		FlagListe = (
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN))

		CharacterTypes = ""
		for i in xrange(self.CHARACTER_COUNT):

			name = self.CHARACTER_NAMES[i]
			Character = FlagListe[i]

			if Character:
				CharacterTypes += " "
				CharacterTypes += name
				
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				CharacterTypes += " "
				CharacterTypes += localeInfo.FOR_FEMALE
				
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				CharacterTypes += " "
				CharacterTypes += localeInfo.FOR_MALE

		self.WeartypesText.SetText(str(CharacterTypes[1:]))
		self.WeartypesText.Show()
		
		if item.ITEM_TYPE_ARMOR == ItemType:
			self.AttackOrDefStatText.Show()
			self.MagicAttackOrDefStatText.Hide()
			DefenseValue0Magic = item.GetValue(0)
			DefenseValue1Physic = item.GetValue(1)
			DefenseValue5Physic = item.GetValue(5) * 2
			if DefenseValue1Physic > 0:
				self.AttackOrDefStatText.SetText(str("Verteidigung: " + str(int(DefenseValue1Physic + DefenseValue5Physic))))		
			if DefenseValue0Magic > 0:
				self.MagicAttackOrDefStatText.SetText(str("Magische Verteidigung: " + str(int(DefenseValue0Magic))))
				
		elif item.ITEM_TYPE_WEAPON == ItemType:
			self.AttackOrDefStatText.Show()
			self.MagicAttackOrDefStatText.Show()
			AttackSpeed = item.GetValue(0)
			MinimumMagicAttack = item.GetValue(1)
			MaximumMagicAttack = item.GetValue(2)
			MinimumPower = item.GetValue(3)
			MaximumPower = item.GetValue(4)
			AdditionalPower = item.GetValue(5)
			if MaximumPower > MinimumPower:
				self.AttackOrDefStatText.SetText(str("Angriffswert: " + str(int(MinimumPower + AdditionalPower)) + " - " + str(int(MaximumPower + AdditionalPower))))
			else:
				self.AttackOrDefStatText.SetText(str("Angriffswert: " + str(int(MinimumPower + AdditionalPower))))

			if MinimumMagicAttack > 0 or MaximumMagicAttack > 0:
				if MaximumMagicAttack > MinimumMagicAttack:
					self.MagicAttackOrDefStatText.SetText("Magischer Angriffswert: " + str(int(MinimumMagicAttack + AdditionalPower)) + " - " + str(int(MaximumMagicAttack + AdditionalPower)))
				else:
					self.MagicAttackOrDefStatText.SetText("Magischer Angriffswert: " + str(int(MinimumMagicAttack + AdditionalPower)))
			else:
				self.MagicAttackOrDefStatText.Hide()
		else:
			self.MagicAttackOrDefStatText.Hide()
			self.AttackOrDefStatText.Hide()		
		
		self.AttackOrMoveSpeed.Hide()
		self.ItemBonusOne.Hide()
		self.ItemBonusTwo.Hide()
		self.ItemBonusThree.Hide()
		for i in xrange(item.ITEM_APPLY_MAX_NUM):

			(AffectType, AffectValue) = item.GetAffect(i)

			AffectString = self.GetAffect(AffectType, AffectValue)
			if AffectString:
				if int(i) == 0:
					self.AttackOrMoveSpeed.SetText(str(AffectString))
					self.AttackOrMoveSpeed.Show()
				if int(i) == 1:
					self.ItemBonusOne.SetText("Bonus 1: " + str(AffectString))
					self.ItemBonusOne.Show()
				if int(i) == 2:
					self.ItemBonusTwo.SetText("Bonus 2: " + str(AffectString))
					self.ItemBonusTwo.Show()
				if int(i) == 3:
					self.ItemBonusThree.SetText("Bonus 3: " + str(AffectString))					
					self.ItemBonusThree.Show()
					
	def GetAffect(self, AffectType, AffectValue):
		if 0 == AffectType:
			return None
		if 0 == AffectValue:
			return None
		try:
			return self.AFFECT_DICT[AffectType](AffectValue)
		except TypeError:
			return "Unknown Value[%s] %s" % (AffectType, AffectValue)
		except KeyError:
			return "Unknown Value[%s] %s" % (AffectType, AffectValue)
		
	def OnUpdate(self):
		global NewItemValue
		global SearchedItem	
			
		if str(SearchedItem) != str(self.ItemSearchEditline.GetText()) and NewItemValue == "TRUE":
			self.ItemSearchEditline.SetText(str(SearchedItem))
			NewItemValue = "FALSE"
			self.SetItem()

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return TRUE

	def SearchItem(self):
		self.fileListBox.RemoveAllItems()
		SearchName = str(self.data)
		try:
			handle = app.OpenTextFile("locale/de/item_list.txt")
			count = app.GetTextFileLineCount(handle)
		except IOError:
			import dbg
			dbg.LogBox("Load Itemlist Error")
			app.Abort()

		for i in xrange(count):
			line = app.GetTextFileLine(handle, i)
			tokens = str(line).split("\t")
			if len(tokens) == 0 or not tokens[0]:
				continue
				
			ItemValue = str(tokens[0])
			if str(ItemValue).find(" ") != -1:
				ItemValue = str(ItemValue).replace(" ", "")
			item.SelectItem(int(ItemValue))
			Itemname = str(item.GetItemName())
			if ItemValue and str(Itemname) != "":
				if str(Itemname).find(str(SearchName)) != -1:
					self.fileListBox.AppendItem(Item(str(ItemValue) + "	" + str(Itemname)))
					
	def SetSearchedItem(self, item):
		searched = item
		selected = searched.GetText()
		selected = selected.split()
		self.data = selected[0]
		self.SetItem()
		
	def UpdateFileList(self):
		self.fileListBox.RemoveAllItems()
		try:
			handle = app.OpenTextFile("locale/de/item_list.txt")
			count = app.GetTextFileLineCount(handle)
		except IOError:
			import dbg
			dbg.LogBox("Load Itemlist Error")
			app.Abort()

		for i in xrange(count):
			line = app.GetTextFileLine(handle, i)
			tokens = str(line).split("\t")
			if len(tokens) == 0 or not tokens[0]:
				continue
				
			ItemValue = str(tokens[0])
			if str(ItemValue).find(" ") != -1:
				ItemValue = str(ItemValue).replace(" ", "")
			item.SelectItem(int(ItemValue))
			Itemname = str(item.GetItemName())
			if ItemValue and str(Itemname) != "":
				self.fileListBox.AppendItem(Item(str(ItemValue) + "	" + str(Itemname)))
		
	def SetBonis(self):
		global SearchedItem
		global NewItemValue
		SelectedIndex = self.fileListBox.GetSelectedItem()
		SelectedIndex = SelectedIndex.GetText()
		Itemvalue = SelectedIndex.split("\t")[0]
		SearchedItem = int(Itemvalue)
		NewItemValue = "TRUE"
		self.Close()

		
	def __OnClickButton(self, parameter):
		Seite = parameter
		if Seite != 0:
			if Seite == 1: # Rüstungs Seite
				## WillkommensText
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				## Rüstung
				self.__CrearRustung()
				## Pfeile
				self.__ClearPfeile()
				## Quest
				self.__ClearQuest()
				## FAQ
				self.__ClearFAQ()
				self.__ClearITEMLIST()
				##Run
				self.__ClearRun()
				self.Rustungupp[str(0)].Show()
				self.Rustungupp[str(1)].Show()
				self.EinstellungsButton[str(1)].Show()
				self.RustungUberschrift[str(0)].Show()
				self.RustungUberschrift[str(1)].Show()
				
				self.RustungIcons[str(0)].Show()
				self.RustungIcons[str(1)].Show()
				self.RustungIcons[str(2)].Show()
				self.RustungIcons[str(3)].Show()
				self.RustungIcons[str(4)].Show()
				self.RustungIcons[str(5)].Show()
				self.RustungIcons[str(6)].Show()
				self.RustungIcons[str(7)].Show()
				
				self.Pfeile_Icon[str(0)].Show()
				self.Pfeile_Icon[str(1)].Show()
				self.Pfeile_Icon[str(2)].Show()
				self.Pfeile_Icon[str(4)].Show()
				self.Pfeile_Icon[str(5)].Show()
				self.Pfeile_Icon[str(6)].Show()
				
				self.__ClearWaffen()
			elif Seite == 2:
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				## Rüstung
				self.__CrearRustung()
				self.__ClearPfeile()
				self.__ClearWaffen()
				## Quest
				self.__ClearQuest()
				## FAQ
				self.__ClearFAQ()
				self.__ClearITEMLIST()
				##Run
				self.__ClearRun()
				
				self.Pfeile_Icon[str(0)].Show()
				self.Pfeile_Icon[str(1)].Show()
				self.Pfeile_Icon[str(2)].Show()
				self.Pfeile_Icon[str(4)].Show()
				self.Pfeile_Icon[str(5)].Show()
				self.Pfeile_Icon[str(6)].Show()
				
				self.Waffenupp.Show()
				
				self.WaffenuppText[str(0)].Show()
				self.WaffenuppText[str(1)].Show()
				
				self.WaffenButtons[str(0)].Show()
				self.WaffenButtons[str(1)].Show()
				self.WaffenButtons[str(2)].Show()
				self.WaffenButtons[str(3)].Show()
				
				self.WaffenIcon[str(0)].Show()
				self.WaffenIcon[str(1)].Show()
				self.WaffenIcon[str(2)].Show()
				self.WaffenIcon[str(3)].Show()
				self.WaffenIcon[str(4)].Show()
				self.WaffenIcon[str(5)].Show()
				self.WaffenIcon[str(6)].Show()
				self.WaffenIcon[str(7)].Show()
			elif Seite == 3:
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				## FAQ
				self.__ClearFAQ()
				## Rüstung
				self.__CrearRustung()
				## Quest
				self.__ClearQuest()
				self.__ClearITEMLIST()
				
				self.__ClearPfeile()
				
				self.__ClearWaffen()
				self.__ClearRun()
				self.RunImages[str(0)].Show()
				self.scroll1.Show()
				self.List[str(0)].Show()
				self.RunButtons[str(0)].Show()
				self.RunButtons[str(1)].Show()
				self.RunButtons[str(2)].Show()
				
			elif Seite == 4:
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				self.__ClearITEMLIST()
				## Rüstung
				self.__CrearRustung()
				
				self.__ClearPfeile()
				## FAQ
				self.__ClearFAQ()
				
				self.__ClearWaffen()
				##Run
				self.__ClearRun()
				self.QuestIcon[str(0)].Show()
				self.Scrollbar.Show()
				self.Listcc[str(0)].Show()
				self.Quest_Buttons[str(0)].Show()
				self.Quest_Buttons[str(1)].Show()
				self.Quest_Buttons[str(2)].Show()
				self.Quest_Buttons[str(3)].Show()
				
			elif Seite == 5:
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				self.__ClearITEMLIST()
				## Rüstung
				self.__CrearRustung()
				## Quest
				self.__ClearQuest()
				
				self.__ClearPfeile()
				
				self.__ClearWaffen()
				self.__ClearRun()
				self.FAQUberschrift.Show()
				self.ScrollBarFAQ.Show()
				self.FAQListBox.Show()
			elif Seite == 6:
				self.__ClearWillkommensText()
				## Bonus Seite
				self.__CrearBonusSeite()
				self.__ClearFAQ()
				## Rüstung
				self.__CrearRustung()
				## Quest
				self.__ClearQuest()
				
				self.__ClearPfeile()
				
				self.__ClearWaffen()
				self.__ClearRun()
				self.ItemSearchText.Show()
				self.ItemSearchSlotBar.Show()
				self.ItemSearchEditline.Show()
				self.SetItemButton.Show()
				self.ItemSearchIcon.Show()
				self.ItemNameText.Show()
				self.ItemDescriptionText.Show()
				self.LevelDescriptionText.Show()
				self.fileListBox.Show()
				self.ScrollBar.Show()
				
		else: #Bonus Seite
			self.__ClearWillkommensText()
			## FAQ
			self.__ClearFAQ()
			self.__CrearRustung()
			self.__ClearWaffen()
				## Quest
			self.__ClearQuest()
			self.__ClearITEMLIST()
			self.__ClearPfeile()
			##Run
			self.__ClearRun()
			## Bonus Seite
			self.Bonusliste[str(0)].Show()
			self.Bonusliste[str(1)].Show()
			self.Bonusliste[str(2)].Show()
			self.Bonusliste[str(3)].Show()
			self.Bonusliste[str(4)].Show()
			self.Bonusliste[str(5)].Show()
			self.Bonusliste[str(6)].Show()
			self.Bonusliste[str(7)].Show()
			
			self.MinniBoard[str(0)].Show()
			self.MinniBoard[str(1)].Show()
			self.MinniBoard[str(2)].Show()
			self.MinniBoard[str(3)].Show()
			self.MinniBoard[str(4)].Show()
			self.MinniBoard[str(5)].Show()
			self.MinniBoard[str(6)].Show()
			self.MinniBoard[str(7)].Show()
			
			self.Bonus_Text[str(0)].Show()
			self.Bonus_Text[str(1)].Show()
			self.Bonus_Text[str(2)].Show()
			self.Bonus_Text[str(3)].Show()
			self.Bonus_Text[str(4)].Show()
			self.Bonus_Text[str(5)].Show()
			self.Bonus_Text[str(6)].Show()
			self.Bonus_Text[str(7)].Show()
			
	def __OnKlickRustung(self, parameter):
		Seite = parameter
		if Seite != 0:
			if Seite == 1:
				self.__CrearRustung()
				self.Rustungupp[str(0)].Show()
				self.Rustungupp[str(1)].Show()
				self.EinstellungsButton[str(0)].Show()
				self.Rustungupp[str(2)].Show()
				self.Rustungupp[str(3)].Show()
				self.RustungUberschrift[str(2)].Show()
				self.RustungUberschrift[str(3)].Show()
				
				self.RustungIcons[str(8)].Show()
				self.RustungIcons[str(9)].Show()
				self.RustungIcons[str(10)].Show()
				self.RustungIcons[str(11)].Show()
				self.RustungIcons[str(12)].Show()
				self.RustungIcons[str(13)].Show()
				self.RustungIcons[str(14)].Show()
				self.RustungIcons[str(15)].Show()
			
				self.Pfeile_Icon[str(8)].Show()
				self.Pfeile_Icon[str(9)].Show()
				self.Pfeile_Icon[str(10)].Show()
				self.Pfeile_Icon[str(12)].Show()
				self.Pfeile_Icon[str(13)].Show()
				self.Pfeile_Icon[str(14)].Show()	
		else:
			self.__CrearRustung()
			self.Rustungupp[str(0)].Show()
			self.Rustungupp[str(1)].Show()
			self.EinstellungsButton[str(1)].Show()
			self.Rustungupp[str(0)].Show()
			self.Rustungupp[str(1)].Show()
			self.RustungUberschrift[str(0)].Show()
			self.RustungUberschrift[str(1)].Show()
				
			self.RustungIcons[str(0)].Show()
			self.RustungIcons[str(1)].Show()
			self.RustungIcons[str(2)].Show()
			self.RustungIcons[str(3)].Show()
			self.RustungIcons[str(4)].Show()
			self.RustungIcons[str(5)].Show()
			self.RustungIcons[str(6)].Show()
			self.RustungIcons[str(7)].Show()
				
			self.Pfeile_Icon[str(0)].Show()
			self.Pfeile_Icon[str(1)].Show()
			self.Pfeile_Icon[str(2)].Show()
			self.Pfeile_Icon[str(4)].Show()
			self.Pfeile_Icon[str(5)].Show()
			self.Pfeile_Icon[str(6)].Show()
			
	def __OnKlickWaffen(self, parameter):
		Seite = parameter
		if Seite != 0:
			if Seite == 1:
				self.__ClearWaffen()
				
				self.Waffenupp.Show()
				self.WaffenuppText[str(2)].Show()
				self.WaffenuppText[str(3)].Show()
			
				self.WaffenButtons[str(0)].Show()
				self.WaffenButtons[str(1)].Show()
				self.WaffenButtons[str(2)].Show()
				self.WaffenButtons[str(3)].Show()
				
				self.WaffenIcon[str(8)].Show()
				self.WaffenIcon[str(9)].Show()
				self.WaffenIcon[str(10)].Show()
				self.WaffenIcon[str(11)].Show()
				self.WaffenIcon[str(12)].Show()
				self.WaffenIcon[str(13)].Show()
				self.WaffenIcon[str(14)].Show()
				self.WaffenIcon[str(15)].Show()
				
				self.Pfeile_Icon[str(4)].Show()
				self.Pfeile_Icon[str(5)].Show()
				self.Pfeile_Icon[str(6)].Show()
			elif Seite == 2:
				self.__ClearWaffen()
				self.Waffenupp.Show()
			
				self.WaffenButtons[str(0)].Show()
				self.WaffenButtons[str(1)].Show()
				self.WaffenButtons[str(2)].Show()
				self.WaffenButtons[str(3)].Show()
				
				self.WaffenuppText[str(4)].Show()
				self.WaffenuppText[str(5)].Show()
				
				self.WaffenIcon[str(16)].Show()
				self.WaffenIcon[str(17)].Show()
				self.WaffenIcon[str(18)].Show()
				self.WaffenIcon[str(19)].Show()
				self.WaffenIcon[str(20)].Show()
				self.WaffenIcon[str(21)].Show()
				self.WaffenIcon[str(22)].Show()
				self.WaffenIcon[str(23)].Show()
				
				self.Pfeile_Icon[str(4)].Show()
				self.Pfeile_Icon[str(5)].Show()
				self.Pfeile_Icon[str(6)].Show()
				
			elif Seite == 3:
				self.__ClearWaffen()
				self.Waffenupp.Show()
				self.__ClearPfeile()
			
				self.WaffenButtons[str(0)].Show()
				self.WaffenButtons[str(1)].Show()
				self.WaffenButtons[str(2)].Show()
				self.WaffenButtons[str(3)].Show()
				
				self.WaffenuppText[str(6)].Show()
				self.WaffenuppText[str(7)].Show()
				
				self.WaffenIcon[str(24)].Show()
				self.WaffenIcon[str(25)].Show()
				self.WaffenIcon[str(26)].Show()
				self.WaffenIcon[str(27)].Show()
			
				self.Pfeile_Icon[str(0)].Show()
				self.Pfeile_Icon[str(1)].Show()
				self.Pfeile_Icon[str(2)].Show()
		else:
			self.__ClearWaffen()
			self.Waffenupp.Show()
			self.WaffenuppText[str(0)].Show()
			self.WaffenuppText[str(1)].Show()
			
			self.WaffenButtons[str(0)].Show()
			self.WaffenButtons[str(1)].Show()
			self.WaffenButtons[str(2)].Show()
			self.WaffenButtons[str(3)].Show()
				
			self.WaffenIcon[str(0)].Show()
			self.WaffenIcon[str(1)].Show()
			self.WaffenIcon[str(2)].Show()
			self.WaffenIcon[str(3)].Show()
			self.WaffenIcon[str(4)].Show()
			self.WaffenIcon[str(5)].Show()
			self.WaffenIcon[str(6)].Show()
			self.WaffenIcon[str(7)].Show()
			
			self.Pfeile_Icon[str(4)].Show()
			self.Pfeile_Icon[str(5)].Show()
			self.Pfeile_Icon[str(6)].Show()
			
	def __OnKlickRun(self, parameter):
		Seite = parameter
		if Seite != 0:
			if Seite == 1:
				self.__ClearRun()
				self.List[str(1)].Show()
				self.RunImages[str(1)].Show()
				self.scroll2.Show()
				self.RunButtons[str(0)].Show()
				self.RunButtons[str(1)].Show()
				self.RunButtons[str(2)].Show()
			elif Seite == 2:
				self.__ClearRun()
				self.List[str(2)].Show()
				self.RunImages[str(2)].Show()
				self.scroll3.Show()
				self.RunButtons[str(0)].Show()
				self.RunButtons[str(1)].Show()
				self.RunButtons[str(2)].Show()
		else:
			self.__ClearRun()
			self.List[str(0)].Show()
			self.RunImages[str(0)].Show()
			self.scroll1.Show()
			self.RunButtons[str(0)].Show()
			self.RunButtons[str(1)].Show()
			self.RunButtons[str(2)].Show()
		
	def __OnKlickBio(self, parameter):
		Seite = parameter
		if Seite != 0:
			if Seite == 1:
				self.__ClearQuest()
				self.Quest_Buttons[str(0)].Show()
				self.Quest_Buttons[str(1)].Show()
				self.Quest_Buttons[str(2)].Show()
				self.Quest_Buttons[str(3)].Show()
				self.Scrollbar1.Show()
				self.Listcc[str(1)].Show()
				self.QuestIcon[str(1)].Show()
			elif Seite == 2:
				self.__ClearQuest()
				self.Quest_Buttons[str(0)].Show()
				self.Quest_Buttons[str(1)].Show()
				self.Quest_Buttons[str(2)].Show()
				self.Quest_Buttons[str(3)].Show()
				self.Scrollbar2.Show()
				self.Listcc[str(2)].Show()
				self.QuestIcon[str(2)].Show()
			elif Seite == 3:
				self.__ClearQuest()
				self.Quest_Buttons[str(0)].Show()
				self.Quest_Buttons[str(1)].Show()
				self.Quest_Buttons[str(2)].Show()
				self.Quest_Buttons[str(3)].Show()
				self.Listcc[str(3)].Show()
				self.QuestIcon[str(3)].Show()
				self.Scrollbar3.Show()
		else:
			self.__ClearQuest()
			self.Quest_Buttons[str(0)].Show()
			self.Quest_Buttons[str(1)].Show()
			self.Quest_Buttons[str(2)].Show()
			self.Quest_Buttons[str(3)].Show()
			self.Scrollbar.Show()
			self.Listcc[str(0)].Show()
			self.QuestIcon[str(0)].Show()
			
	def __ClearWillkommensText(self):
		self.haupttext[str(0)].Hide()
		self.haupttext[str(1)].Hide()
		self.haupttext[str(2)].Hide()
		self.haupttext[str(3)].Hide()
		self.haupttext[str(4)].Hide()
		
	def __CrearBonusSeite(self):
		self.Bonusliste[str(0)].Hide()
		self.Bonusliste[str(1)].Hide()
		self.Bonusliste[str(2)].Hide()
		self.Bonusliste[str(3)].Hide()
		self.Bonusliste[str(4)].Hide()
		self.Bonusliste[str(5)].Hide()
		self.Bonusliste[str(6)].Hide()
		self.Bonusliste[str(7)].Hide()
		
		self.MinniBoard[str(0)].Hide()
		self.MinniBoard[str(1)].Hide()
		self.MinniBoard[str(2)].Hide()
		self.MinniBoard[str(3)].Hide()
		self.MinniBoard[str(4)].Hide()
		self.MinniBoard[str(5)].Hide()
		self.MinniBoard[str(6)].Hide()
		self.MinniBoard[str(7)].Hide()
		
		self.Bonus_Text[str(0)].Hide()
		self.Bonus_Text[str(1)].Hide()
		self.Bonus_Text[str(2)].Hide()
		self.Bonus_Text[str(3)].Hide()
		self.Bonus_Text[str(4)].Hide()
		self.Bonus_Text[str(5)].Hide()
		self.Bonus_Text[str(6)].Hide()
		self.Bonus_Text[str(7)].Hide()
		
	def __CrearRustung(self):
		self.Rustungupp[str(0)].Hide()
		self.Rustungupp[str(1)].Hide()
		self.Rustungupp[str(2)].Hide()
		self.Rustungupp[str(3)].Hide()
		self.EinstellungsButton[str(1)].Hide()
		self.EinstellungsButton[str(0)].Hide()
		self.RustungUberschrift[str(0)].Hide()
		self.RustungUberschrift[str(1)].Hide()
		self.RustungUberschrift[str(2)].Hide()
		self.RustungUberschrift[str(3)].Hide()
		
		self.RustungIcons[str(0)].Hide()
		self.RustungIcons[str(1)].Hide()
		self.RustungIcons[str(2)].Hide()
		self.RustungIcons[str(3)].Hide()
		self.RustungIcons[str(4)].Hide()
		self.RustungIcons[str(5)].Hide()
		self.RustungIcons[str(6)].Hide()
		self.RustungIcons[str(7)].Hide()
		self.RustungIcons[str(8)].Hide()
		self.RustungIcons[str(9)].Hide()
		self.RustungIcons[str(10)].Hide()
		self.RustungIcons[str(11)].Hide()
		self.RustungIcons[str(12)].Hide()
		self.RustungIcons[str(13)].Hide()
		self.RustungIcons[str(14)].Hide()
		self.RustungIcons[str(15)].Hide()
		
	def __ClearWaffen(self):
		self.Waffenupp.Hide()
		self.WaffenuppText[str(0)].Hide()
		self.WaffenuppText[str(1)].Hide()
		self.WaffenuppText[str(2)].Hide()
		self.WaffenuppText[str(3)].Hide()
		self.WaffenuppText[str(4)].Hide()
		self.WaffenuppText[str(5)].Hide()
		self.WaffenuppText[str(6)].Hide()
		self.WaffenuppText[str(7)].Hide()
		self.WaffenButtons[str(0)].Hide()
		self.WaffenButtons[str(1)].Hide()
		self.WaffenButtons[str(2)].Hide()
		self.WaffenButtons[str(3)].Hide()
		self.WaffenIcon[str(0)].Hide()
		self.WaffenIcon[str(1)].Hide()
		self.WaffenIcon[str(2)].Hide()
		self.WaffenIcon[str(3)].Hide()
		self.WaffenIcon[str(4)].Hide()
		self.WaffenIcon[str(5)].Hide()
		self.WaffenIcon[str(6)].Hide()
		self.WaffenIcon[str(7)].Hide()
		self.WaffenIcon[str(8)].Hide()
		self.WaffenIcon[str(9)].Hide()
		self.WaffenIcon[str(10)].Hide()
		self.WaffenIcon[str(11)].Hide()
		self.WaffenIcon[str(12)].Hide()
		self.WaffenIcon[str(13)].Hide()
		self.WaffenIcon[str(14)].Hide()
		self.WaffenIcon[str(15)].Hide()
		self.WaffenIcon[str(16)].Hide()
		self.WaffenIcon[str(17)].Hide()
		self.WaffenIcon[str(18)].Hide()
		self.WaffenIcon[str(19)].Hide()
		self.WaffenIcon[str(20)].Hide()
		self.WaffenIcon[str(21)].Hide()
		self.WaffenIcon[str(22)].Hide()
		self.WaffenIcon[str(23)].Hide()
		self.WaffenIcon[str(24)].Hide()
		self.WaffenIcon[str(25)].Hide()
		self.WaffenIcon[str(26)].Hide()
		self.WaffenIcon[str(27)].Hide()
		
	def __ClearPfeile(self):
		self.Pfeile_Icon[str(0)].Hide()
		self.Pfeile_Icon[str(1)].Hide()
		self.Pfeile_Icon[str(2)].Hide()
		self.Pfeile_Icon[str(4)].Hide()
		self.Pfeile_Icon[str(5)].Hide()
		self.Pfeile_Icon[str(6)].Hide()
		self.Pfeile_Icon[str(8)].Hide()
		self.Pfeile_Icon[str(9)].Hide()
		self.Pfeile_Icon[str(10)].Hide()
		self.Pfeile_Icon[str(12)].Hide()
		self.Pfeile_Icon[str(13)].Hide()
		self.Pfeile_Icon[str(14)].Hide()
		
	def __ClearRun(self):
		self.RunImages[str(0)].Hide()
		self.RunImages[str(1)].Hide()
		self.RunImages[str(2)].Hide()
		self.scroll1.Hide()
		self.scroll2.Hide()
		self.scroll3.Hide()
		self.List[str(0)].Hide()
		self.List[str(1)].Hide()
		self.List[str(2)].Hide()
		self.RunButtons[str(0)].Hide()
		self.RunButtons[str(1)].Hide()
		self.RunButtons[str(2)].Hide()
		
	def __ClearQuest(self):
		self.QuestIcon[str(0)].Hide()
		self.QuestIcon[str(1)].Hide()
		self.QuestIcon[str(2)].Hide()
		self.QuestIcon[str(3)].Hide()
		self.Scrollbar.Hide()
		self.Scrollbar1.Hide()
		self.Scrollbar2.Hide()
		self.Scrollbar3.Hide()
		self.Listcc[str(0)].Hide()
		self.Listcc[str(1)].Hide()
		self.Listcc[str(2)].Hide()
		self.Listcc[str(3)].Hide()
		self.Quest_Buttons[str(0)].Hide()
		self.Quest_Buttons[str(1)].Hide()
		self.Quest_Buttons[str(2)].Hide()
		self.Quest_Buttons[str(3)].Hide()
		
	def __ClearFAQ(self):
		self.FAQUberschrift.Hide()
		self.ScrollBarFAQ.Hide()
		self.FAQListBox.Hide()
		
	def __ClearITEMLIST(self):
		self.ItemSearchText.Hide()
		self.ItemSearchSlotBar.Hide()
		self.ItemSearchEditline.Hide()
		self.SetItemButton.Hide()
		self.ItemSearchIcon.Hide()
		self.ItemNameText.Hide()
		self.ItemDescriptionText.Hide()
		self.LevelDescriptionText.Hide()
		self.fileListBox.Hide()
		self.ScrollBar.Hide()
		
		
	def __ShowToolTip(self):
		self.toolTiprustung.ShowToolTip()

	def __HideToolTip(self):
		self.toolTiprustung.HideToolTip()
		
	def __ShowToolTip1(self):
		self.toolTipwaffen.ShowToolTip()

	def __HideToolTip1(self):
		self.toolTipwaffen.HideToolTip()
		
	def __ShowToolTip2(self):
		self.toolTipschuhe.ShowToolTip()

	def __HideToolTip2(self):
		self.toolTipschuhe.HideToolTip()
		
	def __ShowToolTip3(self):
		self.toolTipSchilld.ShowToolTip()

	def __HideToolTip3(self):
		self.toolTipSchilld.HideToolTip()
		
	def __ShowToolTip4(self):
		self.toolTipOhr.ShowToolTip()

	def __HideToolTip4(self):
		self.toolTipOhr.HideToolTip()
		
	def __ShowToolTip5(self):
		self.toolTipHelm.ShowToolTip()

	def __HideToolTip5(self):
		self.toolTipHelm.HideToolTip()
		
	def __ShowToolTip6(self):
		self.toolTipKetten.ShowToolTip()

	def __HideToolTip6(self):
		self.toolTipKetten.HideToolTip()
		
	def __ShowToolTip7(self):
		self.toolTipABand.ShowToolTip()

	def __HideToolTip7(self):
		self.toolTipABand.HideToolTip()
		
	def __ShowRustungUpp(self):
		self.UppBoard.Show()
		self.Upp_Items[str(0)].Show()
		self.Upp_Items[str(1)].Show()
		self.Upp_Items[str(2)].Show()
		self.UppText_Stufe1_1.Show()
		self.UppText_Stufe1_2.Show()
		self.UppText_Stufe1_3.Show()
		self.UppText.Show()
		
	def __HideRustungUpp(self):
		self.UppBoard.Hide()
		self.Upp_Items[str(0)].Hide()
		self.Upp_Items[str(1)].Hide()
		self.Upp_Items[str(2)].Hide()
		self.UppText_Stufe1_1.Hide()
		self.UppText_Stufe1_2.Hide()
		self.UppText_Stufe1_3.Hide()
		self.UppText.Hide()
	
	def __ShowRustungUpp_Stufe2(self):
		self.UppBoard.Show()
		self.UppText.Show()
		self.UppText_Stufe2_1.Show()
		self.UppText_Stufe2_2.Show()
		self.UppText_Stufe2_3.Show()
		self.UppText_Stufe2_4.Show()
		self.Upp_Items[str(0)].Show()
		self.Upp_Items[str(3)].Show()
		self.Upp_Items[str(4)].Show()
		self.Upp_Items[str(5)].Show()
		
	def __HideRustungUpp_Stufe2(self):
		self.UppBoard.Hide()
		self.UppText.Hide()
		self.UppText_Stufe2_1.Hide()
		self.UppText_Stufe2_2.Hide()
		self.UppText_Stufe2_3.Hide()
		self.UppText_Stufe2_4.Hide()
		self.Upp_Items[str(0)].Hide()
		self.Upp_Items[str(3)].Hide()
		self.Upp_Items[str(4)].Hide()
		self.Upp_Items[str(5)].Hide()
		
	def __ShowRustungUpp_Stufe3(self):
		self.UppBoard.Show()
		self.UppText.Show()
		self.UppText_Stufe3_1.Show()
		self.UppText_Stufe3_2.Show()
		self.UppText_Stufe3_3.Show()
		self.UppText_Stufe3_4.Show()
		self.Upp_Items[str(0)].Show()
		self.Upp_Items[str(6)].Show()
		self.Upp_Items[str(7)].Show()
		self.Upp_Items[str(8)].Show()
		
	def __HideRustungUpp_Stufe3(self):
		self.UppBoard.Hide()
		self.UppText.Hide()
		self.UppText_Stufe3_1.Hide()
		self.UppText_Stufe3_2.Hide()
		self.UppText_Stufe3_3.Hide()
		self.UppText_Stufe3_4.Hide()
		self.Upp_Items[str(0)].Hide()
		self.Upp_Items[str(6)].Hide()
		self.Upp_Items[str(7)].Hide()
		self.Upp_Items[str(8)].Hide()
		
	def __ShowWaffenUpp_Stufe1(self):
		self.UppBoard.Show()
		self.UppText_w.Show()
		self.Upp_Items_2[str(0)].Show()
		self.Upp_Items_2[str(1)].Show()
		self.Upp_Items_2[str(2)].Show()
		self.UppText_Waffen_Stufe1_1.Show()
		self.UppText_Waffen_Stufe1_2.Show()
		self.UppText_Waffen_Stufe1_3.Show()
		
	def __HideWaffenUpp_Stufe1(self):
		self.UppBoard.Hide()
		self.UppText_w.Hide()
		self.Upp_Items_2[str(0)].Hide()
		self.Upp_Items_2[str(1)].Hide()
		self.Upp_Items_2[str(2)].Hide()
		self.UppText_Waffen_Stufe1_1.Hide()
		self.UppText_Waffen_Stufe1_2.Hide()
		self.UppText_Waffen_Stufe1_3.Hide()
		
	def __ShowWaffenUpp_Stufe2(self):
		self.UppBoard.Show()
		self.UppText_w.Show()
		self.Upp_Items_2[str(0)].Show()#yang
		self.Upp_Items_2[str(1)].Show()#Segenrolle
		self.Upp_Items_2[str(2)].Show()#Tiktat
		self.Upp_Items_2[str(3)].Show()#Energie
		self.UppText_Waffen_Stufe2_1.Show()
		self.UppText_Waffen_Stufe2_2.Show()
		self.UppText_Waffen_Stufe2_3.Show()
		self.UppText_Waffen_Stufe2_4.Show()
		
	def __HideWaffenUpp_Stufe2(self):
		self.UppBoard.Hide()
		self.UppText_w.Hide()
		self.Upp_Items_2[str(0)].Hide()
		self.Upp_Items_2[str(1)].Hide()
		self.Upp_Items_2[str(2)].Hide()
		self.Upp_Items_2[str(3)].Hide()
		self.UppText_Waffen_Stufe2_1.Hide()
		self.UppText_Waffen_Stufe2_2.Hide()
		self.UppText_Waffen_Stufe2_3.Hide()
		self.UppText_Waffen_Stufe2_4.Hide()
		
	def __ShowWaffenUpp_Stufe3(self):
		self.UppBoard.Show()
		self.UppText_w.Show()
		self.Upp_Items_2[str(0)].Show()#yang
		self.Upp_Items_2[str(1)].Show()#Segenrolle
		self.Upp_Items_2[str(2)].Show()#Tiktat
		self.Upp_Items_2[str(3)].Show()#Energie
		self.UppText_Waffen_Stufe3_1.Show()
		self.UppText_Waffen_Stufe3_2.Show()
		self.UppText_Waffen_Stufe3_3.Show()
		self.UppText_Waffen_Stufe3_4.Show()
		
	def __HideWaffenUpp_Stufe3(self):
		self.UppBoard.Hide()
		self.UppText_w.Hide()
		self.Upp_Items_2[str(0)].Hide()
		self.Upp_Items_2[str(1)].Hide()
		self.Upp_Items_2[str(2)].Hide()
		self.Upp_Items_2[str(3)].Hide()
		self.UppText_Waffen_Stufe3_1.Hide()
		self.UppText_Waffen_Stufe3_2.Hide()
		self.UppText_Waffen_Stufe3_3.Hide()
		self.UppText_Waffen_Stufe3_4.Hide()

	def OnOpen(self):
		if self.IsShow():
			self.Hide()
			return
		self.Show()
		
NewItemValue = "FALSE"
SearchedItem = 0		
FILE_NAME_LEN = 40

