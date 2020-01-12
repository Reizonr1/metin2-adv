*cmd_general.cpp

Find - Bul:
ACMD(do_pvp)

Add it upper - Üstüne ekle:
ACMD(do_deny_pvp)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	
	if (!*arg1)
		return;

	DWORD vid = 0;
	str_to_number(vid, arg1);
	LPCHARACTER pkVictim = CHARACTER_MANAGER::instance().Find(vid);

	if (!pkVictim)
		return;

	if (pkVictim->IsNPC())
		return;

	CPVPManager::instance().Reject(ch, pkVictim);
}

