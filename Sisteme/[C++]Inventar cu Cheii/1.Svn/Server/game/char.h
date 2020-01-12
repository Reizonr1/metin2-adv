//Find
POINT_RESIST_PENETRATE = 137,

///Add
#ifdef NEW_ADD_INVENTORY
	POINT_BLACK = 145, 				// New_inventory
#endif

//Find
bool			DropItem(TItemPos Cell,  BYTE bCount=0);

///Add
#ifdef NEW_ADD_INVENTORY
	bool            Envanter_update();
#endif

//Find
void			GiveGold(INT iAmount);

///Add
#ifdef NEW_ADD_INVENTORY
	DWORD 			Black_Envanter() const;
	void 			Set_Envanter_Black(int black);
#endif