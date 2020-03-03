// Check this:

	HEADER_GC_REFINE_INFORMATION_OLD		= 95,

// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	HEADER_GC_SUPPORT_SKILL			= 147,
#endif

//Search in TPacketGCCharacterUpdate:
	DWORD	dwAffectFlag[2];

	DWORD	dwGuildID;
	short	sAlignment;

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
	DWORD   dwLevel;
#endif

//Search:
typedef struct packet_pvp
{
	BYTE        bHeader;
	DWORD       dwVIDSrc;
	DWORD       dwVIDDst;
	BYTE        bMode;	// 0 ?? ?, 1?? ?
} TPacketGCPVP;

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
typedef struct support_use_skill
{
	BYTE	bHeader;
	DWORD	dwVnum;
	DWORD	dwVid;
	DWORD	dwLevel;
}TPacketGCSupportUseSkill;
#endif
