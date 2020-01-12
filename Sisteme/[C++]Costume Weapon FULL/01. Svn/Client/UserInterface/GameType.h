// 1) Search: const DWORD	c_Costume_Slot_Hair = c_Costume_Slot_Start + 1;
// 2) Make a new line and paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	const DWORD c_Costume_Slot_Weapon = c_Costume_Slot_Start + 2;
#endif

// 1) Search: const DWORD c_Costume_Slot_Count = 2;
// 2) Replace with:
const DWORD c_Costume_Slot_Count = 3;

// 1) Search: const DWORD c_New_Equipment_Start = c_Equipment_Start +
// 2) Chance with:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 22 + 1;
#else
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 22;
#endif