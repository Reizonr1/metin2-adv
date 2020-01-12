// 1. Paste these functions "any"where in the file(where cannot summon syntax error<!>)
// ********************************* BEGIN ********************************* //
#ifdef WJ_ENABLE_TRADABLE_ICON
PyObject * wndMgrSetCanMouseEventSlot(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWnd;
	if (!PyTuple_GetWindow(poArgs, 0, &pWnd))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	if (!pWnd->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWnd = (UI::CSlotWindow *)pWnd;
	pSlotWnd->SetCanMouseEventSlot(iSlotIndex);
	return Py_BuildNone();
}

PyObject * wndMgrSetCantMouseEventSlot(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWnd;
	if (!PyTuple_GetWindow(poArgs, 0, &pWnd))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	if (!pWnd->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWnd = (UI::CSlotWindow *)pWnd;
	pSlotWnd->SetCantMouseEventSlot(iSlotIndex);
	return Py_BuildNone();
}

PyObject * wndMgrSetUsableSlotOnTopWnd(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWnd;
	if (!PyTuple_GetWindow(poArgs, 0, &pWnd))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	if (!pWnd->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWnd = (UI::CSlotWindow *)pWnd;
	pSlotWnd->SetUsableSlotOnTopWnd(iSlotIndex);
	return Py_BuildNone();
}

PyObject * wndMgrSetUnusableSlotOnTopWnd(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWnd;
	if (!PyTuple_GetWindow(poArgs, 0, &pWnd))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	if (!pWnd->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWnd = (UI::CSlotWindow *)pWnd;
	pSlotWnd->SetUnusableSlotOnTopWnd(iSlotIndex);
	return Py_BuildNone();
}
#endif
// ********************************** END ********************************** //

// 2. Extend the methodlist of module:
// ********************************* BEGIN ********************************* //
#ifdef WJ_ENABLE_TRADABLE_ICON
		{ "SetCanMouseEventSlot",		wndMgrSetCanMouseEventSlot,			METH_VARARGS },
		{ "SetCantMouseEventSlot",		wndMgrSetCantMouseEventSlot,		METH_VARARGS },
		{ "SetUsableSlotOnTopWnd",		wndMgrSetUsableSlotOnTopWnd,		METH_VARARGS },
		{ "SetUnusableSlotOnTopWnd",	wndMgrSetUnusableSlotOnTopWnd,		METH_VARARGS },
#endif
// ********************************** END ********************************** //

