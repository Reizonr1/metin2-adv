//Find:
	RemoveAffect(SKILL_JEOKRANG);
	RemoveAffect(SKILL_CHEONGRANG);
//Or if you don't have wolfman:
	RemoveAffect(SKILL_GICHEON);
//Add after(down to it):
#ifdef ITEM_BUFF_SYSTEM
	RemoveAffect(SKILL_RESIST_BUFF);
	RemoveAffect(SKILL_CRITICAL_BUFF);
	RemoveAffect(SKILL_REFLECT_BUFF);
#endif
//Find:
//Be aware it should be member of: bool CHARACTER::IsGoodAffect(BYTE bAffectType) const
		case (SKILL_CHEONGRANG):
//Of you don't have wolfman:
		case (SKILL_GICHEON):
//Add after(down to it):
#ifdef ITEM_BUFF_SYSTEM
		case (SKILL_RESIST_BUFF):
		case (SKILL_CRITICAL_BUFF):
		case (SKILL_REFLECT_BUFF):
#endif		