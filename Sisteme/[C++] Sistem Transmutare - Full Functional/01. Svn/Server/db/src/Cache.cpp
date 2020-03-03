// 1) Search:
void CItemCache::OnFlush()
// 2) Inside this func search:
,vnum
// 3) If don't found search:
, vnum
// 4) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
							", transmutation"
#endif
// 5) Example of result:
		int iLen = snprintf(szColumns, sizeof(szColumns),
							"id, "
							"owner_id, "
							"window, "
							"pos, "
							"count, "
							"vnum"
#ifdef __CHANGELOOK_SYSTEM__
							", transmutation"
#endif
							);


// 1) Search:
void CItemCache::OnFlush()
// 2) Inside this func search (the 4th one):
%u 
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
								", %u "
#endif
// 4) Search:
p->vnum
// 5) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
								, p->transmutation
#endif
// 6) Example of result:
		int iValueLen = snprintf(szValues, sizeof(szValues),
								"%u, "
								"%u, "
								"%d, "
								"%d, "
								"%u, "
								"%u "
#ifdef __CHANGELOOK_SYSTEM__
								", %u "
#endif
								,
								p->id, 
								p->owner, 
								p->window, 
								p->pos, 
								p->count, 
								p->vnum
#ifdef __CHANGELOOK_SYSTEM__
								, p->transmutation
#endif
								);


// 1) Search:
void CItemCache::OnFlush()
// 2) Inside this func search (the 4th one):
vnum=%u 
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
								", transmutation=%u "
#endif
// 4) Search:
p->vnum
// 5) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
								, p->transmutation
#endif
// 6) Example of result:
		int iUpdateLen = snprintf(szUpdate, sizeof(szUpdate),
								"owner_id=%u, "
								"window=%d, "
								"pos=%d, "
								"count=%u, "
								"vnum=%u "
#ifdef __CHANGELOOK_SYSTEM__
								", transmutation=%u "
#endif
								,p->owner, 
								p->window, 
								p->pos, 
								p->count, 
								p->vnum
#ifdef __CHANGELOOK_SYSTEM__
								, p->transmutation
#endif
								);