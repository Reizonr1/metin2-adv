// 1) Search: HEADER_GC_HANDSHAKE = 0xff,
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	HEADER_CG_TITLE_CHOOSE = 208,
	HEADER_GG_TITLE_ANSWER = 37,
#endif


// 1) Search: BYTE    bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int		iTitleID;
#endif


// 1) Search: BYTE		bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int			iTitleID;
#endif


// 1) Search: BYTE		bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int			iTitleID;
#endif


// 1) Search: BYTE		bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int			iTitleID;
#endif


// 1) Search: POINT_ENERGY_END_TIME = 129,
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	POINT_TITLE = 150,
	POINT_TITLE_1 = 151,
	POINT_TITLE_2 = 152,
	POINT_TITLE_3 = 153,
	POINT_TITLE_4 = 154,
	POINT_TITLE_5 = 155,
	POINT_TITLE_6 = 156,
	POINT_TITLE_7 = 157,
	POINT_TITLE_8 = 158,
	POINT_TITLE_9 = 159,
	POINT_TITLE_10 = 160,
	POINT_TITLE_11 = 161,
	POINT_TITLE_12 = 162,
	POINT_TITLE_13 = 163,
	POINT_TITLE_14 = 164,
	POINT_TITLE_15 = 165,
	POINT_TITLE_16 = 166,
	POINT_TITLE_17 = 167,
	POINT_TITLE_18 = 168,
	POINT_TITLE_19 = 169,
	POINT_TITLE_20 = 170,
#endif


// 1) Search: } TPacketGCDragonSoulRefine;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
typedef struct SPacketGGTitleInfo
{
	BYTE	bHeader;
	int		iTitle;
	BYTE	bAnswer;
} TPacketGGTitleInfo;
#endif