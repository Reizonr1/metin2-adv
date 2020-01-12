Search:
CSafebox::CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold) : m_pkChrOwner(pkChrOwner), m_iSize(iSize), m_lGold(dwGold)

Change:
#ifdef __OFFLINE_SHOP__
CSafebox::CSafebox(LPCHARACTER pkChrOwner, int iSize, uint64_t dwGold) : m_pkChrOwner(pkChrOwner), m_iSize(iSize), m_lGold(dwGold)
#else
CSafebox::CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold) : m_pkChrOwner(pkChrOwner), m_iSize(iSize), m_lGold(dwGold)
#endif

https://puu.sh/sgHzV/eb64e066cb.png

---

Search:
void CSafebox::Save()

Add it upper:
#ifdef __OFFLINE_SHOP__
void CSafebox::SetGold(int64_t llGold)
{
	m_lGold += llGold;

	TPacketGCSafeboxMoneyChange pack;
	pack.bHeader = HEADER_GC_SAFEBOX_MONEY_CHANGE;
	pack.lMoney = m_lGold;
	m_pkChrOwner->GetDesc()->Packet(&pack, sizeof(pack));
}
#else

https://puu.sh/sgHBl/6406f87fd5.png

---

Search:
void CSafebox::Save()
{
	TSafeboxTable t;

	memset(&t, 0, sizeof(TSafeboxTable));

	t.dwID = m_pkChrOwner->GetDesc()->GetAccountTable().id;
	t.dwGold = m_lGold;

	db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_SAVE, 0, &t, sizeof(TSafeboxTable));
	sys_log(1, "SAFEBOX: SAVE %s", m_pkChrOwner->GetName());
}

Add it under:
#endif

https://puu.sh/sgHCx/52bd35a7b5.png