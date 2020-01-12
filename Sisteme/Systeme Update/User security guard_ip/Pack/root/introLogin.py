Search:
[...]
def __init__(self, stream):
[...]
		self.timeOutMsg = False

Add it under
		if app.ENABLE_USER_SECURITY_GUARD:
			self.GuardInput = None


---

Search:
		self.loginFailureMsgDict={
			#"DEFAULT" : localeInfo.LOGIN_FAILURE_UNKNOWN,

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
			"BADSCLID"	: localeInfo.LOGIN_FAILURE_WRONG_SOCIALID,
			"AGELIMIT"	: localeInfo.LOGIN_FAILURE_SHUTDOWN_TIME,
		}

Add it under:
		if app.ENABLE_USER_SECURITY_GUARD:
			self.loginFailureMsgDict.update({
				"WSRVERR"		: "Unable to connect to the web server",
				"WBUNKNW"		: "Webserver returned as unknown error",
				"MSENDED"		: "Mail sended to your e-mail please check it",
				"ALRDSND"		: "Already sended mail in your e-mail please check it",
				"MAILERR"		: "Mailserver returned as unknown error",
				"NTVALID"		: "Your entered e-mail key isn't valid",
			})


---

Search:
		self.loginFailureFuncDict = {
			"WRONGPWD"	: self.__DisconnectAndInputPassword,
			"QUIT"		: app.Exit,
		}

Add it under:
		if app.ENABLE_USER_SECURITY_GUARD:
			self.loginFailureFuncDict.update({
				"MSENDED"		: self.AskGuardCode,
				"ALRDSND"		: self.AskGuardCode,
				"NTVALID"		: self.CheckGuardCode,
			})

---

Search:
[...]
def Close(self):
[...]
		self.VIRTUAL_KEY_NUMBERS = None

Add it under:
		if app.ENABLE_USER_SECURITY_GUARD:
			self.GuardInput = None

---
Search:
	def Connect(self, id, pwd):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.SetPasswordEditLineFocus, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()

Change:
	def Connect(self, id, pwd, guard):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.SetPasswordEditLineFocus, localeInfo.UI_CANCEL)

		if app.ENABLE_USER_SECURITY_GUARD:
			constInfo.GUARD_KEY = ""

		self.stream.SetLoginInfo(id, pwd, guard)
		self.stream.Connect()

---

Search:
	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()

		if not id:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return

		if not pwd:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		self.Connect(id, pwd)

Change:
	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		guard = constInfo.GUARD_KEY

		if not id:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return

		if not pwd:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		self.Connect(id, pwd, guard)

	def AskGuardCode(self):
		GuardInput = uiCommon.InputDialog()
		GuardInput.SetTitle("Enter the code sent to your e-mail address")
		GuardInput.SetAcceptEvent(ui.__mem_func__(self.ConfirmGuardCode))
		GuardInput.SetCancelEvent(ui.__mem_func__(self.CancelGuardCode))
		GuardInput.Open()

		self.GuardInput = GuardInput

	def ConfirmGuardCode(self):
		constInfo.GUARD_KEY = self.GuardInput.GetText()
		self.__OnClickLoginButton()

		self.GuardInput.Close()
		self.GuardInput = None
		return True

	def CancelGuardCode(self):
		self.GuardInput.Close()
		self.GuardInput = None
		return True

	def CheckGuardCode(self):
		if constInfo.GUARD_TRY_COUNT == 3:
			self.PopupNotifyMessage("You already tried too much", self.__ExitGame)

		constInfo.GUARD_TRY_COUNT += 1
