//Search in char_item.cpp:
#include "war_map.h"
#include "xmas_event.h"
#include "marriage.h"
#include "monarch.h"

//Add after this:
#ifdef NEW_PET_SYSTEM
#include "New_PetSystem.h"
#endif

//Search in char_item.cpp:
	if (-1 != iLimitRealtimeStartFirstUseFlagIndex)
	{
		// ? ???? ??? ????? ??? Socket1? ?? ????. (Socket1? ???? ??)
		if (0 == item->GetSocket(1))
		{
			// ??????? Default ??? Limit Value ?? ????, Socket0? ?? ??? ? ?? ????? ??. (??? ?)
			long duration = (0 != item->GetSocket(0)) ? item->GetSocket(0) : item->GetProto()->aLimits[iLimitRealtimeStartFirstUseFlagIndex].lValue;

			if (0 == duration)
				duration = 60 * 60 * 24 * 7;

			item->SetSocket(0, time(0) + duration);
			item->StartRealTimeExpireEvent();
		}	

		if (false == item->IsEquipped())
			item->SetSocket(1, item->GetSocket(1) + 1);		
	}
	
//Add after this:
#ifdef NEW_PET_SYSTEM

	if (item->GetVnum() == 55001) {

		LPITEM item2;

		if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
			return false;

		if (item2->IsExchanging())
			return false;

		if (item2->GetVnum() > 55704 || item2->GetVnum() < 55701)
			return false;

		
		char szQuery1[1024];
		snprintf(szQuery1, sizeof(szQuery1), "SELECT duration FROM new_petsystem WHERE id = %lu LIMIT 1", item2->GetID());
		std::auto_ptr<SQLMsg> pmsg2(DBManager::instance().DirectQuery(szQuery1));
		if (pmsg2->Get()->uiNumRows > 0) {
			MYSQL_ROW row = mysql_fetch_row(pmsg2->Get()->pSQLResult);
			if (atoi(row[0]) > 0) {
				if (GetNewPetSystem()->IsActivePet()) {
					ChatPacket(CHAT_TYPE_INFO, "You have to unsummon your pet first.");
					return false;
				}

				DBManager::instance().DirectQuery("UPDATE new_petsystem SET duration =(tduration) WHERE id = %d", item2->GetID());
				ChatPacket(CHAT_TYPE_INFO, "Your Pet's life is now full.");
			}
			else {
				DBManager::instance().DirectQuery("UPDATE new_petsystem SET duration =(tduration/2) WHERE id = %d", item2->GetID());
				ChatPacket(CHAT_TYPE_INFO, "Your Pet's life is now restored.");
			}
			item->SetCount(item->GetCount() - 1);
			return true;
		}
		else
			return false;
	}

	if (item->GetVnum() >= 55701 && item->GetVnum() <= 55704) {
		LPITEM item2;

		if (item2 = GetItem(DestCell)) {
			if (item2->GetVnum() == 55002) {
				if(item2->GetAttributeValue(0) > 0){
					ChatPacket(CHAT_TYPE_INFO, "Cutia are deja un animalut inauntru.");
				}
				else{
					if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
						return false;

					if (item2->IsExchanging())
						return false;

					if (GetNewPetSystem()->IsActivePet()) {
						ChatPacket(CHAT_TYPE_INFO, "You have to unsummon your pet first.");
						return false;
					}
					
					for (int b = 0; b < 3; b++) {
						item2->SetForceAttribute(b, 1, item->GetAttributeValue(b));
					}

					item2->SetForceAttribute(3, 1, item->GetAttributeValue(3));
					item2->SetForceAttribute(4, 1, item->GetAttributeValue(4));
					DWORD vnum1 = item->GetVnum()-55700;
					item2->SetSocket(0, vnum1);
					item2->SetSocket(1, item->GetSocket(1));
					//ChatPacket(CHAT_TYPE_INFO, "Pet %d %d %d //// %d %d %d",item->GetAttributeValue(0),item->GetAttributeValue(1),item->GetAttributeValue(2),item2->GetAttributeValue(0),item2->GetAttributeValue(1),item2->GetAttributeValue(2));
					DBManager::instance().DirectQuery("UPDATE new_petsystem SET id =%d WHERE id = %d", item2->GetID(), item->GetID());
					ITEM_MANAGER::instance().RemoveItem(item);
					return true;
				}
			}
		}
	}


	if (item->GetVnum() == 55002 && item->GetAttributeValue(0) > 0) {

		int pos = GetEmptyInventory(item->GetSize());
		if(pos == -1)
		{
			ChatPacket(CHAT_TYPE_INFO, "You don't have enought space.");
			return false;
		}

		if (item->IsExchanging())
			return false;
		DWORD vnum2 = 55700+item->GetSocket(0);
		LPITEM item2 = AutoGiveItem(vnum2, 1);
		for (int b = 0; b < 3; b++) {
			item2->SetForceAttribute(b, 1, item->GetAttributeValue(b));
		}
		item2->SetForceAttribute(3, 1, item->GetAttributeValue(3));
		item2->SetForceAttribute(4, 1, item->GetAttributeValue(4));
		item2->SetSocket(1,item->GetSocket(1));
		//ChatPacket(CHAT_TYPE_INFO, "Pet1 %d %d %d",item->GetAttributeValue(0),item->GetAttributeValue(1),item->GetAttributeValue(2));
		DBManager::instance().DirectQuery("UPDATE new_petsystem SET id =%d WHERE id = %d", item2->GetID(), item->GetID());
		ITEM_MANAGER::instance().RemoveItem(item);
		return true;

	}
#endif
