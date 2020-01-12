Arat ;
#include "DragonSoul.h"

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
#include "offline_shop.h"
#include "offlineshop_manager.h"
#include "offlineshop_config.h"
#endif

extern bool offlineshop_map_allow_find(int mapIndex);





Arat ;
	m_pkPartyRequestEvent = NULL;

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	// Offline Shop
	m_pkOfflineShop = NULL;
	m_pkChrOfflineShopOwner = NULL;
	m_pkOfflineShopUpdateEvent = NULL;
	// End Of Offline Shop
#endif







Arat ;
	if (GetMyShop())
	{
		TPacketGCShopSign p;

		p.bHeader = HEADER_GC_SHOP_SIGN;
		p.dwVID = GetVID();
		strlcpy(p.szSign, m_stShopSign.c_str(), sizeof(p.szSign));

		d->Packet(&p, sizeof(TPacketGCShopSign));
	}
	
Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	if (IsOfflineShopNPC() && GetRaceNum() == 30000)
	{
		TPacketGCShopSign p;

		p.bHeader = HEADER_GC_OFFLINE_SHOP_SIGN;
		p.dwVID = GetVID();
		if (m_stOfflineShopSign.empty())
		{
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT sign FROM player.offline_shop_npc WHERE owner_id = %u", GetOfflineShopRealOwner()));
			if (pMsg->Get()->uiNumRows > 0)
			{				
				MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
				strlcpy(p.szSign, row[0], sizeof(p.szSign));				
			}
		}
		else
		{
			strlcpy(p.szSign, m_stOfflineShopSign.c_str(), sizeof(p.szSign));
		}
		
		d->Packet(&p, sizeof(TPacketGCShopSign));
	}
#endif






Arat ;
void CHARACTER::Disconnect(const char * c_pszReason)
{
	assert(GetDesc() != NULL);

	sys_log(0, "DISCONNECT: %s (%s)", GetName(), c_pszReason ? c_pszReason : "unset" );

	if (GetShop())
	{
		GetShop()->RemoveGuest(this);
		SetShop(NULL);
	}
	
Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	if (GetOfflineShop())
	{
		GetOfflineShop()->RemoveGuest(this);
		SetOfflineShop(NULL);
	}
#endif







Arat ;
	// MINING
	if (mining::IsVeinOfOre (GetRaceNum()))
	{
		char_event_info* info = AllocEventInfo<char_event_info>();

		info->ch = this;

		m_pkMiningEvent = event_create(kill_ore_load_event, info, PASSES_PER_SEC(number(7 * 60, 15 * 60)));
	}
	// END_OF_MINING
	
	
Altına Ekle ;
	SetOfflineShopVID(COfflineShopManager::instance().FindMyOfflineShop(GetPlayerID()));

	
	
	
	
	
Arat ;
void CHARACTER::SetShop(LPSHOP pkShop)
{
	if ((m_pkShop = pkShop))
		SET_BIT(m_pointsInstant.instant_flag, INSTANT_FLAG_SHOP);
	else
	{
		REMOVE_BIT(m_pointsInstant.instant_flag, INSTANT_FLAG_SHOP); 
		SetShopOwner(NULL);
	}
}


Altına Ekle ;
void CHARACTER::SetOfflineShop(LPOFFLINESHOP pkOfflineShop)
{
	if ((m_pkOfflineShop = pkOfflineShop))
		SET_BIT(m_pointsInstant.instant_flag, INSTANT_FLAG_OFFLINE_SHOP);
	else
	{
		REMOVE_BIT(m_pointsInstant.instant_flag, INSTANT_FLAG_OFFLINE_SHOP);
		SetOfflineShopOwner(NULL);
	}
}


void CHARACTER::OpenMyOfflineShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount, BYTE bTime)
{
	quest::PC * pPC = quest::CQuestManager::Instance().GetPC(GetPlayerID());

	if (pPC->IsRunning())
		return;

	if (bItemCount == 0)
		return;

	if (GetShop() || GetOfflineShop())
		return;

	// Brazil is not use for this option.
	if (!LC_IsBrazil())
	{
		DWORD nTotalMoney = 0;
		for (BYTE n = 0; n < bItemCount; ++n)
			nTotalMoney += (pTable + n)->price;

		if (GOLD_MAX - 1 <= nTotalMoney)
		{
			sys_err("[OVERFLOW_GOLD] Overflow (GOLD_MAX) id %u name %s", GetPlayerID(), GetName());
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("20¾ï ³ÉÀ» ÃÊ°úÇÏ¿© »óÁ¡À» ¿­¼ö°¡ ¾ø½À´Ï´Ù"));
			return;
		}
	}
	// Check if player has current items in database.
	{
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM %soffline_shop_item WHERE owner_id = %u and status = 1", get_table_postfix(), GetPlayerID()));
		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		
		BYTE bResult = 0;
		str_to_number(bResult, row[0]);
		
		if (bResult)
		{
			ChatPacket(CHAT_TYPE_INFO, "Çevrimdışı mağazayı tekrar açtıktan sonra, ilk önce öğelerinizi alacaksınız.");
			COfflineShopManager::instance().Giveback2(this);
			return;
		}
	}
	// End of check if player has current items in database
	
	// Check player is open offline shop or not
	{
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), GetPlayerID()));
		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		
		BYTE bResult = 0;
		str_to_number(bResult, row[0]);
		
		if (bResult)
		{
			ChatPacket(CHAT_TYPE_INFO, "Zaten çevrimdışı mağazanız var. Tekrar açamazsın !");
			return;
		}
	}
	// End Of check player is open offline shop or not
	
	// Check map allows for Offline Shop
	if (g_bOfflineShopMapAllowLimit)
	{
		if (!offlineshop_map_allow_find(GetMapIndex()))
		{
			ChatPacket(CHAT_TYPE_INFO, "Bu yerde çevrimdışı mağazayı açamazsınız !");
			return;
		}
	}
	// End Of Check map allows for offline shop

	// Need Item For Offline Shop
	if (g_bNeedItem)
	{
		BYTE bCount = quest::CQuestManager::instance().GetCurrentCharacterPtr()->CountSpecifyItem(g_iItemVnum);
		if (bCount < g_bItemCount)
		{
			LPITEM item = ITEM_MANAGER::instance().CreateItem(g_iItemVnum);
			ChatPacket(CHAT_TYPE_INFO, "Şu anda çevrimdışı mağazayı açamazsınız. %d Adet %s gerekiyor", g_bItemCount, item->GetName());
			return;
		}
	}
	// End Of Need Item For Offline Shop

	// Need Money For Offline Shop
	if (g_bNeedMoney)
	{
		if (GetGold() < static_cast<int>(g_dwNeedMoney))
		{
			ChatPacket(CHAT_TYPE_INFO, "Paranız açık çevrimdışı mağazada yetmiyor. Gerekli para: %u", g_dwNeedMoney);
			return;
		}
	}
	// End Of Need Money For Offline Shop
	
	char szSign[SHOP_SIGN_MAX_LEN+1];
	strlcpy(szSign, c_pszSign, sizeof(szSign));

	m_stOfflineShopSign = szSign;

	if (m_stOfflineShopSign.length() == 0)
		return;	
	
	if (CBanwordManager::instance().CheckString(m_stShopSign.c_str(), m_stShopSign.length()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ºñ¼Ó¾î³ª Àº¾î°¡ Æ÷ÇÔµÈ »óÁ¡ ÀÌ¸§À¸·Î »óÁ¡À» ¿­ ¼ö ¾ø½À´Ï´Ù."));
		return;
	}
	
	LPCHARACTER npc = CHARACTER_MANAGER::instance().SpawnMob(30000, GetMapIndex(), GetX(), GetY(), GetZ(), false, -1, false, true, GetPlayerID());
	
	if (!npc)
	{
		ChatPacket(CHAT_TYPE_INFO, "Çevrimdışı shop npc oluşturulamıyor! Lütfen tekrar deneyin.");
		return;
	}
	
	std::map<DWORD, DWORD> itemkind;
	std::set<TItemPos> cont;

	for (BYTE i = 0; i < bItemCount; ++i)
	{
		if (cont.find((pTable + i)->pos) != cont.end())
		{
			sys_err("MY_OFFLINE_SHOP: duplicate shop item detected! (name: %s)", GetName());
			return;
		}

		// ANTI_GIVE, ANTI_MYSHOP check
		LPITEM pkItem = GetItem((pTable + i)->pos);

		if (pkItem)
		{
			const TItemTable * item_table = pkItem->GetProto();

			if (item_table && (IS_SET(item_table->dwAntiFlags, ITEM_ANTIFLAG_GIVE | ITEM_ANTIFLAG_MY_OFFLINE_SHOP)))
			{
				ChatPacket(CHAT_TYPE_INFO, "Bu item satılamaz.");
				return;
			}

			if (pkItem->IsEquipped() == true)
			{
				return;
			}

			if (true == pkItem->isLocked())
			{
				ChatPacket(CHAT_TYPE_INFO, "Kilitli item satılamaz.");
				return;
			}

			itemkind[pkItem->GetVnum()] = (pTable + i)->price / pkItem->GetCount();

			char szColumns[QUERY_MAX_LEN], szValues[QUERY_MAX_LEN];

			int iLen = snprintf(szColumns, sizeof(szColumns), "id,owner_id,pos,count,price,vnum");
			int iUpdateLen = snprintf(szValues, sizeof(szValues), "%u,%u,%d,%u,%u,%u", pkItem->GetID(), GetPlayerID(), (pTable + i)->display_pos, pkItem->GetCount(), (pTable + i)->price, pkItem->GetVnum());

			iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",socket0,socket1,socket2");
			iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%ld,%ld,%ld", pkItem->GetSocket(0), pkItem->GetSocket(1), pkItem->GetSocket(2));

			iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4");
			iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",
				pkItem->GetAttributeType(0), pkItem->GetAttributeValue(0),
				pkItem->GetAttributeType(1), pkItem->GetAttributeValue(1),
				pkItem->GetAttributeType(2), pkItem->GetAttributeValue(2),
				pkItem->GetAttributeType(3), pkItem->GetAttributeValue(3),
				pkItem->GetAttributeType(4), pkItem->GetAttributeValue(4));

			char szInsertQuery[QUERY_MAX_LEN];
			snprintf(szInsertQuery, sizeof(szInsertQuery), "INSERT INTO %soffline_shop_item (%s) VALUES (%s)", get_table_postfix(), szColumns, szValues);
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szInsertQuery));
			pkItem->RemoveFromCharacter();
		}

		cont.insert((pTable + i)->pos);
	}

	// Time Mechanism
	int iTime = 0;
	switch (bTime)
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
	}
	
	// If bTime is not equal to unlimited time, start the time!
	if (bTime != 4)
	{
		npc->SetOfflineShopTimer(iTime);
		npc->StartOfflineShopUpdateEvent();
	}
	
	// Insert
	char szQuery2[512];
	snprintf(szQuery2, sizeof(szQuery2), "INSERT INTO %soffline_shop_npc(owner_id, sign, name, time, x, y, z, mapIndex, channel) VALUES(%u, '%s', '%s', %d, %ld, %ld, %ld, %ld, %d)", get_table_postfix(), GetPlayerID(), c_pszSign, GetName(), iTime, GetX(), GetY(), GetZ(), GetMapIndex(), g_bChannel);
	DBManager::Instance().DirectQuery(szQuery2);
	
	// Create Offline Shop
	LPOFFLINESHOP pkOfflineShop = COfflineShopManager::instance().CreateOfflineShop(npc, GetPlayerID());
	
	if (!pkOfflineShop)
	{
		ChatPacket(CHAT_TYPE_INFO, "Offline shop npc oluşturulamıyor. Lütfen tekrar deneyin.");
		return;
	}
	
	npc->SetOfflineShop(pkOfflineShop);
	npc->SetOfflineShopChannel(g_bChannel);
	// End Of Create Offline Shop
	
	// Set Name
	char szName[CHARACTER_NAME_MAX_LEN + 1];
	snprintf(szName, sizeof(szName), "[Lv.%d] %s", GetName());
	npc->SetName(szName);
	// End Of Set Name
	
	SetOfflineShopVID(npc->GetVID());
	npc->Show(GetMapIndex(), GetX(), GetY(), GetZ(), true);
	
	// Send Offline Shop Sign to Everyone
	TPacketGCShopSign p;
	p.bHeader = HEADER_GC_OFFLINE_SHOP_SIGN;
	p.dwVID = npc->GetVID();
	strlcpy(p.szSign, c_pszSign, sizeof(p.szSign));
	
	PacketAround(&p, sizeof(TPacketGCShopSign));
	// End Of Send Offline Shop Sign to Everyone
	
	if (bTime != 4)
		ChatPacket(CHAT_TYPE_INFO, "Çevrimdışı mağazanın süresi %d saat sonra doldu.", bTime);
	else
		ChatPacket(CHAT_TYPE_INFO, "Çevrimdışı mağazanızın zamanı sınırsız olarak yapılandırılmıştır!");

	if (g_bNeedItem)
	{
		LPITEM item = FindSpecifyItem(g_iItemVnum);
		if (!item)
		{
			ChatPacket(CHAT_TYPE_INFO, "Güç kaynağı! Bir şeyler ters gidiyor !");
			return;
		}

		if (item->IsStackable())
			if (item->GetCount() == g_bItemCount)
				ITEM_MANAGER::instance().RemoveItem(item);
			else
				item->SetCount(item->GetCount() - g_bItemCount);
		else
			ITEM_MANAGER::instance().RemoveItem(item);
	}

	if (g_bNeedMoney)
		PointChange(POINT_GOLD, -g_dwNeedMoney, false);
}


EVENTFUNC(offline_shop_update_event)
{
	char_event_info* pInfo = dynamic_cast<char_event_info*>(event->info);

	if (pInfo == NULL)
	{
		sys_err("offline_shop_update_event> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER npc = pInfo->ch;

	if (npc == NULL)
		return 0;
	
	int remain_time = npc->GetOfflineShopTimer() - processing_time / passes_per_sec;
	if (remain_time <= 0)
	{
		sys_log(0, "OFFLINE SHOP EXPIRED : expired %s", npc->GetName());
		LPCHARACTER pChar = CHARACTER_MANAGER::instance().Find(npc->GetOfflineShopRealOwner());			
		if (pChar)
		{
			pChar->ChatPacket(CHAT_TYPE_INFO, "Çevrimdışı mağazanızın süresi bitti .İtemler size tekrar verecektir.");			
			COfflineShopManager::instance().Giveback(pChar);
		}	
		COfflineShopManager::instance().DestroyOfflineShop(NULL, npc->GetVID());
		DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), npc->GetOfflineShopRealOwner());
		M2_DESTROY_CHARACTER(npc);
		return 0;
	}

	// If the variable is reach to maximum, start to save it
	if (npc->GetOfflineShopSaveTime() >= g_bOfflineShopSaveTime)
	{
		DBManager::instance().DirectQuery("UPDATE %soffline_shop_npc SET time = %d WHERE owner_id = %u", get_table_postfix(), npc->GetOfflineShopTimer(), npc->GetOfflineShopRealOwner());
		npc->SetOfflineShopTimer(1);
	}

	npc->SetOfflineShopTimer(remain_time);
	npc->SetOfflineShopSaveTime(npc->GetOfflineShopSaveTime() + 1);
	return PASSES_PER_SEC(MIN(60, remain_time));
}

void CHARACTER::StartOfflineShopUpdateEvent()
{
	if (m_pkOfflineShopUpdateEvent)
		return;

	if (IsPC() || IsMonster())
		return;

	char_event_info * pInfo = AllocEventInfo<char_event_info>();
	pInfo->ch = this;
	m_pkOfflineShopUpdateEvent = event_create(offline_shop_update_event, pInfo, PASSES_PER_SEC(60));
}


void CHARACTER::StopOfflineShopUpdateEvent()
{
	m_pointsInstant.bSaveTime = 0;
	m_pointsInstant.leftTime = 0;
	event_cancel(&m_pkOfflineShopUpdateEvent);
}



Arat ;
	if (IsPC())
	{
		// Å¸°ÙÀ¸·Î ¼³Á¤µÈ °æ¿ì´Â PC¿¡ ÀÇÇÑ Å¬¸¯µµ Äù½ºÆ®·Î Ã³¸®ÇÏµµ·Ï ÇÕ´Ï´Ù.
		if (!CTargetManager::instance().GetTargetInfo(pkChrCauser->GetPlayerID(), TARGET_TYPE_VID, GetVID()))
		{
			// 2005.03.17.myevan.Å¸°ÙÀÌ ¾Æ´Ñ °æ¿ì´Â °³ÀÎ »óÁ¡ Ã³¸® ±â´ÉÀ» ÀÛµ¿½ÃÅ²´Ù.
			if (GetMyShop())
			{
				if (pkChrCauser->IsDead() == true) return;

				//PREVENT_TRADE_WINDOW
				if (pkChrCauser == this) // ÀÚ±â´Â °¡´É
				{
					if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen())
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Áß(Ã¢°í,±³È¯,»óÁ¡)¿¡´Â °³ÀÎ»óÁ¡À» »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
						return;
					}
				}
				else // ´Ù¸¥ »ç¶÷ÀÌ Å¬¸¯ÇßÀ»¶§
				{
					// Å¬¸¯ÇÑ »ç¶÷ÀÌ ±³È¯/Ã¢°í/°³ÀÎ»óÁ¡/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
					if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen() )
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Áß(Ã¢°í,±³È¯,»óÁ¡)¿¡´Â °³ÀÎ»óÁ¡À» »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
						return;
					}

					// Å¬¸¯ÇÑ ´ë»óÀÌ ±³È¯/Ã¢°í/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
					//if ((GetExchange() || IsOpenSafebox() || GetShopOwner()))
					if ((GetExchange() || IsOpenSafebox() || IsCubeOpen()))
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡¸¦ ÇÏ°í ÀÖ´Â ÁßÀÔ´Ï´Ù."));
						return;
					}
				}
				//END_PREVENT_TRADE_WINDOW

				if (pkChrCauser->GetShop())
				{
					pkChrCauser->GetShop()->RemoveGuest(pkChrCauser);
					pkChrCauser->SetShop(NULL);
				}

				GetMyShop()->AddGuest(pkChrCauser, GetVID(), false);
				pkChrCauser->SetShopOwner(this);
				return;
			}

			if (test_server)
				sys_err("%s.OnClickFailure(%s) - target is PC", pkChrCauser->GetName(), GetName());

			return;
		}
	}

	// Ã»¼Ò³âÀº Äù½ºÆ® ¸øÇÔ
	if (LC_IsNewCIBN())
	{
		if (pkChrCauser->IsOverTime(OT_3HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 3);
			return;
		}
		else if (pkChrCauser->IsOverTime(OT_5HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 5);
			return;
		}
	}
	
Değiştir ;
	if (IsPC())
	{
		// Å¸°ÙÀ¸·Î ¼³Á¤µÈ °æ¿ì´Â PC¿¡ ÀÇÇÑ Å¬¸¯µµ Äù½ºÆ®·Î Ã³¸®ÇÏµµ·Ï ÇÕ´Ï´Ù.
		if (!CTargetManager::instance().GetTargetInfo(pkChrCauser->GetPlayerID(), TARGET_TYPE_VID, GetVID()))
		{
			// 2005.03.17.myevan.Å¸°ÙÀÌ ¾Æ´Ñ °æ¿ì´Â °³ÀÎ »óÁ¡ Ã³¸® ±â´ÉÀ» ÀÛµ¿½ÃÅ²´Ù.
			if (GetMyShop())
			{
				if (pkChrCauser->IsDead() == true) return;

				//PREVENT_TRADE_WINDOW
				if (pkChrCauser == this) // ÀÚ±â´Â °¡´É
				{
					if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen() || GetOfflineShopOwner())
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Áß(Ã¢°í,±³È¯,»óÁ¡)¿¡´Â °³ÀÎ»óÁ¡À» »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
						return;
					}
				}
				else // ´Ù¸¥ »ç¶÷ÀÌ Å¬¸¯ÇßÀ»¶§
				{
					// Å¬¸¯ÇÑ »ç¶÷ÀÌ ±³È¯/Ã¢°í/°³ÀÎ»óÁ¡/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
					if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen() || pkChrCauser->GetOfflineShopOwner())
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Áß(Ã¢°í,±³È¯,»óÁ¡)¿¡´Â °³ÀÎ»óÁ¡À» »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
						return;
					}

					// Å¬¸¯ÇÑ ´ë»óÀÌ ±³È¯/Ã¢°í/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
					//if ((GetExchange() || IsOpenSafebox() || GetShopOwner()))
					if ((GetExchange() || IsOpenSafebox() || IsCubeOpen() || GetOfflineShopOwner()))
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡¸¦ ÇÏ°í ÀÖ´Â ÁßÀÔ´Ï´Ù."));
						return;
					}
				}
				//END_PREVENT_TRADE_WINDOW

				if (pkChrCauser->GetShop())
				{
					pkChrCauser->GetShop()->RemoveGuest(pkChrCauser);
					pkChrCauser->SetShop(NULL);
				}

				GetMyShop()->AddGuest(pkChrCauser, GetVID(), false);
				pkChrCauser->SetShopOwner(this);
				return;
			}

			if (test_server)
				sys_err("%s.OnClickFailure(%s) - target is PC", pkChrCauser->GetName(), GetName());

			return;
		}
	}

	// Offline Shop
	if (IsOfflineShopNPC())
	{
		pkChrCauser->SetOfflineShopOwner(this);
		GetOfflineShop()->AddGuest(pkChrCauser, this);
		return;
	}

	// Ã»¼Ò³âÀº Äù½ºÆ® ¸øÇÔ
	if (LC_IsNewCIBN())
	{
		if (pkChrCauser->IsOverTime(OT_3HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 3);
			return;
		}
		else if (pkChrCauser->IsOverTime(OT_5HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 5);
			return;
		}
	}
	
	
	
	
	
	
Arat ;
	//°Å·¡°ü·Ã Ã¢ Ã¼Å©
	if (bCheckShopOwner)
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			if (bSendMsg)
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("°Å·¡Ã¢,Ã¢°í µîÀ» ¿¬ »óÅÂ¿¡¼­´Â ´Ù¸¥°÷À¸·Î ÀÌµ¿,Á¾·á ÇÒ¼ö ¾ø½À´Ï´Ù"));

			return true;
		}
	}
	
Değiştir ;
	//°Å·¡°ü·Ã Ã¢ Ã¼Å©
	if (bCheckShopOwner)
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || GetOfflineShopOwner())
		{
			if (bSendMsg)
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("°Å·¡Ã¢,Ã¢°í µîÀ» ¿¬ »óÅÂ¿¡¼­´Â ´Ù¸¥°÷À¸·Î ÀÌµ¿,Á¾·á ÇÒ¼ö ¾ø½À´Ï´Ù"));

			return true;
		}
	}
	
	
	
Arat ;
	if ((iPulse - GetMyShopTime()) < limit_time)
		return false;

	if ((iPulse - GetRefineTime()) < limit_time)
		return false;

	if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		return false;

	return true;
	
Değiştir ;
	if ((iPulse - GetMyShopTime()) < limit_time)
		return false;

	if ((iPulse - GetRefineTime()) < limit_time)
		return false;

	if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || GetOfflineShopOwner())
		return false;

	return true;
	
	
	
	
	
Arat ;
int	CHARACTER::GetSkillPowerByLevel(int level, bool bMob) const
{
	return CTableBySkill::instance().GetSkillPowerByLevelFromType(GetJob(), GetSkillGroup(), MINMAX(0, level, SKILL_MAX_LEVEL), bMob); 
}

Altına Ekle ;
void CHARACTER::SetOfflineShopSign(const char * c_szSign)
{
	char szSign[SHOP_SIGN_MAX_LEN + 1];
	strlcpy(szSign, c_szSign, sizeof(szSign));
	m_stOfflineShopSign = szSign;
}

void CHARACTER::DestroyOfflineShop()
{
	DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), GetOfflineShopRealOwner());
	LPOFFLINESHOP pkOfflineShop = GetOfflineShop();
	if (pkOfflineShop)
		pkOfflineShop->RemoveAllGuest();
	M2_DESTROY_CHARACTER(this);	
}