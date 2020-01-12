// 1) Search: #include "ItemCSVReader.h"
// 2) After this make a new line and paste:
#include "../../../Client/UserInterface/Locale_inc.h"


// 1) If vs can't include the file from first step search: #include "ItemCSVReader.h"
// 2) After this make a new line and paste:
#define ENABLE_EFFECT_SYSTEM

// 1) Search: "COSTUME_HAIR",
// 2) If: "COSTUME_HAIR", is not the last subtype of costume type, add this after last one:
// 3) After make new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
								,"USE_EFFECT"
#endif


// 1) Search: "WEAR_COSTUME_HAIR",
// 2) If: "WEAR_COSTUME_HAIR", is not the last subtype of costumes wear cell, add this after last one:
// 3) After make new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
								,"WEAR_EFFECT_ARMOR",
								"WEAR_EFFECT_WEAPON"
#endif