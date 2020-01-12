Search:
PyObject * wndMgrSetCoverButton(PyObject * poSelf, PyObject * poArgs)
{
	...
}

Add it under:
PyObject * wndMgrDeleteCoverButton(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWindow;
	pSlotWin->DeleteCoverButton(iSlotIndex);

	return Py_BuildNone();
}

PyObject * wndMgrHasCoverButton(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWindow;
	return Py_BuildValue("i", pSlotWin->HasCoverButton(iSlotIndex));
}

https://puu.sh/sgJST/7af0f18db6.png
---

Search:
		{ "SetCoverButton",				wndMgrSetCoverButton,				METH_VARARGS },

Add it under:
		{ "DeleteCoverButton",			wndMgrDeleteCoverButton,			METH_VARARGS },
		{ "HasCoverButton",				wndMgrHasCoverButton,				METH_VARARGS },


https://puu.sh/sgJSe/9c4fa72fd2.png