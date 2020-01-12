//1.) Search:
#include "log.h"
//2.) Add bellow:
#ifdef ENABLE_TELEPORT_COMMAND
#include "commandTeleporter_vegas.h"
#endif
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
//3.) Search:
ACMD(do_stat_reset)
{
	ch->PointChange(POINT_STAT_RESET_COUNT, 12 - ch->GetPoint(POINT_STAT_RESET_COUNT));
}
//4.) Add bellow:
#ifdef ENABLE_TELEPORT_COMMAND
ACMD(do_teleport)
{
	if (!ch->IsPC() || NULL == ch)
		return;
	
	char szNumber[3];
	one_argument(argument, szNumber, sizeof(szNumber));

	if (!*szNumber || !isdigit(*szNumber) || !strcmp(szNumber, "show_list"))
		goto TELEPORT_COMMAND_INFORMATION;
	
	if (ch->IsObserverMode())
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[0]);
		return;
	}
	
	if (ch->IsDead()) {
		ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[1]);
		return;
	}
	
	if (ch->IsStun())
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[2]);
		return;
	}
	
	if (ch->GetDungeon())
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[4]);
		return;
	}
	
    if (ch->GetExchange() || ch->IsOpenSafebox() || ch->IsCubeOpen() || ch->GetShop() || ch->GetMyShop()
#ifdef ENABLE_ACCE_COSTUME_SYSTEM
    || ch->IsAcceOpen()
#endif
#ifdef ENABLE_OFFLINE_SHOP
    || ch->GetOfflineShop() || ch->GetOfflineShopOwner()
#endif
    )
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[5]);
		return;	
	}
	
	else if (isdigit(*szNumber))
	{		
		int iRequestIndexMap = 0;
		str_to_number(iRequestIndexMap, szNumber);
		
		if (iRequestIndexMap < 1)
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[6]);
			return;
		}	
		
		if (iRequestIndexMap > NUMBER_MAX_MAPS)
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[7], NUMBER_MAX_MAPS);
			return;
		}
		
		if (ch->GetLevel() < szTeleportConfig[iRequestIndexMap][2])
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[8], szTeleportConfig[iRequestIndexMap][2]);
			return;
		}	
		
		if (ch->GetLevel() > szTeleportConfig[iRequestIndexMap][3])
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, szTableTranslate[9], szTeleportConfig[iRequestIndexMap][3]);
			return;
		}	
		
		ch->ChatPacket(CHAT_TYPE_INFO, szTableTranslate[10], iRequestIndexMap);
		ch->WarpSet(szTeleportConfig[iRequestIndexMap][0], szTeleportConfig[iRequestIndexMap][1]);
	}
	
TELEPORT_COMMAND_INFORMATION:
	ch->ChatPacket(CHAT_TYPE_INFO,  szTableTranslate[11]);
	ch->ChatPacket(CHAT_TYPE_INFO,  szTableTranslate[12]);
	
	// With this for, it will show you all the maps that are activated in a table. -> szTeleportConfig -> szTableNameMaps (name map, level min, level max) 
	// https://i.gyazo.com/142374a43ff72003829a9016b7b1935d.png // lool :nice
	for (int iRequest_vegas = 0; iRequest_vegas < _countof(szTeleportConfig); iRequest_vegas++)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, szTableNameMaps[iRequest_vegas], szTeleportConfig[iRequest_vegas][2], szTeleportConfig[iRequest_vegas][3]);
	}
}
#endif
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""