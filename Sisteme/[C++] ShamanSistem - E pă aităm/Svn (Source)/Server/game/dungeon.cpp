//1. Search: if (!ch->IsPC() && !ch->IsPet())
	
//change with:
				if (!ch->IsPC() && !ch->IsPet() && !ch->IsNewPet() && !ch->IsSupport())

//2. Search: if (!ch->IsPC() && !ch->IsPet())
	
//change with:
				if (!ch->IsPC() && !ch->IsPet() && !ch->IsNewPet() && !ch->IsSupport())
				{