// 1) Search: PART_HAIR
// 2) After make a new line and paste:
			PART_ACCE,

// 1) Search: struct SHair
// 2) After their function make a new line and paste:
		struct SAcce
		{
			std::string m_stModelFileName;
			std::vector<SSkin> m_kVct_kSkin;
		};
		
// 1) Search: void SetHairSkin(UINT eHair, UINT ePart, const char* c_szModelFileName, const char* c_szSrcFileName, const char* c_szDstFileName);
// 2) After make a new line and paste:
		void SetAcceSkin(UINT eAcce, UINT ePart, const char* c_szModelFileName, const char* c_szSrcFileName, const char* c_szDstFileName);

// 1) Search: SHair* FindHair(UINT eHair);
// 2) After make a new line and paste:
		SAcce* FindAcce(UINT eAcce);

// 1) Search: std::map<DWORD, SHair> m_kMap_dwHairKey_kHair;
// 2) After make a new line and paste:
		std::map<DWORD, SAcce> m_kMap_dwAcceKey_kAcce;