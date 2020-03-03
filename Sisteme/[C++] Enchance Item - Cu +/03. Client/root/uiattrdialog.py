import app
import net
import grp
import snd
import item
import chat
import player
import locale
import mouseModule

import ui
import uiToolTip
import uiScriptLocale
import uiinventory

itemCell = 0
choosedOption = 0

class AttrDialogWindow(ui.ScriptWindow):
	AFFECT_DICT = {
		item.APPLY_MAX_HP : locale.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : locale.TOOLTIP_MAX_SP,
		item.APPLY_CON : locale.TOOLTIP_CON,
		item.APPLY_INT : locale.TOOLTIP_INT,
		item.APPLY_STR : locale.TOOLTIP_STR,
		item.APPLY_DEX : locale.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : locale.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : locale.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : locale.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : locale.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : locale.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : locale.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : locale.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : locale.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : locale.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : locale.TOOLTIP_APPLY_PENETRATE_PCT,
		item.APPLY_ATTBONUS_WARRIOR : locale.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : locale.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : locale.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : locale.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : locale.TOOLTIP_APPLY_ATTBONUS_MONSTER,
		item.APPLY_ATTBONUS_HUMAN : locale.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : locale.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : locale.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : locale.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : locale.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : locale.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : locale.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : locale.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : locale.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : locale.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : locale.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : locale.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : locale.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : locale.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : locale.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : locale.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : locale.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : locale.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : locale.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : locale.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : locale.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : locale.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : locale.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : locale.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : locale.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : locale.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : locale.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : locale.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : locale.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : locale.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : locale.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : locale.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : locale.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : locale.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : locale.TOOLTIP_BOW_DISTANCE,
		item.APPLY_DEF_GRADE_BONUS : locale.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : locale.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : locale.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : locale.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : locale.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : locale.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : locale.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : locale.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : locale.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : locale.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : locale.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : locale.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : locale.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : locale.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_PC_BANG_EXP_BONUS : locale.TOOLTIP_MALL_EXPBONUS_P_STATIC,
		item.APPLY_PC_BANG_DROP_BONUS : locale.TOOLTIP_MALL_ITEMBONUS_P_STATIC,
		item.APPLY_RESIST_WARRIOR : locale.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : locale.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : locale.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : locale.TOOLTIP_APPLY_RESIST_SHAMAN,
		item.APPLY_MAX_HP_PCT : locale.TOOLTIP_APPLY_MAX_HP_PCT,
		item.APPLY_MAX_SP_PCT : locale.TOOLTIP_APPLY_MAX_SP_PCT,
		item.APPLY_ENERGY : locale.TOOLTIP_ENERGY,
		item.APPLY_COSTUME_ATTR_BONUS : locale.TOOLTIP_COSTUME_ATTR_BONUS,
		item.APPLY_MAGIC_ATTBONUS_PER : locale.TOOLTIP_MAGIC_ATTBONUS_PER,
		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : locale.TOOLTIP_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_ICE : locale.TOOLTIP_RESIST_ICE,
		item.APPLY_RESIST_EARTH : locale.TOOLTIP_RESIST_EARTH,
		item.APPLY_RESIST_DARK : locale.TOOLTIP_RESIST_DARK,
		item.APPLY_ANTI_CRITICAL_PCT : locale.TOOLTIP_ANTI_CRITICAL_PCT,
		item.APPLY_ANTI_PENETRATE_PCT : locale.TOOLTIP_ANTI_PENETRATE_PCT,
	}
	
	if app.ENABLE_WOLFMAN_CHARACTER:
		AFFECT_DICT.update({
			item.APPLY_BLEEDING_PCT : locale.TOOLTIP_APPLY_BLEEDING_PCT,
			item.APPLY_BLEEDING_REDUCE : locale.TOOLTIP_APPLY_BLEEDING_REDUCE,
			item.APPLY_ATTBONUS_WOLFMAN : locale.TOOLTIP_APPLY_ATTBONUS_WOLFMAN,
			item.APPLY_RESIST_CLAW : locale.TOOLTIP_APPLY_RESIST_CLAW,
			item.APPLY_RESIST_WOLFMAN : locale.TOOLTIP_APPLY_RESIST_WOLFMAN,
		})
	
	if app.ANTI_RESIST_MAGIC_BONUS:
		AFFECT_DICT.update({
			item.APPLY_ANTI_RESIST_MAGIC : locale.APPLY_ANTI_RESIST_MAGIC,
		})
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isUsable = FALSE
		self.isLoaded = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		if self.isLoaded == 1:
			return
		
		self.isLoaded = 1
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/selectattrdialog.py")
		except:
			import exception
			exception.Abort("AttrDialog.LoadDialog.LoadScript")
		
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("SelectAttr_TitleBar")
			self.targetSlot = GetObject("toolTipItemSlot")
			self.left_attr0 = GetObject("lText0")
			self.left_attr1 = GetObject("lText1")
			self.left_attr2 = GetObject("lText2")
			self.left_attr3 = GetObject("lText3")
			self.left_attr4 = GetObject("lText4")
			self.left_attr5 = GetObject("lText5")
			self.left_attr6 = GetObject("lText6")
			self.left_select_btn = GetObject("SelectBtn0")
			self.right_attr0 = GetObject("rText0")
			self.right_attr1 = GetObject("rText1")
			self.right_attr2 = GetObject("rText2")
			self.right_attr3 = GetObject("rText3")
			self.right_attr4 = GetObject("rText4")
			self.right_attr5 = GetObject("rText5")
			self.right_attr6 = GetObject("rText6")
			self.right_select_btn = GetObject("SelectBtn1")
			self.AcceptButton = GetObject("accept_button")
		except:
			import exception
			exception.Abort("AttrDialog.LoadDialog.BindObject")
		
		if self.titleBar:
			self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		if self.targetSlot:
			self.targetSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
			self.targetSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		if self.left_attr0:
			self.left_attr0.Hide()
		if self.left_attr1:
			self.left_attr1.Hide()
		if self.left_attr2:
			self.left_attr2.Hide()
		if self.left_attr3:
			self.left_attr3.Hide()
		if self.left_attr4:
			self.left_attr4.Hide()
		if self.left_attr5:
			self.left_attr5.Hide()
		if self.left_attr6:
			self.left_attr6.Hide()
		if self.left_select_btn:
			self.left_select_btn.SAFE_SetEvent(self.__OnClickLeftButton)
		if self.right_attr0:
			self.right_attr0.Hide()
		if self.right_attr1:
			self.right_attr1.Hide()
		if self.right_attr2:
			self.right_attr2.Hide()
		if self.right_attr3:
			self.right_attr3.Hide()
		if self.right_attr4:
			self.right_attr4.Hide()
		if self.right_attr5:
			self.right_attr5.Hide()
		if self.right_attr6:
			self.right_attr6.Hide()
		if self.right_select_btn:
			self.right_select_btn.SAFE_SetEvent(self.__OnClickRightButton)
		if self.AcceptButton:
			self.AcceptButton.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))

	def IsOpened(self):
		if self.isLoaded == 1:
			return TRUE
		
		return FALSE

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def __OnOverInItem(self):
		if self.tooltipItem:
			self.tooltipItem.SetInventoryItem(itemCell)

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def __GetAffectString(self, affectType, affectValue):
		if affectType == 0:
			return None
		
		if affectValue == 0:
			return None
		
		try:
			return self.AFFECT_DICT[affectType](affectValue)
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectValue)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectValue)

	def Destroy(self):
		self.ClearDictionary()
		self.targetSlot.ClearSlot(0)
		self.titleBar = None
		self.targetSlot = None
		self.left_attr0 = None
		self.left_attr1 = None
		self.left_attr2 = None
		self.left_attr3 = None
		self.left_attr4 = None
		self.left_attr5 = None
		self.left_attr6 = None
		self.left_select_btn = None
		self.right_attr0 = None
		self.right_attr1 = None
		self.right_attr2 = None
		self.right_attr3 = None
		self.right_attr4 = None
		self.right_attr5 = None
		self.right_attr6 = None
		self.right_select_btn = None
		self.AcceptButton = None

	def Open(self, cell, new_attrSlot = 0):
		self.Show()
		self.isUsable = TRUE
		self.targetSlot.SetItemSlot(0, player.GetItemIndex(cell), 0)
		global itemCell
		itemCell = cell
		
		if self.left_select_btn:
			self.left_select_btn.SetUp()
		
		if self.right_select_btn:
			self.right_select_btn.SetUp()
		
		if self.left_attr0:
			self.left_attr0.Hide()
		if self.left_attr1:
			self.left_attr1.Hide()
		if self.left_attr2:
			self.left_attr2.Hide()
		if self.left_attr3:
			self.left_attr3.Hide()
		if self.left_attr4:
			self.left_attr4.Hide()
		if self.left_attr5:
			self.left_attr5.Hide()
		if self.left_attr6:
			self.left_attr6.Hide()
		
		if self.left_attr0:
			self.left_attr0.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr1:
			self.left_attr1.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr2:
			self.left_attr2.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr3:
			self.left_attr3.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr4:
			self.left_attr4.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr5:
			self.left_attr5.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr6:
			self.left_attr6.SetFontColor(0.3549, 0.3549, 0.3549)
		
		if self.right_attr0:
			self.right_attr0.Hide()
		if self.right_attr1:
			self.right_attr1.Hide()
		if self.right_attr2:
			self.right_attr2.Hide()
		if self.right_attr3:
			self.right_attr3.Hide()
		if self.right_attr4:
			self.right_attr4.Hide()
		if self.right_attr5:
			self.right_attr5.Hide()
		if self.right_attr6:
			self.right_attr6.Hide()
		
		if self.right_attr0:
			self.right_attr0.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr1:
			self.right_attr1.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr2:
			self.right_attr2.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr3:
			self.right_attr3.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr4:
			self.right_attr4.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr5:
			self.right_attr5.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr6:
			self.right_attr6.SetFontColor(0.3549, 0.3549, 0.3549)
		
		attrSlot = [player.GetItemAttribute(player.INVENTORY, itemCell, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		if 0 != attrSlot:
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type = attrSlot[i][0]
				value = attrSlot[i][1]
				if 0 == value:
					continue
				
				affectString = self.__GetAffectString(type, value)
				if affectString:
					if i == 0:
						self.left_attr0.SetText(affectString)
						self.left_attr0.Show()
					if i == 1:
						self.left_attr1.SetText(affectString)
						self.left_attr1.Show()
					if i == 2:
						self.left_attr2.SetText(affectString)
						self.left_attr2.Show()
					if i == 3:
						self.left_attr3.SetText(affectString)
						self.left_attr3.Show()
					if i == 4:
						self.left_attr4.SetText(affectString)
						self.left_attr4.Show()
					if i == 5:
						self.left_attr5.SetText(affectString)
						self.left_attr5.Show()
					if i == 6:
						self.left_attr6.SetText(affectString)
						self.left_attr6.Show()
		
		if 0 != new_attrSlot:
			#for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			for i in xrange(5):
				type = new_attrSlot[i][0]
				value = new_attrSlot[i][1]
				if 0 == value:
					continue
				
				affectString = self.__GetAffectString(type, value)
				if affectString:
					if i == 0:
						self.right_attr0.SetText(affectString)
						self.right_attr0.Show()
					if i == 1:
						self.right_attr1.SetText(affectString)
						self.right_attr1.Show()
					if i == 2:
						self.right_attr2.SetText(affectString)
						self.right_attr2.Show()
					if i == 3:
						self.right_attr3.SetText(affectString)
						self.right_attr3.Show()
					if i == 4:
						self.right_attr4.SetText(affectString)
						self.right_attr4.Show()
					if i == 5:
						self.right_attr5.SetText(affectString)
						self.right_attr5.Show()
					if i == 6:
						self.right_attr6.SetText(affectString)
						self.right_attr6.Show()

		global choosedOption
		choosedOption = 0

	def __OnClickLeftButton(self):
		global choosedOption
		choosedOption = 1
		
		if self.right_select_btn:
			self.right_select_btn.SetUp()
		
		if self.left_select_btn:
			self.left_select_btn.Down()
		
		if self.left_attr0:
			self.left_attr0.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr1:
			self.left_attr1.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr2:
			self.left_attr2.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr3:
			self.left_attr3.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr4:
			self.left_attr4.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr5:
			self.left_attr5.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.left_attr6:
			self.left_attr6.SetFontColor(0.8549, 0.8549, 0.8549)
		
		if self.right_attr0:
			self.right_attr0.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr1:
			self.right_attr1.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr2:
			self.right_attr2.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr3:
			self.right_attr3.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr4:
			self.right_attr4.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr5:
			self.right_attr5.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.right_attr6:
			self.right_attr6.SetFontColor(0.3549, 0.3549, 0.3549)

	def __OnClickRightButton(self):
		global choosedOption
		choosedOption = 2
		
		if self.left_select_btn:
			self.left_select_btn.SetUp()
		
		if self.right_select_btn:
			self.right_select_btn.Down()
		
		if self.left_attr0:
			self.left_attr0.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr1:
			self.left_attr1.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr2:
			self.left_attr2.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr3:
			self.left_attr3.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr4:
			self.left_attr4.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr5:
			self.left_attr5.SetFontColor(0.3549, 0.3549, 0.3549)
		if self.left_attr6:
			self.left_attr6.SetFontColor(0.3549, 0.3549, 0.3549)
		
		if self.right_attr0:
			self.right_attr0.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr1:
			self.right_attr1.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr2:
			self.right_attr2.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr3:
			self.right_attr3.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr4:
			self.right_attr4.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr5:
			self.right_attr5.SetFontColor(0.8549, 0.8549, 0.8549)
		if self.right_attr6:
			self.right_attr6.SetFontColor(0.8549, 0.8549, 0.8549)

	def __OnAcceptButtonClick(self):
		global choosedOption
		if choosedOption != 1 and choosedOption != 2:
			chat.AppendChat(chat.CHAT_TYPE_INFO, locale.NEW_ENCHANT_DIALOG_ALERT_2)
			return FALSE
		
		if choosedOption == 1:
			net.SendChatPacket("/enchant_old")
		elif choosedOption == 2:
			net.SendChatPacket("/enchant_new")
		
		self.Close()
		return TRUE

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return TRUE

	def Close(self):
		if self.isUsable:
			self.isUsable = FALSE
		
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.Hide()	

	def __OnCloseButtonClick(self):
		#self.Close()
		chat.AppendChat(chat.CHAT_TYPE_INFO, locale.NEW_ENCHANT_DIALOG_ALERT_1)
		return FALSE
