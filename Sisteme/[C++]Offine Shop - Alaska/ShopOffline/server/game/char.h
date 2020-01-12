
//find class CArena; and add after

#ifdef OFFLINE_SHOP
#include "../libgame/include/grid.h"
typedef struct SPrivShop
{
	DWORD	shop_id;
	DWORD	shop_vid;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	item_count;
	BYTE	rest_count;
	BYTE	days;
	DWORD	date_close;
	long long gold;

} TPrivShop;

typedef std::map<DWORD, TPrivShop> PSHOP_MAP;
#endif

#ifdef GIFT_SYSTEM
typedef struct SGiftItem
{
	DWORD	id;
	WORD	pos;
#ifdef FULL_YANG
	long long    count;
#else
	DWORD count;
#endif
	DWORD	vnum;
	long	alSockets[ITEM_SOCKET_MAX_NUM];	// ĽŇÄĎąřČŁ

	TPlayerItemAttribute    aAttr[ITEM_ATTRIBUTE_MAX_NUM];
	char szFrom[101];
	char szReason[101];
	DWORD dwDateAdd;
} TGiftItem;
typedef std::map<int, std::vector<TGiftItem> > GIFT_MAP;
#endif

[..]
/*
Add before:
};

ESex GET_SEX(LPCHARACTER ch);

*/

#ifdef OFFLINE_SHOP
	public:
		void			OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount, DWORD days);
		void			SendShops(bool isGm = false);
		void			OpenShop(DWORD id, const char *name, bool onboot = false);
		void			SetPrivShop(DWORD shop_id) { bprivShop = shop_id; }
		BOOL			IsPrivShop(void)  const { return bprivShop>0; }
		DWORD			GetPrivShop()  const { return bprivShop; }
		void			SetPrivShopOwner(DWORD id) { bprivShopOwner = id; }
		DWORD			GetPrivShopOwner()  const { return bprivShopOwner; }
		void			DeleteMyShop();
		DWORD			GetShopTime()  const { return dw_ShopTime; }
		void			SetShopTime(DWORD time) { dw_ShopTime = time; }
		void			SetShopSign(const char * name);
		void			LoadPrivShops();
		TPrivShop		GetPrivShopTable(DWORD id);
		void			RemovePrivShopTable(DWORD id);
		void			UpdatePrivShopTable(DWORD id, TPrivShop shop);
		void			UpdateShopItems();
		void			SendShopCost();
	private:
		PSHOP_MAP		m_mapshops;
		DWORD			bprivShop;
		DWORD			bprivShopOwner;
		DWORD			dw_ShopTime;
	public:
		void			StartRefreshShopEvent();
	protected:
		LPEVENT			m_pkRefreshShopEvent;
#endif	

#ifdef GIFT_SYSTEM
	protected:
		void			AddGiftGrid(int page);
		int				AddGiftGridItem(int page, int size);
		GIFT_MAP		m_mapGiftGrid;
		LPEVENT			m_pkGiftRefresh;
		DWORD			m_dwLastGiftPage;
	public:
		void			StartRefreshGift();
		void			LoadGiftPage(int page);
		void			RefreshGift();
		int				GetGiftPages() { return m_mapGiftGrid.size(); }
		int				GetLastGiftPage() { return m_dwLastGiftPage; }
#endif
	
[..]