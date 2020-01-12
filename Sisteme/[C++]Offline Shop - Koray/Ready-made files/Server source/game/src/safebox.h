#ifndef __INC_METIN_II_GAME_SAFEBOX_H__
#define __INC_METIN_II_GAME_SAFEBOX_H__

class CHARACTER;
class CItem;
class CGrid;

class CSafebox
{
	public:
#ifdef __OFFLINE_SHOP__
		CSafebox(LPCHARACTER pkChrOwner, int iSize, uint64_t dwGold);
#else
		CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold);
#endif
		~CSafebox();

		bool		Add(DWORD dwPos, LPITEM pkItem);
		LPITEM		Get(DWORD dwPos);
		LPITEM		Remove(DWORD dwPos);
		void		ChangeSize(int iSize);

		bool		MoveItem(BYTE bCell, BYTE bDestCell, BYTE count);
		LPITEM		GetItem(BYTE bCell);

		void		Save();

		bool		IsEmpty(DWORD dwPos, BYTE bSize);
		bool		IsValidPosition(DWORD dwPos);

		void		SetWindowMode(BYTE bWindowMode);
#ifdef __OFFLINE_SHOP__
		void		SetGold(int64_t llGold);
		uint64_t	GetGold() { return  m_lGold; };
#endif

	protected:
		void		__Destroy();

		LPCHARACTER	m_pkChrOwner;
		LPITEM		m_pkItems[SAFEBOX_MAX_NUM];
		CGrid *		m_pkGrid;
		int		m_iSize;
#ifdef __OFFLINE_SHOP__
		uint64_t	m_lGold;
#else
		long		m_lGold;
#endif
		BYTE		m_bWindowMode;
};

#endif
