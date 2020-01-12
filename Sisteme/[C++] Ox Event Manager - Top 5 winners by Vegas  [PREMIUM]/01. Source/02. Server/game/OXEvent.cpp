//1.) Search:
#include "desc.h"
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
//@version 0.0.1
	#include "db.h"
	#include "p2p.h"
	#include "guild.h"
	#include "item_manager.h"
	#include "item.h"
#endif

//1.) Search:
	m_timedEvent = NULL;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	m_counterEvent = NULL;
	m_map_answers.clear();
#endif

//1.) Search:
	CloseEvent();
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	m_map_answers.clear();
#endif

//1.) Search:
			if (pos.x < rect[0] || pos.x > rect[2] || pos.y < rect[1] || pos.y > rect[3])
			{
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
				COXEventManager::instance().TruncateAnswers(pkChar);
#endif

//1.) Search:
			else
			{
				pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("?????!"));
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
				COXEventManager::instance().InsertAnswers(pkChar);
#endif

//1.) Search:
bool COXEventManager::Quiz(unsigned char level, int timelimit)
{
	[........................]
}
//2.) Add below after function ends:
#ifdef ENABLE_FEATURES_OXEVENT
bool COXEventManager::IsLastManStanding()
{
	return (m_map_attender.size() == 1) ? true : false;
}

bool COXEventManager::IsExistKeyAnswers(LPCHARACTER pkChar, int * keyAnswers)
{
    itertype(m_map_answers) it = m_map_answers.find(pkChar->GetPlayerID());

	if (it == m_map_answers.end())
		return false;
	
	*keyAnswers = it->second;
}

void COXEventManager::TruncateAnswers(LPCHARACTER pkChar)
{
	m_map_answers.erase(pkChar->GetPlayerID());
}

void COXEventManager::InsertAnswers(LPCHARACTER pkChar)
{
	int keyAnswers = 0;
	int sumKeys = 0;

	if (!COXEventManager::instance().IsExistKeyAnswers(pkChar, &keyAnswers))
	{
		m_map_answers.insert(std::make_pair(pkChar->GetPlayerID(), OXEVENT_FIRST_ANSWER));
	}

	sumKeys = keyAnswers += 1;
	m_map_answers[pkChar->GetPlayerID()] = sumKeys;
	pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_correct_answers"), sumKeys);
}

std::string COXEventManager::GetGuildWinner(LPCHARACTER pkChar)
{
	CGuild * m_name = pkChar->GetGuild();
	return (m_name) ? m_name->GetName() : "EMPTY";
}

bool COXEventManager::IsExistVnum(DWORD dwItemVnum)
{
	return (ITEM_MANAGER::instance().GetTable(dwItemVnum)) ? true : false;	
}

bool COXEventManager::IsExistCount(BYTE count)
{
	return (count > 0 && count <= ITEM_MAX_COUNT) ? true : false;	
}

void COXEventManager::RefreshWinners()
{
	itertype(m_map_char) iter = m_map_char.begin();

	LPCHARACTER pkChar = NULL;
	for (; iter != m_map_char.end(); ++iter)
	{
		pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);

		if (pkChar != NULL)
			COXEventManager::instance().InitializePacket(pkChar);
	}	
}

void COXEventManager::RegisterWinner()
{
	if (COXEventManager::instance().IsLastManStanding())
	{
		itertype(m_map_attender) iter = m_map_attender.begin();

		for (; iter != m_map_attender.end(); ++iter)
		{
			LPCHARACTER pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->first);

			if (pkChar)
			{
				char szBuf[CHAT_MAX_LEN + 1];
				snprintf(szBuf, sizeof(szBuf), LC_TEXT("oxevent_announcement_winner"), pkChar->GetName());
				COXEventManager::instance().NoticeAll(szBuf);
				
				char szQuery[QUERY_MAX_LEN + 1];
				snprintf(szQuery, sizeof(szQuery), "INSERT INTO player.oxevent (name, level, empire, job, guild, date, correct_answers) VALUES('%s','%d','%d','%d','%s',NOW(),'%d')", pkChar->GetName(), pkChar->GetLevel(), pkChar->GetEmpire(), pkChar->GetJob(), COXEventManager::Instance().GetGuildWinner(pkChar).c_str(), m_map_answers[pkChar->GetPlayerID()]);
				DBManager::Instance().DirectQuery(szQuery);
				
				COXEventManager::instance().RefreshWinners();
			}
		}
	}
}

void COXEventManager::InitializePacket(LPCHARACTER pkChar)
{
	TPacketCGOxEventData p;
	p.header = HEADER_GC_OXEVENT;

	SQLMsg *extractList = DBManager::instance().DirectQuery("SELECT * FROM player.oxevent ORDER BY date DESC LIMIT %d", OXEVENT_TOP_LIMIT);
	MYSQL_ROW row;
	int i = 0;
			
	if(extractList->uiSQLErrno != 0)
		return;

	while ((row = mysql_fetch_row(extractList->Get()->pSQLResult)))
	{
		p.tempInfo[i] = TPacketCGOxEvent();
		strncpy(p.tempInfo[i].name, row[1], sizeof(p.tempInfo[i].name));
		str_to_number(p.tempInfo[i].level, row[2]);
		strncpy(p.tempInfo[i].guild, row[3], sizeof(p.tempInfo[i].guild));		
		str_to_number(p.tempInfo[i].empire, row[4]);
		str_to_number(p.tempInfo[i].job, row[5]);
		strncpy(p.tempInfo[i].date, row[6], sizeof(p.tempInfo[i].date));	
		str_to_number(p.tempInfo[i].correct_answers, row[7]);			
		i++;
	}

	if(extractList->Get()->uiNumRows < OXEVENT_TOP_LIMIT)
	{
		while (i < OXEVENT_TOP_LIMIT)
		{
			p.tempInfo[i] = TPacketCGOxEvent();
			strncpy(p.tempInfo[i].name, "", sizeof(p.tempInfo[i].name));
			p.tempInfo[i].level = OXEVENT_NO_DATA;
			strncpy(p.tempInfo[i].guild, "", sizeof(p.tempInfo[i].guild));
			p.tempInfo[i].empire = OXEVENT_NO_DATA;
			p.tempInfo[i].job = OXEVENT_NO_DATA;
			strncpy(p.tempInfo[i].date, "", sizeof(p.tempInfo[i].date));			
			p.tempInfo[i].correct_answers = OXEVENT_NO_DATA;
			i++;
		}
	}
	pkChar->GetDesc()->Packet(&p, sizeof(p));
}

void COXEventManager::NoticeAll(std::string msg)
{
	TPacketGGNotice p;
	p.bHeader = HEADER_GG_NOTICE;
	p.lSize = strlen(msg.c_str()) + 1;

	TEMP_BUFFER buf;
	buf.write(&p, sizeof(p));
	buf.write(msg.c_str(), p.lSize);

	P2P_MANAGER::instance().Send(buf.read_peek(), buf.size());

	SendNotice(msg.c_str());
}

void COXEventManager::GetErrByStatus(LPCHARACTER staff, int key)
{
	switch(key)
	{
		case OXEVENT_FINISH:
			staff->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_err_status_a")); 
			break;
		case OXEVENT_OPEN:
			staff->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_err_status_b")); 
			break;
		case OXEVENT_CLOSE:
			staff->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_err_status_c")); 
			break;
		case OXEVENT_QUIZ:
			staff->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_err_status_d")); 
			break;
		default:
			break;
	}
}

EVENTINFO(end_oxevent_info)
{
	int empty;

	end_oxevent_info() 
	: empty( 0 )
	{
	}
};

EVENTFUNC(end_oxevent)
{
	COXEventManager::instance().CloseEvent();
	return 0;
}

EVENTINFO(TOxEventCounterInfo)
{
    DynamicCharacterPtr pkChar;
    TOxEventCounterInfo() : pkChar(){}
};

void COXEventManager::Disconnect(LPCHARACTER pkChar)
{
	m_map_answers.erase(pkChar->GetPlayerID());
	m_map_char.erase(pkChar->GetPlayerID());
	m_map_attender.erase(pkChar->GetPlayerID());
}

EVENTFUNC(start_counter_oxevent)
{   
    TOxEventCounterInfo* info = dynamic_cast<TOxEventCounterInfo*>(event->info);
    
    if (info == NULL)
        return 0;
    
    LPCHARACTER pkChar = info->pkChar;
    
    if (pkChar == NULL)
        return 0;

	pkChar->ChatPacket(CHAT_TYPE_COMMAND, "oxevent_manager refresh %d %d", COXEventManager::instance().GetAttenderCount(), COXEventManager::instance().GetObserverCount());
	return PASSES_PER_SEC(3);
}
	
void COXEventManager::OpenGui(LPCHARACTER pkChar)
{
	if (m_counterEvent != NULL)
	{
		event_cancel(&m_counterEvent);
	}

	TOxEventCounterInfo* info = AllocEventInfo<TOxEventCounterInfo>();
	info->pkChar = pkChar;

	m_counterEvent = event_create(start_counter_oxevent, info, PASSES_PER_SEC(1));	
	pkChar->ChatPacket(CHAT_TYPE_COMMAND, "oxevent_manager open");
}

/*
bool COXEventManager::CheckPassword(LPCHARACTER pkChar, const char* c_szPassword)
{
}
*/

void COXEventManager::Manager(LPCHARACTER pkChar, const char* c_pData)
{
	TPacketCGOxEventManager * p = (TPacketCGOxEventManager *)c_pData;
	
	OXEventStatus resultKey = COXEventManager::instance().GetStatus();
	
	if (!pkChar)
		return;
	
	if (pkChar->GetMapIndex() != OXEVENT_MAP_INDEX)
		return;
	
	if (pkChar->GetGMLevel() != GM_IMPLEMENTOR)
		return;
	
	if (p->type > OXEVENT_FORCE_CLOSE_EVENT)
		return;
	
	switch(p->type)
	{
		case OXEVENT_OPEN_LOGIN:
		{
			if (strlen(p->password) > 12)
			{
				pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_wrong_password_length"));
				return;
			}

			if (strcmp(p->password, PASSWORD_MANAGER))
			{
				pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_wrong_password"));
				return;		
			}

			COXEventManager::instance().OpenGui(pkChar);
		}
		break;
			
		case OXEVENT_OPEN_EVENT:
		{
			if (resultKey == OXEVENT_FINISH)
			{
				COXEventManager::instance().ClearQuiz();
				
				char szFile[256];
				snprintf(szFile, sizeof(szFile), "%s/oxquiz.lua", LocaleService_GetBasePath().c_str());
				int result = lua_dofile(quest::CQuestManager::instance().GetLuaState(), szFile);
				
				if (result != 0)
				{
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_error_file_quiz"));	
					return;
				}
				else
				{
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_succes_file_quiz"));	
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_succes_start"));	

					COXEventManager::instance().SetStatus(OXEVENT_OPEN);
					COXEventManager::instance().NoticeAll(LC_TEXT("oxevent_start_message_1"));
					COXEventManager::instance().NoticeAll(LC_TEXT("oxevent_start_message_2"));
				}
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, resultKey);
		}
		break;
		
		case OXEVENT_CLOSE_GATES:
		{
			if (resultKey == OXEVENT_OPEN)
			{
				COXEventManager::instance().SetStatus(OXEVENT_CLOSE);
				COXEventManager::instance().NoticeAll(LC_TEXT("oxevent_close_gates"));
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, resultKey);	
		}
		break;
		
		case OXEVENT_CLOSE_EVENT:
		{
			if (resultKey == OXEVENT_CLOSE)
			{
				COXEventManager::instance().RegisterWinner();
				COXEventManager::instance().InitializePacket(pkChar);
				COXEventManager::instance().SetStatus(OXEVENT_FINISH);

				end_oxevent_info* info = AllocEventInfo<end_oxevent_info>();
				event_create(end_oxevent, info, PASSES_PER_SEC(15));
				
				COXEventManager::instance().NoticeAll(LC_TEXT("oxevent_finish"));
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, resultKey);	
		}
		break;
		
		case OXEVENT_ASK_QUESTION:
		{
			if (resultKey == OXEVENT_CLOSE)
			{
				bool ret = COXEventManager::instance().Quiz(1, 30);
				
				if (ret == false)
				{
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_fail_question"));	
					return;					
				}
				else
				{
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_succes_question"));	
				}
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, resultKey);	
		}
		break;
		
		case OXEVENT_REWARD_PLAYERS:
		{
			if (resultKey == OXEVENT_CLOSE)
			{
				if (!COXEventManager::instance().IsExistCount(p->count))
				{
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_fail_reward_count"));
					return;
				}
				
				if (COXEventManager::instance().IsExistVnum(p->vnum))
				{
					TItemTable * item = ITEM_MANAGER::instance().GetTable(p->vnum);
					
					DWORD count;

					char hyperlinks[512 + 1];
					snprintf(hyperlinks, sizeof(hyperlinks), "item:%x:%x:%x:%x:%x", p->vnum, item->dwFlags, 0, 0, 0);
					
					if (item->dwFlags == ITEM_FLAG_STACKABLE)
						count = p->count;
					else
						count = 1;

					char szBuf[512 + 1];
					snprintf(szBuf, sizeof(szBuf), "%s %d x |cffffc700|H%s|h[%s]|h|r", LC_TEXT("oxevent_reward_item_chat"), count, hyperlinks, item->szLocaleName);
					
					COXEventManager::instance().NoticeAll(szBuf);
					COXEventManager::instance().GiveItemToAttender(p->vnum, count);
				}
				else
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("oxevent_fail_reward_item"));	
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, resultKey);	
		}
		break;
		
		case OXEVENT_FORCE_CLOSE_EVENT:
		{
			if (resultKey != OXEVENT_FINISH)
			{
				COXEventManager::instance().CloseEvent();
				COXEventManager::instance().SetStatus(OXEVENT_FINISH);
				
				COXEventManager::instance().NoticeAll(LC_TEXT("oxevent_force_close"));
			}
			else
				COXEventManager::instance().GetErrByStatus(pkChar, OXEVENT_FINISH);	
		}
		break;		

		default:
			break;
	}
}
#endif