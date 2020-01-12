Search for:
	int pc_get_skillgroup(lua_State* L)
up this function put:
	int pc_costume(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if(!lua_isnumber(L, 1))
			return 0;

		int part_value = 0;
		bool enable = (bool)lua_tonumber(L, 1);
		if(enable)
		{
			const CItem* pArmor = ch->GetWear(WEAR_BODY);
			part_value = (NULL != pArmor) ? pArmor->GetVnum() : ch->GetOriginalPart(PART_MAIN);
		}
		else
		{
			const CItem* pArmor = ch->GetWear(WEAR_COSTUME_BODY);
			part_value = (NULL != pArmor) ? pArmor->GetVnum() : ch->GetOriginalPart(PART_MAIN);
		}
		//ch->ChatPacket(CHAT_TYPE_INFO, "CostumeVisible : %d -> %d", (int)ch->CostumeVisible(), (int)!enable);
		ch->SetCostumeVisible(!enable);
		ch->SetPart(PART_MAIN, part_value);
		ch->UpdatePacket();
		return 0;
	}