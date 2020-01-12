cauti :
			AFFECT_CHINA_FIREWORK,			// 38
			
iar sub adaugi:

#ifdef __ONEX_VIP__
			AFFECT_VIP = 39,
#endif

cauti:

		BOOL					IsGameMaster();
		
iar sub adaugi:

#ifdef __ONEX_VIP__
		BOOL                    IsVIP();
#endif
	