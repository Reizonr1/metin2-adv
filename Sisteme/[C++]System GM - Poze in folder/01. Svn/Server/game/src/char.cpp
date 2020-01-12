/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
// void CHARACTER::SetPlayerProto(const TPlayerTable * t) Bulunur Ve ��erisinde : 
// if (GetGMLevel() > GM_LOW_WIZARD) if blo�u komple de�i�tirilir :

#ifdef ENABLE_GM_AFFECTS
		if (GetGMLevel() == GM_IMPLEMENTOR)
		{
			m_afAffectFlag.Set(AFF_YMIR_GA);
			m_bPKMode = PK_MODE_PROTECT;			
		}
		else if (GetGMLevel() == GM_HIGH_WIZARD)
		{
			m_afAffectFlag.Set(AFF_YMIR_SGM);
			m_bPKMode = PK_MODE_PROTECT;			
		}
		else if (GetGMLevel() == GM_GOD)
		{
			m_afAffectFlag.Set(AFF_YMIR);
			m_bPKMode = PK_MODE_PROTECT;				
		}
		else if (GetGMLevel() == GM_LOW_WIZARD)
		{
			m_afAffectFlag.Set(AFF_YMIR_MOD);
			m_bPKMode = PK_MODE_PROTECT;
		}
#else
		if (GetGMLevel() > GM_LOW_WIZARD)
		{
			m_afAffectFlag.Set(AFF_YMIR);
			m_bPKMode = PK_MODE_PROTECT;
		}
#endif

/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */