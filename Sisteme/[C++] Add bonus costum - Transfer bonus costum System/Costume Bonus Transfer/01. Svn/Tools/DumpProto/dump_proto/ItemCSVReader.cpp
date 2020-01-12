// 1) Search: "ITEM_BELT",
// 2) Make a new line and paste:
#ifdef ENABLE_ATTR_TRANSFER_SYSTEM
						"ITEM_TRANSFER_SCROLL",
#endif

// 1) Search: static string* arSubType[] = {0, arSub1, arSub2, arSub3, arSub4, arSub5, arSub6, arSub7, arSub8, 0, arSub10, 0, arSub12, 0, arSub14, 0, arSub16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, arSub28, arSub29, arSub29, arSub31, 0, 0, 0,};
// 2) Replace this with:
	static string* arSubType[] = {0, arSub1, arSub2, arSub3, arSub4, arSub5, arSub6, arSub7, arSub8, 0, arSub10, 0, arSub12, 0, arSub14, 0, arSub16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, arSub28, arSub29, arSub29, arSub31, 0, 0, 0,
#ifdef ENABLE_ATTR_TRANSFER_SYSTEM
	0,
#endif
	};

// 1) Search: static int arNumberOfSubtype[_countof(arSubType)] = {0, sizeof(arSub1)/sizeof(arSub1[0]), sizeof(arSub2)/sizeof(arSub2[0]), sizeof(arSub3)/sizeof(arSub3[0]), sizeof(arSub4)/sizeof(arSub4[0]), sizeof(arSub5)/sizeof(arSub5[0]), sizeof(arSub6)/sizeof(arSub6[0]), sizeof(arSub7)/sizeof(arSub7[0]), sizeof(arSub8)/sizeof(arSub8[0]), 0, sizeof(arSub10)/sizeof(arSub10[0]), 0, sizeof(arSub12)/sizeof(arSub12[0]), 0, sizeof(arSub14)/sizeof(arSub14[0]), 0, sizeof(arSub16)/sizeof(arSub16[0]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, sizeof(arSub28)/sizeof(arSub28[0]), sizeof(arSub29)/sizeof(arSub29[0]), sizeof(arSub29)/sizeof(arSub29[0]), sizeof(arSub31)/sizeof(arSub31[0]), 0, 0, 0};
// 2) Replace this with:
	static int arNumberOfSubtype[_countof(arSubType)] = {0, sizeof(arSub1)/sizeof(arSub1[0]), sizeof(arSub2)/sizeof(arSub2[0]), sizeof(arSub3)/sizeof(arSub3[0]), sizeof(arSub4)/sizeof(arSub4[0]), sizeof(arSub5)/sizeof(arSub5[0]), sizeof(arSub6)/sizeof(arSub6[0]), sizeof(arSub7)/sizeof(arSub7[0]), sizeof(arSub8)/sizeof(arSub8[0]), 0, sizeof(arSub10)/sizeof(arSub10[0]), 0, sizeof(arSub12)/sizeof(arSub12[0]), 0, sizeof(arSub14)/sizeof(arSub14[0]), 0, sizeof(arSub16)/sizeof(arSub16[0]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, sizeof(arSub28)/sizeof(arSub28[0]), sizeof(arSub29)/sizeof(arSub29[0]), sizeof(arSub29)/sizeof(arSub29[0]), sizeof(arSub31)/sizeof(arSub31[0]), 0, 0, 0,
#ifdef ENABLE_ATTR_TRANSFER_SYSTEM
	0,
#endif
	};