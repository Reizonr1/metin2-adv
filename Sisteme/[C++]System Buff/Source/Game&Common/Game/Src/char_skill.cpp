//Find:
//Be aware it should be member of bool CHARACTER::UseSkill(DWORD dwVnum, LPCHARACTER pkVictim, bool bUseGrandMaster)	
	if (false == CanUseSkill(dwVnum))
		return false;
//Add after(down to the function I metioned below):
#ifdef ITEM_BUFF_SYSTEM		
	if (pkVictim)
	{
	if(pkVictim != this && pkVictim->IsAffectFlag(AFF_RESIST_BUFF) && (dwVnum == SKILL_HOSIN))
		return false;
	else if(this && IsAffectFlag(AFF_RESIST_BUFF) && (dwVnum == SKILL_HOSIN) && (pkVictim == this))
		return false;
	}

	if (pkVictim)
	{
	if(pkVictim != this && pkVictim->IsAffectFlag(AFF_CRITICAL_BUFF) && (dwVnum == SKILL_GICHEON))
		return false;
	else if(this && IsAffectFlag(AFF_CRITICAL_BUFF) && (dwVnum == SKILL_GICHEON) && (pkVictim == this))
		return false; 
	}

	if (pkVictim)
	{
	if(pkVictim != this && pkVictim->IsAffectFlag(AFF_REFLECT_BUFF) && (dwVnum == SKILL_REFLECT))
		return false;
	else if(this && IsAffectFlag(AFF_REFLECT_BUFF) && (dwVnum == SKILL_REFLECT) && (pkVictim == this))
		return false; 	
	}		
#endif		