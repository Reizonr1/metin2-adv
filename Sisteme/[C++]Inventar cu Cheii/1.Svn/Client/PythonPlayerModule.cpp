//Find
PyObject * playerGetElk(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetStatus(POINT_GOLD));
}

///Add
#ifdef NEW_ADD_INVENTORY
PyObject * playerGetEnvanter(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetStatus(POINT_BLACK));
}

//Find
{ "GetMoney",					playerGetElk,						METH_VARARGS },

///Add
#ifdef NEW_ADD_INVENTORY
		{ "GetEnvanter",				playerGetEnvanter,						METH_VARARGS },
#endif