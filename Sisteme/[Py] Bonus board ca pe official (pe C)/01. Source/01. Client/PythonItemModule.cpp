// Search void initItem() add above:

PyObject * itemGetApplyPoint(PyObject* poSelf, PyObject* poArgs)
{
	int applyType = 0;
	if (!PyTuple_GetInteger(poArgs, 0, &applyType))
		return Py_BadArgument();

	return Py_BuildValue("i", ApplyTypeToPointType((BYTE)applyType));
}

// Search static PyMethodDef s_methods[] = add:

{ "GetApplyPoint",					itemGetApplyPoint,						METH_VARARGS },