//Find
PyObject* netSendItemUseToItemPacket(PyObject* poSelf, PyObject* poArgs)
{
	TItemPos SourceCell;
	TItemPos TargetCell;
	switch (PyTuple_Size(poArgs))
	{
	case 2:
		if (!PyTuple_GetInteger(poArgs, 0, &SourceCell.cell))
			return Py_BuildException();

		if (!PyTuple_GetInteger(poArgs, 1, &TargetCell.cell))
			return Py_BuildException();
		break;
	case 4:
		if (!PyTuple_GetByte(poArgs, 0, &SourceCell.window_type))
			return Py_BuildException();

		if (!PyTuple_GetInteger(poArgs, 1, &SourceCell.cell))
			return Py_BuildException();

		if (!PyTuple_GetByte(poArgs, 2, &TargetCell.window_type))
			return Py_BuildException();

		if (!PyTuple_GetInteger(poArgs, 3, &TargetCell.cell))
			return Py_BuildException();
		break;
	default:
		return Py_BuildException();
	}
	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendItemUseToItemPacket(SourceCell, TargetCell);
	return Py_BuildNone();
}

///Add
#ifdef NEW_ADD_INVENTORY
PyObject* netEnvanterpaketi(PyObject* poSelf, PyObject* poArgs)
{	
	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.Envanter_paketi();
	return Py_BuildNone();
}
#endif

//Find
{ "SendItemUseToItemPacket",			netSendItemUseToItemPacket,				METH_VARARGS },

///Add
#ifdef NEW_ADD_INVENTORY
	{ "Envanter_genislet",					netEnvanterpaketi,						METH_VARARGS },
#endif