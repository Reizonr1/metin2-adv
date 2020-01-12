// 1) Search: void CActorInstance::SetHair(DWORD eHair)
// 2) After their function make a new line and paste:
void CActorInstance::SetAcce(DWORD eAcce, float fSpecular)
{
	m_eAcce = eAcce;
	CRaceData * pRaceData;
	if (!CRaceManager::Instance().GetRaceDataPointer(m_eRace, &pRaceData))
		return;
	
	CRaceData::SAcce* pkAcce = pRaceData->FindAcce(eAcce);
	if (pkAcce)
	{
		if (!pkAcce->m_stModelFileName.empty())
		{
			CGraphicThing * pkAcceThing = (CGraphicThing *)CResourceManager::Instance().GetResourcePointer(pkAcce->m_stModelFileName.c_str());
			RegisterModelThing(CRaceData::PART_ACCE, pkAcceThing);
			SetModelInstance(CRaceData::PART_ACCE, CRaceData::PART_ACCE, 0, CRaceData::PART_MAIN);
		}

		const std::vector<CRaceData::SSkin>& c_rkVct_kSkin = pkAcce->m_kVct_kSkin;
		std::vector<CRaceData::SSkin>::const_iterator i;
		for (i = c_rkVct_kSkin.begin(); i != c_rkVct_kSkin.end(); ++i)
		{
			const CRaceData::SSkin& c_rkSkinItem = *i;
			CResource * pkRes = CResourceManager::Instance().GetResourcePointer(c_rkSkinItem.m_stDstFileName.c_str());
			if (pkRes)
			{
				if (fSpecular > 0.0f)
				{
					SMaterialData kMaterialData;
					kMaterialData.pImage = static_cast<CGraphicImage*>(pkRes);
					kMaterialData.isSpecularEnable = TRUE;
					kMaterialData.fSpecularPower = fSpecular;
					kMaterialData.bSphereMapIndex = 0;
	 				SetMaterialData(CRaceData::PART_ACCE, c_rkSkinItem.m_stSrcFileName.c_str(), kMaterialData);
				}
				else
				{
					SetMaterialImagePointer(CRaceData::PART_ACCE, c_rkSkinItem.m_stSrcFileName.c_str(), static_cast<CGraphicImage*>(pkRes));
				}
			}
		}
	}
}