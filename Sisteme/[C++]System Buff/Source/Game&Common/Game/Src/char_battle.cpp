//Find:
		if (IsAffectFlag(AFF_HOSIN))
			dam = dam * (100 - GetPoint(POINT_RESIST_NORMAL_DAMAGE)) / 100;
//Add after(down to it):
#ifdef ITEM_BUFF_SYSTEM
		if (IsAffectFlag(AFF_RESIST_BUFF))
			dam = dam * (100 - GetPoint(POINT_RESIST_NORMAL_DAMAGE)) / 100;		
#endif		