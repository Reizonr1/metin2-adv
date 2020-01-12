//Search in this file:

#include "XTrapManager.h"
#include "DragonSoul.h"
#include <boost/bind.hpp>


//Add after this:

#ifdef NEW_PET_SYSTEM
#include "fstream"
#endif

//Search in this file:

	Cube_init();
	Blend_Item_init();
	ani_init();
	PanamaLoad();
	
//Add after:
#ifdef NEW_PET_SYSTEM
    std::string temp_exp_line;
	std::ifstream exppet_table_open("/usr/home/game/share/exppettable.txt");
	/*if (!exp_table_open.is_open())
	return 0;*/

	int exppet_table_counter = 0;
	int tmppet_exp = 0;
	while (!exppet_table_open.eof())
	{
		exppet_table_open >> temp_exp_line;
		str_to_number(exppet_table_common[exppet_table_counter], temp_exp_line.c_str());
		if (exppet_table_common[exppet_table_counter] < 2147483647) {
			sys_log(0, "Livelli Pet caricati da exppettable.txt: %d !", exppet_table_common[exppet_table_counter]);
			exppet_table_counter++;
		}
		else {
			fprintf(stderr, "[main] Impossibile caricare la tabella exp valore non valido\n");
			break;
		}
	}
#endif
