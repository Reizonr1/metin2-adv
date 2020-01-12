//Search in this file:
extern const DWORD		exp_table_euckr[PLAYER_EXP_TABLE_MAX + 1];
extern const DWORD		exp_table_common[PLAYER_EXP_TABLE_MAX + 1];
extern const DWORD		exp_table_newcibn[PLAYER_EXP_TABLE_MAX + 1];

extern const DWORD*		exp_table;


//Add after:
#ifdef NEW_PET_SYSTEM
extern DWORD		exppet_table_common[121];
extern DWORD*		exppet_table;
extern const DWORD		Pet_SKill_TablePerc[3][20];
extern const DWORD		Pet_Skill_Table[18][23];
extern const DWORD		Pet_Table[4][2];
#endif