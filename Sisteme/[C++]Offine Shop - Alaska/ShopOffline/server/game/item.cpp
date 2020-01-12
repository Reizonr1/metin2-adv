void CItem::Initialize()
{
	CEntity::Initialize(ENTITY_ITEM);

	[..]
#ifdef OFFLINE_SHOP
	m_dwRealID = 0;
#endif
}