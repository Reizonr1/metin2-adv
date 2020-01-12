Search:
import wndMgr

Add it under:
import ingamebank

---

Search:
			self.wndMoneySlot = self.GetChild("Money_Slot")

Add it under:
			self.wndBarFirst = self.GetChild("BarFirstText")
			self.wndBarSecond = self.GetChild("BarSecondText")
			self.wndBarThird = self.GetChild("BarThirdText")
			self.wndBarFirstSlot = self.GetChild("Bar_First_Slot")
			self.wndBarSecondSlot = self.GetChild("Bar_Second_Slot")
			self.wndBarThirdSlot = self.GetChild("Bar_Third_Slot")
			self.wndBarFirstIcon = self.GetChild("Bar_First_Icon")
			self.wndBarSecondIcon = self.GetChild("Bar_Second_Icon")
			self.wndBarThirdIcon = self.GetChild("Bar_Third_Icon")

---

Search:
		## AttachMetinDialog
		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()

Add it under:
		self.IngameBankDialog = ingamebank.IngameBank()
		self.IngameBankDialog.Close()


---

Search:
		## MoneySlot
		self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

Add it under:
		self.wndBarFirstIcon.SetEvent(ui.__mem_func__(self.ShowIngameBank))
		self.wndBarSecondIcon.SetEvent(ui.__mem_func__(self.ShowIngameBank))
		self.wndBarThirdIcon.SetEvent(ui.__mem_func__(self.ShowIngameBank))
		self.wndBarFirstSlot.SetEvent(ui.__mem_func__(self.ShowIngameBank))
		self.wndBarSecondSlot.SetEvent(ui.__mem_func__(self.ShowIngameBank))
		self.wndBarThirdSlot.SetEvent(ui.__mem_func__(self.ShowIngameBank))

---

Search:
		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0

Add it under:
		self.IngameBankDialog.Close()
		self.IngameBankDialog = 0

---

Search:
		self.wndMoneySlot = 0

Add it under:
		self.wndBarFirst = 0
		self.wndBarSecond = 0
		self.wndBarThird = 0
		self.wndBarFirstIcon = 0
		self.wndBarSecondIcon = 0
		self.wndBarThirdIcon = 0
		self.wndBarFirstSlot = 0
		self.wndBarSecondSlot = 0
		self.wndBarThirdSlot = 0

---

Search:
	def Close(self):
		self.Hide()

Add it under:
	def ShowIngameBank(self):
		self.IngameBankDialog.OpenWindow()


---

Search:
	def RefreshStatus(self):
		money = player.GetElk()
		self.wndMoney.SetText(localeInfo.NumberToMoneyString(money))

Add it under:
	def RefreshBarAmount(self):
		bar_first, bar_second, bar_third = constInfo.bar_first_amount, constInfo.bar_second_amount, constInfo.bar_third_amount

		self.wndBarFirst.SetText(bar_first)
		self.wndBarSecond.SetText(bar_second)
		self.wndBarThird.SetText(bar_third)

