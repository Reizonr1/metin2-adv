//arat©¥l©¥r

bool CInstanceBase::SetAcce(DWORD eAcce)

//de?i?tirilir

bool CInstanceBase::SetAcce(DWORD eAcce)
{
	if (IsPoly())
		return false;

	if (__IsShapeAnimalWear())
		return false;


	m_GraphicThingInstance.AttachAcce(eAcce);
	m_awPart[CRaceData::PART_ACCE] = eAcce;
	m_awPart[CRaceFile::PART_SCALE] = eScale;


	if (!eAcce)
	{

		m_GraphicThingInstance.SetScale(1.0f, 1.0f, 1.0f);
		m_GraphicThingInstance.SetScalePosition(0.0f, 0.0f, 0.0f);
		m_GraphicThinsItemScale.SetScaleSetting(1.0f, 0.0f, 2.0f);
		//TraceError("X = [%d] Y=[%d] Z=[%d]", m_GraphicThingInstance.SetScalePosition);
	}
	else
	{

		CItemData * pItemData;
		if (CItemManager::Instance().GetItemDataPointer(eAcce, &pItemData))
		{

			DWORD Race = GetRace();
			DWORD Job = RaceToJob(Race);
			DWORD Sex = RaceToSex(Race);

			m_GraphicThingInstance.SetScaleNew(pItemData->GetItemScale(Job, Sex));
			m_GraphicThingInstance.SetScalePosition(pItemData->GetItemScalePosition(Job, Sex));
			//TraceError("Job = [%d] Sex = [%d] Item = [%d]", Job, Sex, eAcce);
		}
	}

	CItemData * pItemData;
	if (CItemManager::Instance().GetItemDataPointer(eAcce, &pItemData))
		__GetRefinedEffect(pItemData);
	else
		__ClearAcceRefineEffect();

	return true;
}