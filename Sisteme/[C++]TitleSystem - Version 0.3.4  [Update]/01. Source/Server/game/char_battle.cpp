// 1) Search:
LPCHARACTER CHARACTER::GetProtege() const
{
	if (m_pkChrStone)
		return m_pkChrStone;

	if (m_pkParty)
		return m_pkParty->GetLeader();

	return NULL;
}
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
int CHARACTER::GetTitle() const
{
	return m_iPrestige;
}

int CHARACTER::GetRealTitle() const	
{
	return m_iRealPrestige;	
}
	
void CHARACTER::ShowTitle(bool bShow)
{
	if (bShow)	{
		if (m_iPrestige != m_iRealPrestige)	{
			m_iPrestige = m_iRealPrestige;
			UpdatePacket();	}	}
	else	{
		if (m_iPrestige != 0)	{
			m_iPrestige = 0;
			UpdatePacket();	}	}
}

void CHARACTER::UpdateTitle(int iAmount)	{
	bool bShow = false;

	if (m_iPrestige == m_iRealPrestige)
		bShow = true;

	int i = m_iPrestige;
	m_iRealPrestige = MINMAX(0, m_iRealPrestige + iAmount, 19);
	if (bShow)	{
		m_iPrestige = m_iRealPrestige;
		if (i != m_iPrestige)
			UpdatePacket();	}
}
#endif
"""""""""""""""""""""""""""""""""""""""""