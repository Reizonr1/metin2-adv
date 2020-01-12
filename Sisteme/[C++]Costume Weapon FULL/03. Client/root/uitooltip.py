""""""
#1) Search: isCostumeBody = 0
#2) After this make a new line and paste:
		if app.ENABLE_COSTUME_WEAPON_SYSTEM:
			isCostumeWeapon = 0
""""""

""""""
#1) Search: isCostumeBody = item.COSTUME_TYPE_BODY == itemSubType
#2) After this make a new line and paste:
				if app.ENABLE_COSTUME_WEAPON_SYSTEM:
					isCostumeWeapon = item.COSTUME_TYPE_WEAPON == itemSubType
""""""