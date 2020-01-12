// 1) Search: void CRaceData::SetHairSkin(UINT eHair, UINT ePart, const char * c_szModelFileName, const char* c_szSrcFileName, const char* c_szDstFileName)
// 2) After their function make a new line and paste:
CRaceData::SAcce* CRaceData::FindAcce(UINT eAcce)
{
	std::map<DWORD, SAcce>::iterator f=m_kMap_dwAcceKey_kAcce.find(eAcce);
	if (m_kMap_dwAcceKey_kAcce.end()==f)
	{
		if (eAcce != 0)
			TraceError("Acce number %d is not exist.", eAcce);
		
		return NULL;
	}
	
	return &f->second;
}

void CRaceData::SetAcceSkin(UINT eAcce, UINT ePart, const char * c_szModelFileName, const char* c_szSrcFileName, const char* c_szDstFileName)
{
	SSkin kSkin;
	kSkin.m_ePart=ePart;
	kSkin.m_stSrcFileName=c_szSrcFileName;
	kSkin.m_stDstFileName=c_szDstFileName;
	
	CFileNameHelper::ChangeDosPath(kSkin.m_stSrcFileName);
	m_kMap_dwAcceKey_kAcce[eAcce].m_kVct_kSkin.push_back(kSkin);
	m_kMap_dwAcceKey_kAcce[eAcce].m_stModelFileName = c_szModelFileName;
}