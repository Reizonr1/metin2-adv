Caută:
if (iExtraLen < 0)
	{
		sys_err("invalid packet length (len %d size %u buffer %u)", iExtraLen, pinfo->size, uiBytes);
		ch->GetDesc()->SetPhase(PHASE_CLOSE);
		return -1;
	}
Adaugă sub:
#ifdef ENABLE_OX_CHAT_BLOCK
	if (quest::CQuestManager::instance().GetEventFlag("ox_chat_engel") == 1)
	{ 
		if(ch->GetMapIndex() == 113 && (pinfo->type == CHAT_TYPE_TALKING || pinfo->type == CHAT_TYPE_PARTY || pinfo->type == CHAT_TYPE_GUILD || pinfo->type == CHAT_TYPE_SHOUT))
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ox_chat_block"));
			return iExtraLen;
		}
	}
#endif