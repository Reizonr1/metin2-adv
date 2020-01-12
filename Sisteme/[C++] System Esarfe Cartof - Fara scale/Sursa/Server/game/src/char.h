// 1) Search: #include "mining.h"
// 2) After make a new line and paste:
#include "acce.h"

// 1) Search: LPCHARACTER		pCubeNpc;
// 2) After make a new line and paste:
	LPITEM			pAcceItems[ACCE_MAX_NUM];
	LPCHARACTER		pAcceNpc;

// 1) Search: bool			RefineItem(LPITEM pkItem, LPITEM pkTarget);
// 2) After make a new line and paste:
		bool			CleanAcceAttr(LPITEM pkItem, LPITEM pkTarget);

// 1) Search: void			AutoGiveItem(LPITEM item, bool longOwnerShip = false);
// 2) After make a new line and paste:
		LPITEM			AutoGiveAcce(DWORD dwItemVnum, BYTE bCount = 1, int iSocketTwo = 0, int iRarePct = -1, bool bMsg = true);
		void			AutoGiveAcce(LPITEM item, bool longOwnerShip = false);

// 1) Search: bool CanDoCube() const;
// 2) After make a new line and paste:
		LPITEM*	GetAcceItem() {return m_pointsInstant.pAcceItems;}
		bool IsAcceOpen () const	{return (m_pointsInstant.pAcceNpc?true:false);}
		void SetAcceNpc(LPCHARACTER npc)	{m_pointsInstant.pAcceNpc = npc;}
		bool CanDoAcce() const;