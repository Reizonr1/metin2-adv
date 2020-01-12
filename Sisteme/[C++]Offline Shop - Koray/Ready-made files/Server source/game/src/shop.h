#ifndef __INC_METIN_II_GAME_SHOP_H__
#define __INC_METIN_II_GAME_SHOP_H__

enum
{
	SHOP_MAX_DISTANCE = 1000
};

class CGrid;

/* ---------------------------------------------------------------------------------- */
class CShop
{
	public:
		typedef struct shop_item
		{
			DWORD	vnum;		// 아이템 번호
			long	price;		// 가격
#ifdef __OFFLINE_SHOP__
			long	price2;
			long	price3;
			long	price4;
#endif
			BYTE	count;		// 아이템 개수

			LPITEM	pkItem;
			int		itemid;		// 아이템 고유아이디
#ifdef __OFFLINE_SHOP__		
			int		isSold;
#endif

			shop_item()
			{
				vnum = 0;
				price = 0;
#ifdef __OFFLINE_SHOP__
				price2 = 0;
				price3 = 0;
				price4 = 0;
#endif				
				count = 0;
				itemid = 0;
#ifdef __OFFLINE_SHOP__
				isSold = 0;
#endif
				pkItem = NULL;
			}
		} SHOP_ITEM;

		CShop();
		~CShop();

		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
#ifdef __OFFLINE_SHOP__
		bool	Create(TOfflineShopTable* table);
		void	SetShopItems(LPCHARACTER pkOwner, TShopItemTable * pItemTable, BYTE bItemCount);
#else
		void	SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);
#endif

		virtual void		SetPCShop(LPCHARACTER ch) { m_pkPC = ch; };
		virtual LPCHARACTER GetPCShop() { return m_pkPC; }
		virtual bool		IsPCShop() { return m_pkPC ? true : false; };

#ifdef __OFFLINE_SHOP__
		virtual void SetOwner(DWORD dwOwnerAID, DWORD dwOwnerPID);
		virtual DWORD GetOwner() { return m_dwOwnerPID; };
		virtual bool HasOwner() { return m_dwOwnerPID ? true : false; };

		virtual uint64_t GetMoney() { return m_Money; };

		virtual void SetShopColor(BYTE bColor) { m_bColor = bColor; };
		virtual void SetShopSize(BYTE bSize) { m_bSize = bSize; };

		virtual void SetLocked(bool bType) { m_bIsLocked = bType; };
		virtual bool IsLocked() { return m_bIsLocked; };

		DWORD GetSoldItemVnum(BYTE pos);
		BYTE GetSoldCount(BYTE pos);
		long GetSoldPrice(BYTE pos, BYTE type);
		const long* GetSoldSockets(BYTE pos);
		const TPlayerItemAttribute* GetSoldAttributes(BYTE pos);
#if 0
		const char* GetSoldNewOwner(BYTE pos);
		DWORD GetSoldDate(BYTE pos);
#endif
#endif
		// 게스트 추가/삭제
		virtual bool	AddGuest(LPCHARACTER ch,DWORD owner_vid, bool bOtherEmpire);
		void	RemoveGuest(LPCHARACTER ch);

		// 물건 구입
		virtual int	Buy(LPCHARACTER ch, BYTE pos);

		// 게스트에게 패킷을 보냄
		void	BroadcastUpdateItem(BYTE pos);

		// 판매중인 아이템의 갯수를 알려준다.
		int		GetNumberByVnum(DWORD dwVnum);

		// 아이템이 상점에 등록되어 있는지 알려준다.
		virtual bool	IsSellingItem(DWORD itemID);

		DWORD	GetVnum() { return m_dwVnum; }
		DWORD	GetNPCVnum() { return m_dwNPCVnum; }
#ifdef __OFFLINE_SHOP__
		void	Apply();
		void	Remove();
#endif
	protected:
		void	Broadcast(const void * data, int bytes);

	protected:
		DWORD				m_dwVnum;
		DWORD				m_dwNPCVnum;

		CGrid *				m_pGrid;

		typedef TR1_NS::unordered_map<LPCHARACTER, bool> GuestMapType;
		GuestMapType m_map_guest;
		std::vector<SHOP_ITEM>		m_itemVector;	// 이 상점에서 취급하는 물건들

		LPCHARACTER			m_pkPC;
#ifdef __OFFLINE_SHOP__
		typedef struct shop_sold_info
		{
			CShop* lpShop;
			DWORD vnum;
			long Price;
			long Price2;
			long Price3;
			long Price4;
			BYTE Count;
			long	alSockets[ITEM_SOCKET_MAX_NUM];
			TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#if 0
			DWORD	soldDate;
			char	newOwner[CHARACTER_NAME_MAX_LEN + 1];
#endif
		} SShopSoldData;
		std::map<BYTE, SShopSoldData> m_SoldItems;

		bool				m_bIsLocked;
		DWORD				m_dwOwnerAID;
		DWORD				m_dwOwnerPID;
		uint64_t			m_Money;
		BYTE				m_bSize;
		BYTE				m_bColor;
#endif
};

#endif 
