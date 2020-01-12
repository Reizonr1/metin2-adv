//1.) Search:
#include "arena.h"
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	#include "OXEvent.h"
#endif

//1.) Search:
	marriage::CManager::instance().Logout(this);
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	COXEventManager::instance().Disconnect(this);
#endif