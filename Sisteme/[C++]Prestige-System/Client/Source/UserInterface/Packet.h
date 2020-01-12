// Suche :
typedef struct packet_char_additional_info
// Unter :
	DWORD		dwMountVnum;
// Das einfügen :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	BYTE		bPrestige;
#endif
// Suche :
typedef struct packet_update_char
// Unter :
	DWORD		dwMountVnum;
// Das einfügen :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	BYTE		bPrestige;
#endif