//Search in this file:
	struct FKillSectree2
	{
		void operator () (LPENTITY ent)
		{
			if (ent->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER ch = (LPCHARACTER) ent;
				if (!ch->IsPC() && !ch->IsPet())
					ch->Dead();
			}
		}
	};
	
//Replace with:

	struct FKillSectree2
	{
		void operator () (LPENTITY ent)
		{
			if (ent->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER ch = (LPCHARACTER) ent;
#ifdef NEW_PET_SYSTEM
				if (!ch->IsPC() && !ch->IsPet() && !ch->IsNewPet())
#else
				if (!ch->IsPC() && !ch->IsPet())
#endif
					ch->Dead();
			}
		}
	};
	
//Search in this file:

		void operator () (LPENTITY ent)
		{
			if (true == ent->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER pChar = static_cast<LPCHARACTER>(ent);

				if (pChar == ExceptChar)
					return;			
				if (!pChar->IsPet() && (true == pChar->IsMonster() || true == pChar->IsStone()))
				{
					if (x1 <= pChar->GetX() && pChar->GetX() <= x2 && y1 <= pChar->GetY() && pChar->GetY() <= y2)
					{
						M2_DESTROY_CHARACTER(pChar);
					}
				}
			}
		}
		
//Replace with:

		void operator () (LPENTITY ent)
		{
			if (true == ent->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER pChar = static_cast<LPCHARACTER>(ent);

				if (pChar == ExceptChar)
					return;
#ifdef NEW_PET_SYSTEM
				if (!pChar->IsPet() && !pChar->IsNewPet() && (true == pChar->IsMonster() || true == pChar->IsStone()))
#else				
				if (!pChar->IsPet() && (true == pChar->IsMonster() || true == pChar->IsStone()))
#endif
				{
					if (x1 <= pChar->GetX() && pChar->GetX() <= x2 && y1 <= pChar->GetY() && pChar->GetY() <= y2)
					{
						M2_DESTROY_CHARACTER(pChar);
					}
				}
			}
		}
		
		