cauti:

BOOL CInstanceBase::IsGameMaster()
{
	if (m_kAffectFlagContainer.IsSet(AFFECT_YMIR))
		return true;
	return false;
}

iar sub adaugi:

#ifdef __ONEX_VIP__
BOOL CInstanceBase::IsVIP()
{
	if (m_kAffectFlagContainer.IsSet(AFFECT_VIP))
		return true;
	return false;
}
#endif


cauti :

BOOL CInstanceBase::IsSameEmpire(CInstanceBase& rkInstDst)
{
iar sub:

	if (IsGameMaster())
		return TRUE;
adaugi:

#ifdef __ONEX_VIP__
	if (IsVIP())
		return TRUE;
#endif

sub:
	if (rkInstDst.IsGameMaster())
		return TRUE;

adaugi:
	
#ifdef __ONEX_VIP__
	if (rkInstDst.IsVIP())
		return TRUE;
#endif

-----------------------------------------------------------------

