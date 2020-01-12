[..]
void CInputLogin::Entergame(LPDESC d, const char * data)
{
	[..]
	ch->ReviveInvisible(5);
	d->SetPhase(PHASE_GAME);
	[..]
	

#ifdef OFFLINE_SHOP
	ch->LoadPrivShops();
	ch->SendShopCost();
	ch->StartRefreshShopEvent();

#endif

#ifdef GIFT_SYSTEM
	ch->StartRefreshGift();
#endif
	[..]
}

