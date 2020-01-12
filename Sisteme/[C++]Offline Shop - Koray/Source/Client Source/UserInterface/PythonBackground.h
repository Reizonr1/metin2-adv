Search:
	const char* GetWarpMapName();

Add it under:
#ifdef __OFFLINE_SHOP__
	std::string GetMapName(DWORD dwX, DWORD dwY);
#endif