Cauta --------

onPressKeyDict[app.DIK_F]			= lambda : self.__PressFKey()

Adauga sub -----

if app.WJ_SPLIT_INVENTORY_SYSTEM:
			onPressKeyDict[app.DIK_K]		= lambda : self.__PressExtendedInventory()

Cauta --------

self.onClickKeyDict=onClickKeyDict

Adauga sub -----

	if app.WJ_SPLIT_INVENTORY_SYSTEM:
		def __PressExtendedInventory(self):
			if self.interface:
				self.interface.ToggleExtendedInventoryWindow()

Cauta ----

def __PutItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, dstChrID):

ALTINDAK� -  if player.SLOT_TYPE_INVENTORY == attachedType  KOMPLE DE���T�R�L�R..

if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedType or player.SLOT_TYPE_STONE_INVENTORY == attachedType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedType:

Cauta --------

dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

Cauta --------

�ST�NDEK� EKLEN�R -----  if player.SLOT_TYPE_INVENTORY == attachedType or  DE���T�R

DE���T�R

if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedType or player.SLOT_TYPE_STONE_INVENTORY == attachedType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedType:

Cauta -------- if dropNumber == player.ITEM_MONEY:  �ST�NDEK�  if player.SLOT_TYPE_INVENTORY == dropType or

KOMPLE DE���T�R.-************

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType:

Cauta --------

def RequestDestroyItem(self, answer):

ALTINDAK�  if player.SLOT_TYPE_INVENTORY == dropType or  KOD SATIRINI KOMPLE DE���T�R

DE���T�R  -----

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType:


Cauta --------

def RequestSellItem(self, answer):   ALTINDAK�  if player.SLOT_TYPE_INVENTORY == dropType or  KOMPLE DE���T�R

DE���T�R ---------

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType: