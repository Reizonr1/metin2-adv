// 1) Search: kNetActorData.m_dwHair=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	kNetActorData.m_dwBodyEffect=0;
	kNetActorData.m_dwWeaponEffectRight=0;
	kNetActorData.m_dwWeaponEffectLeft=0;
#endif


// 1) Search: kNetActorData.m_dwHair=chrInfoPacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		kNetActorData.m_dwBodyEffect=chrInfoPacket.awPart[CHR_BODY_EFFECT];
		kNetActorData.m_dwWeaponEffectRight=chrInfoPacket.awPart[CHR_WEAPON_RIGHT_EFFECT];
		kNetActorData.m_dwWeaponEffectLeft=chrInfoPacket.awPart[CHR_WEAPON_LEFT_EFFECT];
#endif


// 1) Search: kNetActorData.m_dwHair=chrAddPacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	kNetActorData.m_dwBodyEffect=chrAddPacket.awPart[CHR_BODY_EFFECT];
	kNetActorData.m_dwWeaponEffectRight=chrAddPacket.awPart[CHR_WEAPON_RIGHT_EFFECT];
	kNetActorData.m_dwWeaponEffectLeft=chrAddPacket.awPart[CHR_WEAPON_LEFT_EFFECT];
#endif


// 1) Search: kNetUpdateActorData.m_dwHair=chrUpdatePacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	kNetUpdateActorData.m_dwBodyEffect=chrUpdatePacket.awPart[CHR_BODY_EFFECT];
	kNetUpdateActorData.m_dwWeaponEffectRight=chrUpdatePacket.awPart[CHR_WEAPON_RIGHT_EFFECT];
	kNetUpdateActorData.m_dwWeaponEffectLeft=chrUpdatePacket.awPart[CHR_WEAPON_LEFT_EFFECT];
#endif


// 1) Search: kNetUpdateActorData.m_dwHair=chrUpdatePacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	kNetUpdateActorData.m_dwBodyEffect=chrUpdatePacket.awPart[CHR_BODY_EFFECT];
	kNetUpdateActorData.m_dwWeaponEffectRight=chrUpdatePacket.awPart[CHR_WEAPON_RIGHT_EFFECT];
	kNetUpdateActorData.m_dwWeaponEffectLeft=chrUpdatePacket.awPart[CHR_WEAPON_LEFT_EFFECT];
#endif