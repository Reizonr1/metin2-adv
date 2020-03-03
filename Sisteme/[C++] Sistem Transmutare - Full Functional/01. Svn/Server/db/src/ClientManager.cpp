// 1) Search:
void CClientManager::RESULT_SAFEBOX_LOAD(CPeer * pkPeer, SQLMsg * msg)
// 2) Inside this func search:
		pi->pSafebox = pSafebox;
		char szQuery[512];
// 3) Replace with:
#ifdef __CHANGELOOK_SYSTEM__
		char szQuery[512 + 15];
#else
		char szQuery[512];
#endif


// 1) Search:
void CClientManager::RESULT_SAFEBOX_LOAD(CPeer * pkPeer, SQLMsg * msg)
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
											"FROM item%s WHERE owner_id=%d AND window='%s'"
											,
											GetTablePostfix(),
											pi->account_id,
											pi->ip[0] == 0 ? "SAFEBOX" : "MALL"
				);


// 1) Search:
void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData)
// 2) Inside this func search:
		char szQuery[512];
// 3) Replace with:
#ifdef __CHANGELOOK_SYSTEM__
		char szQuery[512 + 27];
#else
		char szQuery[512];
#endif


// 1) Search:
void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData)
// 2) Inside this func search:
,vnum
// 3) If don't found search:
, vnum
// 4) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
											"transmutation, "
#endif
// 5) Search (the 4th one):
%u 
// 6) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
											"%u, "
#endif
// 7) Search:
p->vnum,
// 8) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
											p->transmutation,
#endif
// 9) Example of result:
		snprintf(szQuery, sizeof(szQuery), 
											"REPLACE INTO item%s ("
											"id, "
											"owner_id, "
											"window, "
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
											"attrvalue6"
											") VALUES("
											"%u, "
											"%u, "
											"%d, "
											"%d, "
											"%u, "
											"%u, "
#ifdef __CHANGELOOK_SYSTEM__
											"%u, "
#endif
											"%ld, "
											"%ld, "
											"%ld, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d, "
											"%d"
											")"
											,
											GetTablePostfix(),
											p->id,
											p->owner,
											p->window,
											p->pos,
											p->count,
											p->vnum,
#ifdef __CHANGELOOK_SYSTEM__
											p->transmutation,
#endif
											p->alSockets[0],
											p->alSockets[1],
											p->alSockets[2],
											p->aAttr[0].bType, p->aAttr[0].sValue,
											p->aAttr[1].bType, p->aAttr[1].sValue,
											p->aAttr[2].bType, p->aAttr[2].sValue,
											p->aAttr[3].bType, p->aAttr[3].sValue,
											p->aAttr[4].bType, p->aAttr[4].sValue,
											p->aAttr[5].bType, p->aAttr[5].sValue,
											p->aAttr[6].bType, p->aAttr[6].sValue
		);