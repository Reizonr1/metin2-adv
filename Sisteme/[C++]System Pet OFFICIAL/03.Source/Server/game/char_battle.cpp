//Seatch this in char_battle.cpp:
#include "threeway_war.h"
#include "BlueDragon.h"
#include "DragonLair.h"

//Add after this:
#ifdef NEW_PET_SYSTEM
#include "New_PetSystem.h"
#endif

//Seatch this in char_battle.cpp:
bool CHARACTER::Damage(LPCHARACTER pAttacker, int dam, EDamageType type) // returns true if dead
{
	
//Add after
#ifdef NEW_PET_SYSTEM
	if (IsImmortal())
		return false;
#endif


//Seatch this in char_battle.cpp:
	if (test_server)
	{
		if (quest::CQuestManager::instance().GetEventFlag("exp_bonus_log") && iBaseExp>0)
			to->ChatPacket(CHAT_TYPE_INFO, "exp bonus %d%%", (iExp-iBaseExp)*100/iBaseExp);
	}

	iExp = AdjustExpByLevel(to, iExp);
	
//Add After This(If you don't use MartySama Source):
#ifdef NEW_PET_SYSTEM
	if (to->GetNewPetSystem()) {
		if (to->GetNewPetSystem()->IsActivePet() && to->GetNewPetSystem()->GetLevelStep() < 4) {
			int tmpexp = iExp * 9 / 20;
			iExp = iExp - tmpexp;
			to->GetNewPetSystem()->SetExp(tmpexp, 0);
		}
	}
#endif

// If you are using MartySama Source Search:
	iExp = AdjustExpByLevel(to, iExp);
	if (test_server)
		to->ChatPacket(CHAT_TYPE_INFO, "exp+minGNE+adjust(%d)", iExp);

//Add after this:
#ifdef NEW_PET_SYSTEM
	if (to->GetNewPetSystem()) {
		if (to->GetNewPetSystem()->IsActivePet() && to->GetNewPetSystem()->GetLevelStep() < 4) {
			int tmpexp = iExp * 9 / 20;
			iExp = iExp - tmpexp;
			to->GetNewPetSystem()->SetExp(tmpexp, 0);
		}
	}
#endif

