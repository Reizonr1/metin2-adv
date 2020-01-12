Search:
#include "PythonItem.h"

Add it under:
#include "PythonSystem.h"
#include "PythonNetworkStream.h"

--

Search:
	CInstanceBase* pNewInstance = rkChrMgr.CreateInstance(kCreateData);
	if (!pNewInstance)
		return NULL;

Add it under:
#ifdef __OFFLINE_SHOP__
	if (pNewInstance->GetRace() >= 30005 && pNewInstance->GetRace() <= 30010)
	{
		CPythonCharacterManager & rkChrMgr = CPythonCharacterManager::Instance();
		CInstanceBase* pkInstMain = rkChrMgr.GetMainInstancePtr();

		if (CPythonSystem::Instance().GetShowOfflineShopFlag() == 0)
		{
			pNewInstance->Hide();
			rkChrMgr.SCRIPT_SetAffect(pNewInstance->GetVirtualID(), 1, true);
		}
		else if (CPythonSystem::Instance().GetShowOfflineShopFlag() == 2)
		{
			char szName[512];
			sprintf(szName, "%s's Offline shop", pkInstMain->GetNameString());
			if (strcmp(pNewInstance->GetNameString(), szName))
			{
				pNewInstance->Hide();
				rkChrMgr.SCRIPT_SetAffect(pNewInstance->GetVirtualID(), 1, true);
			}
		}
	}
#endif


https://puu.sh/sgKuo/7b0d5133e0.png