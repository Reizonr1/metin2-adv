//1.0 suchen:
void CHARACTER::ShowAlignment(bool bShow)
{
	if (bShow)
	{
		if (m_iAlignment != m_iRealAlignment)
		{
			m_iAlignment = m_iRealAlignment;
			UpdatePacket();
		}
	}
	else
	{
		if (m_iAlignment != 0)
		{
			m_iAlignment = 0;
			UpdatePacket();
		}
	}
}

//1.0 dahinter:
#ifdef ENABLE_VIP_SYSTEM
int CHARACTER::GetVip() const
{
	return m_iVip;
}

int CHARACTER::GetRealVip() const
{
	return m_iRealVip;
}

void CHARACTER::ShowVip(bool bShow)
{
	if (bShow)
	{
		if (m_iVip != m_iRealVip)
		{
			m_iVip = m_iRealVip;
			UpdatePacket();
		}
	}
	else
	{
		if (m_iVip != 0)
		{
			m_iVip = 0;
			UpdatePacket();
		}
	}
}

void CHARACTER::ResetVip()
{
	m_iVip = 0;
	m_iRealVip = 0;
	UpdatePacket();
}

void CHARACTER::SetVip(int VIP_LEVEL)
{
	m_iVip = VIP_LEVEL;
	UpdatePacket();
}
#endif

