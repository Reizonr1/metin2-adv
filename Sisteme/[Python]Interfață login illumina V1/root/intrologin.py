import app
import net
import ui
import snd
import wndMgr
import musicInfo
import systemSetting
import localeInfo
import constInfo
import ime
from _weakref import proxy

g_ip = "5.154.174.118"

import _winreg
REG_PATH = r"SOFTWARE\Arianea"

def set_reg(name, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return str(value)
    except WindowsError:
        return None		
		
class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.stream = stream	
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)

	def Open(self):
		self.loginFailureMsgDict={

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
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		self.__LoadScript("pongo_work/loginwindow/loginwindow.py")
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())
		self.CheckAccount()

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		self.SetChannel(0)
		
		self.Show()
		app.ShowCursor()	

	def Close(self):
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.idEditLine = self.GetChild("id")
			self.pwdEditLine = self.GetChild("pwd")
			self.loginButton = self.GetChild("login_button")
			self.exitButton = self.GetChild("exit_button")
			self.jebanyPies = self.GetChild("dog")
			
			self.channelButton = {
				0 : self.GetChild("ch1"),
				1 :	self.GetChild("ch2"),
				2 : self.GetChild("ch3"),
				3 : self.GetChild("ch4"),
				4 : self.GetChild("ch5"),
				5 : self.GetChild("ch6")}
			
			self.accountData = {
				0 : [[self.GetChild("load_button_0"), self.GetChild("save_button_0"), self.GetChild("delete_button_0")], self.GetChild("account_0_text")],
				1 : [[self.GetChild("load_button_1"), self.GetChild("save_button_1"), self.GetChild("delete_button_1")], self.GetChild("account_1_text")],
				2 : [[self.GetChild("load_button_2"), self.GetChild("save_button_2"), self.GetChild("delete_button_2")], self.GetChild("account_2_text")],
				3 : [[self.GetChild("load_button_3"), self.GetChild("save_button_3"), self.GetChild("delete_button_3")], self.GetChild("account_3_text")]}

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
			
		for (key, item) in self.accountData.items():
			if isinstance(item[0], list):
				item[0][0].SetEvent(ui.__mem_func__(self.LoadAccount), key)
				item[0][1].SetEvent(ui.__mem_func__(self.SaveAccount), key)
				item[0][2].SetEvent(ui.__mem_func__(self.DeleteAccount), key)
				
		for (channelID, channelButtons) in self.channelButton.items():
				channelButtons.SetEvent(ui.__mem_func__(self.SetChannel), channelID)

		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))
		
		self.jebanyPies.SetEvent(ui.__mem_func__(self.IHavePoorPC))
		
		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
		self.idEditLine.SetFocus()
		
	def IHavePoorPC(self):
		if get_reg("mob") == "0":
			self.jebanyPies.SetUpVisual("pongo_work/loginwindow/dog2.tga")
			self.jebanyPies.SetOverVisual("pongo_work/loginwindow/dog1.tga")
			self.jebanyPies.SetDownVisual("pongo_work/loginwindow/dog1.tga")
			set_reg("mob", "1")
		else:
			self.jebanyPies.SetUpVisual("pongo_work/loginwindow/dog1.tga")
			self.jebanyPies.SetOverVisual("pongo_work/loginwindow/dog2.tga")
			self.jebanyPies.SetDownVisual("pongo_work/loginwindow/dog2.tga")
			set_reg("mob", "0")
		
	def CheckAccount(self):
		for i in xrange(4):
			if get_reg("id_%d" % i):
				self.accountData[i][1].SetText(str(get_reg("id_%d" % i)))
				self.accountData[i][0][1].Hide()
				self.accountData[i][0][0].Show()
			else:
				self.accountData[i][1].SetText("Slot liber")
				self.accountData[i][0][1].Show()
				self.accountData[i][0][0].Hide()
				
	def DeleteAccount(self, key):
		if get_reg("id_%d" % key):
			set_reg("id_%d" % key, "")
			set_reg("pwd_%d" % key, "")
			self.PopupNotifyMessage("Contul tocmai a fost ºters.")
		else:
			self.PopupNotifyMessage("Pentru a ºterge un cont, trebuie sã salvezi unul.")
			
		self.CheckAccount()
		
	def LoadAccount(self, key):
		if get_reg("id_%d" % key):
			self.idEditLine.SetText(str(get_reg("id_%d" % key)))
			self.pwdEditLine.SetText(str(get_reg("pwd_%d" % key)))
			self.pwdEditLine.SetFocus()
		else:
			self.PopupNotifyMessage("Nu este nici un cont salvat.")
			
	def SaveAccount(self, key):
		if get_reg("id_%d" % key):
			self.PopupNotifyMessage("Pentru a-þi salva un cont, trebuie sã îl ºtergi.")
			return
		
		if self.idEditLine.GetText() == "" or self.pwdEditLine.GetText() == "":
			self.PopupNotifyMessage("Introdu datele contului pentru a-l salva.")
			return
		
		set_reg("id_%d" % key, self.idEditLine.GetText())
		set_reg("pwd_%d" % key, self.pwdEditLine.GetText())
		self.PopupNotifyMessage("Contul a fost salvat cu succes.")
		self.CheckAccount()

	def SetChannel(self, ch):
		for key, button in self.channelButton.items():
			button.SetUp()
			
		self.channelButton[ch].Down()

		self.stream.SetConnectInfo(g_ip, self.ChannelPort(ch, 0), g_ip, self.ChannelPort("LOGIN"))
		net.SetMarkServer(g_ip, self.ChannelPort("LOGO"))
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		net.SetServerInfo(self.ChannelPort(ch, 2))
		
	def ChannelPort(self, ch, value=0):
		channel = {

			0	:	13000,
			1	:	13001,
			2	:	13002,
			3	:	13003,
			4	:	13004,
			5	:	13005}
		
		if ch == "LOGIN":
			return 11002
		elif ch == "LOGO":
			return channel[0]
		elif value == 2:
			return "Arianea, Channel %s" % (ch+1)
		else:
			return channel[ch]
				
	def Connect(self, id, pwd):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()
			
		constInfo.LastAccount = id.lower()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def EmptyFunc(self):
		pass

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		self.Connect(id, pwd)

