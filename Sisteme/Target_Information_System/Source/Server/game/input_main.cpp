// Search for:
static int __deposit_limit()
{
	return (1000*10000); // 1Ãµ¸¸
}

// Add (Under):
#ifdef __SEND_TARGET_INFO__
void CInputMain::TargetInfoLoad(LPCHARACTER ch, const char* c_pData)
{
	TPacketCGTargetInfoLoad* p = (TPacketCGTargetInfoLoad*)c_pData;
	TPacketGCTargetInfo pInfo;
	pInfo.header = HEADER_GC_TARGET_INFO;
	static std::vector<LPITEM> s_vec_item;
	s_vec_item.clear();
	LPITEM pkInfoItem;
	LPCHARACTER m_pkChrTarget = CHARACTER_MANAGER::instance().Find(p->dwVID);

	// if (m_pkChrTarget && (m_pkChrTarget->IsMonster() || m_pkChrTarget->IsStone()))
	// {
		// if (thecore_heart->pulse - (int) ch->GetLastTargetInfoPulse() < passes_per_sec * 3)
			// return;

		// ch->SetLastTargetInfoPulse(thecore_heart->pulse);

	if (ITEM_MANAGER::instance().CreateDropItemVector(m_pkChrTarget, ch, s_vec_item) && (m_pkChrTarget->IsMonster() || m_pkChrTarget->IsStone()))
	{
		if (s_vec_item.size() == 0);
		else if (s_vec_item.size() == 1)
		{
			pkInfoItem = s_vec_item[0];
			pInfo.dwVID	= m_pkChrTarget->GetVID();
			pInfo.race = m_pkChrTarget->GetRaceNum();
			pInfo.dwVnum = pkInfoItem->GetVnum();
			pInfo.count = pkInfoItem->GetCount();
			ch->GetDesc()->Packet(&pInfo, sizeof(TPacketGCTargetInfo));
		}
		else
		{
			int iItemIdx = s_vec_item.size() - 1;
			while (iItemIdx >= 0)
			{
				pkInfoItem = s_vec_item[iItemIdx--];

				if (!pkInfoItem)
				{
					sys_err("pkInfoItem null in vector idx %d", iItemIdx + 1);
					continue;
				}

					pInfo.dwVID	= m_pkChrTarget->GetVID();
					pInfo.race = m_pkChrTarget->GetRaceNum();
					pInfo.dwVnum = pkInfoItem->GetVnum();
					pInfo.count = pkInfoItem->GetCount();
					ch->GetDesc()->Packet(&pInfo, sizeof(TPacketGCTargetInfo));
			}
		}
	}
	// }
}
#endif

// Search for:
		case HEADER_CG_XTRAP_ACK:
			{
				TPacketXTrapCSVerify* p = reinterpret_cast<TPacketXTrapCSVerify*>((void*)c_pData);
				CXTrapManager::instance().Verify_CSStep3(d->GetCharacter(), p->bPacketData);
			}
			break;

// Add (Under):
#ifdef __SEND_TARGET_INFO__
		case HEADER_CG_TARGET_INFO_LOAD:
			{
				TargetInfoLoad(ch, c_pData);
			}
			break;
#endif
