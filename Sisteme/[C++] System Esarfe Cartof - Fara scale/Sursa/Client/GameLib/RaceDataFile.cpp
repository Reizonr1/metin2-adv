// 1) Search: if (TextFileLoader.SetChildNode("hairdata"))
// 2) After their function make a new line and paste:
	if (TextFileLoader.SetChildNode("accedata"))
	{
		std::string strPathName;
		DWORD dwAcceDataCount = 0;
		if (TextFileLoader.GetTokenString("pathname", &strPathName) && TextFileLoader.GetTokenDoubleWord("accedatacount", &dwAcceDataCount))
		{
			for (DWORD i = 0; i < dwAcceDataCount; ++i)
			{
				if (!TextFileLoader.SetChildNode("accedata", i))
				{
					continue;
				}
				
				TextFileLoader.GetTokenString("specialpath", &strPathName);
				DWORD dwShapeIndex;
				if (!TextFileLoader.GetTokenDoubleWord("acceindex", &dwShapeIndex))
				{
					continue;
				}
				
				std::string strModel;
				std::string strSourceSkin;
				std::string strTargetSkin;
				if (TextFileLoader.GetTokenString("model", &strModel) && TextFileLoader.GetTokenString("sourceskin", &strSourceSkin) && TextFileLoader.GetTokenString("targetskin", &strTargetSkin))
				{
					SetAcceSkin(dwShapeIndex, 0, (strPathName + strModel).c_str(), (strPathName + strSourceSkin).c_str(), (strPathName + strTargetSkin).c_str());
				}
				
				TextFileLoader.SetParentNode();
			}
		}
		
		TextFileLoader.SetParentNode();
	}