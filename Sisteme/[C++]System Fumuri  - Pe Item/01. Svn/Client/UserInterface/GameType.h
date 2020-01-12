// 1) Search:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23;
	const DWORD c_New_Equipment_Count = 3;
	const DWORD c_Equipment_Ring1 = c_New_Equipment_Start + 0;
	const DWORD c_Equipment_Ring2 = c_New_Equipment_Start + 1;
	const DWORD c_Equipment_Belt = c_New_Equipment_Start + 2;
#endif
// 2) Replace with:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
#ifdef ENABLE_EFFECT_SYSTEM
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23 + 1 + 2;
#else
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23 + 1;
#endif
#else
#ifdef ENABLE_EFFECT_SYSTEM
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23 + 2;
#else
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23;
#endif
#endif
	const DWORD c_New_Equipment_Count = 3;
	const DWORD c_Equipment_Ring1 = c_New_Equipment_Start + 0;
	const DWORD c_Equipment_Ring2 = c_New_Equipment_Start + 1;
	const DWORD c_Equipment_Belt = c_New_Equipment_Start + 2;
#endif


// 1) Search:
#ifdef ENABLE_COSTUME_SYSTEM
	const DWORD c_Costume_Slot_Start = c_Equipment_Start + 19;
	const DWORD	c_Costume_Slot_Body = c_Costume_Slot_Start + 0;
	const DWORD	c_Costume_Slot_Hair = c_Costume_Slot_Start + 1;
	const DWORD c_Costume_Slot_Count = 2;
	const DWORD c_Costume_Slot_End = c_Costume_Slot_Start + c_Costume_Slot_Count;
#endif
// 2) Replace with:
#ifdef ENABLE_COSTUME_SYSTEM
	const DWORD c_Costume_Slot_Start = c_Equipment_Start + 19;
	const DWORD	c_Costume_Slot_Body = c_Costume_Slot_Start + 0;
	const DWORD	c_Costume_Slot_Hair = c_Costume_Slot_Start + 1;
	const DWORD	c_Costume_Slot_Acce = c_Costume_Slot_Start + 2;
#ifdef ENABLE_MOUNT_SYSTEM
	const DWORD	c_Costume_Slot_Mount = c_Costume_Slot_Start + 3;
#endif
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	const DWORD c_Costume_Slot_Weapon = c_Costume_Slot_Start + 4;
#endif
#ifdef ENABLE_EFFECT_SYSTEM
	const DWORD c_Costume_Effect_Body = c_Costume_Slot_Start + 5;
	const DWORD c_Costume_Effect_Weapon = c_Costume_Slot_Start + 6;
#endif
	const DWORD c_Costume_Slot_Count = 7;
	const DWORD c_Costume_Slot_End = c_Costume_Slot_Start + c_Costume_Slot_Count;
#endif