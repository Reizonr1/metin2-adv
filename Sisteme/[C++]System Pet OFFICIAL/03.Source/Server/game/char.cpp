//Search this code in char.cpp:
#ifdef __PET_SYSTEM__
#include "PetSystem.h"
#endif

//Add after this:
#ifdef NEW_PET_SYSTEM
#include "New_PetSystem.h"
#endif

//Search this code in char.cpp:
	m_fSyncTime = get_float_time()-3;
	m_dwPlayerID = 0;

//Add after this:
#ifdef NEW_PET_SYSTEM
	m_stImmortalSt = 0;

	m_newpetskillcd[0] = 0;
	m_newpetskillcd[1] = 0;
	m_newpetskillcd[2] = 0;
#endif

//Search this code in char.cpp:
#ifdef __PET_SYSTEM__
	m_petSystem = 0;
	m_bIsPet = false;
#endif

//Add after this:
#ifdef NEW_PET_SYSTEM
	m_newpetSystem = 0;
	m_bIsNewPet = false;
	m_eggvid = 0;
#endif

//Search this code in char.cpp:
#ifdef __PET_SYSTEM__
	if (m_petSystem)
	{
		m_petSystem->Destroy();
		delete m_petSystem;

		m_petSystem = 0;
	}
#endif

//Add after this:
#ifdef NEW_PET_SYSTEM
	if (m_newpetSystem)
	{
		m_newpetSystem->Destroy();
		delete m_newpetSystem;

		m_newpetSystem = 0;
	}
#endif

//Search this code in char.cpp:
	if (IsPet())
	{
		pack.bMovingSpeed	= 150;
	}

//Replace with:
#ifdef NEW_PET_SYSTEM
	if (IsPet() || IsNewPet())
#else
	if (IsPet())
#endif
	{
		pack.bMovingSpeed	= 150;
	}
	
//Search this code in char.cpp:
		if (IsPC() == true && (LC_IsEurope() == true || LC_IsCanada() == true || LC_IsSingapore() == true))
		{
			addPacket.dwLevel = GetLevel();
		}
		
//Replace with:
#ifdef NEW_PET_SYSTEM
		if (IsPC() == true || IsNewPet() == true)
#else
		if (IsPC() == true && (LC_IsEurope() == true || LC_IsCanada() == true || LC_IsSingapore() == true))
#endif
		{
			addPacket.dwLevel = GetLevel();
		}
		
//Search this code in char.cpp:
	pack.bStateFlag	= m_bAddChrState;
	pack.dwAffectFlag[0] = m_afAffectFlag.bits[0];
	pack.dwAffectFlag[1] = m_afAffectFlag.bits[1];
	pack.dwGuildID	= 0;
	pack.sAlignment	= m_iAlignment / 10;
//Add After this:
#ifdef NEW_PET_SYSTEM
	pack.dwLevel = GetLevel();
#endif

//Search this code in char.cpp:
	pack2 = pack;
	pack2.dwGuildID = 0;
	pack2.sAlignment = 0;

//Add After this:
#ifdef NEW_PET_SYSTEM
	pack2.dwLevel = 0;
#endif

//Search this code in char.cpp:
#ifdef __PET_SYSTEM__
	// NOTE: ?? ???? PC? ???? PetSystem? ??? ?. ?? ??? ??? ?????? NPC?? ?? ?..
	if (m_petSystem)
	{
		m_petSystem->Destroy();
		delete m_petSystem;
	}

	m_petSystem = M2_NEW CPetSystem(this);
#endif

//Add After this:
#ifdef NEW_PET_SYSTEM
	if (m_newpetSystem)
	{
		m_newpetSystem->Destroy();
		delete m_newpetSystem;
	}

	m_newpetSystem = M2_NEW CNewPetSystem(this);
#endif

//Search this code in char.cpp:
		else
			pack.amount = 0;

		if (!bBroadcast)
			GetDesc()->Packet(&pack, sizeof(struct packet_point_change));
		else
			PacketAround(&pack, sizeof(pack));
	}
}

//Add After this:
#ifdef NEW_PET_SYSTEM
void CHARACTER::SendPetLevelUpEffect(int vid, int type, int value, int amount) {
	struct packet_point_change pack;

	pack.header = HEADER_GC_CHARACTER_POINT_CHANGE;
	pack.dwVID = vid;
	pack.type = type;
	pack.value = value;
	pack.amount = amount;
	PacketAround(&pack, sizeof(pack));
}
#endif

//Search this code in char.cpp:
	if (IsGuardNPC())
	{
		if (5000 < DISTANCE_APPROX(m_pkMobInst->m_posLastAttacked.x - GetX(), m_pkMobInst->m_posLastAttacked.y - GetY()))
			if (Return())
				return true;
	}
	if (pkChr->IsState(pkChr->m_stateMove) && 
		GetMobBattleType() != BATTLE_TYPE_RANGE && 
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet())
		
//Replace with:
	if (IsGuardNPC())
	{
		if (5000 < DISTANCE_APPROX(m_pkMobInst->m_posLastAttacked.x - GetX(), m_pkMobInst->m_posLastAttacked.y - GetY()))
			if (Return())
				return true;
	}
#ifdef NEW_PET_SYSTEM
	if (pkChr->IsState(pkChr->m_stateMove) &&
		GetMobBattleType() != BATTLE_TYPE_RANGE &&
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet() && false == IsNewPet())
#else
	if (pkChr->IsState(pkChr->m_stateMove) && 
		GetMobBattleType() != BATTLE_TYPE_RANGE && 
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet())
#endif

//Search this code in char.cpp:
DWORD CHARACTER::GetNextExp() const
{
	if (PLAYER_EXP_TABLE_MAX < GetLevel())
		return 2500000000;
	else
		return exp_table[GetLevel()];
}

//Add after this:
#ifdef NEW_PET_SYSTEM
DWORD CHARACTER::PetGetNextExp() const
{
	if (IsNewPet()) {
		if (120 < GetLevel())
			return 2500000000;
		else
			return exppet_table[GetLevel()];
	}
}
#endif


