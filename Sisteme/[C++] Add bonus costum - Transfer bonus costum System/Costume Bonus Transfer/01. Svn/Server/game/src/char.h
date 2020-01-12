// 1) Search: #include "cube.h"
// 2) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
#include "attr_transfer.h"
#endif

// 1) Search: LPCHARACTER		pCubeNpc;
// 2) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	LPITEM			pAttrTransferItems[MAX_ATTR_TRANSFER_SLOT];
	LPCHARACTER		pAttrTransferNpc;
#endif

// 1) Search: #ifdef __PET_SYSTEM__
// 2) At the end of definition make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	public:
		LPITEM*	GetAttrTransferItem() {return m_pointsInstant.pAttrTransferItems;}
		bool IsAttrTransferOpen () const	{return (m_pointsInstant.pAttrTransferNpc?true:false);}
		void SetAttrTransferNpc(LPCHARACTER npc)	{m_pointsInstant.pAttrTransferNpc = npc;}
		bool CanDoAttrTransfer() const;
#endif