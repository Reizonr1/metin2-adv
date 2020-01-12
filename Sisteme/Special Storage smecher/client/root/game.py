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

ALTINDAKÝ -  if player.SLOT_TYPE_INVENTORY == attachedType  KOMPLE DEÐÝÞTÝRÝLÝR..

if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedType or player.SLOT_TYPE_STONE_INVENTORY == attachedType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedType:

Cauta --------

dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

Cauta --------

ÜSTÜNDEKÝ EKLENÝR -----  if player.SLOT_TYPE_INVENTORY == attachedType or  DEÐÝÞTÝR

DEÐÝÞTÝR

if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedType or player.SLOT_TYPE_STONE_INVENTORY == attachedType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedType:

Cauta -------- if dropNumber == player.ITEM_MONEY:  ÜSTÜNDEKÝ  if player.SLOT_TYPE_INVENTORY == dropType or

KOMPLE DEÐÝÞTÝR.-************

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType:

Cauta --------

def RequestDestroyItem(self, answer):

ALTINDAKÝ  if player.SLOT_TYPE_INVENTORY == dropType or  KOD SATIRINI KOMPLE DEÐÝÞTÝR

DEÐÝÞTÝR  -----

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType:


Cauta --------

def RequestSellItem(self, answer):   ALTINDAKÝ  if player.SLOT_TYPE_INVENTORY == dropType or  KOMPLE DEÐÝÞTÝR

DEÐÝÞTÝR ---------

if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType or player.SLOT_TYPE_STONE_INVENTORY == dropType or player.SLOT_TYPE_SANDIK_INVENTORY == dropType: