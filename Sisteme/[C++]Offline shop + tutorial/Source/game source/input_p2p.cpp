Arat ;
#include "threeway_war.h"

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
#include "offlineshop_manager.h"
#endif
#include "sectree_manager.h"





Arat ;
void CInputP2P::IamAwake(LPDESC d, const char * c_pData)
{
	std::string hostNames;
	P2P_MANAGER::instance().GetP2PHostNames(hostNames);
	sys_log(0, "P2P Awakeness check from %s. My P2P connection number is %d. and details...\n%s", d->GetHostName(), P2P_MANAGER::instance().GetDescCount(), hostNames.c_str());
}

Altına Ekle ;
struct FFindOfflineShop
{
	const char * szName;
	
	FFindOfflineShop(const char * c_szName) : szName(c_szName) {};
	
	void operator()(LPENTITY ent)
	{
		if (!ent)
			return;
		
		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER)ent;
			if (ch->IsOfflineShopNPC() && !strcmp(szName, ch->GetName()))			
				ch->DestroyOfflineShop();			
		}
	}
};

struct FChangeOfflineShopTime
{
	int iTime;
	DWORD dwOwnerPID;
	
	FChangeOfflineShopTime(int time, DWORD dwOwner) : iTime(time), dwOwnerPID(dwOwner) {};
	
	void operator()(LPENTITY ent)
	{
		if (!ent)
			return;
		
		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER)ent;
			if (ch->IsOfflineShopNPC() && ch->GetOfflineShopRealOwner() == dwOwnerPID)
			{
				DBManager::instance().DirectQuery("UPDATE %soffline_shop_npc SET time = %d WHERE owner_id = %u", get_table_postfix(), iTime, dwOwnerPID);
				ch->StopOfflineShopUpdateEvent();
				ch->SetOfflineShopTimer(iTime);
				ch->StartOfflineShopUpdateEvent();			
			}
		}
	}
};

void CInputP2P::RemoveOfflineShop(LPDESC d, const char * c_pData)
{
	TPacketGGRemoveOfflineShop * p = (TPacketGGRemoveOfflineShop *)c_pData;
	LPSECTREE_MAP pMap = SECTREE_MANAGER::instance().GetMap(p->lMapIndex);
	
	if (pMap)
	{
		FFindOfflineShop offlineshop(p->szNpcName);
		pMap->for_each(offlineshop);
	}
}

void CInputP2P::ChangeOfflineShopTime(LPDESC d, const char * c_pData)
{
	TPacketGGChangeOfflineShopTime * p = (TPacketGGChangeOfflineShopTime *)c_pData;
	
	int iTime;
	switch(p->bTime)
	{
		case 1:
			iTime = 1 * 60 * 60;
			break;
		case 2:
			iTime = 2 * 60 * 60;
			break;
		case 3:
			iTime = 4 * 60 * 60;
			break;
		default:
			iTime = 0;
	}
	
	LPSECTREE_MAP pMap = SECTREE_MANAGER::instance().GetMap(p->lMapIndex);	
	FChangeOfflineShopTime offlineShopTime(iTime, p->dwOwnerPID);
	if (pMap)	
		pMap->for_each(offlineShopTime);
}

void CInputP2P::OfflineShopBuy(LPDESC d, const char * c_pData)
{
	TPacketGGOfflineShopBuy * p = (TPacketGGOfflineShopBuy *)c_pData;
}






Arat ;
		case HEADER_GG_CHECK_AWAKENESS:
			IamAwake(d, c_pData);
			break;

			
Altına Ekle ;
		case HEADER_GG_REMOVE_OFFLINE_SHOP:
			RemoveOfflineShop(d, c_pData);
			break;
			
		case HEADER_GG_CHANGE_OFFLINE_SHOP_TIME:
			ChangeOfflineShopTime(d, c_pData);
			break;
			
			
			
			
			
			