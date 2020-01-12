//Search in cmd_gm.cpp:
		if (pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)
		{
			M2_DESTROY_CHARACTER(pkChr);
		}
		
//Replace with:

#ifdef NEW_PET_SYSTEM
		if (pkChr->IsNPC() && !pkChr->IsPet() && !pkChr->IsNewPet() && pkChr->GetRider() == NULL)
#else
		if (pkChr->IsNPC() && !pkChr->IsPet() && pkChr->GetRider() == NULL)
#endif
		{
			M2_DESTROY_CHARACTER(pkChr);
		}