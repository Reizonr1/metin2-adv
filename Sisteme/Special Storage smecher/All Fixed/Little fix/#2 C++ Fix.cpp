
This fix stackeble fix ##



/ BURHANBEY - DRACARYS \

charitem.cpp aç ve cauta

LPITEM CHARACTER::AutoGiveItem(DWORD dwItemVnum, BYTE bCount, int iRarePct, bool bMsg)

bunun gaseste sub

	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)

bunu değiştir

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)

Sandık,quest vs direk item verdiğinizde direk üst üste gelicek

---------------------------------------------------

bunu cauta

LPITEM CHARACTER::FindSpecifyItem(DWORD vnum) const

gaseste sub

	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)

bununla değiştir

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)

----------------------------------------------------------------

bunu cauta

int CHARACTER::CountEmptyInventory() const

gaseste sub

	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)

onu değiştir

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)	

----------------------------------------------------------

bunu cauta

bool CHARACTER::PickupItem(DWORD dwVID)

gaseste sub

	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)

onu değiştir bununla

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)

Bu fonksiyon içerisinde 2 tane flag sorgulaması olduğu için 2 kere aynı işlemi uygulayın.
Yani demek istediğim bu fonsiyonda 2 adet mevcut.

----------------------------------------------------------

LPITEM CHARACTER::FindItemByID(DWORD id) const

sub el cauta
	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)

değiştir

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)

-----------------------------------------------------------

int CHARACTER::CountEmptyInventory() const

altında bunu cauta 

	for (int i = 0; i < INVENTORY_MAX_NUM; ++i)	

değiştir

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)

---------------------------------------------------------
