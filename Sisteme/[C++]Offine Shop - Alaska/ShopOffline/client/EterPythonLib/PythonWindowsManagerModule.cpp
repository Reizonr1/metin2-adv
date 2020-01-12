//add new function
PyObject * wndMgrSetSlotID(PyObject * poSelf, PyObject * poArgs)
{
	UI::CWindow * pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();

	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iSlotIndex))
		return Py_BuildException();

	int id;
	if (!PyTuple_GetInteger(poArgs, 2, &id))
		return Py_BuildException();

	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	UI::CSlotWindow * pSlotWin = (UI::CSlotWindow *)pWin;
	pSlotWin->SetSlotID(iSlotIndex, id);

	return Py_BuildNone();
}

//find and add new function to list
void initwndMgr()
{
	static PyMethodDef s_methods[] =
	{
		[..]
		
		{ "SetSlotID",					wndMgrSetSlotID,					METH_VARARGS },
		[..]
	};
[..]
}