""""""
#1) Search: pyScrLoader.LoadScriptFile(self, "UIScript/costumewindow.py")
#2) Replace with:
			if app.ENABLE_EFFECT_SYSTEM:
				pyScrLoader.LoadScriptFile(self, "UIScript/costumewindow_effect_slot.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/costumewindow.py")
""""""