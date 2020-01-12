#include "StdAfx.h"
#include "../eterBase/CRC32.h"
#include "../eterBase/Filename.h"
#include "PythonWindow.h"
#include "PythonSlotWindow.h"

//#define __RENDER_SLOT_AREA__

using namespace UI;

[..]
##find function BOOL CSlotWindow::OnMouseLeftButtonUp() and add after 
void CSlotWindow::SetSlotID(DWORD dwIndex, DWORD dwID)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	if (dwID <= 0)
	{
		return;
	}
	else
	{
		
		pSlot->dwItemID=dwID;
	}
}
[..]
##find BOOL CSlotWindow::OnOverInItem(DWORD dwSlotNumber) and replace
BOOL CSlotWindow::OnOverInItem(DWORD dwSlotNumber)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwSlotNumber, &pSlot))
		return FALSE;

	if (!pSlot->isItem)
		return FALSE;

	if (pSlot->dwSlotNumber == m_dwToolTipSlotNumber)
		return TRUE;

	m_dwToolTipSlotNumber = dwSlotNumber;
	PyCallClassMemberFunc(m_poHandler, "OnOverInItem", Py_BuildValue("(iii)", dwSlotNumber,pSlot->dwItemIndex,pSlot->dwItemID));

	return TRUE;
}