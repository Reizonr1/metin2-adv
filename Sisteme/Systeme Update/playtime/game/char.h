*char.h

Find - Bul:
BYTE			GetChatCounter() const;

Add it under- Altına ekle:
		DWORD			GetLogonTime();
		void			CheckLogonTime(int time);
		void			InitCharLogonEvent();

Find - Bul:
BYTE			m_bCharType;

Add it under- Altına ekle:
		LPEVENT			m_pkLogonEvent;
		DWORD			m_dwLogonTime;
		int				m_iLogonIsRewarded;
		int				m_iLogonIsStarted;
		
http://puu.sh/kmwGi/4678a627c9.png