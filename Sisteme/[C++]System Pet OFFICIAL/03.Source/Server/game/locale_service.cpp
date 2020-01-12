//Search in this file:

	if (!check_name)
		check_name = check_name_euckr;

	if (!is_twobyte)
		is_twobyte = is_twobyte_euckr;

	if (!exp_table)
		exp_table = exp_table_common;

	
//Add after:

#ifdef NEW_PET_SYSTEM
	if (!exppet_table)
		exppet_table = exppet_table_common;
#endif

