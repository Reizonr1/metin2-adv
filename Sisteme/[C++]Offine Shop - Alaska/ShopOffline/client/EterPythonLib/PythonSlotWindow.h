#pragma once

#include "PythonWindow.h"

namespace UI 
{
	
	class CSlotWindow : public CWindow
	{
		public:
			static DWORD Type();

		public:
			[..]

			typedef struct SSlot
			{
				DWORD	dwState;
				DWORD	dwSlotNumber;
				DWORD	dwCenterSlotNumber;		// NOTE : 사이즈가 큰 아이템의 경우 아이템의 실제 위치 번호
				DWORD	dwItemIndex;			// NOTE : 여기서 사용되는 Item이라는 단어는 좁은 개념의 것이 아닌,
				BOOL	isItem;					//        "슬롯의 내용물"이라는 포괄적인 개념어. 더 좋은 것이 있을까? - [levites]
				DWORD	dwItemID;
				[..]
			} TSlot;
			typedef std::list<TSlot> TSlotList;
			typedef TSlotList::iterator TSlotListIterator;

		public:
			CSlotWindow(PyObject * ppyObject);
			[..]
			void SetSlotID(DWORD dwIndex, DWORD dwID);
			
		[..]
	};
};