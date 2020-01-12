// 1) Search: else if (0 == rstrBoneName.compare("PART_WEAPON_LEFT"))
// 2) After their conclusion make a new line and paste:
		else if (0 == rstrBoneName.compare("PART_ACCE"))
		{
			if (m_GraphicThingInstance.GetAttachingBoneName(CRaceData::PART_ACCE, &c_szBoneName))
			{
				return m_GraphicThingInstance.AttachEffectByID(0, c_szBoneName, ms_adwCRCAffectEffect[eEftType]);
			}
		}