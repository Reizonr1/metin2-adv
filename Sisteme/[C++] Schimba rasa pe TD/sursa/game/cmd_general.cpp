//Adauga la sfarsitul fisierului:

ACMD(do_change_race)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));
	bool bIsSetSkillGroup = false;
	DWORD dwRace = MAIN_RACE_MAX_NUM;
	DWORD dwSkillGroup = 0;
	if (!*arg1)
	{
		return;
	}
	if (*arg2)
	{
		str_to_number(dwSkillGroup, arg2);
		dwSkillGroup = MINMAX(0, dwSkillGroup, 2);
		bIsSetSkillGroup = true;
	}
	str_to_number(dwRace, arg1);
	if (dwRace >= MAIN_RACE_MAX_NUM)
	{
		return;
	}
	ch->SetRace(dwRace);
	ch->ClearSkill();
	if (bIsSetSkillGroup)
	{
		ch->SetSkillGroup(dwSkillGroup);
	}
	ch->SetPolymorph(20032);
	ch->SetPolymorph(0);
	return;
}