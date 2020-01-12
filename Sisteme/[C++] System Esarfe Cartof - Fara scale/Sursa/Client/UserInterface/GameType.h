// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) Delete from ifdef to endif and paste:
#ifdef ENABLE_COSTUME_SYSTEM
	const DWORD c_Costume_Slot_Start = c_Equipment_Start + 19;
	const DWORD	c_Costume_Slot_Body = c_Costume_Slot_Start + 0;
	const DWORD	c_Costume_Slot_Hair = c_Costume_Slot_Start + 1;
	const DWORD	c_Costume_Slot_Acce = c_Costume_Slot_Start + 2;
	const DWORD	c_Costume_Slot_Mount = c_Costume_Slot_Start + 3;
	const DWORD c_Costume_Slot_Count = 4;
	const DWORD c_Costume_Slot_End = c_Costume_Slot_Start + c_Costume_Slot_Count;
#endif

// 1) Search: ITEM_ATTRIBUTE_SLOT_MAX_NUM = 7,
// 2) Delete it and paste:
	ITEM_ATTRIBUTE_SLOT_MAX_NUM = 15,