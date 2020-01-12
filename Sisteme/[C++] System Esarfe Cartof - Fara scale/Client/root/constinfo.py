""""""
#1) Search: PVPMODE_PROTECTED_LEVEL
#2) Make a new line and paste:
ACCE_WINDOW = 0
""""""

""""""
#1) Search: def IS_AUTO_POTION_SP(itemVnum):
#2) Make a new line and paste:
def IS_ACCE_ITEM(itemVnum, abs):
	if itemVnum >= 85001 and itemVnum <= 85003:
		return TRUE
	elif itemVnum >= 85005 and itemVnum <= 85007:
		return TRUE
	
	if abs == 1 and itemVnum == 85004 or abs == 1 and itemVnum == 85008:
		return TRUE
	
	return FALSE
""""""

""""""
#1) Search: def IS_ACCE_ITEM(itemVnum, abs):
#2) Make a new line and paste:
def IS_ACCE_ITEM_DETACH(itemVnum):
	if itemVnum >= 85009 and itemVnum <= 85009:
		return TRUE
	
	return FALSE
""""""