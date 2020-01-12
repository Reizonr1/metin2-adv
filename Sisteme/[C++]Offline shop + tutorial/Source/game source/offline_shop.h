#pragma once

enum
{
	OFFLINE_SHOP_MAX_DISTANCE = 1500,
};

class COfflineShop
{
	public:
		COfflineShop();
		~COfflineShop();

		virtual void	SetOfflineShopNPC(LPCHARACTER npc);
		virtual bool	IsOfflineShopNPC(){ return m_pkOfflineShopNPC ? true : false; }

		virtual bool	AddGuest(LPCHARACTER ch, LPCHARACTER npc);
		
		void			RemoveGuest(LPCHARACTER ch);
		void			RemoveAllGuest();
		void			Destroy(LPCHARACTER npc);

		virtual int		Buy(LPCHARACTER ch, BYTE bPos);
		
		void			BroadcastUpdateItem(BYTE bPos, DWORD dwPID, bool bDestroy = false);
		void			BroadcastUpdatePrice(BYTE bPos, DWORD dwPrice);
		void			Refresh(LPCHARACTER ch);

		bool			RemoveItem(DWORD dwVID, BYTE bPos);
		BYTE			GetLeftItemCount(DWORD dwPID);
	protected:
		void			Broadcast(const void * data, int bytes);

	private:
		// Grid
		CGrid *				m_pGrid;

		// Guest Map
		typedef TR1_NS::unordered_map<LPCHARACTER, bool> GuestMapType;
		GuestMapType m_map_guest;
		// End Of Guest Map

		LPCHARACTER m_pkOfflineShopNPC;
};

