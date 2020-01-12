// 1) Search: WORD CHARACTER::GetOriginalPart(BYTE bPartPos) const
// 2) Change their function with:
WORD CHARACTER::GetOriginalPart(BYTE bPartPos) const
{
	switch (bPartPos)
	{
		case PART_MAIN:
			if (!IsPC())
				return GetPart(PART_MAIN);
			else
				return m_pointsInstant.bBasePart;
		case PART_HAIR:
			return GetPart(PART_HAIR);
		case PART_ACCE:
			return GetPart(PART_ACCE);
#ifdef __WEAPON_COSTUME_SYSTEM__
		case PART_WEAPON:
			return GetPart(PART_WEAPON);
#endif
		default:
			return 0;
	}
}