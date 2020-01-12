#include "stdafx.h"
#include "constants.h"
#include "config.h"
#include "questmanager.h"
#include "start_position.h"
#include "packet.h"
#include "buffer_manager.h"
#include "log.h"
#include "char.h"
#include "char_manager.h"
#include "DeathMatch.h"
#include "desc.h"
#include "sectree_manager.h"
#include "battle.h"
#include "item.h"

bool CDeathMatchManager::Initialize()
{
	m_map_char.clear();
	dwWinnerPID = 0;

	SetStatus(DEATHMATCH_FINISH);

	return true;
}

void CDeathMatchManager::Destroy()
{
	CloseEvent();
	dwWinnerPID = 0;

	m_map_char.clear();

	SetStatus(DEATHMATCH_FINISH);
}

DeathMatchStatus CDeathMatchManager::GetStatus()
{
	BYTE ret = quest::CQuestManager::instance().GetEventFlag("deathmatch_status");

	switch (ret)
	{
	case 0:
		return DEATHMATCH_FINISH;

	case 1:
		return DEATHMATCH_OPEN;

	case 2:
		return DEATHMATCH_STARTED;

	case 3:
		return DEATHMATCH_CLOSE;

	default:
		return DEATHMATCH_ERR;
	}

	return DEATHMATCH_ERR;
}

void CDeathMatchManager::SetStatus(DeathMatchStatus status)
{
	BYTE val = 0;

	switch (status)
	{
	case DEATHMATCH_OPEN:
		val = 1;
		break;

	case DEATHMATCH_STARTED:
		val = 2;
		break;

	case DEATHMATCH_CLOSE:
		val = 3;
		break;

	case DEATHMATCH_FINISH:
	case DEATHMATCH_ERR:
	default:
		val = 0;
		break;
	}
	quest::CQuestManager::instance().RequestSetEventFlag("deathmatch_status", val);
}

void CDeathMatchManager::CheckEventStatus(){
	if (quest::CQuestManager::instance().GetEventFlag("deathmatch_kill_limit") > 0)
	{
		if (dwWinnerPID)
		{
			LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwWinnerPID);
			if (pkChar)
			{
				LogWinner();

				ResetScore(pkChar);

				SetHighScore(0, 0);
				SetStatus(DEATHMATCH_FINISH);
			}
			else{
				sys_err("Unknown winner %u", pkChar->GetPlayerID());
			}
		}
		else if (GetAttenderCount() == 1){
			itertype(m_map_char) iter = m_map_char.begin();
			for (; iter != m_map_char.end(); ++iter)
			{
				LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);
				if (pkChar){
					dwWinnerPID = pkChar->GetPlayerID();
					LogWinner();

					ResetScore(pkChar);

					SetHighScore(0, 0);
					SetStatus(DEATHMATCH_FINISH);
				}
				break;
			}
		}
	}
	//ELSE ÝF attender count == 1
}

bool CDeathMatchManager::StartEvent()
{
	SetStatus(DEATHMATCH_STARTED);
	SendNotice("Deathmatch event has been stared");

	return true;
}

int CDeathMatchManager::GetScore(DWORD dwPID){
	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwPID);
	if (!pkChar)
		return 0;

	int iMy_score = pkChar->GetQuestFlag("qDeathMatchPanel.my_score");;
	return iMy_score;
}

void CDeathMatchManager::SetScore(DWORD dwPID, int iNewScore){
	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwPID);
	if (!pkChar){
		sys_err("Unknown PID: %u", dwPID);
		return;
	}

	if (iNewScore <= 0){
		sys_err("improper score: %d", iNewScore);
		return;
	}

	pkChar->SetQuestFlag("qDeathMatchPanel.my_score", iNewScore);
}

void CDeathMatchManager::NoticeScore(DWORD dwPID, int iScore){
	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwPID);
	if (!pkChar){
		sys_err("Unknown PID: %u", dwPID);
		return;
	}

	if (iScore <= 0){
		sys_err("improper score: %d", iScore);
		return;
	}

	char buf[64];
	snprintf(buf, sizeof(buf), "<DeathMatch> Player %s reached %d score", pkChar->GetName(), iScore);
	SendNotice(buf);
}

void CDeathMatchManager::SendScoreInfo(DWORD dwPID, int iScore){
	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwPID);
	if (!pkChar){
		sys_err("Unknown PID: %u", dwPID);
		return;
	}

	if (iScore <= 0){
		sys_err("improper score: %d", iScore);
		return;
	}

	pkChar->ChatPacket(CHAT_TYPE_INFO, "Your reached new score: %d", iScore);
}

int CDeathMatchManager::GetHighScore(){
	int iTmpHighScore = quest::CQuestManager::instance().GetEventFlag("deatmatch_high_score");
	if (!iTmpHighScore){
		sys_err("Improper Hightscore: %d", iTmpHighScore);
		return 0;
	}

	return iTmpHighScore;
}

DWORD CDeathMatchManager::GetHighScoreOwner(){
	DWORD dwTmpHighScorePID = (DWORD)quest::CQuestManager::instance().GetEventFlag("deatmatch_high_score_owner");
	if (!dwTmpHighScorePID){
		sys_err("Improper Hightscore PID: %u", dwTmpHighScorePID);
		return 0;
	}

	return dwTmpHighScorePID;
}

void CDeathMatchManager::SetHighScore(DWORD dwPID, int iNewScore){
	if (iNewScore < 0){
		sys_err("improper score: %d", iNewScore);
		return;
	}

	quest::CQuestManager::instance().RequestSetEventFlag("deatmatch_high_score", iNewScore);
	quest::CQuestManager::instance().RequestSetEventFlag("deatmatch_high_score_owner", dwPID);

	
	//if (test_server){
		if (dwPID && iNewScore){
			LPCHARACTER lpHighScoreOwner = CHARACTER_MANAGER::instance().FindByPID(dwPID);
			if (!lpHighScoreOwner)
				return;

			char szWinNotice[500];
			sprintf(szWinNotice, "New highscore: %d owner %s", iNewScore, lpHighScoreOwner->GetName());
			SendNotice(szWinNotice);


			if (iNewScore >= quest::CQuestManager::instance().GetEventFlag("deathmatch_kill_limit")){
				char szWinNotice[500];
				sprintf(szWinNotice, "Player: %s reached a %d score and finished event", lpHighScoreOwner->GetName(), iNewScore);
				SendNotice(szWinNotice);
				SetWinner(lpHighScoreOwner);
				CheckEventStatus();
			}
		}
	//}

}

void CDeathMatchManager::CheckHighScore(DWORD dwPID){
	if (!dwPID){
		sys_err("Unknown PID: %u", dwPID);
		return;
	}

	int iDMHighScore = GetHighScore();
	int iDMMyScore = GetScore(dwPID);

	if (iDMMyScore > iDMHighScore)
		SetHighScore(dwPID, iDMMyScore);
}

void CDeathMatchManager::SetWinner(LPCHARACTER x_pkChar)
{
	//Observer
	if (!x_pkChar)
		return;

	if (GetAttenderCount() <= 1){
		sys_err("Inadequate player");
		return;
	}

	if (!x_pkChar->IsPC())
		return;

	dwWinnerPID = x_pkChar->GetPlayerID();
}

bool CDeathMatchManager::Enter(LPCHARACTER pkChar)
{
	if (!pkChar) return false;

	if ((GetStatus() == DEATHMATCH_STARTED || GetStatus() == DEATHMATCH_FINISH) && !pkChar->IsGM())
	{
		sys_log(0, "Deathmatch Event info: event started or finished but non-GM char enter in event area %s", pkChar->GetName());
		return false;
	}

	//if (test_server){
		if (!pkChar->IsGM()){
			char szWinNotice[500];
			sprintf(szWinNotice, "Player: %s attended to Deathmatch event", pkChar->GetName());
			SendNotice(szWinNotice);
		}
	//}

	return EnterAttender(pkChar);
}

bool CDeathMatchManager::EnterAttender(LPCHARACTER pkChar)
{
	if (GetStatus() != DEATHMATCH_OPEN && !pkChar->IsGM())
	{
		sys_err("Deathmatch Event info: event isn't open but non-GM char enter in event area %s", pkChar->GetName());
		return false;
	}

	if (!pkChar->IsGM()){
		DWORD pid = pkChar->GetPlayerID();
		m_map_char.insert(std::make_pair(pid, pid));

		SpawnRandomPos(pkChar);
	}

	return true;
}

bool CDeathMatchManager::EnterSpectator(LPCHARACTER pkChar)
{
	if (!pkChar)
		return false;

	if (GetStatus() != DEATHMATCH_OPEN && !pkChar->IsGM())
	{
		sys_err("Deathmatch Event info: event isn't open but non-GM char enter in event area %s", pkChar->GetName());
		return false;
	}

	pkChar->SetQuestFlag("qDeathMatchPanel.is_observer", 1);

	if (pkChar->GetMapIndex() != 200)
		pkChar->WarpSet(95500, 12500, 200);

	//RemoveFromEvent(pkChar);
	DWORD pid = pkChar->GetPlayerID();
	m_map_miss.insert(std::make_pair(pid, pid));

	//if (test_server){
		char szWinNotice[500];
		sprintf(szWinNotice, "Player: %s attended as a spectator to Deathmatch event", pkChar->GetName());
		SendNotice(szWinNotice);
	//}

	return true;
}

void CDeathMatchManager::RemoveStuns(){
	itertype(m_map_char) iter = m_map_char.begin();

	LPCHARACTER pkChar = NULL;
	for (; iter != m_map_char.end(); ++iter)
	{
		LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);

		if (pkChar != NULL){
			if (pkChar->IsAffectFlag(AFF_STUN))
				pkChar->RemoveAffect(AFFECT_STUN);
			else
				sys_err("ERROR ! DON'T HAVE STUN IN %s", pkChar->GetName());
		}
	}
}

void CDeathMatchManager::SpawnRandomPos(LPCHARACTER pkChar){
	if (pkChar){
		PIXEL_POSITION pos;
		for (;;)
		{
			pos.x = number(pkChar->GetX() - 2000, pkChar->GetX() + 2000);
			pos.y = number(pkChar->GetY() - 1000, pkChar->GetY() + 1000);
			if (SECTREE_MANAGER::instance().IsMovablePosition(pkChar->GetMapIndex(), pos.x, pos.y))
			{
				pkChar->Show(pkChar->GetMapIndex(), pos.x, pos.y);
				pkChar->Stop();
				break;
			}
		}
	}
}

void CDeathMatchManager::ResetScore(LPCHARACTER pkChar){
	if (pkChar){
		pkChar->SetQuestFlag("qDeathMatchPanel.my_score", 0);		// Öldürülen oyuncu
		pkChar->SetQuestFlag("qDeathMatchPanel.kill_count", 0);		// Ölme miktarý
		pkChar->SetQuestFlag("qDeathMatchPanel.kill_average", 0);	// Skor 0da ölünce düþen miktar
		pkChar->SetQuestFlag("qDeathMatchPanel.last_killer", 0);	// Son öldüren oyuncunun pidi
		pkChar->SetQuestFlag("qDeathMatchPanel.same_killer", 0);	// last_killer ile yeni öldüren ayný kiþi ise artan deðer
		pkChar->SetQuestFlag("qDeathMatchPanel.IsInLoginned", 0);	// Evente giriþ durumu
		pkChar->SetQuestFlag("qDeathMatchPanel.is_observer", 0);	// Izleyici durumu

		//if (test_server){
			sys_log(0, "Player: %s scores has been reset", pkChar->GetName());
		//}
	}
}

void CDeathMatchManager::RemoveFromEvent(LPCHARACTER x_pkChar)
{
	//Observer
	if (!x_pkChar)
		return;

	if (m_map_char.size() <= 0)
		return;

	if (!x_pkChar->IsPC())
		return;

	DWORD dwPID = x_pkChar->GetPlayerID();
	m_map_char.erase(dwPID);

	if (m_map_char.size() == 1 && GetStatus() == DEATHMATCH_STARTED)
		CheckEventStatus();
}

bool CDeathMatchManager::SwitchToSpectator(LPCHARACTER x_pkChar)
{
	//Observer
	if (!x_pkChar)
		return true;

	if (m_map_char.size() <= 0)
		return true;

	if (!x_pkChar->IsPC())
		return true;

	DWORD dwPID = x_pkChar->GetPlayerID();
	m_map_char.erase(dwPID);
	m_map_miss.insert(std::make_pair(dwPID, dwPID));

	x_pkChar->SetObserverMode(true);

	sys_log(0, "%s switched to spectator. Remaining Player: %d", x_pkChar->GetName(), GetAttenderCount());

	if (GetAttenderCount() == 1)
		CheckEventStatus();
	
	return true;
}

bool CDeathMatchManager::CloseEvent()
{
	// Players
	itertype(m_map_char) iter = m_map_char.begin();

	LPCHARACTER pkChar = NULL;
	for (; iter != m_map_char.end(); ++iter)
	{
		LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);

		if (pkChar != NULL){
			if (pkChar->IsAffectFlag(AFF_STUN))
				pkChar->RemoveAffect(AFFECT_STUN);

			ResetScore(pkChar);
			pkChar->WarpSet(EMPIRE_START_X(pkChar->GetEmpire()), EMPIRE_START_Y(pkChar->GetEmpire()));
		}
	}

	m_map_char.clear();

	// Spectators
	itertype(m_map_miss) iter2 = m_map_miss.begin();

	for (; iter2 != m_map_miss.end(); ++iter2)
	{
		LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(iter2->second);

		if (pkChar != NULL){
			if (pkChar->IsAffectFlag(AFF_STUN))
				pkChar->RemoveAffect(AFFECT_STUN);

			pkChar->SetObserverMode(false);
			ResetScore(pkChar);
			pkChar->WarpSet(EMPIRE_START_X(pkChar->GetEmpire()), EMPIRE_START_Y(pkChar->GetEmpire()));
		}
	}

	m_map_miss.clear();
	dwWinnerPID = 0;

	return true;
}

bool CDeathMatchManager::LogWinner()
{
	if (!dwWinnerPID){
		sys_err("Winner not found in event!");
		return false;
	}

	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwWinnerPID);

	if (pkChar){
		//if (test_server){
			char szWinNotice[500];
			sprintf(szWinNotice, "%s won the Deathmatch event", pkChar->GetName());
			SendNotice(szWinNotice);
		//}

		LogManager::instance().CharLog(pkChar, 0, "DEATHMATCH", "LastManStanding");
	}

	return true;
}

bool CDeathMatchManager::GiveItemToAttender(DWORD dwItemVnum, BYTE count)
{
	if (m_map_char.size() <= 0){
		sys_err("DON'T HAVE PLAYER IN EVENT");
		return false;
	}
	
	if (!dwWinnerPID){
		sys_err("Winner not found in event!");
		return false;
	}

	LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(dwWinnerPID);
	if (pkChar)
	{
		LPITEM pkRewardItem = pkChar->AutoGiveItem(dwItemVnum, count);
		if (!pkRewardItem){
			sys_err("Winner: %s reward item([%dx]%u) isn't created.", pkChar->GetName(), count, dwItemVnum);
			return true;
		}
		else{
			quest::CQuestManager::Instance().SetCurrentItem(pkRewardItem);
		}

		if (pkChar->GetDesc()){
			//if (test_server){
				char szWinNotice[500];
				sprintf(szWinNotice, "Winner of the Deathmatch event: %s reward: [%dx]%s", pkChar->GetName(), count, pkRewardItem->GetName());
				SendNotice(szWinNotice);
			//}

			LogManager::instance().ItemLog(pkChar->GetPlayerID(), 0, count, dwItemVnum, "DEATHMATCH_REWARD", "", pkChar->GetDesc()->GetHostName(), dwItemVnum);
		}
	}

	return true;
}

bool CDeathMatchManager::IsLimitedItem(DWORD dwVnum)
{
	// Tau
	if (50800 > dwVnum && dwVnum <= 50826)
		return true;

	switch (dwVnum)
	{
		case 50020:
		case 50021:
		case 50022:
		case 50801:
		case 50802:
		case 50813:
		case 50814:
		case 50817:
		case 50818:
		case 50819:
		case 50820:
		case 50821:
		case 50822:
		case 50823:
		case 50824:
		case 50825:
		case 50826:
		case 71044:
		case 71055:
			return true;
	}

	return false;
}

