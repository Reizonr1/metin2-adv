class CItem : public CEntity
{
	protected:
		// override methods from ENTITY class
		virtual void	EncodeInsertPacket(LPENTITY entity);
		virtual void	EncodeRemovePacket(LPENTITY entity);

	[..]
#ifdef OFFLINE_SHOP
	public:
		void		SetRealID(DWORD id)		{ m_dwRealID = id; }
		DWORD		GetRealID()			{ return m_dwRealID; }
	protected:
		DWORD			m_dwRealID;
#endif
};