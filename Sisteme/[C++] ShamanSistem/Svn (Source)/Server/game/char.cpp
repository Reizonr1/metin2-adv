// Check this:

#include "skill_power.h"
#include "XTrapManager.h"
#include "buff_on_attributes.h"

// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	#include "SupportSystem.h"
#endif

// Check this:

	m_HackShieldCheckEvent = NULL;
	m_HackShieldCheckMode = false;

	m_bIsLoadedAffect = false;
	cannot_dead = false;
	
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	m_supportSystem = 0;
	m_dwSupportHair = 0;
	m_dwSupportWeapon = 0;
	m_dwSupportCostume = 0;
	m_bIsSupport = false;
	m_Owner = NULL;
#endif

// Check this:

	if (m_pkDungeon)
	{
		SetDungeon(NULL);
	}
	
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	if (m_supportSystem)
	{
		m_supportSystem->Destroy();
		delete m_supportSystem;

		m_supportSystem = 0;
	}
#endif

// Check this:

void CHARACTER::UpdatePacket()

// Check this:

	pack.bMovingSpeed	= GetLimitPoint(POINT_MOV_SPEED);
	pack.bAttackSpeed	= GetLimitPoint(POINT_ATT_SPEED);
	pack.bStateFlag	= m_bAddChrState;
	pack.dwAffectFlag[0] = m_afAffectFlag.bits[0];
	pack.dwAffectFlag[1] = m_afAffectFlag.bits[1];
	pack.dwGuildID	= 0;
	pack.sAlignment	= m_iAlignment / 10;
	
// Add above:
#ifdef ENABLE_SUPPORT_SYSTEM
	if(IsSupport())
	{
		pack.awPart[CHR_EQUIPPART_ARMOR] = GetSupportArmor();
		pack.awPart[CHR_EQUIPPART_WEAPON] = GetSupportWeapon();
		pack.awPart[CHR_EQUIPPART_HAIR] = GetSupportHair();
	}	
#endif

// Check this:

	if (GetHorseLevel() > 0)
		UpdateHorseDataByLogoff(t->logoff_interval);

	thecore_memcpy(m_aiPremiumTimes, t->aiPremiumTimes, sizeof(t->aiPremiumTimes));

	m_dwLogOffInterval = t->logoff_interval;

	sys_log(0, "PLAYER_LOAD: %s PREMIUM %d %d, LOGGOFF_INTERVAL %u PTR: %p", t->name, m_aiPremiumTimes[0], m_aiPremiumTimes[1], t->logoff_interval, this);

	if (GetGMLevel() != GM_PLAYER)
	{
		LogManager::instance().CharLog(this, GetGMLevel(), "GM_LOGIN", "");
		sys_log(0, "GM_LOGIN(gmlevel=%d, name=%s(%d), pos=(%d, %d)", GetGMLevel(), GetName(), GetPlayerID(), GetX(), GetY());
	}
	
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	if (m_supportSystem)
	{
		m_supportSystem->Destroy();
		delete m_supportSystem;
	}

	m_supportSystem = M2_NEW CSupportSystem(this);
#endif

// Check this:

void CHARACTER::SendMovePacket(BYTE bFunc, BYTE bArg, DWORD x, DWORD y, DWORD dwDuration, DWORD dwTime, int iRot)

// Add under the whole function:

#ifdef ENABLE_SUPPORT_SYSTEM
void CHARACTER::SendSupportSkillPacket(DWORD skill_vnum)
{
	TPacketGCSupportUseSkill pack;
	pack.bHeader = HEADER_GC_SUPPORT_SKILL;
	pack.dwVnum = skill_vnum;
	pack.dwVid = GetVID();
	pack.dwLevel = 41;
	
	PacketView(&pack, sizeof(TPacketGCSupportUseSkill), this);
}
#endif

// Check this:

DWORD CHARACTER::GetNextExp() const

// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
DWORD CHARACTER::SupportGetNextExp() const
{
	if (120 < GetLevel())
		return 2500000000;
	else
		return exp_support_table[GetLevel()];
}
#endif


// Check:

void CHARACTER::EncodeInsertPacket(LPENTITY entity)
{

// Check:

	if (IsPet())
		
// Edit like this:

	if (IsPet() || IsSupport())

// If you have got new pet system change like this:

	if (IsPet() || IsSupport() || IsNewPet())
		
	
// Check:
bool CHARACTER::Follow(LPCHARACTER pkChr, float fMinDistance)
{

// Check this:


	if (pkChr->IsState(pkChr->m_stateMove) && 
		GetMobBattleType() != BATTLE_TYPE_RANGE && 
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet())
		
// Edit like this:


	if (pkChr->IsState(pkChr->m_stateMove) && 
		GetMobBattleType() != BATTLE_TYPE_RANGE && 
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet() && false == IsSupport())

		
// If you have got new pet system change like this:

	if (pkChr->IsState(pkChr->m_stateMove) && 
		GetMobBattleType() != BATTLE_TYPE_RANGE && 
		GetMobBattleType() != BATTLE_TYPE_MAGIC &&
		false == IsPet() && false == IsSupport() && false == IsNewPet())
