// serach this 

	typedef struct SChatLine
	{
	
	[]
	
		int iType;
		float fAppendedTime;
		D3DXCOLOR aColor[CHAT_LINE_COLOR_ARRAY_MAX_NUM];
		CGraphicTextInstance Instance;
		...
	[]
	
	}
// after this
			D3DXCOLOR aColor[CHAT_LINE_COLOR_ARRAY_MAX_NUM];
			CGraphicTextInstance Instance;
// add this
#ifdef ENABLE_GLOBAL_CHAT
	CGraphicImageInstance* ImageInstance;
#endif