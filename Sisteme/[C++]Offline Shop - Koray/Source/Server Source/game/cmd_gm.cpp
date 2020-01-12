Search:
struct FuncPurge
{
	...

	LPCHARACTER pkChr = (LPCHARACTER) ent;

	...

}

Change like this:
struct FuncPurge
{
	...

	LPCHARACTER pkChr = (LPCHARACTER) ent;
#ifdef __OFFLINE_SHOP__
	if (pkChr->GetOfflineShopOwner())
		return;
#endif
	...

}

https://puu.sh/sgGmk/bb0565fd89.png