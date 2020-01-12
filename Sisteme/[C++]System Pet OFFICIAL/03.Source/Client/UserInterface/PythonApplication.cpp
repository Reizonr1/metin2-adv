//Search in this file:
	CItemManager&		rkItemMgr	= CItemManager::Instance();	
	CPythonSkill&		rkSkillMgr	= CPythonSkill::Instance();

//Add after:
#ifdef NEW_PET_SYSTEM
	CPythonSkillPet&    rkSkillPetMgr = CPythonSkillPet::Instance();
#endif

//Search in this file:
	char szItemList[256];
	char szItemProto[256];
	char szItemDesc[256];	

//Add after:
#ifdef NEW_PET_SYSTEM
	char szSkillPetFileName[256];
#endif


//Search in this file:
	snprintf(szItemProto,	sizeof(szItemProto),	"%s/item_proto",	localePath);
	snprintf(szItemDesc,	sizeof(szItemDesc),	"%s/itemdesc.txt",	localePath);	

//Add after:

#ifdef NEW_PET_SYSTEM
	snprintf(szSkillPetFileName, sizeof(szSkillPetFileName), "%s/pet_skill.txt", localePath);
#endif

//Search in this file:
	rkItemMgr.Destroy();	
	rkSkillMgr.Destroy();

//Add after:

#ifdef NEW_PET_SYSTEM
	rkSkillPetMgr.Destroy();
#endif

//Search in this file:
	if (!rkSkillMgr.RegisterSkillTable(szSkillTableFileName))
	{
		TraceError("LoadLocaleData - RegisterSkillTable(%s) Error", szMobProto);
		return false;
	}
	
//Add after:

#ifdef NEW_PET_SYSTEM
	if (!rkSkillPetMgr.RegisterSkillPet(szSkillPetFileName))
	{
		TraceError("LoadLocaleData - RegisterSkillPet(%s) Error", szSkillPetFileName);
		return false;
	}
#endif
