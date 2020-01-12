// Check this:

static DWORD __GetPartyExpNP(const DWORD level)
{
	if (!level || level > PLAYER_EXP_TABLE_MAX)
		return 14000;
	return party_exp_distribute_table[level];
}

// Add above:

#ifdef ENABLE_SUPPORT_SYSTEM
	#include "SupportSystem.h"
#endif

// Check this:

static void GiveExp(

// Change the whole function with this:

static void GiveExp(LPCHARACTER from, LPCHARACTER to, int iExp)
{
	// ??? ??? ????
	iExp = CALCULATE_VALUE_LVDELTA(to->GetLevel(), from->GetLevel(), iExp);

	// ?? ??? ?? ??? 3? ???
	if (distribution_test_server)
		iExp *= 3;

	int iBaseExp = iExp;

	// ??, ?? ??? ??? ??
	iExp = iExp * (100 + CPrivManager::instance().GetPriv(to, PRIV_EXP_PCT)) / 100;

	// ??? ?? ???? ??? ???
	{
		// ??? ??
		if (to->IsEquipUniqueItem(UNIQUE_ITEM_LARBOR_MEDAL))
			iExp += iExp * 20 /100;

		// ???? ??? ???
		if (to->GetMapIndex() >= 660000 && to->GetMapIndex() < 670000)
			iExp += iExp * 20 / 100; // 1.2? (20%)

		// ??? ??? ?? ??
		if (to->GetPoint(POINT_EXP_DOUBLE_BONUS))
			if (number(1, 100) <= to->GetPoint(POINT_EXP_DOUBLE_BONUS))
				iExp += iExp * 30 / 100; // 1.3? (30%)

		// ??? ?? (2????)
		if (to->IsEquipUniqueItem(UNIQUE_ITEM_DOUBLE_EXP))
			iExp += iExp * 50 / 100;

		switch (to->GetMountVnum())
		{
			case 20110:
			case 20111:
			case 20112:
			case 20113:
				if (to->IsEquipUniqueItem(71115) || to->IsEquipUniqueItem(71117) || to->IsEquipUniqueItem(71119) ||
						to->IsEquipUniqueItem(71121) )
				{
					iExp += iExp * 10 / 100;
				}
				break;

			case 20114:
			case 20120:
			case 20121:
			case 20122:
			case 20123:
			case 20124:
			case 20125:
				// ??? ??? ???
				iExp += iExp * 30 / 100;
				break;
		}
	}

	// ??? ? ?? ??? ???
	{
		// ??? ?: ??? ??
		if (to->GetPremiumRemainSeconds(PREMIUM_EXP) > 0)
		{
			iExp += (iExp * 50 / 100);
		}

		if (to->IsEquipUniqueGroup(UNIQUE_GROUP_RING_OF_EXP) == true)
		{
			iExp += (iExp * 50 / 100);
		}

		// PC? ?? ?? ???
		if (to->GetPoint(POINT_PC_BANG_EXP_BONUS) > 0)
		{
			if (to->IsPCBang() == true)
				iExp += (iExp * to->GetPoint(POINT_PC_BANG_EXP_BONUS)/100);
		}

		// ?? ???
		iExp += iExp * to->GetMarriageBonus(UNIQUE_ITEM_MARRIAGE_EXP_BONUS) / 100;
	}

	iExp += (iExp * to->GetPoint(POINT_RAMADAN_CANDY_BONUS_EXP)/100);
	iExp += (iExp * to->GetPoint(POINT_MALL_EXPBONUS)/100);
	iExp += (iExp * to->GetPoint(POINT_EXP)/100);

/*	if (speed_server)
	{
		iExp += iExp * CSpeedServerManager::ExpBonus();

	}
*/
	if (test_server)
	{
		sys_log(0, "Bonus Exp : Ramadan Candy: %d MallExp: %d PointExp: %d",
				to->GetPoint(POINT_RAMADAN_CANDY_BONUS_EXP),
				to->GetPoint(POINT_MALL_EXPBONUS),
				to->GetPoint(POINT_EXP)
			   );
	}

	// ??? ??? 2005.04.21 ?? 85%
	iExp = iExp * CHARACTER_MANAGER::instance().GetMobExpRate(to) / 100;

	// ??? ?? ??? ??
	iExp = MIN(to->GetNextExp() / 10, iExp);

	if (test_server)
	{
		if (quest::CQuestManager::instance().GetEventFlag("exp_bonus_log") && iBaseExp>0)
			to->ChatPacket(CHAT_TYPE_INFO, "exp bonus %d%%", (iExp-iBaseExp)*100/iBaseExp);
		to->ChatPacket(CHAT_TYPE_INFO, "exp(%d) base_exp(%d)", iExp, iBaseExp);
	}

	iExp = AdjustExpByLevel(to, iExp);
#ifdef ENABLE_NEW_PET_SYSTEM
	if (to->GetNewPetSystem()) {
		if (to->GetNewPetSystem()->IsActivePet() && to->GetNewPetSystem()->GetLevelStep() < 4) {
			int tmpexp = iExp * 9 / 20;
			iExp = iExp - tmpexp;
			to->GetNewPetSystem()->SetExp(tmpexp, 0);
		}
	}
#endif
#ifdef ENABLE_SUPPORT_SYSTEM
	if (to->GetSupportSystem()) {
		if (to->GetSupportSystem()->IsActiveSupport() && to->GetSupportSystem()->GetLevel() < 120) {
			int tmpexp = iExp * 9 / 20;
			iExp = iExp - tmpexp;
			to->GetSupportSystem()->SetExp(tmpexp);
		}
	}
#endif
	to->PointChange(POINT_EXP, iExp, true);
	from->CreateFly(FLY_EXP, to);

	{
		LPCHARACTER you = to->GetMarryPartner();
		// ??? ?? ????? ??? ???
		if (you)
		{
			// 1?? 100%
			DWORD dwUpdatePoint = 2000*iExp/to->GetLevel()/to->GetLevel()/3;

			if (to->GetPremiumRemainSeconds(PREMIUM_MARRIAGE_FAST) > 0 ||
					you->GetPremiumRemainSeconds(PREMIUM_MARRIAGE_FAST) > 0)
				dwUpdatePoint = (DWORD)(dwUpdatePoint * 3);

			marriage::TMarriage* pMarriage = marriage::CManager::instance().Get(to->GetPlayerID());

			// DIVORCE_NULL_BUG_FIX
			if (pMarriage && pMarriage->IsNear())
				pMarriage->Update(dwUpdatePoint);
			// END_OF_DIVORCE_NULL_BUG_FIX
		}
	}
}