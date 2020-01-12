//Find

bool CHARACTER::MoveItem(TItemPos Cell, TItemPos DestCell, BYTE count)
{
	LPITEM item = NULL;
	
///Add
#ifdef NEW_ADD_INVENTORY
	if (DestCell.cell >= (90 + (5*Black_Envanter())))
	{
		// ChatPacket(CHAT_TYPE_INFO, "Yasak");
		return false;
	}
#endif

//Find
int CHARACTER::GetEmptyInventory(BYTE size) const

///Change like this
#ifdef NEW_ADD_INVENTORY
int CHARACTER::GetEmptyInventory(BYTE size) const
{
	// NOTE: 현재 이 함수는 아이템 지급, 획득 등의 행위를 할 때 인벤토리의 빈 칸을 찾기 위해 사용되고 있는데,
	//		벨트 인벤토리는 특수 인벤토리이므로 검사하지 않도록 한다. (기본 인벤토리: INVENTORY_MAX_NUM 까지만 검사)
	// int malibuclub = INVENTORY_MAX_NUM;
	//45 first page
	//90 second page
	int malibuclub = 90 + (5*Black_Envanter());
	for ( int i = 0; i < malibuclub; ++i)
		if (IsEmptyItemGrid(TItemPos (INVENTORY, i), size))
			return i;
	return -1;
}
#else
int CHARACTER::GetEmptyInventory(BYTE size) const
{
	// NOTE: 현재 이 함수는 아이템 지급, 획득 등의 행위를 할 때 인벤토리의 빈 칸을 찾기 위해 사용되고 있는데,
	//		벨트 인벤토리는 특수 인벤토리이므로 검사하지 않도록 한다. (기본 인벤토리: INVENTORY_MAX_NUM 까지만 검사)
	for ( int i = 0; i < INVENTORY_MAX_NUM; ++i)
		if (IsEmptyItemGrid(TItemPos (INVENTORY, i), size))
			return i;
	return -1;
}
#endif

//Find
bool CHARACTER::IsEmptyItemGrid(TItemPos Cell, BYTE bSize, int iExceptionCell) const

///Change

bool CHARACTER::IsEmptyItemGrid(TItemPos Cell, BYTE bSize, int iExceptionCell) const
{
	#ifdef NEW_ADD_INVENTORY
	int malibuclub2 = (90 + (5*Black_Envanter()));
	switch (Cell.window_type)
	{
	case INVENTORY:
		{
			BYTE bCell = Cell.cell;

			// bItemCell은 0이 false임을 나타내기 위해 + 1 해서 처리한다.
			// 따라서 iExceptionCell에 1을 더해 비교한다.
			++iExceptionCell;

			if (Cell.IsBeltInventoryPosition())
			{
				LPITEM beltItem = GetWear(WEAR_BELT);

				if (NULL == beltItem)
					return false;

				if (false == CBeltInventoryHelper::IsAvailableCell(bCell - BELT_INVENTORY_SLOT_START, beltItem->GetValue(0)))
					return false;

				if (m_pointsInstant.bItemGrid[bCell])
				{
					if (m_pointsInstant.bItemGrid[bCell] == iExceptionCell)
						return true;

					return false;
				}

				if (bSize == 1)
					return true;

			}
			//black
			else if (bCell >= malibuclub2)
				return false;

			if (m_pointsInstant.bItemGrid[bCell])
			{
				if (m_pointsInstant.bItemGrid[bCell] == iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;
					BYTE bPage = bCell / (INVENTORY_MAX_NUM / 4);
					do
					{
						BYTE p = bCell + (5 * j);

						if (p >= malibuclub2)
							return false;

						if (p / (INVENTORY_MAX_NUM / 4) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
				else
					return false;
			}

			// 크기가 1이면 한칸을 차지하는 것이므로 그냥 리턴
			if (1 == bSize)
				return true;
			else
			{
				int j = 1;
				BYTE bPage = bCell / (INVENTORY_MAX_NUM / 4);

				do
				{
					BYTE p = bCell + (5 * j);

					if (p >= malibuclub2)
						return false;
					if (p / (INVENTORY_MAX_NUM / 4) != bPage)
						return false;

					if (m_pointsInstant.bItemGrid[p])
						if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
							return false;
				}
				while (++j < bSize);

				return true;
			}
		}
		break;
	#else
		switch (Cell.window_type)
		{
		case INVENTORY:
			{
				BYTE bCell = Cell.cell;

				// bItemCell은 0이 false임을 나타내기 위해 + 1 해서 처리한다.
				// 따라서 iExceptionCell에 1을 더해 비교한다.
				++iExceptionCell;

				if (Cell.IsBeltInventoryPosition())
				{
					LPITEM beltItem = GetWear(WEAR_BELT);

					if (NULL == beltItem)
						return false;

					if (false == CBeltInventoryHelper::IsAvailableCell(bCell - BELT_INVENTORY_SLOT_START, beltItem->GetValue(0)))
						return false;

					if (m_pointsInstant.bItemGrid[bCell])
					{
						if (m_pointsInstant.bItemGrid[bCell] == iExceptionCell)
							return true;

						return false;
					}

					if (bSize == 1)
						return true;

				}
				//black
				else if (bCell >= INVENTORY_MAX_NUM)
					return false;

				if (m_pointsInstant.bItemGrid[bCell])
				{
					if (m_pointsInstant.bItemGrid[bCell] == iExceptionCell)
					{
						if (bSize == 1)
							return true;

						int j = 1;
						BYTE bPage = bCell / (INVENTORY_MAX_NUM / 4);

						do
						{
							BYTE p = bCell + (5 * j);

							if (p >= INVENTORY_MAX_NUM)
								return false;

							if (p / (INVENTORY_MAX_NUM / 4) != bPage)
								return false;

							if (m_pointsInstant.bItemGrid[p])
								if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
									return false;
						}
						while (++j < bSize);

						return true;
					}
					else
						return false;
				}

				// 크기가 1이면 한칸을 차지하는 것이므로 그냥 리턴
				if (1 == bSize)
					return true;
				else
				{
					int j = 1;
					BYTE bPage = bCell / (INVENTORY_MAX_NUM / 4);

					do
					{
						BYTE p = bCell + (5 * j);

						if (p >= INVENTORY_MAX_NUM)
							return false;
						if (p / (INVENTORY_MAX_NUM / 4) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
			}
			break;
	#endif
	case DRAGON_SOUL_INVENTORY:
		{
			WORD wCell = Cell.cell;
			if (wCell >= DRAGON_SOUL_INVENTORY_MAX_NUM)
				return false;

			// bItemCell은 0이 false임을 나타내기 위해 + 1 해서 처리한다.
			// 따라서 iExceptionCell에 1을 더해 비교한다.
			iExceptionCell++;

			if (m_pointsInstant.wDSItemGrid[wCell])
			{
				if (m_pointsInstant.wDSItemGrid[wCell] == iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;

					do
					{
						BYTE p = wCell + (DRAGON_SOUL_BOX_COLUMN_NUM * j);

						if (p >= DRAGON_SOUL_INVENTORY_MAX_NUM)
							return false;

						if (m_pointsInstant.wDSItemGrid[p])
							if (m_pointsInstant.wDSItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
				else
					return false;
			}

			// 크기가 1이면 한칸을 차지하는 것이므로 그냥 리턴
			if (1 == bSize)
				return true;
			else
			{
				int j = 1;

				do
				{
					BYTE p = wCell + (DRAGON_SOUL_BOX_COLUMN_NUM * j);

					if (p >= DRAGON_SOUL_INVENTORY_MAX_NUM)
						return false;

					if (m_pointsInstant.bItemGrid[p])
						if (m_pointsInstant.wDSItemGrid[p] != iExceptionCell)
							return false;
				}
				while (++j < bSize);

				return true;
			}
		}
	}
}