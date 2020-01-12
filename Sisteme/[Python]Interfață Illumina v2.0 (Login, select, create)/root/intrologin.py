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
import uiScriptLocale
import twix_work
import os
import uitooltipGold
''' codin' pass '''
import binascii

''' Registry '''
import _winreg
REG_PATH = r"SOFTWARE\Avantador"

used = 0

def set_reg(name, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

class LoginWindow(ui.ScriptWindow):

    IS_TEST = net.IsTest()

    def __init__(self, stream):
        print "NEW LOGIN WINDOW  ----------------------------------------------------------------------------"
        ui.ScriptWindow.__init__(self)
        net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
        net.SetAccountConnectorHandler(self)

        self.stream = stream
        self.channels = None
        self.channelButton = None
        self.aID = None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

        net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
        net.SetAccountConnectorHandler(0)

    def Open(self):
        self.loginFailureMsgDict={

            "ALREADY"    : localeInfo.LOGIN_FAILURE_ALREAY,
            "NOID"        : localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
            "WRONGPWD"    : localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
            "FULL"        : localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
            "SHUTDOWN"    : localeInfo.LOGIN_FAILURE_SHUTDOWN,
            "REPAIR"    : localeInfo.LOGIN_FAILURE_REPAIR_ID,
            "BLOCK"        : localeInfo.LOGIN_FAILURE_BLOCK_ID,
            "WRONGMAT"    : localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
            "QUIT"        : localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
            "BESAMEKEY"    : localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
            "NOTAVAIL"    : localeInfo.LOGIN_FAILURE_NOT_AVAIL,
            "NOBILL"    : localeInfo.LOGIN_FAILURE_NOBILL,
            "BLKLOGIN"    : localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
            "WEBBLK"    : localeInfo.LOGIN_FAILURE_WEB_BLOCK,
        }

        self.loginFailureFuncDict = {
            "WRONGPWD"    : localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
            "WRONGMAT"    : localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
            "QUIT"        : app.Exit,
        }

        self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
        self.SetWindowName("LoginWindow")

        self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoginWindow.py")

        if musicInfo.loginMusic != "":
            snd.SetMusicVolume(systemSetting.GetMusicVolume())
            snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

        snd.SetSoundVolume(systemSetting.GetSoundVolume())

        ime.AddExceptKey(91)
        ime.AddExceptKey(93)

        self.SetChannel("CH1")
        self.idEditLine.SetFocus()
        self.pressKey()

        for aID in xrange(0, 4):
            if get_reg("%d_id" % aID):
                self.accountText[aID].SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_id" % aID)))

        self.Show()
        app.ShowCursor()

    def Close(self):
        if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
            snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)

        self.idEditLine.SetTabEvent(0)
        self.idEditLine.SetReturnEvent(0)
        self.pwdEditLine.SetReturnEvent(0)
        self.pwdEditLine.SetTabEvent(0)

        self.idEditLine = None
        self.pwdEditLine = None

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
            ui.PythonScriptLoader().LoadScriptFile(self, fileName)

            self.loginBoard                = self.GetChild("LoginBoard")
            # self.serverInfo                = self.GetChild("ConnectName")
            self.loginButton            = self.GetChild("LoginButton")
            self.loginExitButton        = self.GetChild("LoginExitButton")
            self.idEditLines			= self.GetChild("id_editlines")
            self.pwdEditLines			= self.GetChild("pwd_editlines")
            self.buttonExpand			= self.GetChild("buttonExpand")
            self.buttonMinimize			= self.GetChild("buttonMinimize")
            self.accountSaveBoardSave			= self.GetChild("accountLog")
            self.buttonMinimize.Hide()
            self.accountSaveBoardSave.Hide()

            self.accountText = {
                0 : self.GetChild("account_1"),
                1 : self.GetChild("account_2"),
                2 : self.GetChild("account_3"),
                3 : self.GetChild("account_4")}

        except:
            import exception
            exception.Abort("LoginWindow.__LoadScript.BindObject")

        self.LoginInputs()
        self.ChannelSelectFunction()
        self.clickOnTextLinks()
        self.saveAccountChenars()
        self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
        self.GetChild("LoginExitButton").SetEvent(ui.__mem_func__(self.OnPressExitKey))
        self.buttonExpand.SetEvent(lambda : self.hideAndShow(0))
        self.buttonMinimize.SetEvent(lambda : self.hideAndShow(1))

        ####
        self.toolTipSaveButton = uitooltipGold.ToolTip()

    def SetChannel(self, ch):
        self.SetChannelInfo(ch)
        self.stream.SetConnectInfo(twix_work.IP, self.ChannelPort(ch, 0), twix_work.IP, self.ChannelPort("LOGIN"))
        net.SetMarkServer(twix_work.IP, self.ChannelPort("LOGO"))
        app.SetGuildMarkPath("10.tga")
        app.SetGuildSymbolPath("10")
        net.SetServerInfo(self.ChannelPort(ch, 2))

    def SetChannelInfo(self, ch):
        self.channels = str(ch)

    def GetChannel(self):
        return self.channels

    def ChannelPort(self, ch="CH1", value=0):
        channel = {
            "CH1"    :    [twix_work.CH1, "CH1", "Metin2Candy"],
            "CH2"    :    [twix_work.CH2, "CH2", "Metin2Candy"],
            "CH3"    :    [twix_work.CH3, "CH3", "Metin2Candy"],
            "CH4"    :    [twix_work.CH4, "CH4", "Metin2Candy"]}

        if ch == "LOGIN":
            return twix_work.AUTH
        elif ch == "LOGO":
            return channel["CH1"][0]
        elif value == 2:
            return "%s, %s" % (channel[ch][1], channel[ch][2])
        else:
            return channel[ch][value]

    def Connect(self, id, pwd):
        if constInfo.SEQUENCE_PACKET_ENABLE:
            net.SetPacketSequenceMode()

        self.stream.popupWindow.Close()
        self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

        self.stream.SetLoginInfo(id, pwd)
        self.stream.Connect()


    def PopupDisplayMessage(self, msg):
        self.stream.popupWindow.Close()
        self.stream.popupWindow.Open(msg, self.EmptyFunc)

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

    def OnUpdate(self):
        self.descritonOverButtons()

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

###### NEW FUNCTIONS

    def LoginInputs(self):
        self.idEditLine = ui.SpecialEditLine()
        self.idEditLine.SetParent(self.idEditLines)
        self.idEditLine.SetPosition(10,-20)
        self.idEditLine.SetSize(121,25)
        self.idEditLine.SetMax(35)
        self.idEditLine.SetIMEFlag(0)
        self.idEditLine.SetPlaceHolderText("8-16 caractere (a-Z,0-9)")
        self.idEditLine.SetPlaceHolderTextColor(0xff5d4d4b)
        self.idEditLine.SetPackedFontColor(twix_work.COLOR_NORMAL)
        self.idEditLine.Show()


        self.pwdEditLine = ui.SpecialEditLine()
        self.pwdEditLine.SetParent(self.pwdEditLines)
        self.pwdEditLine.SetPosition(10,-20)
        self.pwdEditLine.SetSize(121,25)
        self.pwdEditLine.SetMax(35)
        self.pwdEditLine.SetIMEFlag(0)
        self.pwdEditLine.SetSecret(1)
        self.pwdEditLine.SetPlaceHolderText("8-16 caractere (a-Z,0-9)")
        self.pwdEditLine.SetPlaceHolderTextColor(0xff5d4d4b)
        self.pwdEditLine.SetPackedFontColor(twix_work.COLOR_NORMAL)
        self.pwdEditLine.Show()


        self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
        self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))

        self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
        self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))

    def ChannelSelectFunction(self):
        self.channelSelect = {}
        self.button_text = {}
        tab = 0
        buttons_info =[
        [[40,200,"Canalul I"]],
        [[40+41*3,200,"Canalul II"]],
        [[40,230,"Canalul III"]],
        [[40+41*3,230,"Canalul IV"]]]
        for a in buttons_info:
            self.channelSelect[tab] = ui.RadioButton()
            self.channelSelect[tab].SetParent(self.loginBoard)
            self.channelSelect[tab].SetPosition(a[0][0],a[0][1])
            self.channelSelect[tab].SetUpVisual("d:/ymir work/ui/intro/login/radio/empty_03_active.tga")
            self.channelSelect[tab].SetOverVisual("d:/ymir work/ui/intro/login/radio/filled_01_normal.tga")
            self.channelSelect[tab].SetDownVisual("d:/ymir work/ui/intro/login/radio/filled_01_normal.tga")
            self.channelSelect[tab].Show()

            self.button_text[tab] = ui.TextLine()
            self.button_text[tab].SetParent(self.channelSelect[tab])
            self.button_text[tab].SetPosition(50,3)
            self.button_text[tab].SetText(a[0][2])
            self.button_text[tab].SetPackedFontColor(twix_work.COLOR_NORMAL)
            self.button_text[tab].SetHorizontalAlignCenter()
            self.button_text[tab].Show()

            tab +=1

        self.Slot1 = (
            self.channelSelect[0],
            self.channelSelect[1],
            self.channelSelect[2],
            self.channelSelect[3],
        )
        self.Slot1_1 = (
            self.button_text[0],
            self.button_text[1],
            self.button_text[2],
            self.button_text[3],
        )

        self.Slot1[0].SetEvent((lambda : self.OpenEvents(0,1)))
        self.Slot1[0].Down()
        self.Slot1_1[0].SetPackedFontColor(twix_work.COLOR_HOVER)
        self.Slot1[1].SetEvent((lambda : self.OpenEvents(1,2)))
        self.Slot1[2].SetEvent((lambda : self.OpenEvents(2,3)))
        self.Slot1[3].SetEvent((lambda : self.OpenEvents(3,4)))

    def OpenEvents(self,index,arg):
        for btn in self.Slot1:
            btn.SetUp()
            for ex in self.Slot1_1:
                ex.SetPackedFontColor(twix_work.COLOR_NORMAL)
        self.Slot1[index].Down()
        self.Slot1_1[index].SetPackedFontColor(twix_work.COLOR_HOVER)
        if index == 0:
            self.SetChannel("CH%s" % arg)
        if index == 1:
            self.SetChannel("CH%s" % arg)
        if index == 2:
            self.SetChannel("CH%s" % arg)
        if index ==3:
            self.SetChannel("CH%s" % arg)

    def clickOnTextLinks(self):
        self.RegButton = ui.TextLink()
        self.RegButton.SetParent(self.loginBoard)
        self.RegButton.SetPosition(100,269)
        self.RegButton.SetText("Inregistreaza-te acum!")
        self.RegButton.SetEvent(ui.__mem_func__(self.__OnClickRegButton))
        self.RegButton.Show()

        self.ForgotButton = ui.TextLink()
        self.ForgotButton.SetParent(self.loginBoard)
        self.ForgotButton.SetPosition(40,274+20)
        self.ForgotButton.SetText("Am uitat parola.")
        self.ForgotButton.SetEvent(ui.__mem_func__(self.__OnClickForgotButton))
        self.ForgotButton.Show()

    def __OnClickRegButton(self):
        os.system("start " + twix_work.REGBUTTON)

    def __OnClickForgotButton(self):
        os.system("start " + twix_work.FORGOTPASS)

    def hideAndShow(self, index):
        if index == 0:
            self.buttonExpand.Hide()
            self.buttonMinimize.Show()
            self.accountSaveBoardSave.Show()
        if index == 1:
            self.buttonExpand.Show()
            self.buttonMinimize.Hide()
            self.accountSaveBoardSave.Hide()

    def saveAccountChenars(self):
        self.chenar = {}
        self.keys = {}
        self.deleteButton = {}
        self.saveButton = {}
        tab = 0
        chenars =[
        [[5,10,120,20,145,20]],
        [[5,48,120,58,145,58]],
        [[5,87,120,58+38,145,58+38]],
        [[5,125,120,58+38*2,145,58+38*2]]]

        for a in chenars:
            self.keys[tab] = ui.ImageBox()
            self.keys[tab].SetParent(self.accountSaveBoardSave)
            self.keys[tab].SetPosition(a[0][0],a[0][1])
            self.keys[tab].LoadImage("d:/ymir work/ui/intro/login/f/f%s.tga" % (tab))
            self.keys[tab].Show()

            ###Buttons
            self.saveButton[tab] = ui.Button()
            self.saveButton[tab].SetParent(self.accountSaveBoardSave)
            self.saveButton[tab].SetPosition(a[0][4],a[0][5])
            self.saveButton[tab].SetUpVisual("d:/ymir work/ui/intro/login/save/save_normal.tga")
            self.saveButton[tab].SetOverVisual("d:/ymir work/ui/intro/login/save/save_hover.tga")
            self.saveButton[tab].SetDownVisual("d:/ymir work/ui/intro/login/save/save_hover.tga")
            self.saveButton[tab].Show()

            self.deleteButton[tab] = ui.Button()
            self.deleteButton[tab].SetParent(self.accountSaveBoardSave)
            self.deleteButton[tab].SetPosition(a[0][2],a[0][3])
            self.deleteButton[tab].SetUpVisual("d:/ymir work/ui/intro/login/delete/delete_normal.tga")
            self.deleteButton[tab].SetOverVisual("d:/ymir work/ui/intro/login/delete/delete_hover.tga")
            self.deleteButton[tab].SetDownVisual("d:/ymir work/ui/intro/login/delete/delete_hover.tga")
            self.deleteButton[tab].Show()

            for (tab, saveButton) in self.saveButton.items():
                saveButton.SetEvent(ui.__mem_func__(self.saveAccountFunction),tab)

            for (tab, deleteButton) in self.deleteButton.items():
                deleteButton.SetEvent(ui.__mem_func__(self.deleteAccountFunction),tab)

            tab +=1

    def deleteAccountFunction(self,index):
        if index == 0:
            if get_reg("%d_id" % index):
                set_reg("%d_id" % index, "")
                set_reg("%d_pwd" % index, "")
                self.accountText[index].SetText(twix_work.SAVE_EMPTY)
                self.idEditLine.SetText("")
                self.pwdEditLine.SetText("")
        if index == 1:
            if get_reg("%d_id" % index):
                set_reg("%d_id" % index, "")
                set_reg("%d_pwd" % index, "")
                self.accountText[index].SetText(twix_work.SAVE_EMPTY)
                self.idEditLine.SetText("")
                self.pwdEditLine.SetText("")
        if index == 2:
            if get_reg("%d_id" % index):
                set_reg("%d_id" % index, "")
                set_reg("%d_pwd" % index, "")
                self.accountText[index].SetText(twix_work.SAVE_EMPTY)
                self.idEditLine.SetText("")
                self.pwdEditLine.SetText("")
        if index ==3:
            if get_reg("%d_id" % index):
                set_reg("%d_id" % index, "")
                set_reg("%d_pwd" % index, "")
                self.accountText[index].SetText(twix_work.SAVE_EMPTY)
                self.idEditLine.SetText("")
                self.pwdEditLine.SetText("")
            else:
                self.PopupNotifyMessage(twix_work.DELETE_FAIL, self.EmptyFunc)

    def saveAccountFunction(self,index):
        if self.idEditLine.GetText() == "" or self.pwdEditLine.GetText() == "":
            self.PopupNotifyMessage(twix_work.SAVE_FAIL, self.EmptyFunc)
            return

        if index == 0:
            if get_reg("%d_id" % index) == "" or get_reg("%d_id" % index) == None:
                set_reg("%d_id" % index, str(binascii.b2a_base64(self.idEditLine.GetText())))
                set_reg("%d_pwd" % index, str(binascii.b2a_base64(self.pwdEditLine.GetText())))
                self.accountText[index].SetText(self.idEditLine.GetText())
                self.PopupNotifyMessage(twix_work.SAVE_SUCCES, self.EmptyFunc)
                # break
        if index == 1:
            if get_reg("%d_id" % index) == "" or get_reg("%d_id" % index) == None:
                set_reg("%d_id" % index, str(binascii.b2a_base64(self.idEditLine.GetText())))
                set_reg("%d_pwd" % index, str(binascii.b2a_base64(self.pwdEditLine.GetText())))
                self.accountText[index].SetText(self.idEditLine.GetText())
                self.PopupNotifyMessage(twix_work.SAVE_SUCCES, self.EmptyFunc)
                # break
        if index == 2:
            if get_reg("%d_id" % index) == "" or get_reg("%d_id" % index) == None:
                set_reg("%d_id" % index, str(binascii.b2a_base64(self.idEditLine.GetText())))
                set_reg("%d_pwd" % index, str(binascii.b2a_base64(self.pwdEditLine.GetText())))
                self.accountText[index].SetText(self.idEditLine.GetText())
                self.PopupNotifyMessage(twix_work.SAVE_SUCCES, self.EmptyFunc)
                # break
        if index == 3:
            if get_reg("%d_id" % index) == "" or get_reg("%d_id" % index) == None:
                set_reg("%d_id" % index, str(binascii.b2a_base64(self.idEditLine.GetText())))
                set_reg("%d_pwd" % index, str(binascii.b2a_base64(self.pwdEditLine.GetText())))
                self.accountText[index].SetText(self.idEditLine.GetText())
                self.PopupNotifyMessage(twix_work.SAVE_SUCCES, self.EmptyFunc)
            # break

    def pressKey(self):
        onPressKeyDict = {}

        onPressKeyDict[app.DIK_F1]	= lambda : self.autoLogin(0)
        onPressKeyDict[app.DIK_F2]	= lambda : self.autoLogin(1)
        onPressKeyDict[app.DIK_F3]	= lambda : self.autoLogin(2)
        onPressKeyDict[app.DIK_F4]	= lambda : self.autoLogin(3)

        self.onPressKeyDict = onPressKeyDict

    def OnKeyDown(self, key):
        try:
            self.onPressKeyDict[key]()
        except KeyError:
            pass
        except:
            raise

        return True

    def autoLogin(self,index):
        if index == 0:
            if get_reg("%d_id" % index):
                self.idEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_id" % index)))
                self.pwdEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_pwd" % index)))
                self.pwdEditLine.SetPlaceHolderText("***********************")
                self.__OnClickLoginButton()
        elif index == 1:
            if get_reg("%d_id" % index):
                self.idEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_id" % index)))
                self.pwdEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_pwd" % index)))
                self.pwdEditLine.SetPlaceHolderText("***********************")
                self.__OnClickLoginButton()
        elif index == 2:
            if get_reg("%d_id" % index):
                self.idEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_id" % index)))
                self.pwdEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_pwd" % index)))
                self.pwdEditLine.SetPlaceHolderText("***********************")
                self.__OnClickLoginButton()
        elif index == 3:
            if get_reg("%d_id" % index):
                self.idEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_id" % index)))
                self.pwdEditLine.SetText("%s" % binascii.a2b_base64("%s" % get_reg("%d_pwd" % index)))
                self.pwdEditLine.SetPlaceHolderText("***********************")
                self.__OnClickLoginButton()
            # elif used == 1:
            #     used = 0
            #     self.PopupNotifyMessage("TEST ALREADY YOU MAKE THIS", self)

    def descritonOverButtons(self):
        if self.saveButton[0].IsIn() ^ self.saveButton[1].IsIn() ^ self.saveButton[2].IsIn() ^ self.saveButton[3].IsIn():
            self.toolTipSaveButton.ClearToolTip()
            self.toolTipSaveButton.AutoAppendTextLine(twix_work.SAVE_BUTTON, twix_work.COLOR_NORMAL)
            self.toolTipSaveButton.AlignHorizonalCenter()
            self.toolTipSaveButton.ShowToolTip()
        elif self.deleteButton[0].IsIn() ^ self.deleteButton[1].IsIn() ^ self.deleteButton[2].IsIn() ^ self.deleteButton[3].IsIn():
            self.toolTipSaveButton.ClearToolTip()
            self.toolTipSaveButton.AutoAppendTextLine(twix_work.DELETE_BUTTON, twix_work.COLOR_NORMAL)
            self.toolTipSaveButton.AlignHorizonalCenter()
            self.toolTipSaveButton.ShowToolTip()
        elif self.keys[0].IsIn() ^ self.keys[1].IsIn() ^ self.keys[2].IsIn() ^ self.keys[3].IsIn():
            self.toolTipSaveButton.ClearToolTip()
            self.toolTipSaveButton.AutoAppendTextLine(twix_work.PRESS_KEY, twix_work.COLOR_NORMAL)
            self.toolTipSaveButton.AlignHorizonalCenter()
            self.toolTipSaveButton.ShowToolTip()
        else:
            self.toolTipSaveButton.HideToolTip()
