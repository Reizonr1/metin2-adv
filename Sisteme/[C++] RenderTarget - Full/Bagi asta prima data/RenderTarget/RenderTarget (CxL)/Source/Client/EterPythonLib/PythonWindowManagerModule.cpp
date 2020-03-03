//1.1 Search:
PyObject * wndMgrRegisterBar(PyObject * poSelf, PyObject * poArgs)

//1.2 Add ABOVE:
PyObject * wndMgrRegisterRenderTarget(PyObject * poSelf, PyObject * poArgs)
{
	PyObject * po;
	if (!PyTuple_GetObject(poArgs, 0, &po))
		return Py_BuildException();
	char * szLayer;
	if (!PyTuple_GetString(poArgs, 1, &szLayer))
		return Py_BuildException();

	UI::CWindow * pWindow = UI::CWindowManager::Instance().RegisterRenderTarget(po, szLayer);
	return Py_BuildValue("i", pWindow);
}


//2.1 Search:
PyObject * wndBarSetColor(PyObject * poSelf, PyObject * poArgs)

//2.1 Add ABOVE:
PyObject * wndRenderTargetSetRenderTarget(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();
	int index;
	if (!PyTuple_GetInteger(poArgs, 1, &index))
		return Py_BuildException();

	if (pWindow->IsType(UI::CUiRenderTarget::Type()))
	{
		((UI::CUiRenderTarget *)pWindow)->SetRenderTarget(index);
	}
	return Py_BuildNone();
}


//3.1 Search:
		{ "RegisterBar",				wndMgrRegisterBar,					METH_VARARGS },

//3.2 Add after:
		{ "RegisterRenderTarget", wndMgrRegisterRenderTarget, METH_VARARGS },
		{ "SetRenderTarget", wndRenderTargetSetRenderTarget, METH_VARARGS },
