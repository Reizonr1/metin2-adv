// 1) Search: enum EAutoPotionType
// 2) After their function make a new line and paste:
		struct SAcceInfo
		{
			SAcceInfo() : bActivated(false) {}
			
			bool bActivated;
			long inventorySlotIndex;
		};

// 1) Search: __inline void					 SetAutoPotionInfo(int type, const SAutoPotionInfo& info)	{ m_kAutoPotionInfo[type] = info; }
// 2) After make a new line and paste:
		__inline const	SAcceInfo& GetAcceInfo() const	{return m_kAcceInfo;}
		__inline		SAcceInfo& GetAcceInfo()		{return m_kAcceInfo;}
		__inline void					 SetAcceInfo(const SAcceInfo& info)	{m_kAcceInfo = info;}

// 1) Search: SAutoPotionInfo			m_kAutoPotionInfo[AUTO_POTION_TYPE_NUM];
// 2) After make a new line and paste:
		SAcceInfo	m_kAcceInfo;