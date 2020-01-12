//find ACMD(do_reload) and add before that line
#ifdef OFFLINE_SHOP
extern void LoadIndexShopLimit();
extern void LoadShopConfig();
#endif

/*find in function ACMD(do_reload) line 
if (*arg1) 
{
And add after
*/

#ifdef OFFLINE_SHOP
		if (!strcmp(arg1, "shop"))
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Reloading shop_limit,shop_costs.");
			LoadIndexShopLimit();
			LoadShopConfig();
		}
#endif
	
	
//find struct FuncPurge and all with:
struct FuncPurge
{
	LPCHARACTER m_pkGM;
	bool	m_bAll;

	FuncPurge(LPCHARACTER ch) : m_pkGM(ch), m_bAll(false)
	{
	}

	void operator () (LPENTITY ent)
	{
		if (!ent->IsType(ENTITY_CHARACTER))
			return;

		LPCHARACTER pkChr = (LPCHARACTER)ent;

		int iDist = DISTANCE_APPROX(pkChr->GetX() - m_pkGM->GetX(), pkChr->GetY() - m_pkGM->GetY());

		if (!m_bAll && iDist >= 1000)	// 10ąĚĹÍ ŔĚ»óżˇ ŔÖ´Â °ÍµéŔş purge ÇĎÁö ľĘ´Â´Ů.
			return;

#ifdef OFFLINE_SHOP
		if (pkChr->IsPrivShop())
			return;
#endif

		sys_log(0, "PURGE: %s %d", pkChr->GetName(), iDist);
		if (pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)

		{
			M2_DESTROY_CHARACTER(pkChr);
		}
	}
};