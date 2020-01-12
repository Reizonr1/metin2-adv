//Find:
	if ((item->GetVnum() == 50200) || (item->GetVnum() == 71049))
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???,?? ?? ? ????? ???,?????? ???? ????."));
			return false;
		}
	}	
//Add after (down to it):
#ifdef ITEM_BUFF_SYSTEM
	if (item->GetVnum() == MASTER_RESIST_BLESS_ITEM_BUFF_VNUM)
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_RESIST_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_HOSIN))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}		
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_RESIST_BUFF, POINT_RESIST_NORMAL_DAMAGE, MASTER_RESIST_BLESS_AFFECT_VALUE, AFF_RESIST_BUFF, MASTER_RESIST_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= MASTER_RESIST_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Resistance Buff , [Item Buff] for 160 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff resist rate applied: 24%.");			
		}			
	}
}

	if (item->GetVnum() == GRAND_RESIST_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_RESIST_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_HOSIN))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_RESIST_BUFF, POINT_RESIST_NORMAL_DAMAGE, GRAND_RESIST_BLESS_AFFECT_VALUE, AFF_RESIST_BUFF, GRAND_RESIST_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= GRAND_RESIST_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Resistance Buff , [Item Buff] for 224 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff resist rate applied: 29%.");			
		}			
	}
}

	if (item->GetVnum() == PERFECT_RESIST_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_RESIST_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_HOSIN))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Resistance Buff, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}		
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_RESIST_BUFF, POINT_RESIST_NORMAL_DAMAGE, PERFECT_RESIST_BLESS_AFFECT_VALUE, AFF_RESIST_BUFF, PERFECT_RESIST_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= PERFECT_RESIST_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Resistance Buff, [Item Buff] for 310 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff resist rate applied: 35%.");			
		}			
	}
}

	if (item->GetVnum() == MASTER_CRITICAL_BLESS_ITEM_BUFF_VNUM)
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_CRITICAL_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_GICHEON))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}			
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_CRITICAL_BUFF, POINT_CRITICAL_PCT, MASTER_CRITICAL_BLESS_AFFECT_VALUE, AFF_CRITICAL_BUFF, MASTER_CRITICAL_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= MASTER_CRITICAL_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Dragon's Strength(Critical Buff), [Item Buff] for 110 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff critical rate applied: 24%.");			
		}			
	}
}

	if (item->GetVnum() == GRAND_CRITICAL_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_CRITICAL_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_GICHEON))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_CRITICAL_BUFF, POINT_CRITICAL_PCT, GRAND_CRITICAL_BLESS_AFFECT_VALUE, AFF_CRITICAL_BUFF, GRAND_CRITICAL_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= GRAND_CRITICAL_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Dragon's Strength(Critical Buff), [Item Buff] for 142 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff critical rate applied: 29%.");			
		}			
	}
}

	if (item->GetVnum() == PERFECT_CRITICAL_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff)!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");	
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_CRITICAL_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		if (IsAffectFlag(AFF_GICHEON))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Dragon's Strength(Critical Buff), [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}	
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_CRITICAL_BUFF, POINT_CRITICAL_PCT, PERFECT_CRITICAL_BLESS_AFFECT_VALUE, AFF_CRITICAL_BUFF, PERFECT_CRITICAL_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= PERFECT_CRITICAL_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Dragon's Strength(Critical Buff), [Item Buff] for 185 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff critical rate applied: 35%.");			
		}			
	}
}

	if (item->GetVnum() == MASTER_REFLECT_BLESS_ITEM_BUFF_VNUM)
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_REFLECT_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}
		if (IsAffectFlag(AFF_BOHO))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}		
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_REFLECT_BUFF, POINT_REFLECT_MELEE, MASTER_REFLECT_BLESS_AFFECT_VALUE, AFF_REFLECT_BUFF, MASTER_REFLECT_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= MASTER_REFLECT_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Reflection, [Item Buff] for 160 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff reflection rate applied: 21%.");			
		}			
	}
}

	if (item->GetVnum() == GRAND_REFLECT_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_REFLECT_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}
		if (IsAffectFlag(AFF_BOHO))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_REFLECT_BUFF, POINT_REFLECT_MELEE, GRAND_REFLECT_BLESS_AFFECT_VALUE, AFF_REFLECT_BUFF, GRAND_REFLECT_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= GRAND_REFLECT_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Reflection, [Item Buff] for 224 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff reflection rate applied: 31%.");			
		}			
	}
}

	if (item->GetVnum() == PERFECT_REFLECT_BLESS_ITEM_BUFF_VNUM) // 
	{
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you have exchange,safebox,refine or other windows opened!");
			return false;
		}
		if (true == IsDead())
		{
			ChatPacket(CHAT_TYPE_INFO, "You can't use buff items while you're dead!");
			return false;
		}	
		else
		{
		if (FindAffect(SKILL_REFLECT_BUFF))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Item Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}
		if (IsAffectFlag(AFF_BOHO))
		{	
			ChatPacket(CHAT_TYPE_INFO, "You're already blessed with: Reflection, [Shaman Buff]!");	
			ChatPacket(CHAT_TYPE_INFO, "Wait for your current buff to disappear and try again!");				
			return false;
		}
		{
			item->SetSocket(0, item->GetSocket(0) + 1);			
			AddAffect(SKILL_REFLECT_BUFF, POINT_REFLECT_MELEE, PERFECT_REFLECT_BLESS_AFFECT_VALUE, AFF_REFLECT_BUFF, PERFECT_REFLECT_BLESS_AFFECT_TIME_VALUE, 0, true, true);
			if (item->GetSocket(0) >= PERFECT_REFLECT_BLESS_USINGS)
			{
			ITEM_MANAGER::instance().RemoveItem(item);
			}	
			ChatPacket(CHAT_TYPE_INFO, "You are blessed now with: Reflection, [Item Buff] for 310 seconds.");
			ChatPacket(CHAT_TYPE_INFO, "Buff reflection rate applied: 45%.");			
		}			
	}
}
#endif	