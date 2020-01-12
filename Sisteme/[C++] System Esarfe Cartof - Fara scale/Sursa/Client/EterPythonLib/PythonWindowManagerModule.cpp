// 1) Search: PyObject * wndMgrActivateSlot(PyObject * poSelf, PyObject * poArgs)
// 2) Make a new line and paste:
PyObject * wndMgrActivateAcceSlot(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();
	
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();
	
	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();
	
	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWin;
	pSlotWin->ActivateAcceSlot(iSlotIndex);
	return Py_BuildNone();
}

PyObject * wndMgrDeactivateAcceSlot(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();
	
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();
	
	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();
	
	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWin;
	pSlotWin->DeactivateAcceSlot(iSlotIndex);
	return Py_BuildNone();
}

// 1) Search: { "SetToggleSlot",				wndMgrSetToggleSlot,				METH_VARARGS },
// 2) Make a new line and paste:
		{"ActivateAcceSlot", wndMgrActivateAcceSlot, METH_VARARGS},
		{"DeactivateAcceSlot", wndMgrDeactivateAcceSlot, METH_VARARGS},