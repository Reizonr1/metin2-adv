import event

CONFIG_YOL = "locale/tr/ui/config/"
PYTHONISLEM = ""
PYTHONTOLUA = 0
INPUT = 0

DICE_SYSTEM = {}

def sendPacket(gelen):
	global PYTHONISLEM
	global PYTHONTOLUA
	
	PYTHONISLEM = gelen
	event.QuestButtonClick(PYTHONTOLUA)