// Search for:
PyObject * wndMgrSetToggleSlot(PyObject * poSelf, PyObject * poArgs)
{
	assert(!"wndMgrSetToggleSlot - Don't use such function");
	return Py_BuildNone();
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject * wndMgrEnableSlotCoverImage(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->EnableSlotCoverImage(iSlotIndex);

	return Py_BuildNone();
}

PyObject * wndMgrDisableSlotCoverImage(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->DisableSlotCoverImage(iSlotIndex);

	return Py_BuildNone();
}
#endif

// Search for:
PyObject * wndMgrDeactivateSlot(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->DeactivateSlot(iSlotIndex);
	return Py_BuildNone();
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject * wndMgrActivateChangeLookSlot(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->ActivateChangeLookSlot(iSlotIndex);
	return Py_BuildNone();
}

PyObject * wndMgrDeactivateChangeLookSlot(PyObject * poSelf, PyObject * poArgs)
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
	pSlotWin->DeactivateChangeLookSlot(iSlotIndex);
	return Py_BuildNone();
}
#endif

// Search for:
		{ "SetToggleSlot",				wndMgrSetToggleSlot,				METH_VARARGS },

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{ "EnableSlotCoverImage",		wndMgrEnableSlotCoverImage,			METH_VARARGS },
		{ "DisableSlotCoverImage",		wndMgrDisableSlotCoverImage,		METH_VARARGS },
#endif

// Search for:
		{ "DeactivateSlot",				wndMgrDeactivateSlot,				METH_VARARGS },

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{ "ActivateChangeLookSlot",		wndMgrActivateChangeLookSlot,		METH_VARARGS },
		{ "DeactivateChangeLookSlot",	wndMgrDeactivateChangeLookSlot,		METH_VARARGS },
#endif
