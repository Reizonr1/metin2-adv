// search this

	void CPythonChat::UpdateViewMode(DWORD dwID)
// after 
		pChatLine->Instance.Update();
// add this
#ifdef ENABLE_GLOBAL_CHAT
		if(pChatLine->ImageInstance)
			pChatLine->ImageInstance->SetPosition(pChatSet->m_ix, pChatSet->m_iy + iHeight + 2);
#endif
// search this

	void CPythonChat::UpdateEditMode(DWORD dwID)
// after this 
		pChatLine->Instance.Update();
// add this
#ifdef ENABLE_GLOBAL_CHAT
	if(pChatLine->ImageInstance)
			pChatLine->ImageInstance->SetPosition(pChatSet->m_ix, pChatSet->m_iy + iHeight + 2);
#endif
// search this

	void CPythonChat::UpdateLogMode(DWORD dwID)
// after this
pChatLine->Instance.Update();
// add this
#ifdef ENABLE_GLOBAL_CHAT
	if(pChatLine->ImageInstance)
			pChatLine->ImageInstance->SetPosition(pChatSet->m_ix, pChatSet->m_iy + iHeight + 2);
#endif
// search this  

	void CPythonChat::Render(DWORD dwID)

// after this
		rInstance.Render();
// add this
#ifdef ENABLE_GLOBAL_CHAT
		CGraphicImageInstance *& imInstance = (*itor)->ImageInstance;
		if (imInstance)
			imInstance->Render();
#endif
// search this  

	void CPythonChat::AppendChat(int iType, const char * c_szChat)
// after this function
	for (TChatSetMap::iterator itor = m_ChatSetMap.begin(); itor != m_ChatSetMap.end(); ++itor)
	{
		-
		-
		-
	}
// add this

#ifdef ENABLE_GLOBAL_CHAT
	std::string const s = c_szChat;
	std::size_t EP1 = 0;
	std::size_t EP2 = 0;
	std::size_t EP3 = 0;

	CGraphicImageInstance *& prFlag = pChatLine->ImageInstance;

	std::string sub_s = s.substr(0, 1);
	if (iType == 6) {
		EP1 = sub_s.find_first_of("1");
		EP2 = sub_s.find_first_of("2");
		EP3 = sub_s.find_first_of("3");
	}
	else {
		EP1 = sub_s.find("!§$%&/(845945)=X");
		EP2 = sub_s.find("!§$%&/(845945)=X");
		EP3 = sub_s.find("!§$%&/(845945)=X");
	}

	if (EP1 != std::string::npos) {

		if (CResourceManager::Instance().IsFileExist("d:/ymir work/ui/game/flag/shinsoo.tga"))
		{
			CGraphicImage * pFlagImage = (CGraphicImage *)CResourceManager::Instance().GetResourcePointer("d:/ymir work/ui/game/flag/shinsoo.tga");
			if (pFlagImage)
			{
				prFlag = CGraphicImageInstance::New();
				prFlag->SetImagePointer(pFlagImage);
			}
		}
	}

	else if (EP2 != std::string::npos) {

		if (CResourceManager::Instance().IsFileExist("d:/ymir work/ui/game/flag/chunjo.tga"))
		{
			CGraphicImage * pFlagImage = (CGraphicImage *)CResourceManager::Instance().GetResourcePointer("d:/ymir work/ui/game/flag/chunjo.tga");
			if (pFlagImage)
			{
				prFlag = CGraphicImageInstance::New();
				prFlag->SetImagePointer(pFlagImage);
			}
		}
	}

	else if (EP3 != std::string::npos) {

		if (CResourceManager::Instance().IsFileExist("d:/ymir work/ui/game/flag/jinno.tga"))
		{
			CGraphicImage * pFlagImage = (CGraphicImage *)CResourceManager::Instance().GetResourcePointer("d:/ymir work/ui/game/flag/jinno.tga");
			if (pFlagImage)
			{
				prFlag = CGraphicImageInstance::New();
				prFlag->SetImagePointer(pFlagImage);
			}
		}
	}

	else {

		if (CResourceManager::Instance().IsFileExist("d:/ymir work/ui/game/flag/none.tga"))
		{
			CGraphicImage * pFlagImage = (CGraphicImage *)CResourceManager::Instance().GetResourcePointer("d:/ymir work/ui/game/flag/none.tga");
			if (pFlagImage)
			{
				prFlag = CGraphicImageInstance::New();
				prFlag->SetImagePointer(pFlagImage);
			}
		}
	}
#endif