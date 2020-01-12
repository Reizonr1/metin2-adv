//Find:
	m_ppyGameWindow = NULL;
//Add below(up to it):
#ifdef ITEM_BUFF_SYSTEM
	m_kMap_dwAffectIndexToSkillIndex.insert(make_pair(int(CInstanceBase::AFFECT_RESIST_BUFF), 97));
	m_kMap_dwAffectIndexToSkillIndex.insert(make_pair(int(CInstanceBase::AFFECT_CRITICAL_BUFF), 98));	
	m_kMap_dwAffectIndexToSkillIndex.insert(make_pair(int(CInstanceBase::AFFECT_REFLECT_BUFF), 99));
#endif