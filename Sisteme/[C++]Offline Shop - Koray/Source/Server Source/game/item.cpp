Search:
	else if (DRAGON_SOUL_INVENTORY == window_type)
	{
		if (m_wCell >= DRAGON_SOUL_INVENTORY_MAX_NUM)
		{
			sys_err("CItem::AddToCharacter: cell overflow: %s to %s cell %d", m_pProto->szName, ch->GetName(), m_wCell);
			return false;
		}
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	if (ch->GetItem(Cell))
	{
		sys_err("CItem::AddToCharacter: item already exist: vnum %u name %s cell %d %s", GetVnum(), GetName(), pos, ch->GetItem(Cell)->GetName());
		return false;
	}
#endif

https://puu.sh/sgH2n/26763217e0.png
---

Search:
void CItem::AlterToSocketItem(int iSocketCount)
{
	if (iSocketCount >= ITEM_SOCKET_MAX_NUM)

Change:
void CItem::AlterToSocketItem(int iSocketCount)
{
#ifdef __OFFLINE_SHOP__
	if (iSocketCount > ITEM_SOCKET_MAX_NUM)
#else
	if (iSocketCount >= ITEM_SOCKET_MAX_NUM)
#endif

https://puu.sh/sgH3x/841bd1cb71.png