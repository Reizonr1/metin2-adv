Search:
#include "DragonLair.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "Deathmatch.h"
#endif


---

Search:
		ch->StartRecoveryEvent();

		ch->ChatPacket(CHAT_TYPE_COMMAND, "CloseRestartWindow");

Add it under:
#ifdef DEATHMATCH_MODE
		if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX && ch->IsObserverMode())
			ch->SetObserverMode(true);
#endif

---

Search:
	if (CArenaManager::instance().IsArenaMap(GetMapIndex()) == true)
		return;

	if (CBattleArena::instance().IsBattleArenaMap(GetMapIndex()) == true)
		return;

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
		if (!IsPC() && pkKiller->GetDungeon())
			pkKiller->GetDungeon()->IncKillCount(pkKiller, this);

		isAgreedPVP = CPVPManager::instance().Dead(this, pkKiller->GetPlayerID());
		isDuel = CArenaManager::instance().OnDead(pkKiller, this);

Add it under:
#ifdef DEATHMATCH_MODE
		if (GetMapIndex() == DEATMATCH_MAP_INDEX){
			isUnderGuildWar = true;

			if (IsPC()){
				// Old info
				int iDMKillerOldScore = CDeathMatchManager::instance().GetScore(pkKiller->GetPlayerID()); // Get killer now score
				int iDMKillerKillAverage = pkKiller->GetQuestFlag("qDeathMatchPanel.kill_average"); // Get killer kill average

				// Set new score to system
				/*                            If killer score in below zero set score in average */
				if (iDMKillerKillAverage > 0)
					pkKiller->SetQuestFlag("qDeathMatchPanel.kill_average", iDMKillerKillAverage - 1);
				else
					CDeathMatchManager::instance().SetScore(pkKiller->GetPlayerID(), iDMKillerOldScore + 1);

				// New Info
				int iDMKillerNewScore = CDeathMatchManager::instance().GetScore(pkKiller->GetPlayerID()); // Get killer new score

				// Send info to killer
				// CDeathMatchManager::instance().SendScoreInfo(pkKiller->GetPlayerID(), iDMKillerNewScore);
				// Send info to system
				sys_log(0, "<DeathMatch> Kill Info: Killer: %s K_Score: %d Victim: %s V_Score: %d", pkKiller->GetName(), iDMKillerNewScore, GetName(), CDeathMatchManager::instance().GetScore(GetPlayerID()));

				// Notice
				if (iDMKillerNewScore == 50 || iDMKillerNewScore == 50 * 2 || iDMKillerNewScore == 50 * 3 || iDMKillerNewScore == 50 * 4 || iDMKillerNewScore == 50 * 5 ||
					iDMKillerNewScore == 50 * 6 || iDMKillerNewScore == 50 * 7 || iDMKillerNewScore == 50 * 8 || iDMKillerNewScore == 50 * 9 || iDMKillerNewScore == 50 * 10)
					CDeathMatchManager::instance().NoticeScore(pkKiller->GetPlayerID(), iDMKillerNewScore);

				// Info to killer
				if (pkKiller->GetQuestFlag("qDeathMatchPanel.kill_average") != 0)
					pkKiller->ChatPacket(CHAT_TYPE_INFO, "%s i öldürdün ve 1 skor kazandın. Skorun: -%d", GetName(), iDMKillerKillAverage - 1);
				else
					pkKiller->ChatPacket(CHAT_TYPE_INFO, "%s i öldürdün ve 1 skor kazandın. Skorun: %d", GetName(), iDMKillerNewScore);

				// Victim Stuffs
				{
					int iDMVictimScore = CDeathMatchManager::instance().GetScore(GetPlayerID()); // Get Victim now score
					int iDMVictimKillCount = GetQuestFlag("qDeathMatchPanel.kill_count"); // Get Victim kill count
					int iDMVictimLastKiller = GetQuestFlag("qDeathMatchPanel.last_killer"); // Get Victim last killer

					// Check victim kill average
					int iDMVictimKillAverage = GetQuestFlag("qDeathMatchPanel.kill_average");
					if (iDMVictimScore <= 0){
						if (iDMVictimKillAverage >= 4){
							ChatPacket(CHAT_TYPE_INFO, "Skorun -5'e indigi icin eventten cikarildin");

							if (IsAffectFlag(AFF_STUN))
								RemoveAffect(AFFECT_STUN);

							CDeathMatchManager::instance().ResetScore(this);
							CDeathMatchManager::instance().SwitchToSpectator(this);
						}

						SetQuestFlag("qDeathMatchPanel.kill_average", iDMVictimKillAverage + 1);
						iDMVictimKillAverage += 1;
					}

					// Check victim dead count
					if (iDMVictimKillCount >= quest::CQuestManager::instance().GetEventFlag("deathmatch_kill_limit")){
						ChatPacket(CHAT_TYPE_INFO, "%d defa oldugun icin eventten cikarildin", iDMVictimKillCount + 1);

						if (IsAffectFlag(AFF_STUN))
							RemoveAffect(AFFECT_STUN);

						CDeathMatchManager::instance().ResetScore(this);
						CDeathMatchManager::instance().SwitchToSpectator(this);
					}

					// Set new scores to system
					SetQuestFlag("qDeathMatchPanel.kill_count", iDMVictimKillCount + 1);
					CDeathMatchManager::instance().SetScore(GetPlayerID(), iDMVictimScore - 1);

					// Last killer
					if (iDMVictimLastKiller && iDMVictimLastKiller == pkKiller->GetPlayerID()){
						if (GetQuestFlag("qDeathMatchPanel.same_killer") >= 4){
							ChatPacket(CHAT_TYPE_INFO, "%s isimli oyuncuya 5 defa ustuste oldugun icin eventten cikarildin", pkKiller->GetName());

							if (IsAffectFlag(AFF_STUN))
								RemoveAffect(AFFECT_STUN);

							CDeathMatchManager::instance().ResetScore(this);
							CDeathMatchManager::instance().SwitchToSpectator(this);
						}

						SetQuestFlag("qDeathMatchPanel.same_killer", GetQuestFlag("qDeathMatchPanel.same_killer") + 1);
					}
					else
						SetQuestFlag("qDeathMatchPanel.same_killer", 0);

					// Set as last killer
					SetQuestFlag("qDeathMatchPanel.last_killer", pkKiller->GetPlayerID());

					// Info
					if (iDMVictimKillAverage != 0)
						ChatPacket(CHAT_TYPE_INFO, "%s seni olduruldu ve 1 skor kaybettin. Skorun: -%d Olme miktarin: %d", pkKiller->GetName(), iDMVictimKillAverage, iDMVictimKillCount + 1);
					else
						ChatPacket(CHAT_TYPE_INFO, "%s seni olduruldu ve 1 skor kaybettin. Skorun: %d Olme miktarin: %d", pkKiller->GetName(), iDMVictimScore, iDMVictimKillCount + 1);


					// Extra bonus
					int iExtraBonus = 0;

					if (iDMVictimScore >= iDMKillerNewScore * 4)
						iExtraBonus += 5;
					else if (iDMVictimScore >= iDMKillerNewScore * 3)
						iExtraBonus += 3;
					else if (iDMVictimScore >= iDMKillerNewScore * 2)
						iExtraBonus += 2;

					if (iExtraBonus > 0 && iDMVictimScore > 5 && iDMKillerNewScore > 5){
						CDeathMatchManager::instance().SetScore(pkKiller->GetPlayerID(), iDMKillerNewScore + iExtraBonus);
						pkKiller->ChatPacket(CHAT_TYPE_INFO, "Senden guclu bir oyuncuyu oldurdun ve %d ekstra bonus kazandin.", iExtraBonus);
					}
				}

				// Check killer score with highscore
				CDeathMatchManager::instance().CheckHighScore(pkKiller->GetPlayerID());
			}
		}
#endif


---

Search:

		if (IsPC())
		{
			pEventInfo->isPC = true;
			pEventInfo->dwID = this->GetPlayerID();

			m_pkDeadEvent = event_create(dead_event, pEventInfo, PASSES_PER_SEC(180));
		}

Change:
#ifdef DEATHMATCH_MODE
		if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		{
			pEventInfo->isPC = true;

			if (IsPC())
				pEventInfo->dwID = this->GetPlayerID();
			else
				pEventInfo->dwID = this->GetVID();

			m_pkDeadEvent = event_create(dead_event, pEventInfo, PASSES_PER_SEC(180));
		}
		else if (IsPC())
#else
		if (IsPC())
#endif
		{
			pEventInfo->isPC = true;
			pEventInfo->dwID = this->GetPlayerID();

			m_pkDeadEvent = event_create(dead_event, pEventInfo, PASSES_PER_SEC(180));
		}

---

Search:
			if (pAttacker->GetPoint(POINT_MANA_BURN_PCT))
			{
				if (number(1, 100) <= pAttacker->GetPoint(POINT_MANA_BURN_PCT))
					PointChange(POINT_SP, -50);
			}

Add it under:
#ifdef DEATHMATCH_MODE
			if (GetMapIndex() == DEATMATCH_MAP_INDEX){
				if (pAttacker->IsPC() && IsPC()){
					// Check event stat
					if (CDeathMatchManager::instance().GetStatus() != DEATHMATCH_STARTED /* && !pAttacker->IsGM() */){
						pAttacker->ChatPacket(CHAT_TYPE_INFO, "Deathmarch event do without an active you can not attack on this map");
						SendDamagePacket(pAttacker, 0, DAMAGE_BLOCK);
						return false;
					}

					// Bonus damage stuffs
					int iDMKillerScore = CDeathMatchManager::instance().GetScore(pAttacker->GetPlayerID());
					int iDMVictimScore = CDeathMatchManager::instance().GetScore(GetPlayerID());

					if (iDMVictimScore >= iDMKillerScore * 4)
						dam += dam * 20 / 100;
					else if (iDMVictimScore >= iDMKillerScore * 3)
						dam += dam * 10 / 100;
					else if (iDMVictimScore >= iDMKillerScore * 2)
						dam += dam * 5 / 100;
				}
			}
#endif

---

Search:
	if (bPKMode == PK_MODE_GUILD && !GetGuild())
		bPKMode = PK_MODE_FREE;

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (IsGM())
			bPKMode = PK_MODE_PROTECT;
		else
			bPKMode = PK_MODE_FREE;
	}
#endif
