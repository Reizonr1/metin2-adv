// 1) Search: snprintf(szDragonSoulTableFileName, sizeof(szDragonSoulTableFileName), "%s/dragon_soul_table.txt", LocaleService_GetBasePath().c_str());
// 2) After make a new line and paste:
	sys_log(0, "Initializing informations of acce system.");
	if (!Acce_InformationInitialize())
	{
		sys_err("Cannot initalizing acce infomation.");
		thecore_shutdown();
		return;
	}

// 1) Search: if (ch->GetShopOwner() || ch->GetExchange() || ch->GetMyShop() || ch->IsCubeOpen())
// 2) Delete this line and paste:
	if (ch->GetShopOwner() || ch->GetExchange() || ch->GetMyShop() || ch->IsCubeOpen() || ch->IsAcceOpen())