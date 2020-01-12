#ifndef __INC_METIN_II_GAME_SHOP_MANAGER_H__
#define __INC_METIN_II_GAME_SHOP_MANAGER_H__

class CShop;
typedef class CShop * LPSHOP;

class CShopManager : public singleton<CShopManager>
{
public:
	typedef std::map<DWORD, CShop *> TShopMap;
#ifdef __OFFLINE_SHOP__
	typedef std::map< DWORD, std::vector<DWORD> > TOfflineShopMap; // PID - VID Container
#endif

public:
	CShopManager();
	virtual ~CShopManager();

	bool	Initialize(TShopTable * table, int size);
#ifdef __OFFLINE_SHOP__
	bool	Initialize(TOfflineShopTable * table, int size);
#endif
	void	Destroy();
#ifdef __OFFLINE_SHOP__
	void	GetOfflineShops(DWORD dwPID);
	void	GotoOfflineShop(DWORD dwPID, DWORD dwVID);
	void	WarpOfflineShop(DWORD dwPID, DWORD dwVID);
	void	CloseOfflineShop(DWORD dwPID, DWORD dwVID);
#endif
	LPSHOP	Get(DWORD dwVnum);
	LPSHOP	GetByNPCVnum(DWORD dwVnum);

	bool	StartShopping(LPCHARACTER pkChr, LPCHARACTER pkShopKeeper, int iShopVnum = 0);
	void	StopShopping(LPCHARACTER ch);

	void	Buy(LPCHARACTER ch, BYTE pos);
	void	Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount=0);

	LPSHOP	CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount);
#ifdef __OFFLINE_SHOP__
	LPSHOP	CreateOfflineShop(LPCHARACTER ch, BYTE bSize, BYTE bColor, TShopItemTable * pTable, BYTE bItemCount);
	DWORD	GetOfflineShopCount(DWORD dwPID) { return m_map_pkOfflineShop[dwPID].size(); }
	DWORD	GetOfflineShopCount() { return m_map_pkOfflineShop.size(); }
#endif
	LPSHOP	FindPCShop(DWORD dwVID);
	void	DestroyPCShop(LPCHARACTER ch);

private:
	TShopMap	m_map_pkShop;
	TShopMap	m_map_pkShopByNPCVnum;
	TShopMap	m_map_pkShopByPC;
#ifdef __OFFLINE_SHOP__
	TOfflineShopMap	m_map_pkOfflineShop;
#endif

	bool	ReadShopTableEx(const char* stFileName);
};

#endif