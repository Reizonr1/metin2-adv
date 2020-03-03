// 1) Search:
		str_to_number(item.vnum, row[cur++]);
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		str_to_number(item.transmutation, row[cur++]);
#endif


// 1) Search:
void CClientManager::QUERY_PLAYER_LOAD(CPeer * peer, DWORD dwHandle, TPlayerLoadPacket * packet)
// 2) Inside this func search:
,vnum
// 3) If don't found search:
, vnum
// 4) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
												"transmutation, "
#endif
// 5) Example of result:
			snprintf(szQuery, sizeof(szQuery), 
												"SELECT "
												"id, "
												"window+0, "
												"pos, "
												"count, "
												"vnum, "
#ifdef __CHANGELOOK_SYSTEM__
												"transmutation, "
#endif
												"socket0, "
												"socket1, "
												"socket2, "
												"attrtype0, "
												"attrvalue0, "
												"attrtype1, "
												"attrvalue1, "
												"attrtype2, "
												"attrvalue2, "
												"attrtype3, "
												"attrvalue3, "
												"attrtype4, "
												"attrvalue4, "
												"attrtype5, "
												"attrvalue5, "
												"attrtype6, "
												"attrvalue6 "
												"FROM item%s WHERE owner_id=%d AND (window < %d or window = %d)"
												,
												GetTablePostfix(),
												pTab->id,
												SAFEBOX,
												DRAGON_SOUL_INVENTORY
					);


// 1) Search:
void CClientManager::QUERY_PLAYER_LOAD(CPeer * peer, DWORD dwHandle, TPlayerLoadPacket * packet)
// 2) Inside this func search:
CDBManager::instance().ReturnQuery(queryStr, QID_PLAYER, peer->GetHandle(), pkInfo);
// 3) Now in down, search:
,vnum
// 4) If don't found search:
, vnum
// 5) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
												"transmutation, "
#endif
// 6) Example of result:
		snprintf(queryStr, sizeof(queryStr), 
												"SELECT "
												"id, "
												"window+0, "
												"pos, "
												"count, "
												"vnum, "
#ifdef __CHANGELOOK_SYSTEM__
												"transmutation, "
#endif
												"socket0, "
												"socket1, "
												"socket2, "
												"attrtype0, "
												"attrvalue0, "
												"attrtype1, "
												"attrvalue1, "
												"attrtype2, "
												"attrvalue2, "
												"attrtype3, "
												"attrvalue3, "
												"attrtype4, "
												"attrvalue4, "
												"attrtype5, "
												"attrvalue5, "
												"attrtype6, "
												"attrvalue6 "
												"FROM item%s WHERE owner_id=%d AND (window < %d or window = %d)"
												,
												GetTablePostfix(),
												packet->player_id,
												SAFEBOX,
												DRAGON_SOUL_INVENTORY
				);