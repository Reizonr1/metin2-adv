/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
// void CInstanceBase::__SetAffect(UINT eAffect, bool isVisible) Arat�l�r Ve ��erisinde :
// case AFFECT_YMIR: Bulunur . break; Alt�na Eklenir :

#ifdef ENABLE_GM_AFFECTS			
		case AFFECT_YMIR_MOD:
			if (IsAffect(AFFECT_INVISIBILITY))
				return;			
			break;
			
		case AFFECT_YMIR_SGM:
			if (IsAffect(AFFECT_INVISIBILITY))
				return;		
			break;
			
		case AFFECT_YMIR_GA:
			if (IsAffect(AFFECT_INVISIBILITY))
				return;			
			break;
#endif

/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */