Search:
#include "DragonSoul.h"

Add it under:
#include "../../common/service.h"
#include "safebox.h"

https://puu.sh/sgGBl/460a45d773.png

---

Search:
	sys_log(0, "sizeof(TShopTable) = %d", sizeof(TShopTable));

Add it under:
#ifdef __OFFLINE_SHOP__
	sys_log(0, "sizeof(TOfflineShopTable) = %d", sizeof(TOfflineShopTable));
#endif

---

Search:
	/*
	 * SHOP
	 */

	if (decode_2bytes(data) != sizeof(TShopTable))
	{
		sys_err("shop table size error");
		thecore_shutdown();
		return;
	}
	data += 2;

	size = decode_2bytes(data);
	data += 2;
	sys_log(0, "BOOT: SHOP: %d", size);


	if (size)
	{
		if (!CShopManager::instance().Initialize((TShopTable *) data, size))
		{
			sys_err("shop table Initialize error");
			thecore_shutdown();
			return;
		}
		data += size * sizeof(TShopTable);
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	/*
	* OFFLINE SHOP
	*/

	if (decode_2bytes(data) != sizeof(TOfflineShopTable))
	{
		sys_err("offline shop table size error");
		thecore_shutdown();
		return;
	}
	data += 2;

	size = decode_2bytes(data);
	data += 2;
	sys_log(0, "BOOT: OFFLINE SHOP: %d", size);

	const char* c_szOfflineShopData = data;
	WORD wOfflineShopSize = 0;
	if (size)
	{
		wOfflineShopSize = size;
		data += size * sizeof(TOfflineShopTable);
	}
#endif

https://puu.sh/sgGEF/17b372efce.png
https://puu.sh/sgGEk/ec253beac7.png

---

Search:
	sys_log(0, "LoadLocaleFile: DragonSoulTable: %s", szDragonSoulTableFileName);
	if (!DSManager::instance().ReadDragonSoulTableFile(szDragonSoulTableFileName))
	{
		sys_err("cannot load DragonSoulTable: %s", szDragonSoulTableFileName);
		//thecore_shutdown();
		//return;
	}

	// END_OF_LOCALE_SERVICE

Add it under:
#ifdef __OFFLINE_SHOP__
	if (!CShopManager::instance().Initialize((TOfflineShopTable *)c_szOfflineShopData, wOfflineShopSize))
	{
		sys_err("offline shop table Initialize error");
		thecore_shutdown();
		return;
	}
#endif

https://puu.sh/sgGGs/c4ee6f223a.png

---

Search:
void CInputDB::MallLoad(LPDESC d, const char * c_pData)
{
	if (!d)
		return;

	TSafeboxTable * p = (TSafeboxTable *) c_pData;

	if (d->GetAccountTable().id != p->dwID)
	{
		sys_err("safebox has different id %u != %u", d->GetAccountTable().id, p->dwID);
		return;
	}

	if (!d->GetCharacter())
		return;

	d->GetCharacter()->LoadMall(p->wItemCount, (TPlayerItem *) (c_pData + sizeof(TSafeboxTable)));
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CInputDB::CollectOfflineShopItem(LPDESC d, const char * c_pData)
{
	if (!d || !d->GetCharacter())
		return;

	LPCHARACTER ch = d->GetCharacter();

	BYTE count = *(BYTE*)c_pData;
	for (int i = 0; i < count; ++i)
	{
		TPlayerItem* pItems = ((TPlayerItem*)(c_pData + 1)) + i;

		LPITEM item = NULL;
		if ((item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id)) == NULL)
		{
			sys_err("CollectOfflineShopItem from %s item[%u] cannot create", ch->GetName(), pItems->id);
			continue;
		}

		int iEmptyCell = ch->GetEmptyInventory(item->GetSize());
		if (iEmptyCell == -1)
		{
			item->SetSkipSave(true);
			M2_DESTROY_ITEM(item);
			sys_log(1, "CollectOfflineShopItem from %s item[%u] full inv", ch->GetName(), pItems->id);
			break;
		}

		item->SetSockets(pItems->alSockets);
		item->SetAttributes(pItems->aAttr);

		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyCell));
		ITEM_MANAGER::instance().FlushDelayedSave(item);

		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¾ÆÀÌÅÛ È¹µæ: %s"), item->GetName());
	}
}
#endif

https://puu.sh/sgGIP/63e367669f.png
---

Search:
	case HEADER_DG_MALL_LOAD:
		MallLoad(DESC_MANAGER::instance().FindByHandle(m_dwHandle), c_pData);
		break;

Add it under:
#ifdef __OFFLINE_SHOP__
	case HEADER_DG_COLLECT_OFFLINE_SHOP_ITEM:
		CollectOfflineShopItem(DESC_MANAGER::instance().FindByHandle(m_dwHandle), c_pData);
		break;
#endif

https://puu.sh/sgGK9/0efdc42a98.png
---

Search:
	case HEADER_DG_RESPOND_CHANNELSTATUS:
		RespondChannelStatus(DESC_MANAGER::instance().FindByHandle(m_dwHandle), c_pData);
		break;

Add it under:
#ifdef __OFFLINE_SHOP__
	case HEADER_DG_SAFEBOX_MONEY:
		SafeboxMoney((TSafeboxMoney*)c_pData);
		break;
#endif

https://puu.sh/sgGLh/5216c06530.png

---

Search:

void CInputDB::RespondChannelStatus(LPDESC desc, const char* pcData)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
void CInputDB::SafeboxMoney(TSafeboxMoney* pcData)
{
	LPDESC d = DESC_MANAGER::instance().FindByAID(pcData->dwAID);
	if (d == NULL)
		return;

	LPCHARACTER ch = d->GetCharacter();
	if (ch == NULL)
		return;

	CSafebox* sb = ch->GetSafebox();
	if (sb == NULL)
		return;

	sb->SetGold(pcData->llAmount);
}
#endif

https://puu.sh/sgGMZ/43f1087dda.png