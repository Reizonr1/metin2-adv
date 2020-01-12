//1.0 suchen:
int CInstanceBase::GetAlignmentType()
{
	switch (GetAlignmentGrade())
	{
		case 0:
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
		{
			return ALIGNMENT_TYPE_WHITE;
			break;
		}

		case 7:
		case 8:
		case 9:
		case 10:
		case 11:
		case 12:
		{
			return ALIGNMENT_TYPE_DARK;
			break;
		}

		case 6:
		{
			return ALIGNMENT_TYPE_NORMAL;
			break;
		}
	}
}
//1.0 dahinter:
#ifdef ENABLE_VIP_SYSTEM
int CInstanceBase::GetVip()
{
	return m_sVip;
}
#endif

//1.1 suchen:
	SetAlignment(c_rkCreateData.m_sAlignment);
//1.1 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	SetVip(c_rkCreateData.m_sVip);
#endif	

//1.2 suchen:
void CInstanceBase::SetAlignment(short sAlignment)
{
	m_sAlignment = sAlignment;
	RefreshTextTailTitle();
}
//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
void CInstanceBase::SetVip(short sVip)
{
	m_sVip = sVip;
}
#endif

//1.3 suchen:
	m_sAlignment = 0;
//1.3 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	m_sVip = 0;
#endif	

