// Find PyObject * chrGetPixelPosition(PyObject* poSelf, PyObject* poArgs) and replace function with:
#ifdef ENABLE_OFFLINE_SHOP
PyObject * chrGetPixelPosition(PyObject* poSelf, PyObject* poArgs)
{
	int iVirtualID;
	if (!PyTuple_GetInteger(poArgs, 0, &iVirtualID))
		return Py_BuildException();

	CInstanceBase * pkInst = CPythonCharacterManager::Instance().GetInstancePtr(iVirtualID);
	if (!pkInst)
		return Py_BuildValue("iii", -100, -100, -100);

	TPixelPosition PixelPosition;
	pkInst->NEW_GetPixelPosition(&PixelPosition);
	return Py_BuildValue("fff", PixelPosition.x, PixelPosition.y, PixelPosition.z);
}
#else
PyObject * chrGetPixelPosition(PyObject* poSelf, PyObject* poArgs)
{
	int iVirtualID;
	if (!PyTuple_GetInteger(poArgs, 0, &iVirtualID))
		return Py_BuildException();

	CInstanceBase * pkInst = CPythonCharacterManager::Instance().GetInstancePtr(iVirtualID);

	if (!pkInst)
		return Py_BuildException();

	TPixelPosition PixelPosition;
	pkInst->NEW_GetPixelPosition(&PixelPosition);

	return Py_BuildValue("fff", PixelPosition.x, PixelPosition.y, PixelPosition.z);
}
#endif