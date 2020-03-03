// Search for:
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

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	void CAniImageBox::SetSlotDiffuseColor(const char * c_szFileName)
	{
		CResource * pResource = CResourceManager::Instance().GetResourcePointer(c_szFileName);
		if (!pResource->IsType(CGraphicImage::Type()))
			return;

		CGraphicExpandedImageInstance * pImageInstance = CGraphicExpandedImageInstance::New();

		pImageInstance->SetImagePointer(static_cast<CGraphicImage*>(pResource));

		pImageInstance->SetDiffuseColor(238.00f / 255.0f, 11.00f / 255.0f, 11.00f / 255.0f, 1.0f);

		if (pImageInstance->IsEmpty())
		{
			CGraphicExpandedImageInstance::Delete(pImageInstance);
			return;
		}

		m_ImageVector.push_back(pImageInstance);

		m_bycurIndex = rand() % m_ImageVector.size();
	}
#endif
