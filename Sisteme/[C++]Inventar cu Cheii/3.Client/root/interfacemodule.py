#Find
	def RefreshInventory(self):
		self.wndTaskBar.RefreshQuickSlot()
		self.wndInventory.RefreshItemSlot()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshItemSlot()
			
#Add
	if app.ADD_INVENTORY:
		def SetInventoryPageKilit(self):
			if constInfo.envanter == 2:#3 envanter
				if player.GetEnvanter() == 0:#Hepsi kapali
					self.wndInventory.engelblack.Show()#open
					self.wndInventory.engelblackcl.Hide()
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Show()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Show()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 1:# 1 tane ac�k
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()
					self.wndInventory.engelblack2.Show()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Show()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 2:# 2 tane ac�k
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Show()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 3:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Show()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 4:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Show()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 5:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Show()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 6:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Show()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 7:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Show()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 8:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Show()
					self.wndInventory.engelblack9cl.Hide()
				elif player.GetEnvanter() == 9:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Hide()
				elif player.GetEnvanter() >= 10:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Hide()
			elif constInfo.envanter == 3:
				if player.GetEnvanter() >= 0 and player.GetEnvanter() <= 8:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Show()
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Show()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Show()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 9:#Hepsi kapali
					self.wndInventory.engelblack.Show()#open
					self.wndInventory.engelblackcl.Hide()
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Show()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Show()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 10:# 1 tane ac�k
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()
					self.wndInventory.engelblack2.Show()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Show()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 11:# 2 tane ac�k
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Show()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()
					self.wndInventory.engelblack4cl.Show()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 12:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Show()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Show()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 13:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Show()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()
					self.wndInventory.engelblack6cl.Show()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 14:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Show()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Show()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 15:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Show()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Show()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 16:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Show()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Show()
				elif player.GetEnvanter() == 17:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Show()
					self.wndInventory.engelblack9cl.Hide()
				elif player.GetEnvanter() == 18:
					self.wndInventory.engelblack.Hide()#open
					self.wndInventory.engelblackcl.Hide()#open
					self.wndInventory.engelblack2.Hide()
					self.wndInventory.engelblack2cl.Hide()#close
					self.wndInventory.engelblack3.Hide()
					self.wndInventory.engelblack3cl.Hide()
					self.wndInventory.engelblack4.Hide()###
					self.wndInventory.engelblack4cl.Hide()
					self.wndInventory.engelblack5.Hide()
					self.wndInventory.engelblack5cl.Hide()
					self.wndInventory.engelblack6.Hide()#open
					self.wndInventory.engelblack6cl.Hide()
					self.wndInventory.engelblack7.Hide()
					self.wndInventory.engelblack7cl.Hide()
					self.wndInventory.engelblack8.Hide()
					self.wndInventory.engelblack8cl.Hide()
					self.wndInventory.engelblack9.Hide()
					self.wndInventory.engelblack9cl.Hide()
			else:
				self.wndInventory.engelblack.Hide()
				self.wndInventory.engelblackcl.Hide()
				self.wndInventory.engelblack2.Hide()
				self.wndInventory.engelblack2cl.Hide()
				self.wndInventory.engelblack3.Hide()
				self.wndInventory.engelblack3cl.Hide()
				self.wndInventory.engelblack4.Hide()
				self.wndInventory.engelblack4cl.Hide()
				self.wndInventory.engelblack5.Hide()
				self.wndInventory.engelblack5cl.Hide()
				self.wndInventory.engelblack6.Hide()
				self.wndInventory.engelblack6cl.Hide()
				self.wndInventory.engelblack7.Hide()
				self.wndInventory.engelblack7cl.Hide()
				self.wndInventory.engelblack8.Hide()
				self.wndInventory.engelblack8cl.Hide()
				self.wndInventory.engelblack9.Hide()
				self.wndInventory.engelblack9cl.Hide()
			self.wndInventory.RefreshBagSlotWindow()