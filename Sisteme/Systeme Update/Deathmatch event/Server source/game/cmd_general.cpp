Search:
#include "gm.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "Deathmatch.h"
#endif


---

Search:
ACMD(do_user_horse_ride)
{
	if (ch->IsObserverMode())
		return;

	if (ch->IsDead() || ch->IsStun())
		return;

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
	int iTimeToDead = (event_time(ch->m_pkDeadEvent) / passes_per_sec);

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
	{
		if (iTimeToDead == 180)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¾ÆÁ÷ Àç½ÃÀÛ ÇÒ ¼ö ¾ø½À´Ï´Ù. (%dÃÊ ³²À½)"), iTimeToDead - 179);
			return;
		}

		if (iTimeToDead - 160 > 0)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "%d saniye sonra dirilebilirsin", iTimeToDead - 160);
			return;
		}

		ch->ChatPacket(CHAT_TYPE_COMMAND, "CloseRestartWindow");
		ch->GetDesc()->SetPhase(PHASE_GAME);
		ch->SetPosition(POS_STANDING);
		ch->StartRecoveryEvent();

		CDeathMatchManager::instance().SpawnRandomPos(ch);

		ch->PointChange(POINT_HP, ch->GetMaxHP() - ch->GetHP());
		ch->PointChange(POINT_SP, ch->GetMaxSP() - ch->GetSP());
		ch->ReviveInvisible(3);
		return;
	}
#endif

---

Search:
ACMD(do_pvp)
{
	if (ch->GetArena() != NULL || CArenaManager::instance().IsArenaMap(ch->GetMapIndex()) == true)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·ÃÀå¿¡¼­ »ç¿ëÇÏ½Ç ¼ö ¾ø½À´Ï´Ù."));
		return;
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
ACMD(do_observer_exit)
{
	if (ch->IsObserverMode())
	{
		if (ch->GetWarMap())
			ch->SetWarMap(NULL);

Add it under:
#ifdef DEATHMATCH_MODE
		if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX){
			ch->SetObserverMode(false);
			CDeathMatchManager::instance().ResetScore(ch);
			ch->GoHome();
			return;
		}
#endif

---

Search:
ACMD(do_party_request)
{
	if (ch->GetArena())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·ÃÀå¿¡¼­ »ç¿ëÇÏ½Ç ¼ö ¾ø½À´Ï´Ù."));
		return;
	}

	if (ch->GetParty())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ÀÌ¹Ì ÆÄÆ¼¿¡ ¼ÓÇØ ÀÖÀ¸¹Ç·Î °¡ÀÔ½ÅÃ»À» ÇÒ ¼ö ¾ø½À´Ï´Ù."));
		return;
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
ACMD(do_party_request_accept)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
		return;

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
ACMD(do_ride)
{
    dev_log(LOG_DEB0, "[DO_RIDE] start");
    if (ch->IsDead() || ch->IsStun())
		return;

Add it under:
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

