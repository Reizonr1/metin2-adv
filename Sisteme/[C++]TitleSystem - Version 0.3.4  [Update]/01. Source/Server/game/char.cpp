// 1) Search:		m_iRealAlignment = 0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_iPrestige = 0;
	m_iRealPrestige = 0;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:				addPacket.sAlignment = 0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
				addPacket.sPrestige = 0;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:			addPacket.sAlignment = m_iAlignment / 10;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			addPacket.sPrestige = m_iPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	pack.sAlignment	= m_iAlignment / 10;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pack.sPrestige	= m_iPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	pack2.sAlignment = 0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	pack2.sPrestige = 0;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	tab.lAlignment = m_iRealAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	tab.lPrestige = m_iRealPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	m_iRealAlignment = t->lAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_iPrestige = t->lPrestige;
	m_iRealPrestige = t->lPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search: (if you not have that you can step)
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %d %d %ld %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment());
		
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %d %d %ld %d %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment(), GetTitle());		
#else		
	char buf[51];
	snprintf(buf, sizeof(buf), "%s %d %d %ld %d", 
		inet_ntoa(GetDesc()->GetAddr().sin_addr), GetGold(), g_bChannel, GetMapIndex(), GetAlignment());		
#endif		