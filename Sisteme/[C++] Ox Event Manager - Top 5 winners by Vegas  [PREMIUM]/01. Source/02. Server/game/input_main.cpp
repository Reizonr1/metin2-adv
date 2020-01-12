//1.) Search:
		case HEADER_CG_REFINE:
			Refine(ch, c_pData);
			break;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		case HEADER_CG_OXEVENT_MANAGER:
			COXEventManager::instance().Manager(ch, c_pData);
			break;
#endif