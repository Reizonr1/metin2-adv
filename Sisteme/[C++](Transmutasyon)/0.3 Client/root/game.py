## Search for:
import stringCommander

## Import under:
if app.ENABLE_CHANGE_LOOK_SYSTEM:
	import uichangelook

## Search for:
		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.03
		self.curtain.Hide()

## Add under:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.ChangeLookWindow = uichangelook.ChangeLookWindow()

## Search for:
		self.serverCommander=stringCommander.Analyzer()

## Add under:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			serverCommandList.update({"ChangeLookWindow" : self.OpenChangeLookWindow})

## Go to the last line of the file and Paste this:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def OpenChangeLookWindow(self):
			self.ChangeLookWindow.Open()
