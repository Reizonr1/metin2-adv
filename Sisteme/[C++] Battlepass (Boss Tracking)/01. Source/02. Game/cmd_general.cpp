// Adauga
#ifdef ENABLE_BOSS_TRACKING
ACMD(do_bosstracking)
{
	if(ch->IsDead() || ch->GetMyShop() || ch->GetShopOwner() || ch->IsOpenSafebox() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("다른 거래중(창고,교환,상점)에는 개인상점을 사용할 수 없습니다."));
		return;
	}
	quest::CQuestManager& BTracking = quest::CQuestManager::instance();

	ch->ChatPacket(CHAT_TYPE_COMMAND,"BossTracking %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d", 
		BTracking.GetEventFlagBR("newtracking","cadi1"),
		BTracking.GetEventFlagBR("newtracking","cadi2"),
		BTracking.GetEventFlagBR("newtracking","cadi3"),
		BTracking.GetEventFlagBR("newtracking","cadi4"),
		BTracking.GetEventFlagBR("newtracking","cadi5"),
		BTracking.GetEventFlagBR("newtracking","cadi6"),
		BTracking.GetEventFlagBR("newtracking","alevkral1"),
		BTracking.GetEventFlagBR("newtracking","alevkral2"),
		BTracking.GetEventFlagBR("newtracking","alevkral3"),
		BTracking.GetEventFlagBR("newtracking","alevkral4"),
		BTracking.GetEventFlagBR("newtracking","alevkral5"),
		BTracking.GetEventFlagBR("newtracking","alevkral6"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek1"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek2"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek3"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek4"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek5"),
		BTracking.GetEventFlagBR("newtracking","kraliceormcek6"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan1"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan2"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan3"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan4"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan5"),
		BTracking.GetEventFlagBR("newtracking","sarikaplan6"),
		BTracking.GetEventFlagBR("newtracking","buzkralice1"),
		BTracking.GetEventFlagBR("newtracking","buzkralice2"),
		BTracking.GetEventFlagBR("newtracking","buzkralice3"),
		BTracking.GetEventFlagBR("newtracking","buzkralice4"),
		BTracking.GetEventFlagBR("newtracking","buzkralice5"),
		BTracking.GetEventFlagBR("newtracking","buzkralice6"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk1"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk2"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk3"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk4"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk5"),
		BTracking.GetEventFlagBR("newtracking","dokuzkuyruk6"),
		BTracking.GetEventFlagBR("newtracking","colejderha1"),
		BTracking.GetEventFlagBR("newtracking","colejderha2"),
		BTracking.GetEventFlagBR("newtracking","colejderha3"),
		BTracking.GetEventFlagBR("newtracking","colejderha4"),
		BTracking.GetEventFlagBR("newtracking","colejderha5"),
		BTracking.GetEventFlagBR("newtracking","colejderha6"),
		BTracking.GetEventFlagBR("newtracking","agac1"),
		BTracking.GetEventFlagBR("newtracking","agac2"),
		BTracking.GetEventFlagBR("newtracking","agac3"),
		BTracking.GetEventFlagBR("newtracking","agac4"),
		BTracking.GetEventFlagBR("newtracking","agac5"),
		BTracking.GetEventFlagBR("newtracking","agac6"),
		BTracking.GetEventFlagBR("newtracking","komutan1"),
		BTracking.GetEventFlagBR("newtracking","komutan2"),
		BTracking.GetEventFlagBR("newtracking","komutan3"),
		BTracking.GetEventFlagBR("newtracking","komutan4"),
		BTracking.GetEventFlagBR("newtracking","komutan5"),
		BTracking.GetEventFlagBR("newtracking","komutan6"),
		BTracking.GetEventFlagBR("newtracking","karanlik1"),
		BTracking.GetEventFlagBR("newtracking","karanlik2"),
		BTracking.GetEventFlagBR("newtracking","karanlik3"),
		BTracking.GetEventFlagBR("newtracking","karanlik4"),
		BTracking.GetEventFlagBR("newtracking","karanlik5"),
		BTracking.GetEventFlagBR("newtracking","karanlik6")
		);
}
#endif