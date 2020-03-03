// 1) Search: #include "ItemCSVReader.h"
// 2) After this make a new line and paste:
#include "../../../Client/UserInterface/Locale_inc.h"


// 1) If vs can't include the file from first step search: #include "ItemCSVReader.h"
// 2) After this make a new line and paste:
#define ENABLE_NEW_ENCHANT_ATTR


// 1) Search: "USE_PUT_INTO_RING_SOCKET"
// 2) After this make a new line and paste:
#ifdef ENABLE_NEW_ENCHANT_ATTR
								,"USE_CHANGE_ATTRIBUTE3"
#endif
// 3) Example of result:
///			static string arSub3[] = {
///										"USE_POTION",
///										"USE_TALISMAN",
///										"USE_TUNING",
///										"USE_MOVE",
///										"USE_TREASURE_BOX",
///										"USE_MONEYBAG",
///										"USE_BAIT",
///										"USE_ABILITY_UP",
///										"USE_AFFECT",
///										"USE_CREATE_STONE",
///										"USE_SPECIAL",
///										"USE_POTION_NODELAY",
///										"USE_CLEAR",
///										"USE_INVISIBILITY",
///										"USE_DETACHMENT",
///										"USE_BUCKET",
///										"USE_POTION_CONTINUE",
///										"USE_CLEAN_SOCKET",
///										"USE_CHANGE_ATTRIBUTE",
///										"USE_ADD_ATTRIBUTE",
///										"USE_ADD_ACCESSORY_SOCKET",
///										"USE_PUT_INTO_ACCESSORY_SOCKET",
///										"USE_ADD_ATTRIBUTE2",
///										"USE_RECIPE",
///										"USE_CHANGE_ATTRIBUTE2",
///										"USE_TIME_CHARGE_PER",
///										"USE_TIME_CHARGE_FIX",
///										"USE_PUT_INTO_BELT_SOCKET",
///										"USE_PUT_INTO_RING_SOCKET"
///#ifdef ENABLE_NEW_ENCHANT_ATTR
///										,"USE_CHANGE_ATTRIBUTE3"
///#endif
///			};