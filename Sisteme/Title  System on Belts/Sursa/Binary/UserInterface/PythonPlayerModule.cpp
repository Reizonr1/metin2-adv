// 1) Search: void initPlayer()
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
PyObject * playerChooseTitle(PyObject* poSelf, PyObject* poArgs)
{
	int iTitle = 0;
	if (!PyTuple_GetInteger(poArgs, 0, &iTitle))
		return Py_BadArgument();
	
	CPythonPlayer::Instance().RequestChangeTitle((int)iTitle);
	return Py_BuildNone();
}
#endif


// 1) Search: {NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		{"ChooseTitle", playerChooseTitle, METH_VARARGS},
#endif