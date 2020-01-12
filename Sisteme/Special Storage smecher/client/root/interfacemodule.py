Cauta ----------

self.wndInventory = None

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			self.wndExtendedInventory = None

Cauta ----------

wndInventory.BindInterfaceClass(self)

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			wndExtendedInventory = uiInventory.ExtendedInventoryWindow()
			wndExtendedInventory.BindInterfaceClass(self)

Cauta ----------

self.wndInventory = wndInventory

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			self.wndExtendedInventory = wndExtendedInventory

Cauta ----------

self.wndInventory.SetItemToolTip(self.tooltipItem)

Adauga sub ----------,

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			self.wndExtendedInventory.SetItemToolTip(self.tooltipItem)

Cauta ----------

if self.wndInventory:
			self.wndInventory.Destroy()

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			if self.wndExtendedInventory:
				self.wndExtendedInventory.Destroy()

Cauta ----------

del self.wndInventory

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			if self.wndExtendedInventory:
				del self.wndExtendedInventory

Cauta ----------

self.wndInventory.RefreshStatus()

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			self.wndExtendedInventory.RefreshStatus()

Cauta ----------

self.wndInventory.RefreshItemSlot()

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			self.wndExtendedInventory.RefreshItemSlot()

Cauta ----------

if self.wndInventory:
			self.wndInventory.Hide()

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			if self.wndExtendedInventory:
				self.wndExtendedInventory.Hide()	

Cauta ----------

def ToggleExpandedButton(self):

üstüne EKLENÝR ----------

	if app.WJ_SPLIT_INVENTORY_SYSTEM:
		def ToggleExtendedInventoryWindow(self):
			if app.WJ_SECURITY_SYSTEM and player.IsSecurityActivate():
				return		
			if FALSE == player.IsObserverMode():
				if self.wndExtendedInventory.IsShow():
					self.wndExtendedInventory.OverOutItem()
					self.wndExtendedInventory.Close()
				else:
					self.wndExtendedInventory.Show()

Cauta ----------

if app.ENABLE_DRAGON_SOUL_SYSTEM:
			hideWindows += self.wndDragonSoul,\
						self.wndDragonSoulRefine,

Adauga sub ----------

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			if self.wndExtendedInventory:
				hideWindows += self.wndExtendedInventory,