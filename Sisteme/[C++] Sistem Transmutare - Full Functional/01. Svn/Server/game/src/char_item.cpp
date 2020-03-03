// 1) Search:
bool CHARACTER::CanHandleItem(bool bSkipCheckRefine, bool bSkipObserver)
// 2) Inside this func look for:
	if (IsWarping())
		return false;
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	if (m_bChangeLook)
		return false;
#endif


// 1) Search:
			pack.count = pItem->GetCount();
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			pack.transmutation = pItem->GetTransmutation();
#endif


// 1) Search:
			pack.count = 0;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			pack.transmutation = 0;
#endif


// 1) Search:
							else if (item2->GetVnum() >= 28330 && item2->GetVnum() <= 28343)
// 2) If you don't find it, search:
							if (item2->GetVnum() >= 28330 && item2->GetVnum() <= 28343)
// 3) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
							if (item->GetValue(0) == CL_CLEAN_ATTR_VALUE0)
							{
								if (!CleanTransmutation(item, item2))
									return false;
								
								return true;
							}
#endif