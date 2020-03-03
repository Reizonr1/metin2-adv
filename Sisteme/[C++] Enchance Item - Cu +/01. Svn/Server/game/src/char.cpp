// 1) Search: m_iSyncHackCount = 0;
// 2) After this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
	dw_EnchantAttr = 5555;
#endif


// 1) Search: bool CAN_ENTER_ZONE(const LPCHARACTER& ch, int map_index)
// 2) Before this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
void CHARACTER::PrepareEnchantAttr(int iAttribute, int iIdx, int iVal)
{
	switch (iAttribute)
	{
		case 0:
		{
			newEnchant_type1 = iIdx;
			newEnchant_value1 = iVal;
		}
		break;
		case 1:
		{
			newEnchant_type2 = iIdx;
			newEnchant_value2 = iVal;
		}
		break;
		case 2:
		{
			newEnchant_type3 = iIdx;
			newEnchant_value3 = iVal;
		}
		break;
		case 3:
		{
			newEnchant_type4 = iIdx;
			newEnchant_value4 = iVal;
		}
		break;
		case 4:
		{
			newEnchant_type5 = iIdx;
			newEnchant_value5 = iVal;
		}
		break;
		default:
		break;
	}
}
#endif