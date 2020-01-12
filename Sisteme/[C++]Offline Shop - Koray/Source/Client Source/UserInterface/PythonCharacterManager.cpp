Search:
#include "PythonTextTail.h"

Add it under:
#include "NetworkActorManager.h"
#include "PythonNetworkStream.h"

---

Search:
void CPythonCharacterManager::DeleteInstanceByFade(DWORD dwVID)
{
	TCharacterInstanceMap::iterator f = m_kAliveInstMap.find(dwVID);
	if (m_kAliveInstMap.end() == f)
	{
		return;
	}
	__DeleteBlendOutInstance(f->second);
	m_kAliveInstMap.erase(f);
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CPythonCharacterManager::SetVisibleForOfflineShops(int iFlag)
{
	CPythonCharacterManager::CharacterIterator itor = CharacterInstanceBegin();
	CPythonCharacterManager::CharacterIterator itorEnd = CharacterInstanceEnd();
	for (; itor != itorEnd; ++itor)
	{
		CInstanceBase * pInstance = *itor;
		if (pInstance) {
			if (pInstance->GetRace() >= 30005 && pInstance->GetRace() <= 30010) {
				CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
				if (iFlag == 1) {
					pInstance->Show();
					SCRIPT_SetAffect(pInstance->GetVirtualID(), 1, false);
					rkNetStream.AppearShopSign(pInstance->GetVirtualID());
				}
				else if (iFlag == 2) {
					char szName[512];
					sprintf(szName, "%s's Offline shop", GetMainInstancePtr()->GetNameString());
					if (strcmp(pInstance->GetNameString(), szName))
					{
						pInstance->Hide();
						SCRIPT_SetAffect(pInstance->GetVirtualID(), 1, true);
						rkNetStream.DisappearShopSign(pInstance->GetVirtualID());
					}
					else if (!strcmp(pInstance->GetNameString(), szName) && pInstance->IsHidden())
					{
						pInstance->Show();
						SCRIPT_SetAffect(pInstance->GetVirtualID(), 1, false);
						rkNetStream.AppearShopSign(pInstance->GetVirtualID());
					}
				}
				else {
					pInstance->Hide();
					SCRIPT_SetAffect(pInstance->GetVirtualID(), 1, true);
					rkNetStream.DisappearShopSign(pInstance->GetVirtualID());
				}

			}
		}
	}
}
#endif

https://puu.sh/sgL5T/5bbf602b40.png