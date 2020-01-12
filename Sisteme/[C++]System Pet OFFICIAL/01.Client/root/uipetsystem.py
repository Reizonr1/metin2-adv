import os
import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import localeInfo
import constInfo
import ime
import wndMgr
import petskill
import uipetfeed
import uiToolTip


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
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_ATT_GRADE,
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
		item.APPLY_MAX_HP_PCT : localeInfo.TOOLTIP_APPLY_MAX_HP_PCT,
		item.APPLY_MAX_SP_PCT : localeInfo.TOOLTIP_APPLY_MAX_SP_PCT,
		item.APPLY_ENERGY : localeInfo.TOOLTIP_ENERGY,
		item.APPLY_COSTUME_ATTR_BONUS : localeInfo.TOOLTIP_COSTUME_ATTR_BONUS,
		
		item.APPLY_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MAGIC_ATTBONUS_PER,
		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_ICE : localeInfo.TOOLTIP_RESIST_ICE,
		item.APPLY_RESIST_EARTH : localeInfo.TOOLTIP_RESIST_EARTH,
		item.APPLY_RESIST_DARK : localeInfo.TOOLTIP_RESIST_DARK,
		item.APPLY_ANTI_CRITICAL_PCT : localeInfo.TOOLTIP_ANTI_CRITICAL_PCT,
		item.APPLY_ANTI_PENETRATE_PCT : localeInfo.TOOLTIP_ANTI_PENETRATE_PCT,
	}
	
	
def checkdiv(n):
	x = str(n/10.0)
	if len(x) > 3:
		return str(x)[0:3]
	return str(x)

def pointop(n):
	t = int(n)
	if t / 10 < 1:
		return "0."+n
	else:		
		return n[0:len(n)-1]+"."+n[len(n)-1:]
		
		
def GetAffectString(affectType, affectValue):
	if 0 == affectType:
		return None

	if 0 == affectValue:
		return None

	try:
		return AFFECT_DICT[affectType](affectValue)
	except TypeError:
		return "UNKNOWN_VALUE[%s] %s" % (affectType, affectValue)
	except KeyError:
		return "UNKNOWN_TYPE[%s] %s" % (affectType, affectValue)
		
class PetSystemMain(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self, y):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignLeft()
			textLine.SetOutline()
			textLine.Show()
			self.y = y
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 60 + self.y)

	def __init__(self, vnum = 0):
		ui.ScriptWindow.__init__(self)
		self.vnum = vnum
		self.__LoadWindow()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		self.feedwind.Close()
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetInformationWindow.py")
		except:
			import exception
			exception.Abort("PetInformationWindow.LoadWindow.LoadObject")
			
		try:
			self.feedwind = uipetfeed.PetFeedWindow()
			self.board = self.GetChild("board")
			self.boardclose = self.GetChild("CloseButton")
			
			self.slotimgpet = self.GetChild("UpBringing_Pet_Slot")
			self.evolname = self.GetChild("EvolName")
			self.petname = self.GetChild("PetName")
			
			self.expwind = self.GetChild("UpBringing_Pet_EXP_Gauge_Board")
			self.tooltipexp = []
			for i in range(0,4):
				self.tooltipexp.append(self.TextToolTip(15*i))
				self.tooltipexp[i].Hide()
			
			self.petlifeg = self.GetChild("LifeGauge")
			
			self.petlevel = self.GetChild("LevelValue")
			self.petexpa = self.GetChild("UpBringing_Pet_EXPGauge_01")
			self.petexpb = self.GetChild("UpBringing_Pet_EXPGauge_02")
			self.petexpc = self.GetChild("UpBringing_Pet_EXPGauge_03")
			self.petexpd = self.GetChild("UpBringing_Pet_EXPGauge_04")
			self.petexpe = self.GetChild("UpBringing_Pet_EXPGauge_05")
			self.petexppages = []			
			self.petexppages.append(self.petexpa)
			self.petexppages.append(self.petexpb)
			self.petexppages.append(self.petexpc)
			self.petexppages.append(self.petexpd)
			self.petexppages.append(self.petexpe)
			
			for exp in self.petexppages:
				exp.SetSize(0, 0)
				#exp.Hide()
				
			
			
			
			
			self.petages = self.GetChild("AgeValue")
			
			self.petdur = self.GetChild("LifeTextValue")
			
			#gaugehp
			
			self.nutribtn = self.GetChild("FeedLifeTimeButton")
			self.sviluppobtn = self.GetChild("FeedEvolButton")
			self.itemexp = self.GetChild("FeedExpButton")
			
			self.pethp = self.GetChild("HpValue")
			self.petdef = self.GetChild("DefValue")
			self.petsp = self.GetChild("SpValue")
			
			self.petskill0 = self.GetChild("PetSkillSlot0")
			
			
			
			
			
			
			
			#self.petskill0.SetPetSkillSlot(0, 2, 10)
			#self.petskill0.SetPetSkillSlot(1, 11, 10)
			#self.petskill0.SetPetSkillSlot(2, 5, 10)
			self.petskill0.SetSlot(0, 2, 32, 32, petskill.GetEmptySkill())
			self.petskill0.SetSlot(1, 2, 32, 32, petskill.GetEmptySkill())
			self.petskill0.SetSlot(2, 2, 32, 32, petskill.GetEmptySkill())
			#self.petskill0.SetCoverButton(0)
			#self.petskill0.SetCoverButton(1)
			#self.petskill0.SetCoverButton(2)
			#self.petskill0.SetAlwaysRenderCoverButton(0, TRUE)
			#self.petskill0.SetAlwaysRenderCoverButton(1, TRUE)
			#self.petskill0.SetAlwaysRenderCoverButton(2, TRUE)
			self.petskill0.SetSelectItemSlotEvent(ui.__mem_func__(self.UseSkill))
			self.petskill0.SetUseSlotEvent(ui.__mem_func__(self.UseSkill))
			self.petskill0.SetOverInItemEvent(ui.__mem_func__(self.PetSkillTooltipShow))
			self.petskill0.SetOverOutItemEvent(ui.__mem_func__(self.PetSkillTooltipHide))	
			
			
			
			self.SetDefaultInfo()
			
			self.arrytooltip = [ [-1,-1], [-1,-1], [-1,-1]]
			PET_FILE_NAME = "%s/pet_skill.txt" % app.GetLocalePath()
			PET_FILE_SKILL = "%s/pet_skill_bonus.txt" % app.GetLocalePath()
			self.linespet = pack_open(PET_FILE_NAME, "r").readlines()
			self.linespetskill = pack_open(PET_FILE_SKILL, "r").readlines()
			self.SkillTooltip = uiToolTip.ToolTip(180)
			
			
			#Event
			self.boardclose.SetEvent(ui.__mem_func__(self.Close,))
			self.nutribtn.SetToggleDownEvent(lambda arg=0,arg1=1: self.OpenFeedBox(arg,arg1))
			self.nutribtn.SetToggleUpEvent(lambda arg=1,arg1=0: self.OpenFeedBox(arg,arg1))
			self.itemexp.SetToggleDownEvent(lambda arg=0,arg1=3: self.OpenFeedBox(arg,arg1))
			self.itemexp.SetToggleUpEvent(lambda arg=1,arg1=0: self.OpenFeedBox(arg,arg1))
			self.sviluppobtn.SetToggleDownEvent(lambda arg=0: self.evolution(arg))
			self.sviluppobtn.SetToggleUpEvent(lambda arg=1: self.evolution(arg))
			
			
		except:
			import exception
			exception.Abort("PetInformationWindow.LoadWindow.BindObject")
	

			
	def PetSkillTooltipShow(self, slot):
		if self.arrytooltip[slot][0] > 0:
			tokens = self.linespet[self.arrytooltip[slot][0]-1][:-1].split("\t")
			tokens2 = self.linespetskill[self.arrytooltip[slot][0]-1][:-1].split("\t")
			self.SkillTooltip.ClearToolTip()
			self.SkillTooltip.AutoAppendTextLine(tokens[1], grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0))
			self.SkillTooltip.AppendDescription(tokens[4], 26)
			self.SkillTooltip.AppendSpace(5)
			if self.arrytooltip[slot][0] != 10 and self.arrytooltip[slot][0] != 17 and self.arrytooltip[slot][0] != 18:
				self.SkillTooltip.AutoAppendTextLine(GetAffectString(int(tokens2[1]), int(tokens2[self.arrytooltip[slot][1]+1])))
			elif self.arrytooltip[slot][0] == 10:
				self.SkillTooltip.AutoAppendTextLine("Hp Restored:" + str(tokens2[self.arrytooltip[slot][1]+1]))
			elif self.arrytooltip[slot][0] == 17:
				self.SkillTooltip.AutoAppendTextLine("Immortality Time:" + checkdiv(int(tokens2[self.arrytooltip[slot][1]+1])) + "s")
			
			self.SkillTooltip.AutoAppendTextLine("Cooldown: "+tokens[5]+"s", grp.GenerateColor(1.0, 0.7843, 0.0, 1.0))
			self.SkillTooltip.AlignHorizonalCenter()
			self.SkillTooltip.ShowToolTip()
		
		
	def PetSkillTooltipHide(self):
		self.SkillTooltip.HideToolTip()
		
		
	def evolution(self, mode):
		if mode == 0:
			net.SendChatPacket("/petvoincrease")
			self.sviluppobtn.Enable()
		#self.SkillTooltip.HideToolTip()
		
	def SetDefaultInfo(self):
		self.evolname.SetText("")
		self.petname.SetText("")
		
		self.petlevel.SetText("")
		self.petages.SetText("")
		self.petdur.SetText("")
		
		self.pethp.SetText("")
		self.petdef.SetText("")
		self.petsp.SetText("")
		
		self.SetDuration("0", "0")
		
		self.slotimgpet.ClearSlot(0)
		self.petskill0.ClearSlot(0)
		self.petskill0.ClearSlot(1)
		self.petskill0.ClearSlot(2)
		self.petskill0.SetSlot(0, 2, 32, 32, petskill.GetEmptySkill())
		self.petskill0.SetSlot(1, 2, 32, 32, petskill.GetEmptySkill())
		self.petskill0.SetSlot(2, 2, 32, 32, petskill.GetEmptySkill())
		
		self.SetExperience(0,0,0)
		
		self.arrytooltip = [ [-1,-1], [-1,-1], [-1,-1]]
		
		self.nutribtn.Disable()
		self.sviluppobtn.Disable()
		self.itemexp.Disable()
	
	def OpenFeedBox(self, mode, btn):
		if constInfo.FEEDWIND == btn or constInfo.FEEDWIND == 0:
			if mode == 0:
				self.feedwind.Show()
				constInfo.FEEDWIND = btn
			else:
				self.feedwind.Close()
				constInfo.FEEDWIND = 0
		else:
			self.nutribtn.Enable()
			self.sviluppobtn.Enable()
			self.itemexp.Enable()
			self.feedwind.Close()
			constInfo.FEEDWIND = 0			
	
	def SetImageSlot(self, vnum):
		self.slotimgpet.SetItemSlot(0, int(vnum), 0)
		self.slotimgpet.SetAlwaysRenderCoverButton(0, TRUE)
	
			
	def SetEvolveName(self, name):
		self.evolname.SetText(name)
	
	def SetName(self, name):
		if name != "":
			self.nutribtn.Enable()
			self.sviluppobtn.Enable()
			self.itemexp.Enable()
			
			#pet.SetTop()
		else:
			self.nutribtn.Disable()
			self.sviluppobtn.Disable()
			self.itemexp.Disable()
			
		self.petname.SetText(name)
	
	def SetLevel(self, level):
		if int(level) == 40 or int(level) == 60 or int(level) == 80:
			constInfo.EVOLUTION = int(level)
		else:
			constInfo.EVOLUTION = 0
		self.petlevel.SetText(level)
	
	def SetAges(self, ages):
		self.petages.SetText(ages)
	
	def SetDuration(self, dur, durt):
		dur1 = int(dur)/60
		durt1 = int(durt)/60
		tmpage = int((int(durt)/60 -int(dur) /60)/24)		
		if int(dur) > 0:
			self.petlifeg.SetPercentage(int(dur)*1.6, int(durt))
			self.petlifeg.Show()
		else:
			self.petlifeg.Hide()
		self.petdur.SetText(str(dur1)+"/"+str(durt1)+" Ore")
		self.SetAges(str(tmpage)+"Zile")
		
	def SetHp(self, hp):
		self.pethp.SetText(pointop(hp)+"%")
		
	def SetDef(self, deff):
		self.petdef.SetText(pointop(deff)+"%")
		
	def SetSp(self, sp):
		self.petsp.SetText(pointop(sp)+"%")
	
	def SetSkill(self, slot, idx, lv):
		if int(idx) != -1:
			self.petskill0.ClearSlot(int(slot))
			self.petskill0.SetPetSkillSlot(int(slot), int(idx), int(lv))
			self.petskill0.SetCoverButton(int(slot))
			self.petskill0.SetAlwaysRenderCoverButton(int(slot), TRUE)
			self.arrytooltip[int(slot)][0] = int(idx)
			self.arrytooltip[int(slot)][1] = int(lv)
			#chat.AppendChat(chat.CHAT_TYPE_INFO, "Slot:"+str(slot)+" idx: "+str(idx)+" Lv:"+str(lv))
			
	def SetExperience(self, expm, expi, exptot):
		expm = int(expm)
		expi = int(expi)
		exptot = int(exptot)
		
		if exptot > 0:	
			totalexp = exptot
			totexpm = int( float(totalexp) / 100 * 90 )
			totexpi = totalexp - totexpm
			expi = min(expi, totexpi)
			expmp =  float(expm) / totexpm * 100
			expip =  float(expi) / totexpi * 100
		else:
			totalexp = 0
			totexpm = 0
			totexpi = 0
			expmp =  0
			expip =  0
			
		
		curPoint = int(min(expm, totexpm))
		curPoint = int(max(expm, 0))
		maxPoint = int(max(totexpm, 0))
		
		curPointi = int(min(expi, totexpi))
		curPointi = int(max(expi, 0))
		maxPointi = int(max(totexpi, 0))

		quarterPoint = maxPoint / 4
		quarterPointi = maxPointi 
		FullCount = 0
		FullCounti = 0

		if 0 != quarterPoint:
			FullCount = min(4, curPoint / quarterPoint)
			
		if 0 != quarterPointi:
			FullCounti = min(1, curPointi / quarterPointi)

		for i in xrange(4):
			self.petexppages[i].Hide()
			
		self.petexppages[4].Hide()

		for i in xrange(FullCount):
			self.petexppages[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.petexppages[i].Show()
			
		for i in xrange(FullCounti):
			self.petexppages[4].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.petexppages[4].Show()

		if 0 != quarterPoint:
			if FullCount < 4:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.petexppages[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.petexppages[FullCount].Show()
				
		if 0 != quarterPointi:
			if FullCounti < 1:
				Percentage = float(curPointi % quarterPointi) / quarterPointi - 1.0
				self.petexppages[4].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.petexppages[4].Show()
			
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(curPoint)+"-"+str(maxPoint)+"-"+str(FullCount)+"--"+str(quarterPoint))
		#####
		self.tooltipexp[0].SetText("Experienta : %d of %d" % (expm, totexpm))
		self.tooltipexp[1].SetText("Experienta : %.2f%%" % expmp)
		self.tooltipexp[2].SetText("ExperientaI : %d of %d" % (expi, totexpi))
		self.tooltipexp[3].SetText("ExperientaI : %.2f%%" % expip)
	
	def UseSkill(self, slot):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "+ --> "+str(slot))
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "Skill: "+ str(petskill.GetSkillbySlot(slot)))
		net.SendChatPacket("/petskills "+str(slot))
	
	def OnUpdate(self):
		if constInfo.FEEDWIND == 0:
			self.nutribtn.Enable()
			#self.sviluppobtn.Enable()
			self.itemexp.Enable()
		if TRUE == self.expwind.IsIn():
			for i in range(0,4):				
				self.tooltipexp[i].Show()
		else:
			for i in range(0,4):				
				self.tooltipexp[i].Hide()
	
class PetSystemMini(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self, y):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignLeft()
			textLine.SetOutline()
			textLine.Show()
			self.y = y
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 60 + self.y)

	def __init__(self, vnum = 0):
		ui.ScriptWindow.__init__(self)
		self.vnum = vnum
		self.__LoadWindow()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetMiniInformationWindow.py")
		except:
			import exception
			exception.Abort("PetMiniInformationWindow.LoadWindow.LoadObject")
			
		try:
			
			self.expwind = self.GetChild("pet_mini_info_exp_gauge_board")
			self.mainbg = self.GetChild("main_bg")
			self.mainicon = self.GetChild("main_slot_img")
			self.main_slot_img = self.GetChild("pet_icon_slot")
			self.tooltipexp = []
			for i in range(0,4):
				self.tooltipexp.append(self.TextToolTip(15*i))
				self.tooltipexp[i].Hide()
			self.pet_icon_slot_ani_img = self.GetChild("pet_icon_slot_ani_img")
			self.pet_mini_exp_01 = self.GetChild("pet_mini_EXPGauge_01")
			self.pet_mini_exp_02 = self.GetChild("pet_mini_EXPGauge_02")
			self.pet_mini_exp_03 = self.GetChild("pet_mini_EXPGauge_03")
			self.pet_mini_exp_04 = self.GetChild("pet_mini_EXPGauge_04")
			self.pet_mini_exp_05 = self.GetChild("pet_mini_EXPGauge_05")
			self.petmini_exp = []
			self.petmini_exp.append(self.pet_mini_exp_01)
			self.petmini_exp.append(self.pet_mini_exp_02)
			self.petmini_exp.append(self.pet_mini_exp_03)
			self.petmini_exp.append(self.pet_mini_exp_04)
			self.petmini_exp.append(self.pet_mini_exp_05)
			self.petlifeg = self.GetChild("LifeGauge")
			
			
			
			self.skillslot = self.GetChild("mini_skill_slot0")
			#self.skillslot.SetSlotScale(0, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
			#self.skillslot.SetSlotScale(1, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
			#self.skillslot.SetSlotScale(2, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
			
			self.skillslot.SetSelectItemSlotEvent(ui.__mem_func__(self.UseSkill))
			self.skillslot.SetUseSlotEvent(ui.__mem_func__(self.UseSkill))
			
			
			
			
			
			
			self.SetDefaultInfo()
			
			
			
			#self.mainbg.Show()
			
		except:
			import exception
			exception.Abort("PetMiniInformationWindow.LoadWindow.BindObject")
			
		
		
	def SetDefaultInfo(self):		
		
		self.SetDuration("0", "0")
		
		self.main_slot_img.ClearSlot(0)
		self.skillslot.ClearSlot(0)
		self.skillslot.ClearSlot(1)
		self.skillslot.ClearSlot(2)
		#self.skillslot.SetSlotScale(0, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
		#self.skillslot.SetSlotScale(1, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
		#self.skillslot.SetSlotScale(2, 2, 16, 16, petskill.GetEmptySkill(), 0.5, 0.5)
		
		self.SetExperience(0,0,0)
		
		
		
	
	def SetImageSlot(self, vnum):
		self.main_slot_img.SetItemSlot(0, int(vnum), 0)
		self.main_slot_img.SetAlwaysRenderCoverButton(0, TRUE)
	
			
	def SetDuration(self, dur, durt):
		tmpage = int((int(durt)/60 -int(dur) /60)/24)		
		if int(dur) > 0:
			self.petlifeg.SetPercentage(int(dur), int(durt))
			self.petlifeg.Show()
		else:
			self.petlifeg.Hide()
		
	def SetSkill(self, slot, idx, lv):
		if int(idx) != -1:
			self.skillslot.ClearSlot(int(slot))
			self.skillslot.SetPetSkillSlot(int(slot), int(idx), int(lv), 0.5, 0.5)
			self.skillslot.SetCoverButton(int(slot), "d:/ymir work/ui/pet/mini_window/pet_slot_corvermini.sub", "d:/ymir work/ui/pet/mini_window/pet_slot_corvermini.sub", "d:/ymir work/ui/pet/mini_window/pet_slot_corvermini.sub" , "d:/ymir work/ui/pet/mini_window/pet_slot_corvermini.sub")
			self.skillslot.SetAlwaysRenderCoverButton(int(slot), TRUE)
			
			
	def SetExperience(self, expm, expi, exptot):
		expm = int(expm)
		expi = int(expi)
		exptot = int(exptot)
		
		if exptot > 0:	
			totalexp = exptot
			totexpm = int( float(totalexp) / 100 * 90 )
			totexpi = totalexp - totexpm
			expi = min(expi, totexpi)
			expmp =  float(expm) / totexpm * 100
			expip =  float(expi) / totexpi * 100
		else:
			totalexp = 0
			totexpm = 0
			totexpi = 0
			expmp =  0
			expip =  0
			
		
		curPoint = int(min(expm, totexpm))
		curPoint = int(max(expm, 0))
		maxPoint = int(max(totexpm, 0))
		
		curPointi = int(min(expi, totexpi))
		curPointi = int(max(expi, 0))
		maxPointi = int(max(totexpi, 0))

		quarterPoint = maxPoint / 4
		quarterPointi = maxPointi 
		FullCount = 0
		FullCounti = 0

		if 0 != quarterPoint:
			FullCount = min(4, curPoint / quarterPoint)
			
		if 0 != quarterPointi:
			FullCounti = min(1, curPointi / quarterPointi)

		for i in xrange(4):
			self.petmini_exp[i].Hide()
			
		self.petmini_exp[4].Hide()

		for i in xrange(FullCount):
			self.petmini_exp[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.petmini_exp[i].Show()
			
		for i in xrange(FullCounti):
			self.petmini_exp[4].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.petmini_exp[4].Show()

		if 0 != quarterPoint:
			if FullCount < 4:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.petmini_exp[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.petmini_exp[FullCount].Show()
				
		if 0 != quarterPointi:
			if FullCounti < 1:
				Percentage = float(curPointi % quarterPointi) / quarterPointi - 1.0
				self.petmini_exp[4].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.petmini_exp[4].Show()
			
		
		#####
		self.tooltipexp[0].SetText("Experienta : %d of %d" % (expm, totexpm))
		self.tooltipexp[1].SetText("Experienta : %.2f%%" % expmp)
		self.tooltipexp[2].SetText("ExperientaI : %d of %d" % (expi, totexpi))
		self.tooltipexp[3].SetText("ExperientaI : %.2f%%" % expip)
	
	def UseSkill(self, slot):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "+ --> "+str(slot))
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "Skill: "+ str(petskill.GetSkillbySlot(slot)))
		net.SendChatPacket("/petskills "+str(slot))

	def OnUpdate(self):
		if TRUE == self.expwind.IsIn():
			for i in range(0,4):				
				self.tooltipexp[i].Show()
		else:
			for i in range(0,4):				
				self.tooltipexp[i].Hide()
				
				


