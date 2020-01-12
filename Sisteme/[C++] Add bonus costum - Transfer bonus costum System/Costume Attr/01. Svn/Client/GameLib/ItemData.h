// 1) Search: #include "GameLibDefines.h"
// 2) After this paste:
#include "../UserInterface/Locale_inc.h"


// 1) Search: USE_PUT_INTO_RING_SOCKET,
// 2) Make a new line and paste:
#ifdef ENABLE_COSTUME_ATTR_SYSTEM
			USE_COSTUME_ENCHANT,
			USE_COSTUME_TRANSFORM,
#endif