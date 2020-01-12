//Search:
			case HEADER_GC_CHARACTER_MOVE:
				ret = RecvCharacterMovePacket();
				break;

//Add after:

#ifdef ENABLE_SUPPORT_SYSTEM
			case HEADER_GC_SUPPORT_SKILL:
				ret = RecvSupportUseSkill();
				break;
#endif