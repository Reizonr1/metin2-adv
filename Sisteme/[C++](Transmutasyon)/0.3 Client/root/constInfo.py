## Import:
import app

## Add under:
if app.ENABLE_CHANGE_LOOK_SYSTEM:
	IsChangeLookWindowOpen = False

	def BusySlots():
		return IsChangeLookWindowOpen
