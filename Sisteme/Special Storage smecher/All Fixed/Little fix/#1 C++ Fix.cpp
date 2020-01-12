Here is the fix for Sell Items to shop:

po0*game/src/input_main.cpp deschide si cauta

if (uiBytes < sizeof(UINT) + sizeof(BYTE))

schimba

if (uiBytes < sizeof(BYTE) + sizeof(BYTE))


vczewqÆb       cauta

UINT pos = *reinterpret_cast<const UINT*>(c_pData++);

schimba
BYTE pos = *(c_pData++);

 
cauta

CShopManager::instance().Sell(ch, pos, count);
return sizeof(UINT) + sizeof(BYTE);

schimba
CShopManager::instance().Sell(ch, pos, count);
return sizeof(BYTE) + sizeof(BYTE);


cauta

ch->SyncQuickslot(QUICKSLOT_TYPE_ITEM, p->ItemPos.cell, 1000);


schimba
ch->SyncQuickslot(QUICKSLOT_TYPE_ITEM, p->ItemPos.cell, 255);



game/src/shop.cpp deschide si cauta

m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 1000);

schimba

m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);


game/src/shop_manager.cpp deschide si cauta


void CShopManager::Sell(LPCHARACTER ch, UINT bCell, BYTE bCount)


schimba
void CShopManager::Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount)

game/src/shop_manager.h deschide si cauta


void    Sell(LPCHARACTER ch, UINT bCell, BYTE bCount = 0);


schimba

void    Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount=0);


Client/UserInterface/PythonNetworkStream.h deschide si cauta

bool SendShopSellPacketNew(UINT bySlot, BYTE byCount);


schimba
bool SendShopSellPacketNew(BYTE bySlot, BYTE byCount);


Client/UserInterface/PythonNetworkStreamPhaseGame.cpp deschide si cauta


bool CPythonNetworkStream::SendShopSellPacketNew(UINT bySlot, BYTE byCount)


schimba
bool CPythonNetworkStream::SendShopSellPacketNew(BYTE bySlot, BYTE byCount)