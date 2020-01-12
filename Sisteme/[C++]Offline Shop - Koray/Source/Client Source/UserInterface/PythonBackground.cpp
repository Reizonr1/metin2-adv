Search:
const char * CPythonBackground::GetWarpMapName()
{
	return m_strMapName.c_str();
}

Add it under:
#ifdef __OFFLINE_SHOP__
std::string CPythonBackground::GetMapName(DWORD dwX, DWORD dwY)
{
	TMapInfo* pkMapInfo = GlobalPositionToMapInfo(dwX, dwY);
	if (!pkMapInfo)
	{
		TraceError("NOT_FOUND_GLOBAL_POSITION(%d, %d)", dwX, dwY);
		return "";
	}
	return pkMapInfo->m_strName;
}
#endif

https://puu.sh/sgKXF/f08f4607ce.png