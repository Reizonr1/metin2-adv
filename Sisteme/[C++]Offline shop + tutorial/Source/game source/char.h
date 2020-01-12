Arat ;
#define INSTANT_FLAG_NO_REWARD			(1 << 4)
Altına Ekle ;
#define INSTANT_FLAG_OFFLINE_SHOP		(1 << 5)






Arat ;
	LPENTITY		m_pDragonSoulRefineWindowOpener;

	Altına Ekle ;

	DWORD			real_owner;
	bool			isOfflineShop;
	int                     leftTime;
	BYTE			bSaveTime;
	BYTE			bChannel;
	DWORD			dwVID;

Arat ;
class CShop;
typedef class CShop * LPSHOP;

Altına Ekle ;
class COfflineShop;
typedef class COfflineShop * LPOFFLINESHOP;








Arat ;
	protected:

		LPSHOP			m_pkShop;
		LPSHOP			m_pkMyShop;
		std::string		m_stShopSign;
		LPCHARACTER		m_pkChrShopOwner;


		Altına Ekle ;

	public:

		void			SetOfflineShop(LPOFFLINESHOP pkOfflineShop);
		LPOFFLINESHOP	GetOfflineShop() const { return m_pkOfflineShop; }

		void			SetOfflineShopOwner(LPCHARACTER ch) { m_pkChrOfflineShopOwner = ch; }
		LPCHARACTER		GetOfflineShopOwner() const { return m_pkChrOfflineShopOwner; }

		void			SetOfflineShopRealOwner(DWORD dwVID) { m_pointsInstant.real_owner = dwVID; }
		DWORD			GetOfflineShopRealOwner() const { return m_pointsInstant.real_owner; }

		void			SetOfflineShopNPC(bool flag) { m_pointsInstant.isOfflineShop = flag; }
		bool			IsOfflineShopNPC() const { return m_pointsInstant.isOfflineShop; }

		void			OpenMyOfflineShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount, BYTE bTime);

		void			SetOfflineShopTimer(int iTime) { m_pointsInstant.leftTime = iTime; }
		int				GetOfflineShopTimer() { return m_pointsInstant.leftTime; }
		void			SetOfflineShopSaveTime(BYTE bSaveTime) { m_pointsInstant.bSaveTime = bSaveTime; }
		BYTE			GetOfflineShopSaveTime() { return m_pointsInstant.bSaveTime; }

		void			SetOfflineShopSign(const char * c_pszSign);

		void			DestroyOfflineShop();

		void			StartOfflineShopUpdateEvent();
		void			StopOfflineShopUpdateEvent();

		void			SetOfflineShopChannel(BYTE bChannel) { m_pointsInstant.bChannel = bChannel; }
		BYTE			GetOfflineShopChannel() { return m_pointsInstant.bChannel; }

		void			SetOfflineShopVID(DWORD dwVID) { m_pointsInstant.dwVID = dwVID; }
		DWORD			GetOfflineShopVID() { return m_pointsInstant.dwVID; }

	protected:
		LPOFFLINESHOP	m_pkOfflineShop;
		LPCHARACTER		m_pkChrOfflineShopOwner;
		std::string		m_stOfflineShopSign;

		
		
		
		
		
Arat ;
		LPEVENT				m_pkPetSystemUpdateEvent;
Altına Ekle ;

		LPEVENT				m_pkOfflineShopUpdateEvent;