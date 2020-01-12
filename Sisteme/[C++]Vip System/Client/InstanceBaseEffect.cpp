Cauti:

void CInstanceBase::__AttachEmpireEffect(DWORD eEmpire)

Iar sub :
	
	if (pkInstMain->IsGameMaster())
	{
	}

Adaugi:	
	
#ifdef __ONEX_VIP__
	else if (pkInstMain->IsVIP())
	{
	}
#endif

Tot in functia asta cauti dupa: else

	if (IsGameMaster())
		return;
	
iar sub el adaugi:

#ifdef __ONEX_VIP__
	if (IsVIP())
		return;
#endif

--------------------------------------------
cauti:

void CInstanceBase::__SetAffect(UINT eAffect, bool isVisible)

iar sub :
		case AFFECT_YMIR:
			if (IsAffect(AFFECT_INVISIBILITY))
				return;
			break;
			
adaugi:

#ifdef __ONEX_VIP__
		case AFFECT_VIP:
			if (IsAffect(AFFECT_INVISIBILITY))
				return;
			break;
#endif
