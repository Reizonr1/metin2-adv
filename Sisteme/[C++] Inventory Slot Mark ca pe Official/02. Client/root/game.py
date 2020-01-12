# 1.1 Search this:
# ********************************* BEGIN ********************************* #
	## BINARY CALLBACK
	######################################################################################
# ********************************** END ********************************** #

# 1.2 Add this below:
# ********************************* BEGIN ********************************* #
	# EXCHANGE
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BINARY_AddItemToExchange(self, inven_type, inven_pos, display_pos):
			if inven_type == player.INVENTORY:
				self.interface.CantTradableItemExchange(display_pos, inven_pos)
	# END_OF_EXCHANGE
# ********************************** END ********************************** #




