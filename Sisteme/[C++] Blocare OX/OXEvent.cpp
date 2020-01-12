Caută:
if (GetStatus() == OXEVENT_FINISH)
	{
		sys_log(0, "OXEVENT : map finished. but char enter. %s", pkChar->GetName());
		return false;
	}
	
Înlocuiește cu :
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
	if (GetStatus() == OXEVENT_FINISH && !pkChar->IsGM())
	{
		sys_log(0, "OXEVENT : map finished. but char enter. %s", pkChar->GetName());
		return false;
	}
#else
	if (GetStatus() == OXEVENT_FINISH)
	{
		sys_log(0, "OXEVENT : map finished. but char enter. %s", pkChar->GetName());
		return false;
	}
#endif
Caută:
else if (pos.x == 896300 && pos.y == 28900)
	{
		return EnterAudience(pkChar);
	}

Înlocuiește cu :
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
	else if (pos.x == 896300 && pos.y == 28900 || pkChar->IsGM())
	{
		return EnterAudience(pkChar);
	}
#else
	else if (pos.x == 896300 && pos.y == 28900)
	{
		return EnterAudience(pkChar);
	}
#endif

Caută:
SetStatus(OXEVENT_QUIZ);
Adaugă sub:
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
	itertype(m_map_attender) iter = m_map_attender.begin();

	LPCHARACTER pkChar = NULL;
	for (; iter != m_map_attender.end(); ++iter) {
		pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);

		if (pkChar){
			if (!pkChar->IsGM()){
				if (pkChar->IsAffectFlag(AFF_INVISIBILITY)){
					sys_err("%s already invisible", pkChar->GetName());
				}
				else {
					pkChar->AddAffect(AFFECT_INVISIBILITY, POINT_NONE, 0, AFF_INVISIBILITY, 30, 0, true);
					pkChar->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You passed the Invisible mode! You will continue this way until you answer the question."));
				}
			}
		}
	}

	itertype(m_map_char) iter2 = m_map_char.begin();

	LPCHARACTER pkChar2 = NULL;
	for (; iter2 != m_map_char.end(); ++iter2) {
		pkChar2 = CHARACTER_MANAGER::instance().FindByPID(iter2->second);

		if (pkChar2){
			if (pkChar2->IsGM()){
				pkChar2->ChatPacket(CHAT_TYPE_COMMAND, "MakeVisibleOX");
			}
		}
	}
#endif
Caută:
pkChar = CHARACTER_MANAGER::instance().FindByPID(iter->second);
		if (pkChar != NULL)
		{
			
Adaugă sub:
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
			if (!pkChar->IsGM()){
				if (pkChar->IsAffectFlag(AFF_INVISIBILITY)){
					pkChar->RemoveAffect(AFFECT_INVISIBILITY);
				}
				else{
					sys_err("%s isn't invisible", pkChar->GetName());
				}
			}
			else {
				pkChar->ChatPacket(CHAT_TYPE_COMMAND, "RemoveTitleOX");
			}
#endif

