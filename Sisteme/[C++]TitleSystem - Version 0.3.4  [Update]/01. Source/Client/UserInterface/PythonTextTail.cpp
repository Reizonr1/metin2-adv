// 1) Search:
		if (pTextTail->pLevelTextInstance)
		{
			pTextTail->pLevelTextInstance->Render();
		}
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		if (pTextTail->pVegaS_TitleText_tInstance)
		{
			pTextTail->pVegaS_TitleText_tInstance->Render();
		}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search in function: void CPythonTextTail::RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight)
	pTextTail->pLevelTextInstance=NULL;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pTextTail->pVegaS_TitleText_tInstance=NULL;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search in function: CPythonTextTail::TTextTail * CPythonTextTail::RegisterTextTail(DWORD dwVirtualID, const char * c_szText, CGraphicObjectInstance * pOwner, float fHeight, const D3DXCOLOR & c_rColor)
	pTextTail->pLevelTextInstance = NULL;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pTextTail->pVegaS_TitleText_tInstance = NULL;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:
	if (pTextTail->pLevelTextInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->pLevelTextInstance);
		pTextTail->pLevelTextInstance = NULL;
	}
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	if (pTextTail->pVegaS_TitleText_tInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->pVegaS_TitleText_tInstance);
		pTextTail->pVegaS_TitleText_tInstance = NULL;
	}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	void CPythonTextTail::DetachTitle(DWORD dwVID)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CPythonTextTail::AttachPrestige_(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor)
{
	if (!bPKTitleEnable)
		return;

	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;

	TTextTail * pTextTail = itor->second;

	CGraphicTextInstance *& prMrVegaS = pTextTail->pVegaS_TitleText_tInstance;
	if (!prMrVegaS)
	{
		prMrVegaS = CGraphicTextInstance::New();
		prMrVegaS->SetTextPointer(ms_pFont);
		prMrVegaS->SetOutline(true);

		prMrVegaS->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_CENTER);
		prMrVegaS->SetVerticalAlign(CGraphicTextInstance::VERTICAL_ALIGN_BOTTOM);
	}

	prMrVegaS->SetValue(c_szName);
	prMrVegaS->SetColor(c_rColor.r, c_rColor.g, c_rColor.b);
	prMrVegaS->Update();
}

void CPythonTextTail::DetachPrestige_(DWORD dwVID)
{
	if (!bPKTitleEnable)
		return;

	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;

	TTextTail * pTextTail = itor->second;

	if (pTextTail->pVegaS_TitleText_tInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->pVegaS_TitleText_tInstance);
		pTextTail->pVegaS_TitleText_tInstance = NULL;
	}
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:			CGraphicTextInstance * pGuildNameInstance = pTextTail->pGuildNameTextInstance;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM		
		CGraphicTextInstance * pMrVegaS_Titan2 = pTextTail->pVegaS_TitleText_tInstance;
#endif	
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:
		if (pMarkInstance && pGuildNameInstance)
		{
			int iWidth, iHeight;
			int iImageHalfSize = pMarkInstance->GetWidth()/2 + c_fxMarkPosition;
			pGuildNameInstance->GetTextSize(&iWidth, &iHeight);

			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			pGuildNameInstance->Update();
		}
// 2) Delete their function and paste:
		if (pMarkInstance && pGuildNameInstance)
		{
			int iWidth, iHeight;
			int iImageHalfSize = pMarkInstance->GetWidth()/2 + c_fxMarkPosition;
			pGuildNameInstance->GetTextSize(&iWidth, &iHeight);
			
#ifdef ENABLE_TITLE_SYSTEM
			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition-15); // 21.04.2016 [VegaS Fix]
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition-15, pTextTail->z);
			pGuildNameInstance->Update();			
#else
			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			pGuildNameInstance->Update();			
#endif					
#ifdef ENABLE_TITLE_SYSTEM			
		if (!pMrVegaS_Titan2)
		{
			int iWidth, iHeight;
			int iImageHalfSize = pMarkInstance->GetWidth()/2 + c_fxMarkPosition;
			
			pGuildNameInstance->GetTextSize(&iWidth, &iHeight);

			pMarkInstance->SetPosition(pTextTail->x - iWidth/2 - iImageHalfSize, pTextTail->y - c_fyMarkPosition);
			pGuildNameInstance->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			pGuildNameInstance->Update();
			}
#endif				
		}
#ifdef ENABLE_TITLE_SYSTEM			
		if (pMrVegaS_Titan2)
		{
			int iImageHalfSize = 0+c_fxMarkPosition;
			int iLevelWidth, iLevelHeight;
			pMrVegaS_Titan2->GetTextSize(&iLevelWidth, &iLevelHeight);
			if (pMarkInstance && pGuildNameInstance)
			{
				pMrVegaS_Titan2->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			}
			else
			{
				pMrVegaS_Titan2->SetPosition(pTextTail->x + iImageHalfSize, pTextTail->y - c_fyGuildNamePosition, pTextTail->z);
			}
			pMrVegaS_Titan2->Update();
		}
#endif
"""""""""""""""""""""""""""""""""""""""""