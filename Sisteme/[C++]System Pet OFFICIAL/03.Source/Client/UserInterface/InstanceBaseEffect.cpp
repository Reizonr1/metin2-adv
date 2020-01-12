//Search in this file:
void CInstanceBase::UpdateTextTailLevel(DWORD level)

//Replace their funtion with:
void CInstanceBase::UpdateTextTailLevel(DWORD level)
{
	//static D3DXCOLOR s_kLevelColor = D3DXCOLOR(119.0f/255.0f, 246.0f/255.0f, 168.0f/255.0f, 1.0f);
	static D3DXCOLOR s_kLevelColor = D3DXCOLOR(152.0f/255.0f, 255.0f/255.0f, 51.0f/255.0f, 1.0f);

	char szText[256];
#ifdef NEW_PET_SYSTEM
	static D3DXCOLOR s_kPetLevelColor = D3DCOLOR_XRGB(255, 255,   0);
	if(IsNewPet())
	{
		sprintf(szText, "Lv %d", level);
		CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kPetLevelColor);
	}
	else{
		sprintf(szText, "Lv %d", level);
		CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kLevelColor);		
	}
#else
	sprintf(szText, "Lv %d", level);
	CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kLevelColor);
#endif
}