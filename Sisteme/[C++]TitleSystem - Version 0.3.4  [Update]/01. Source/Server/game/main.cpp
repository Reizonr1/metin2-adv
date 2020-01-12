// 1)  Seearch:
#include "DragonSoul.h"
// 2) Add bellow:
#ifdef ENABLE_TITLE_SYSTEM	
	#include "title.h"
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1)  Seearch:
	SECTREE_MANAGER	sectree_manager;
// 2) Add bellow:
#ifdef ENABLE_TITLE_SYSTEM	
	TitleManager title;
#endif