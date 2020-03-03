// 1) Search:
	void CAniImageBox::AppendImage(const char * c_szFileName)
	{
		CResource * pResource = CResourceManager::Instance().GetResourcePointer(c_szFileName);
		if (!pResource->IsType(CGraphicImage::Type()))
			return;

		CGraphicExpandedImageInstance * pImageInstance = CGraphicExpandedImageInstance::New();

		pImageInstance->SetImagePointer(static_cast<CGraphicImage*>(pResource));
		if (pImageInstance->IsEmpty())
		{
			CGraphicExpandedImageInstance::Delete(pImageInstance);
			return;
		}

		m_ImageVector.push_back(pImageInstance);

		m_bycurIndex = rand() % m_ImageVector.size();
//		SetSize(pImageInstance->GetWidth(), pImageInstance->GetHeight());
//		UpdateRect();
	}
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	void CAniImageBox::AppendImage(const char * c_szFileName, float r, float g, float b, float a)
#else
	void CAniImageBox::AppendImage(const char * c_szFileName)
#endif
	{
		CResource * pResource = CResourceManager::Instance().GetResourcePointer(c_szFileName);
		if (!pResource->IsType(CGraphicImage::Type()))
			return;
		
		CGraphicExpandedImageInstance * pImageInstance = CGraphicExpandedImageInstance::New();
		pImageInstance->SetImagePointer(static_cast<CGraphicImage*>(pResource));
#ifdef ENABLE_CHANGELOOK_SYSTEM
		pImageInstance->SetDiffuseColor(r, g, b, a);
#endif
		
		if (pImageInstance->IsEmpty())
		{
			CGraphicExpandedImageInstance::Delete(pImageInstance);
			return;
		}
		
		m_ImageVector.push_back(pImageInstance);
		m_bycurIndex = rand() % m_ImageVector.size();
	}