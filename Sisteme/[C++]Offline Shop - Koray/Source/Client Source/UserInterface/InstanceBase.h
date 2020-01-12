Search:
			NAMECOLOR_WAYPOINT,

Add it under:
#ifdef __OFFLINE_SHOP__
			NAMECOLOR_OFFSHOP,
#endif


https://puu.sh/sgKeP/26b8bcc14a.png


---

Search:
		DWORD					m_dwGuildID;

Add it under:
		bool					m_bIsHidden;
	public:
		bool					IsHidden();

https://puu.sh/sgKgE/db8a4fbb8d.png
---

Search:
		void __EffectContainer_Initialize();
		void __EffectContainer_Destroy();

Add it under:
		void __EffectContainer_Suspend();
		void __EffectContainer_Continue();




