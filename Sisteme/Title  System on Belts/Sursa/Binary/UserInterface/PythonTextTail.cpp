// 1) Search:
/*
const float c_fyGuildNamePosition = 15.0f;
const float c_fyMarkPosition = 15.0f + 11.0f;
*/
// 2) And replace with:
#ifdef ENABLE_TITLE_SYSTEM
const float c_fyGuildNamePosition = 25.0f;
const float c_fyMarkPosition = 25.0f + 11.0f;
const float c_fysTitlePosition = 12.0f;
const float c_fyGuildNamePositionOld = 15.0f;
const float c_fyMarkPositionOld = 15.0f + 11.0f;
#else
const float c_fyGuildNamePosition = 15.0f;
const float c_fyMarkPosition = 15.0f + 11.0f;
#endif


// 1) Search:
/*
	for (itor = m_CharacterTextTailList.begin(); itor != m_CharacterTextTailList.end(); ++itor)
	{
		TTextTail * pTextTail = *itor;
		float fxAdd = 0.0f;
		CGraphicMarkInstance * pMarkInstance = pTextTail->pMarkInstance;
		CGraphicTextInstance * pGuildNameInstance = pTextTail->pGuildNameTextInstance;
		if (pMarkInstance && pGuildNameInstance)
		{
			int iWidth, iHeight;
			int iImageHalfSize = pMarkInstance->GetWidth()/2 + c_fxMarkPosition;
			pGuildNameInstance->GetTextSize(&iWidth, &iHeight);
			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			pGuildNameInstance->Update();
		}
*/
// 2) And replace with:
	for (itor = m_CharacterTextTailList.begin(); itor != m_CharacterTextTailList.end(); ++itor)
	{
		TTextTail * pTextTail = *itor;
		float fxAdd = 0.0f;
#ifdef ENABLE_TITLE_SYSTEM
		CGraphicTextInstance * psTitleNameInstance = pTextTail->psTitleNameTextInstance;
		if (psTitleNameInstance)
		{
			int iWidth, iHeight;
			psTitleNameInstance->GetTextSize(&iWidth, &iHeight);
			psTitleNameInstance->SetPosition(pTextTail->x, pTextTail->y - c_fysTitlePosition, pTextTail->z);
			psTitleNameInstance->Update();
		}
#endif
		CGraphicMarkInstance * pMarkInstance = pTextTail->pMarkInstance;
		CGraphicTextInstance * pGuildNameInstance = pTextTail->pGuildNameTextInstance;
		if (pMarkInstance && pGuildNameInstance)
		{
			int iWidth, iHeight;
			int iImageHalfSize = pMarkInstance->GetWidth()/2 + c_fxMarkPosition;
			pGuildNameInstance->GetTextSize(&iWidth, &iHeight);
#ifdef ENABLE_TITLE_SYSTEM
			if (!psTitleNameInstance)
			{
				pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPositionOld);
				pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePositionOld, pTextTail->z);
			}
			else
			{
				pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
				pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			}
#else
			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
#endif
			pGuildNameInstance->Update();
		}


// 1) Search: pTextTail->pTextInstance->Render();
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		if (pTextTail->psTitleNameTextInstance)
		{
			pTextTail->psTitleNameTextInstance->Render();
		}
#endif


// 1) Search: pTextInstance->SetVerticalAlign(CGraphicTextInstance::VERTICAL_ALIGN_BOTTOM);
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pTextTail->psTitleNameTextInstance=NULL;
#endif


// 1) Search: pTextTail->pMarkInstance = NULL;
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pTextTail->psTitleNameTextInstance = NULL;
#endif


// 1) Search:
/*
	if (pTextTail->pMarkInstance)
	{
		CGraphicMarkInstance::Delete(pTextTail->pMarkInstance);
		pTextTail->pMarkInstance = NULL;
	}
*/
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	if (pTextTail->psTitleNameTextInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->psTitleNameTextInstance);
		pTextTail->psTitleNameTextInstance = NULL;
	}
#endif


// 1) Search: void CPythonTextTail::AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor)
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CPythonTextTail::AttachsTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor)
{
	if (!bPKTitleEnable)
		return;
	
	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;
	
	TTextTail * pTextTail = itor->second;
	CGraphicTextInstance *& prTitleNameInstance = pTextTail->psTitleNameTextInstance;
	if (!prTitleNameInstance)
	{
		prTitleNameInstance = CGraphicTextInstance::New();
		prTitleNameInstance->SetTextPointer(ms_pFont);
		prTitleNameInstance->SetOutline(true);
		prTitleNameInstance->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_CENTER);
		prTitleNameInstance->SetVerticalAlign(CGraphicTextInstance::VERTICAL_ALIGN_BOTTOM);
	}
	
	prTitleNameInstance->SetValue(c_szName);
	prTitleNameInstance->SetColor(c_rColor.r, c_rColor.g, c_rColor.b);
	prTitleNameInstance->Update();
}

void CPythonTextTail::DetachsTitle(DWORD dwVID)
{
	if (!bPKTitleEnable)
		return;
	
	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;
	
	TTextTail * pTextTail = itor->second;
	if (pTextTail->psTitleNameTextInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->psTitleNameTextInstance);
		pTextTail->psTitleNameTextInstance = NULL;
	}
}
#endif