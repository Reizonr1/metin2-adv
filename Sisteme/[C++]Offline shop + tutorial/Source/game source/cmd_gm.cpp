Arat ;
		sys_log(0, "PURGE: %s %d", pkChr->GetName(), iDist);

		if (pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)
		{
			M2_DESTROY_CHARACTER(pkChr);
		}
		
		
Değiştir ;
		sys_log(0, "PURGE: %s %d", pkChr->GetName(), iDist);

#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
		if (!pkChr->IsOfflineShopNPC() && pkChr->GetRaceNum() != 30000 && pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)
#else
		if (!pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)
#endif
		{
			M2_DESTROY_CHARACTER(pkChr);
		}
		
		
		
		
		
Arat ;
	if (ch->GetShop())
		strlcat(buf, ", Shop", sizeof(buf));

	if (ch->GetExchange())
		strlcat(buf, ", Exchange", sizeof(buf));

		
Değiştir ;
	if (ch->GetShop())
		strlcat(buf, ", Shop", sizeof(buf));

#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	if (ch->GetOfflineShop())
		strlcat(buf, ", Offline Shop", sizeof(buf));
#endif

	if (ch->GetExchange())
		strlcat(buf, ", Exchange", sizeof(buf));

	
	
	
	
	
	
	
Arat ;
ACMD(do_user)
{
	const DESC_MANAGER::DESC_SET & c_ref_set = DESC_MANAGER::instance().GetClientSet();
	user_func func;

	func.initialize(ch);
	std::for_each(c_ref_set.begin(), c_ref_set.end(), func);

	if (func.count % 4)
		ch->ChatPacket(CHAT_TYPE_INFO, func.str);

	ch->ChatPacket(CHAT_TYPE_INFO, "Total %d", func.count);
}

Altına Ekle ;
struct FFindOfflineShop
{
	const char * szName;
	bool bResult;
	
	FFindOfflineShop(const char * c_szName) : szName(c_szName), bResult(false) {};

	void operator()(LPENTITY ent)
	{
		if (!ent)
			return;

		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER)ent;
			if (ch->IsOfflineShopNPC() && !strcmp(szName, ch->GetName()))
			{
				bResult = true;
				ch->DestroyOfflineShop();
			}
		}
	}
};





Arat ;
ACMD(do_disconnect)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "ex) /dc <player name>");
		return;
	}

	LPDESC d = DESC_MANAGER::instance().FindByCharacterName(arg1);
	LPCHARACTER	tch = d ? d->GetCharacter() : NULL;

	if (!tch)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "%s: no such a player.", arg1);
		return;
	}

	if (tch == ch)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "cannot disconnect myself");
		return;
	}
	
	DESC_MANAGER::instance().DestroyDesc(d);
}

Değiştir ;
ACMD(do_disconnect)
{
	char arg1[256];
	char arg2[256];
	
	//one_argument(argument, arg1, sizeof(arg1));
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	if (!*arg1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "ex) /dc <player name>");
		return;
	}

#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	// 06.27.2015 fix
	if (*arg2 && !strcmp(arg2, "offlineshop"))
	// end of 06.27.2015 fix
	{
		LPSECTREE_MAP pMap = SECTREE_MANAGER::instance().GetMap(ch->GetMapIndex());
		if (pMap)
		{
			FFindOfflineShop offlineShop(arg1);
			pMap->for_each(offlineShop);
			if (offlineShop.bResult)
				ch->ChatPacket(CHAT_TYPE_INFO, "%s Offline shop yıkıldı!", arg1);			
		}
	}
#endif

	LPDESC d = DESC_MANAGER::instance().FindByCharacterName(arg1);
	LPCHARACTER	tch = d ? d->GetCharacter() : NULL;

	if (!tch)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "%s: Böyle bir oyuncu yok.", arg1);
		return;
	}

	if (tch == ch)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Kendine zarar veremessin :D");
		return;
	}
	
	DESC_MANAGER::instance().DestroyDesc(d);
}




