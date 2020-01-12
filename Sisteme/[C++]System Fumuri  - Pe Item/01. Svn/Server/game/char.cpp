// 1) Search: addPacket.awPart[CHR_EQUIPPART_HAIR] = GetPart(PART_HAIR);
// 2) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
		addPacket.awPart[CHR_BODY_EFFECT] = GetPart(BODY_EFFECT);
		addPacket.awPart[CHR_WEAPON_RIGHT_EFFECT] = GetPart(WEAPON_RIGHT_EFFECT);
		addPacket.awPart[CHR_WEAPON_LEFT_EFFECT] = GetPart(WEAPON_LEFT_EFFECT);
#endif


// 1) Search: pack.awPart[CHR_EQUIPPART_HAIR] = GetPart(PART_HAIR);
// 2) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
	pack.awPart[CHR_BODY_EFFECT] = GetPart(BODY_EFFECT);
	pack.awPart[CHR_WEAPON_RIGHT_EFFECT] = GetPart(WEAPON_RIGHT_EFFECT);
	pack.awPart[CHR_WEAPON_LEFT_EFFECT] = GetPart(WEAPON_LEFT_EFFECT);
#endif


// 1) Search: SetPart(PART_HAIR, GetOriginalPart(PART_HAIR));
// 2) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
	SetPart(BODY_EFFECT, GetOriginalPart(BODY_EFFECT));
	SetPart(WEAPON_RIGHT_EFFECT, GetOriginalPart(WEAPON_RIGHT_EFFECT));
	SetPart(WEAPON_LEFT_EFFECT, GetOriginalPart(WEAPON_LEFT_EFFECT));
#endif


// 1) Search: return GetPart(PART_HAIR);
// 2) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
		case BODY_EFFECT:
			return GetPart(BODY_EFFECT);
		case WEAPON_RIGHT_EFFECT:
			return GetPart(WEAPON_RIGHT_EFFECT);
		case WEAPON_LEFT_EFFECT:
			return GetPart(WEAPON_LEFT_EFFECT);
#endif