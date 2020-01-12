*char.cpp

Find - Bul:
m_pkMuyeongEvent = NULL;

Add it under- Altına ekle:
m_pkLogonEvent = NULL;
m_iLogonIsRewarded = 0;



Find - Bul:
m_dwLoginPlayTime = 0;

Add it under- Altına ekle:
m_dwLogonTime = get_dword_time();



Find - Bul:
	//DELAYED_WARP
	event_cancel(&m_pkWarpEvent);
	event_cancel(&m_pkCheckSpeedHackEvent);
	//END_DELAYED_WARP
	
Add it under- Altına ekle:
event_cancel(&m_pkLogonEvent);



Find - Bul:
int	CHARACTER::GetSkillPowerByLevel(int level, bool bMob) const
{
	return CTableBySkill::instance().GetSkillPowerByLevelFromType(GetJob(), GetSkillGroup(), MINMAX(0, level, SKILL_MAX_LEVEL), bMob); 
}

Add it under- Altına ekle:
DWORD CHARACTER::GetLogonTime(){
	return (get_dword_time() - m_dwLogonTime) / 1000 + 0.5; //now - logon_time -> convert ms to sec > convert float to int
}

void CHARACTER::CheckLogonTime(int time){
	if (time / 60 > 180 && !m_iLogonIsRewarded){
		ChatPacket(CHAT_TYPE_INFO, "3 saattir oyunda oldugun icin 10M kazandin"); //You are won 10M for that 3 hours in the game
		PointChange(POINT_GOLD, 10000000, false); //10.000.000
		DBManager::instance().SendMoneyLog(MONEY_LOG_QUEST, 1, 10000000);

		m_iLogonIsRewarded = 1;
	}

	ChatPacket(CHAT_TYPE_COMMAND, "ClientLogonUpdate %d", time / 60);
}

EVENTFUNC(logontime_check_event)
{
	char_event_info* info = dynamic_cast<char_event_info*>(event->info);
	if (info == NULL)
	{
		sys_err("logontime_check_event> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER	ch = info->ch;
	if (ch == NULL) { // <Factor>
		return 0;
	}

	ch->CheckLogonTime(ch->GetLogonTime());

	return PASSES_PER_SEC(60); //1min
}

void CHARACTER::InitCharLogonEvent(){
	if (m_pkLogonEvent)
		return;

	if (m_iLogonIsStarted != 1) {
		ChatPacket(CHAT_TYPE_COMMAND, "ClientLogonStart 0");
		m_iLogonIsStarted = 1;
	}

	char_event_info* info = AllocEventInfo<char_event_info>();

	info->ch = this;

	m_pkLogonEvent = event_create(logontime_check_event, info, PASSES_PER_SEC(60));
}