// 1) Search: int CInstanceBase::GetAlignment()
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
int CInstanceBase::GetTitleID()
{
	return m_iTitleID;
}
#endif


// 1) Search: SetAlignment(c_rkCreateData.m_sAlignment);
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	SetsTitle(c_rkCreateData.m_iTitleID);
#endif


// 1) Search: void CInstanceBase::SetAlignment(short sAlignment)
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CInstanceBase::SetsTitle(int iTitle)
{
	m_iTitleID = iTitle;
	RefreshTextTailTitle();
}
#endif


// 1) Search: m_sAlignment = 0;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_iTitleID = 0;
#endif