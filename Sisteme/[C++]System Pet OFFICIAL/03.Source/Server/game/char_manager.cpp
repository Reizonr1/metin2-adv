//Search in char_manager.cpp:
	if (ch->IsNPC() && !ch->IsPet() && ch->GetRider() == NULL)

//Replace with:
#ifdef NEW_PET_SYSTEM
	if (ch->IsNPC() && !ch->IsPet() && !ch->IsNewPet() && ch->GetRider() == NULL)
#else
	if (ch->IsNPC() && !ch->IsPet() && ch->GetRider() == NULL)
#endif