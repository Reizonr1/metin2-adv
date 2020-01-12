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
				DWORD	dwCenterSlotNumber;		// NOTE : ����� ū �������� ��� �������� ���� ��ġ ��ȣ
				DWORD	dwItemIndex;			// NOTE : ���⼭ ���Ǵ� Item�̶�� �ܾ�� ���� ������ ���� �ƴ�,
				BOOL	isItem;					//        "������ ���빰"�̶�� �������� �����. �� ���� ���� ������? - [levites]
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