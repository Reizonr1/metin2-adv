// 1) Search: bool g_isEmpireNameMode=false;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
const int iMaxSTitle = POINT_TITLE_20 - POINT_TITLE;
std::map<int, std::string> g_sTitleNameMap;
D3DXCOLOR g_akD3DXClrsTitle[iMaxSTitle];
#endif


// 1) Search: void CInstanceBase::RefreshTextTail()
// 2) At the end of their function before: }
// 3) Make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	if (IsPC())
	{
		int iTitle = GetTitleID();
		if (!iTitle)
		{
			CPythonTextTail::Instance().DetachsTitle(GetVirtualID());
		}
		else
		{
			std::map<int, std::string>::iterator itor = g_sTitleNameMap.find(iTitle);
			if (g_sTitleNameMap.end() != itor)
			{
				const std::string & c_rstrTitleName = itor->second;
				CPythonTextTail::Instance().AttachsTitle(GetVirtualID(), c_rstrTitleName.c_str(), GetsTitleColor(iTitle));
			}
		}
	}
#endif


// 1) Search: bool CInstanceBase::RegisterTitleColor(UINT uIndex, UINT r, UINT g, UINT b)
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CInstanceBase::RegistersTitleName(int iIndex, const char * c_szTitleName)
{
	if (iIndex > iMaxSTitle)
		return;
	
	g_sTitleNameMap.insert(make_pair(iIndex, c_szTitleName));
}

bool CInstanceBase::RegistersTitleColor(int iIndex, UINT r, UINT g, UINT b)
{
	if (iIndex > iMaxSTitle)
		return false;
	
	g_akD3DXClrsTitle[iIndex]=__RGBToD3DXColoru(r, g, b);
	return true;
}

const D3DXCOLOR& CInstanceBase::GetsTitleColor(int iTitle)
{
	if (iTitle > iMaxSTitle)
	{
		static D3DXCOLOR s_kD3DXClrTitleDefault(0xffffffff);
		return s_kD3DXClrTitleDefault;
	}
	
	return g_akD3DXClrsTitle[iTitle];
}
#endif