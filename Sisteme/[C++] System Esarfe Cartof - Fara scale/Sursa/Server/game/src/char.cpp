// 1) Search: addPacket.awPart[CHR_EQUIPPART_HAIR] = GetPart(PART_HAIR);
// 2) After make a new line and paste:
		addPacket.awPart[CHR_EQUIPPART_ACCE] = GetPart(PART_ACCE);

// 1) Search: pack.awPart[CHR_EQUIPPART_HAIR] = GetPart(PART_HAIR);
// 2) After make a new line and paste:
	pack.awPart[CHR_EQUIPPART_ACCE] = GetPart(PART_ACCE);

// 1) Search: void CHARACTER::PointsPacket()
// 2) Delete their function and paste:
void CHARACTER::PointsPacket()
{
	if (!GetDesc())
		return;
	
	TPacketGCPoints pack;
	pack.header	= HEADER_GC_CHARACTER_POINTS;
	pack.points[POINT_LEVEL] = GetLevel();
	pack.points[POINT_PRESTIGE_LEVEL] = GetPrestigeLevel();
	pack.points[POINT_EXP] = GetExp();
	pack.points[POINT_NEXT_EXP] = GetNextExp();
	pack.points[POINT_HP] = GetHP();
	pack.points[POINT_MAX_HP] = GetMaxHP();
	pack.points[POINT_SP] = GetSP();
	pack.points[POINT_MAX_SP] = GetMaxSP();
	pack.points[POINT_GOLD] = GetGold();
	pack.points[POINT_STAMINA] = GetStamina();
	pack.points[POINT_MAX_STAMINA] = GetMaxStamina();
	for (int i = POINT_ST; i < POINT_MAX_NUM; ++i)
		pack.points[i] = GetPoint(i);
	
	GetDesc()->Packet(&pack, sizeof(TPacketGCPoints));
	
	if (!IsAcceOpen())
	{
		LPITEM item;
		for (int j = 0; j < INVENTORY_AND_EQUIP_SLOT_MAX; ++j)
		{
			if ((item = GetInventoryItem(j)))
				if (item->GetType() == ITEM_COSTUME && item->GetSubType() == COSTUME_ACCE && item->GetSocket(0) == 1)
					item->SetSocket(0, 0);
		}
	}
}

// 1) Search: SetPart(PART_HAIR, t->parts[PART_HAIR]);
// 2) After make a new line and paste:
	SetPart(PART_ACCE, t->parts[PART_ACCE]);

// 1) Search: SetPart(PART_HAIR, GetOriginalPart(PART_HAIR));
// 2) After make a new line and paste:
	SetPart(PART_ACCE, GetOriginalPart(PART_ACCE));

// 1) Search: WORD CHARACTER::GetOriginalPart(BYTE bPartPos) const
// 2) Delete their function and paste:
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
		default:
			return 0;
	}
}

// 1) Search: if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen())
// 2) Delete this line and paste:
if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen() || IsAcceOpen())

// 1) Search: if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen())
// 2) Delete this line and paste:
if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen() || pkChrCauser->IsAcceOpen())

// 1) Search: if ((GetExchange() || IsOpenSafebox() || IsCubeOpen()))
// 2) Delete this line and paste:
if ((GetExchange() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen()))

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) Delete this line and paste:
if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())

// 1) Search: if (GetExchange() || GetMyShop() || IsOpenSafebox() || IsCubeOpen())
// 2) Delete this line and paste:
if (GetExchange() || GetMyShop() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) Delete this line and paste:
if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())