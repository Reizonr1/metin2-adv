void CInstanceBase::UpdateTextTailLevel(DWORD level)
{
	static D3DXCOLOR s_kLevelColor = D3DXCOLOR(152.0f/255.0f, 255.0f/255.0f, 51.0f/255.0f, 1.0f); //Culoare nivel
	static D3DXCOLOR s_kStaffColor = D3DXCOLOR(255.0f/255.0f, 162.0f/255.0f, 0.0f/255.0f, 1.0f); //Culoare [Staff]
	static D3DXCOLOR s_kFondatorColor = D3DXCOLOR(255.0f/255.0f, 162.0f/255.0f, 0.0f/255.0f, 1.0f); //Culoare [Fondator]
	static D3DXCOLOR s_kSGMColor = D3DXCOLOR(255.0f/255.0f, 162.0f/255.0f, 0.0f/255.0f, 1.0f); //Culoare [SGM]
	static D3DXCOLOR s_kGMColor = D3DXCOLOR(255.0f/255.0f, 162.0f/255.0f, 0.0f/255.0f, 1.0f); //Culoare [GM]
	
	//Pentru culori : https://www.w3schools.com/colors/colors_picker.asp

	char szText[256];
	if (IsGameMaster())
	{
		sprintf(szText, "[Staff]");
		CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kStaffColor);
		std::string szName = GetNameString();
		if (szName.find("axde3l") != std::string::npos)
			sprintf(szText, "[Server Administrator]");
			CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kFondatorColor);
		if (szName.find("Kidro") != std::string::npos)
			sprintf(szText, "[Server Developer]");
			CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kSGMColor);
		if (szName.find("Heler") != std::string::npos)
			sprintf(szText, "[Helper]");
			CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kGMColor);
	}
	else if (IsGameMaster())
	{
		sprintf(szText, "[Staff]");
		CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kStaffColor);
	}
	else
	{
		sprintf(szText, "[Lv.]");
		CPythonTextTail::Instance().AttachLevel(GetVirtualID(), szText, s_kLevelColor);
	}
}