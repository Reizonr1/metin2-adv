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
// make changes line this
	public:
		typedef struct shop_item
		{
			DWORD	vnum;		// 아이템 번호
			#ifdef FULL_YANG
			long	long	price;		// °ˇ°Y
			#else
			DWORD	price;		// °ˇ°Y
			#endif
			BYTE	count;		// 아이템 개수

			LPITEM	pkItem;
			int		itemid;		// 아이템 고유아이디
			shop_item()
			{
				vnum = 0;
				price = 0;
				count = 0;
				itemid = 0;
				pkItem = NULL;
			}
		} SHOP_ITEM;
//add new defines
	[..]
	
#ifdef OFFLINE_SHOP
public:
	int		GetItemCount();
	bool	GetItems();
	void	SetLocked(bool val) { m_bLocked = val; }
	bool	IsLocked() { return m_bLocked; }
	void	RemoveGuests(LPCHARACTER except=NULL);
	void	ClearItems();
	void	SetPrivShopItems(std::vector<TShopItemTable *> map_shop);
	LPCHARACTER GetPC() { return m_pkPC; }
protected:
	bool					m_bLocked;
#endif
	[..]