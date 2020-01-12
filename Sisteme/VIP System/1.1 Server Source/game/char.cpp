//1.0 suchen:
	m_iAlignment = 0;
	m_iRealAlignment = 0;
//1.0 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	m_iVip = 0;
	m_iRealVip = 0;
#endif	

//1.1 suchen:
				addPacket.sAlignment = 0;
//1.1 dahinter:				
#ifdef ENABLE_VIP_SYSTEM
				addPacket.sVip = 0;
#endif	

//1.2 suchen:
			addPacket.sAlignment = m_iAlignment / 10;
//1.2 dahinter:			
#ifdef ENABLE_VIP_SYSTEM
			addPacket.sVip = m_iVip;
#endif			

//1.3 suchen:
	pack.sAlignment	= m_iAlignment / 10;
//1.3 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	pack.sVip	= m_iVip;
#endif	

//1.4 suchen:
	pack2.sAlignment = 0;
//1.4 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	pack2.sVip = 0;
#endif	

//1.5 suchen:
	tab.lAlignment = m_iRealAlignment;
//1.5 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	tab.lVip = m_iRealVip;
#endif	

//1.6 suchen:
void CHARACTER::FlushDelayedSaveItem()
{
	// 저장 안된 소지품을 전부 저장시킨다.
	LPITEM item;

	for (int i = 0; i < INVENTORY_AND_EQUIP_SLOT_MAX; ++i)
		if ((item = GetInventoryItem(i)))
			ITEM_MANAGER::instance().FlushDelayedSave(item);
}
//1.6 dahinter:
#ifdef ENABLE_VIP_SYSTEM
void CHARACTER::RefreshVip()
{
	m_afAffectFlag.Set(AFF_VIP);
}
#endif

//1.7 suchen:
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %lld %d %ld %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment());	
//1.7 anpassen:	
#ifdef ENABLE_VIP_SYSTEM
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %lld %d %ld %d %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment(), GetVip());		
#else		
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %lld %d %ld %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment());		
#endif		

//1.8 suchen:
	m_iAlignment = t->lAlignment;
	m_iRealAlignment = t->lAlignment;
//1.8 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	m_iVip = t->lVip;
	m_iRealVip = t->lVip;
#endif	

