// arat

void CItemManager::Destroy()

// altına ekle

bool CItemManager::LoadItemScale(const char* szItemScale)
{
	CMappedFile File;
	LPCVOID pData;

	if (!CEterPackManager::Instance().Get(File, szItemScale, &pData))
		return false;

	CMemoryTextFileLoader textFileLoader;
	textFileLoader.Bind(File.Size(), pData);

	CTokenVector TokenVector;
	for (DWORD i = 0; i < textFileLoader.GetLineCount(); ++i)
	{
		if (!textFileLoader.SplitLine(i, &TokenVector, "\t"))
			continue;

		if (!(TokenVector.size() == 9))
		{
			TraceError(" CItemManager::LoadItemList(%s) - LoadItemScale in %d\n", szItemScale, i);
			continue;
		}

		const std::string & c_rstrID = TokenVector[0];
		const std::string & c_rstrJob = TokenVector[1];
		const std::string & c_rstrSex = TokenVector[2];
		const std::string & c_rstrX = TokenVector[3];
		const std::string & c_rstrY = TokenVector[4];
		const std::string & c_rstrZ = TokenVector[5];
		const std::string & c_rstrPosX = TokenVector[6];
		const std::string & c_rstrPosY = TokenVector[7];
		const std::string & c_rstrPosZ = TokenVector[8];
		DWORD dwItemVNum = atoi(c_rstrID.c_str());
		float xScale = atof(c_rstrX.c_str()) * 0.01f;
		float yScale = atof(c_rstrY.c_str()) * 0.01f;
		float zScale = atof(c_rstrZ.c_str()) * 0.01f;
		float yPosScale = atof(c_rstrPosX.c_str()) * 100.0f;
		float xPosScale = atof(c_rstrPosY.c_str()) * 100.0f;
		float zPosScale = atof(c_rstrPosZ.c_str()) * 100.0f;

		DWORD dwJob;
		if (c_rstrJob == "JOB_WARRIOR")
		{
			dwJob = NRaceData::JOB_WARRIOR;
		}

		if (c_rstrJob == "JOB_ASSASSIN")
		{
			dwJob = NRaceData::JOB_ASSASSIN;
		}

		if (c_rstrJob == "JOB_SURA")
		{
			dwJob = NRaceData::JOB_SURA;
		}

		if (c_rstrJob == "JOB_SHAMAN")
		{
			dwJob = NRaceData::JOB_SHAMAN;
		}

		DWORD dwSex = c_rstrSex[0] == 'M';


		for (int i = 0; i <= 4; ++i)
		{
			CItemData * pItemData = MakeItemData(dwItemVNum + i);
			//TraceError("Set Sash %d to scale %f %f %f and  pos = %f %f %f for job %d, sex %d", dwItemVNum, xScale, yScale, zScale, xPosScale, yPosScale, zPosScale, dwJob, dwSex);
			pItemData->SetItemTableScaleData(dwJob, dwSex, xScale, yScale, zScale, xPosScale, yPosScale, zPosScale);
		}

	}
	return true;
}