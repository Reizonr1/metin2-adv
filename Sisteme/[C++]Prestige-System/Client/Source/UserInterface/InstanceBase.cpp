// Suche :
		SetWeapon(c_rkCreateData.m_dwWeapon);
// Füge darunter das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
		SetPrestigeLevel(c_rkCreateData.m_byPrestige);
#endif

// Suche :
	if (!IsGuildWall())
// Nach der if findet ihr das :
	AttachTextTail();
// Das Ersetzt ihr mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
	if (GetPrestigeLevel())
		AttachTextTail(GetPrestigeLevel());
	else
		AttachTextTail();
#else
	AttachTextTail();
#endif
	
// Suche :
void CInstanceBase::ChangeGuild(DWORD dwGuildID)
// Ersetze die ganze Funktion mit :
void CInstanceBase::ChangeGuild(DWORD dwGuildID)
{
	m_dwGuildID=dwGuildID;

	DetachTextTail();

#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
	if (GetPrestigeLevel())
		AttachTextTail(GetPrestigeLevel());
	else
		AttachTextTail();
#else
	AttachTextTail();
#endif

	RefreshTextTail();
}

// Füge am ende der Datei das hinzu :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
void CInstanceBase::RefreshPrestigeTextTail()
{
	DetachTextTail();
#ifdef ENABLE_NEW_PRESTIGE_SYSTEM == 1
	if (GetPrestigeLevel())
		AttachTextTail(GetPrestigeLevel());
	else
		AttachTextTail();
#else
	AttachTextTail();
#endif
	RefreshTextTail();
}
#endif