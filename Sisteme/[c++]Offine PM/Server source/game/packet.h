Search:
	HEADER_CG_REFINE = 96,

Add it under:
#ifdef OFFLINE_MESSAGE
	HEADER_CG_OFFLINE_WHISPER = 98,
#endif

---

Search:
typedef struct packet_whisper	// °¡º¯ ÆĞÅ¶
{
	BYTE	bHeader;
	WORD	wSize;
	BYTE	bType;
	char	szNameFrom[CHARACTER_NAME_MAX_LEN + 1];
} TPacketGCWhisper;

Add it under:
#ifdef OFFLINE_MESSAGE
typedef struct get_offline_message
{
	BYTE	bHeader;
	char	szTargetName[CHARACTER_NAME_MAX_LEN + 1];
	char	szText[CHAT_MAX_LEN + 1];
} TPacketCGOfflineMessage;
#endif

