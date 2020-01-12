#pragma once
class COfflineShopManager : public singleton<COfflineShopManager>
{
	public:
		typedef std::map<DWORD, COfflineShop *> TShopMap;
		typedef std::map<DWORD, DWORD> TOfflineShopMap;
	public:
		COfflineShopManager();
		~COfflineShopManager();

		bool StartShopping(LPCHARACTER pkChr, LPCHARACTER pkChrShopKeeper);
		void StopShopping(LPCHARACTER ch);

		void Buy(LPCHARACTER ch, BYTE bPos);

		LPOFFLINESHOP	CreateOfflineShop(LPCHARACTER npc, DWORD dwOwnerPID);
		LPOFFLINESHOP	FindOfflineShop(DWORD dwVID);
		void			DestroyOfflineShop(LPCHARACTER ch, DWORD dwVID, bool bDestroyAll = false);
		
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		void			AddItem(LPCHARACTER ch, BYTE bDisplayPos, BYTE bPos, long long llPrice);
#else
		void			AddItem(LPCHARACTER ch, BYTE bDisplayPos, BYTE bPos, int iPrice);
#endif
		void			RemoveItem(LPCHARACTER ch, BYTE bPos);
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		void			ChangePrice(LPCHARACTER ch, BYTE bPos, long long llPrice);
#else
		void			ChangePrice(LPCHARACTER ch, BYTE bPos, DWORD dwPrice);
#endif
		void			Refresh(LPCHARACTER ch);
        void            RefreshMoney(LPCHARACTER ch);

		DWORD			FindMyOfflineShop(DWORD dwPID);
		void			ChangeOfflineShopTime(LPCHARACTER ch, BYTE bTime);
		void			WithdrawMoney(LPCHARACTER ch, long long llRequiredMoney);
		BYTE			LeftItemCount(LPCHARACTER ch);

		void			RefreshUnsoldItems(LPCHARACTER ch);
		void			TakeItem(LPCHARACTER ch, BYTE bPos);
		bool			HasOfflineShop(LPCHARACTER ch);

	private:
		TOfflineShopMap	m_Map_pkOfflineShopByNPC2;
		TShopMap		m_map_pkOfflineShopByNPC;
};

