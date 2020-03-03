// 1) Search: #include "config.h"
// 2) After this make a new line and paste:
#include "utils.h"


// 1) Search: void CItem::AddAttribute()
// 2) Before this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
void CItem::PrepareAttribute()
{
	int iAttributeCount = GetAttributeCount();
	if (iAttributeCount == 0)
		return;
	
	int w = 0;
	TItemTable const * pProto = GetProto();
	if (pProto && pProto->sAddonType)
	{
		w = 2;
		int iSkillBonus = MINMAX(-30, (int) (gauss_random(0, 5) + 0.5f), 30);
		int iNormalHitBonus = 0;
		if (abs(iSkillBonus) <= 20)
			iNormalHitBonus = -2 * iSkillBonus + abs(number(-8, 8) + number(-8, 8)) + number(1, 4);
		else
			iNormalHitBonus = -2 * iSkillBonus + number(1, 5);
		
		GetOwner()->PrepareEnchantAttr(0, APPLY_NORMAL_HIT_DAMAGE_BONUS, iNormalHitBonus);
		GetOwner()->PrepareEnchantAttr(1, APPLY_SKILL_DAMAGE_BONUS, iSkillBonus);
	}
	
	static const int tmpChangeProb[ITEM_ATTRIBUTE_MAX_LEVEL] = {0, 10, 40, 35, 15,};
	for (int i = w; i < iAttributeCount; ++i)
	{
		int iAttrLevelPercent = number(1, 100);
		int c;
		for (c = 0; c < ITEM_ATTRIBUTE_MAX_LEVEL; ++c)
		{
			if (iAttrLevelPercent <= tmpChangeProb[c])
				break;
			
			iAttrLevelPercent -= tmpChangeProb[c];
		}
		
		BYTE bLevel = c + 1;
		int iAttributeSet = GetAttributeSetIndex();
		if (iAttributeSet < 0)
			break;
		
		if (bLevel > ITEM_ATTRIBUTE_MAX_LEVEL)
			break;
		
		int total = 0;
		std::vector<int> avail;
		for (int b = 0; b < MAX_APPLY_NUM; ++b)
		{
			const TItemAttrTable & r = g_map_itemAttr[b];
			if (r.bMaxLevelBySet[iAttributeSet] && !HasAttr(b))
			{
				if (GetOwner()->GetEnchantType1() != b && GetOwner()->GetEnchantType2() != b && GetOwner()->GetEnchantType3() != b && GetOwner()->GetEnchantType4() != b && GetOwner()->GetEnchantType5() != b)
				{
					avail.push_back(b);
					total += r.dwProb;
				}
			}
		}
		
		unsigned int prob = number(1, total);
		int attr_idx = APPLY_NONE;
		for (DWORD j = 0; j < avail.size(); ++j)
		{
			const TItemAttrTable & r = g_map_itemAttr[avail[j]];
			if (prob <= r.dwProb)
			{
				attr_idx = avail[j];
				break;
			}
			
			prob -= r.dwProb;
		}
		
		if (!attr_idx)
		{
			sys_err("Cannot prepare item attribute: %d %d.", iAttributeSet, bLevel);
			break;
		}
		
		const TItemAttrTable & r = g_map_itemAttr[attr_idx];
		if (bLevel > r.bMaxLevelBySet[iAttributeSet])
			bLevel = r.bMaxLevelBySet[iAttributeSet];
		
		long lVal = r.lValues[MIN(4, bLevel - 1)];
		if (!lVal)
			lVal = 0;
		
		GetOwner()->PrepareEnchantAttr(i, attr_idx, lVal);
	}
}
#endif