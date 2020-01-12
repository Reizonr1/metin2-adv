// Suche :
				m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
// Ersetze :
				AttachTextTail();
// Mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
				if (GetPrestigeLevel())
					AttachTextTail(GetPrestigeLevel());
				else
					AttachTextTail();
#else
				AttachTextTail();
#endif


// Suche :
void CInstanceBase::AttachTextTail()
// Ersetze das mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
void CInstanceBase::AttachTextTail(BYTE bPrestige)
#else
void CInstanceBase::AttachTextTail()
#endif

// Suche in der Funktion :
		CPythonTextTail::Instance().RegisterCharacterTextTail(m_dwGuildID, dwVID, s_kD3DXClrTextTail, fTextTailHeight);
// Ersetze das mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
	if (bPrestige < 0)
		CPythonTextTail::Instance().RegisterCharacterTextTail(m_dwGuildID, dwVID, s_kD3DXClrTextTail, fTextTailHeight);
	else
		CPythonTextTail::Instance().RegisterCharacterTextTail(m_dwGuildID, dwVID, s_kD3DXClrTextTail, fTextTailHeight, bPrestige);
#else
	CPythonTextTail::Instance().RegisterCharacterTextTail(m_dwGuildID, dwVID, s_kD3DXClrTextTail, fTextTailHeight);
#endif

// Suche :
void CInstanceBase::RefreshTextTail()
// Ersetzt die ganze Funktion mit :
void CInstanceBase::RefreshTextTail()
{
	CPythonTextTail::Instance().SetCharacterTextTailColor(GetVirtualID(), GetNameColor());

	int iAlignmentGrade = GetAlignmentGrade();
	if (TITLE_NONE == iAlignmentGrade)
	{
#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
		if (GetPrestigeLevel() <= 0)
			CPythonTextTail::Instance().DetachTitle(GetVirtualID());
		else
		{
			D3DXCOLOR test(0xffffffff);
			CPythonTextTail::Instance().AttachTitle(GetVirtualID(), "", test, GetPrestigeLevel());
		}
#else
		CPythonTextTail::Instance().DetachTitle(GetVirtualID());
#endif
	}
	else
	{
		std::map<int, std::string>::iterator itor = g_TitleNameMap.find(iAlignmentGrade);
		if (g_TitleNameMap.end() != itor)
		{
			const std::string & c_rstrTitleName = itor->second;
#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
			CPythonTextTail::Instance().AttachTitle(GetVirtualID(), c_rstrTitleName.c_str(), GetTitleColor(), GetPrestigeLevel());
#else
			CPythonTextTail::Instance().AttachTitle(GetVirtualID(), c_rstrTitleName.c_str(), GetTitleColor());
#endif
		}
	}
}

