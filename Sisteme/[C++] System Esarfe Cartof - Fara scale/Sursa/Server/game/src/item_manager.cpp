// 1) Search: #include "cube.h"
// 2) After make a new line and paste:
#include "acce.h"

// 1) Search: void ITEM_MANAGER::RemoveItem(LPITEM item, const char * c_pszReason)
// 2) After make a new line and paste:
void ITEM_MANAGER::RemoveItem(LPITEM item, const char * c_pszReason)
{
	LPCHARACTER o;
	if ((o = item->GetOwner()))
	{
		char szHint[64];
		snprintf(szHint, sizeof(szHint), "%s %u ", item->GetName(), item->GetCount());
		if (item->GetOwner()->IsAcceOpen())
		{
			Acce_delete_item(item->GetOwner(), 0);
			Acce_delete_item(item->GetOwner(), 1);
		}
		
		LogManager::instance().ItemLog(o, item, c_pszReason ? c_pszReason : "REMOVE", szHint);
		if (item->GetWindow() == MALL || item->GetWindow() == SAFEBOX)
		{
			CSafebox* pSafebox = item->GetWindow() == MALL ? o->GetMall() : o->GetSafebox();
			if (pSafebox)
			{
				pSafebox->Remove(item->GetCell());
			}
		}
		else
		{
			o->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);
			item->RemoveFromCharacter();
		}
	}

	M2_DESTROY_ITEM(item);
}