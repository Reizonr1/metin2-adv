// 1) Search:	int CInstanceBase::GetAlignmentType()
// 2) After their function make a new line and paste:

#ifdef ENABLE_TITLE_SYSTEM
int CInstanceBase::GetPrestige()
{
	return m_sPrestige;
}

UINT CInstanceBase::GetPrestigeGrade()
{
	int pTitle_vegas[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};	

	if (m_sPrestige == pTitle_vegas[1])
		return 0;
	else if (m_sPrestige == pTitle_vegas[2])
		return 1;
	else if (m_sPrestige == pTitle_vegas[3])
		return 2;
	else if (m_sPrestige == pTitle_vegas[4])
		return 3;
	else if (m_sPrestige == pTitle_vegas[5])
		return 4;
	else if (m_sPrestige == pTitle_vegas[6])
		return 5;
	else if (m_sPrestige == pTitle_vegas[7])
		return 6;
	else if (m_sPrestige == pTitle_vegas[8])
		return 7;
	else if (m_sPrestige == pTitle_vegas[9])
		return 8;
	else if (m_sPrestige == pTitle_vegas[10])
		return 9;
	else if (m_sPrestige == pTitle_vegas[11])
		return 10;
	else if (m_sPrestige == pTitle_vegas[12])
		return 11;
	else if (m_sPrestige == pTitle_vegas[13])
		return 12;
	else if (m_sPrestige == pTitle_vegas[14])
		return 13;
	else if (m_sPrestige == pTitle_vegas[15])
		return 14;
	else if (m_sPrestige == pTitle_vegas[16]) 
		return 15;
	else if (m_sPrestige == pTitle_vegas[17])
		return 16;
	else if (m_sPrestige == pTitle_vegas[18])
		return 17;
	else if (m_sPrestige == pTitle_vegas[19])
		return 18;
	else if (m_sPrestige == pTitle_vegas[0])
		return 19;
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search: 	m_sAlignment = 0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_sPrestige = 0;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	void CInstanceBase::SetAlignment(short sAlignment)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CInstanceBase::SetPrestige(short sPrestige)
{
	m_sPrestige = sPrestige;
	RefreshTextTailTitle();	
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search: 	SetAlignment(c_rkCreateData.m_sAlignment);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	SetPrestige(c_rkCreateData.m_sPrestige);
#endif
"""""""""""""""""""""""""""""""""""""""""