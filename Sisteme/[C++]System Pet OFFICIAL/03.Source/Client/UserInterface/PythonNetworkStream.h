//Search in this file:
		bool SendGuildDepositMoneyPacket(DWORD dwMoney);
		bool SendGuildWithdrawMoneyPacket(DWORD dwMoney);

//Add after:
#ifdef NEW_PET_SYSTEM
		bool PetSetNamePacket(const char * petname);
#endif
