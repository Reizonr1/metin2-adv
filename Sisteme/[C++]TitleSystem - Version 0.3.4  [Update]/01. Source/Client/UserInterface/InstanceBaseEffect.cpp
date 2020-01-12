// 1) Search: 
D3DXCOLOR g_akD3DXClrTitle[CInstanceBase::TITLE_NUM];
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
D3DXCOLOR g_akD3DXClrTitlePrestige[CInstanceBase::TITLE_NUM_PRESTIGE];
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search: 
std::map<int, std::string> g_TitleNameMap;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
std::map<int, std::string> g_TitlePrestigeNameMap;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search: 
bool CInstanceBase::RegisterTitleColor(UINT uIndex, UINT r, UINT g, UINT b)
{
	if (uIndex>=TITLE_NUM)
		return false;

	g_akD3DXClrTitle[uIndex]=__RGBToD3DXColoru(r, g, b);
	return true;	
}
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
bool CInstanceBase::RegisterTitlePrestigeColor(UINT uIndex, UINT r, UINT g, UINT b)
{
	if (uIndex>=TITLE_NUM_PRESTIGE)
		return false;

	g_akD3DXClrTitlePrestige[uIndex]=__RGBToD3DXColoru(r, g, b);
	return true;	
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	void CInstanceBase::RefreshTextTail()
// 2) Delete their function and paste:
void CInstanceBase::RefreshTextTail()
{
	CPythonTextTail::Instance().SetCharacterTextTailColor(GetVirtualID(), GetNameColor());

	int iAlignmentGrade = GetAlignmentGrade();
	if (TITLE_NONE == iAlignmentGrade)
	{
		CPythonTextTail::Instance().DetachTitle(GetVirtualID());
	}
	else
	{
		std::map<int, std::string>::iterator itor = g_TitleNameMap.find(iAlignmentGrade);
		if (g_TitleNameMap.end() != itor)
		{
			const std::string & c_rstrTitleName = itor->second;
			CPythonTextTail::Instance().AttachTitle(GetVirtualID(), c_rstrTitleName.c_str(), GetTitleColor());
		}
	}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef ENABLE_TITLE_SYSTEM
	int iPrestigeGrade = GetPrestigeGrade();	
	
	if (TITLE_NONE_PRESTIGE == iPrestigeGrade)
	{
		CPythonTextTail::Instance().DetachPrestige_(GetVirtualID());
	}
	else
		{
		std::map<int, std::string>::iterator itor2_vegas = g_TitlePrestigeNameMap.find(iPrestigeGrade);
		if (g_TitlePrestigeNameMap.end() != itor2_vegas)
		{
			const std::string & c_rstrTitlePrestigeName = itor2_vegas->second;
			CPythonTextTail::Instance().AttachPrestige_(GetVirtualID(), c_rstrTitlePrestigeName.c_str(), GetTitlePrestigeColor());
		}
	}
#endif	
}
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	const D3DXCOLOR& CInstanceBase::GetTitleColor()
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
const D3DXCOLOR& CInstanceBase::GetTitlePrestigeColor()
{
	UINT uGradePrestige = GetPrestigeGrade();
	if ( uGradePrestige >= TITLE_NUM_PRESTIGE)
	{
		static D3DXCOLOR s_kD3DXClrTitlePrestigeDefault(0xffffffff);
		return s_kD3DXClrTitlePrestigeDefault;
	}

	return g_akD3DXClrTitlePrestige[uGradePrestige];
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	void CInstanceBase::RegisterTitleName(int iIndex, const char * c_szTitleName)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CInstanceBase::RegisterTitlePrestigeName(int iIndex, const char * c_szTitlePrestigeName)
{
	g_TitlePrestigeNameMap.insert(make_pair(iIndex, c_szTitlePrestigeName));
}
#endif
"""""""""""""""""""""""""""""""""""""""""