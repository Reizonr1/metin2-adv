// 1) Search:
void initwndMgr()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
PyObject * wndMgrActivateEffect(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();
	
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();
	
	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();
	
	float r, g, b, a;
	if (!PyTuple_GetFloat(poArgs, 2, &r))
		return Py_BuildException();
	
	if (!PyTuple_GetFloat(poArgs, 3, &g))
		return Py_BuildException();
	
	if (!PyTuple_GetFloat(poArgs, 4, &b))
		return Py_BuildException();
	
	if (!PyTuple_GetFloat(poArgs, 5, &a))
		return Py_BuildException();
	
	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWin;
	pSlotWin->ActivateEffect(iSlotIndex, r, g, b, a);
	return Py_BuildNone();
}

PyObject * wndMgrDeactivateEffect(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->DeactivateEffect(iSlotIndex);
	return Py_BuildNone();
}
#endif


// 1) Search:
		{NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{"ActivateEffect", wndMgrActivateEffect, METH_VARARGS},
		{"DeactivateEffect", wndMgrDeactivateEffect, METH_VARARGS},
#endif