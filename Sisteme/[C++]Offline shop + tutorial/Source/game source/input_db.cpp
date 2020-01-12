Arat ;
#include "XTrapManager.h"

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
#include "offlineshop_config.h"
#include "offlineshop_manager.h"
#endif




Arat ;
#ifdef __AUCTION__
#include "auction_manager.h"
#endif

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
extern bool g_bEnableRespawnOfflineShop;
#endif 






Arat ;
	signal_timer_enable(30);

	if (test_server)
	{
		CMobManager::instance().DumpRegenCount("mob_count");
	}

	CPCBangManager::instance().RequestUpdateIPList(0);

	// castle_boot
	castle_boot();

	// request blocked_country_ip
	{
		db_clientdesc->DBPacket(HEADER_GD_BLOCK_COUNTRY_IP, 0, NULL, 0);
		dev_log(LOG_DEB0, "<sent HEADER_GD_BLOCK_COUNTRY_IP>");
	}
	
	
Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
		if (g_bEnableRespawnOfflineShop)
		{
			MYSQL_ROW row;
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT * FROM %soffline_shop_npc", get_table_postfix()));

			if(pMsg->Get()->uiNumRows != 0)
			{
				while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
				{			
					char szName[CHARACTER_NAME_MAX_LEN + 1];
					char szSign[SHOP_SIGN_MAX_LEN + 1];
					DWORD dwOwnerID = 0;
					long lMapIndex = 0,x = 0, y = 0, z = 0;
					int iTime = 0;
					BYTE bChannel = 0;

					str_to_number(dwOwnerID, row[0]);
					snprintf(szSign, sizeof(szSign), "%s", row[1]);					
					snprintf(szName, sizeof(szName), "%s's offline shop", row[2]);
					str_to_number(iTime, row[3]);
					str_to_number(x, row[4]);
					str_to_number(y, row[5]);
					str_to_number(z, row[6]);
					str_to_number(lMapIndex, row[7]);
					str_to_number(bChannel, row[8]);

					if (g_bChannel == bChannel)
					{
						LPCHARACTER npc = CHARACTER_MANAGER::instance().SpawnMob(30000, lMapIndex, x, y, z, false, -1, false, true, dwOwnerID);
						if (npc)
						{
							npc->SetName(szName);
							npc->SetOfflineShopSign(szSign);							
							
							// bug fixed - 6.20.2015
							if (iTime != 0)							
							{
								npc->SetOfflineShopTimer(iTime);                        
								npc->StartOfflineShopUpdateEvent();						
							}
							// end of bug fixed - 6.20.2015

							LPOFFLINESHOP pkOfflineShop = COfflineShopManager::instance().CreateOfflineShop(npc, dwOwnerID);
							npc->SetOfflineShop(pkOfflineShop);
							npc->SetOfflineShopChannel(bChannel);

							npc->Show(lMapIndex, x, y, z, true);
						}
					}
				}
            }
        }
#endif





Arat ;
	if (ch->GetShopOwner() || ch->GetExchange() || ch->GetMyShop() || ch->IsCubeOpen() )

Değiştir ;
	if (ch->GetShopOwner() || ch->GetExchange() || ch->GetMyShop() || ch->IsCubeOpen() || ch->GetOfflineShopOwner())
