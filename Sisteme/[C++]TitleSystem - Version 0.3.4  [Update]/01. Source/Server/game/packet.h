// 1) Search in function: 	typedef struct packet_char_additional_info
	short	sAlignment;
// 2) Add bellow:
typedef struct packet_char_additional_info
#ifdef ENABLE_TITLE_SYSTEM
	short	sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search in function:	typedef struct packet_update_char
	short	sAlignment;
// 2) Add bellow:
#ifdef ENABLE_TITLE_SYSTEM
	short	sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""