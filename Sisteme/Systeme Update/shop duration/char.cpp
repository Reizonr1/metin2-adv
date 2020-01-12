*char.cpp

Find - Bul:
m_pkMuyeongEvent = NULL;

Add it under- Altına ekle:
m_pkShopDurationEvent = NULL;



Find - Bul:
m_dwLoginPlayTime = 0;

Add it under- Altına ekle:
m_dwShopDuration = 0;
m_bShopDurationIsActive = 0;



Find - Bul:
	//DELAYED_WARP
	event_cancel(&m_pkWarpEvent);
	event_cancel(&m_pkCheckSpeedHackEvent);
	//END_DELAYED_WARP

Add it under- Altına ekle:
event_cancel(&m_pkShopDurationEvent);



Find - Bul:
//if (!LC_IsNewCIBN())
SetPolymorph(30000, true);

Add it under- Altına ekle:
	if (GetMapIndex() == 1 || GetMapIndex() == 21 || GetMapIndex() == 41){
		StartShopDuration();
		StartShopDurationEvent();
	}
	else{
		ChatPacket(CHAT_TYPE_INFO, "1.koyde olmadigin icin yang kazanamayacaksin"); //you can not won gold because this map isn't supported in event
	}



Find - Bul:
//if (!LC_IsNewCIBN())
SetPolymorph(GetJob(), true);

Add it under- Altına ekle:
if (GetMapIndex() == 1 || GetMapIndex() == 21 || GetMapIndex() == 41)
	CancelShopDuration();



Find - Bul:
int	CHARACTER::GetSkillPowerByLevel(int level, bool bMob) const
{
	return CTableBySkill::instance().GetSkillPowerByLevelFromType(GetJob(), GetSkillGroup(), MINMAX(0, level, SKILL_MAX_LEVEL), bMob);
}

Add it under- Altına ekle:

int CHARACTER::GetShopDuration(){
	return (get_dword_time() - m_dwShopDuration) / 1000 + 0.5;
}

void CHARACTER::CheckShopDuration(int time){
	if (!m_bShopDurationIsActive)
		return;

	if (time / 60 > 60){
		ChatPacket(CHAT_TYPE_INFO, "1 saattir pazarin acik oldugu icin 5M kazandin"); // you won 5M
		PointChange(POINT_GOLD, 5000000, false);
		DBManager::instance().SendMoneyLog(MONEY_LOG_QUEST, 1, 5000000);

		SetShopDuration();
	}
}

EVENTFUNC(shop_duration_event)
{
	char_event_info* info = dynamic_cast<char_event_info*>(event->info);
	if (info == NULL)
	{
		sys_err("shop_duration_event> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER	ch = info->ch;
	if (ch == NULL) { // <Factor>
		return 0;
	}

	ch->ChatPacket(CHAT_TYPE_INFO, "Pazar Aktif ! %d dakika sonra 5M Kazanacaksin !", abs(ch->GetShopDuration() / 60 - 60)); //shop active you won 5M after %d  minute later

	ch->CheckShopDuration(ch->GetShopDuration());

	return PASSES_PER_SEC(60); //1min
}

void CHARACTER::StartShopDurationEvent(){
	if (m_pkShopDurationEvent)
		return;

	char_event_info* info = AllocEventInfo<char_event_info>();

	info->ch = this;

	m_pkShopDurationEvent = event_create(shop_duration_event, info, PASSES_PER_SEC(60));
	SetShopDuration();
}

void CHARACTER::CancelShopDuration(){
	EndShopDuration();
	event_cancel(&m_pkShopDurationEvent);
}
