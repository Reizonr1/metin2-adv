cauti:
		DWORD			GetPlayerID() const	{ return m_dwPlayerID; }
iar sub adaugi:

#ifdef __ONEX_VIP__
		void			oneX_vip();
		bool			onex_vip_timp();
#endif
