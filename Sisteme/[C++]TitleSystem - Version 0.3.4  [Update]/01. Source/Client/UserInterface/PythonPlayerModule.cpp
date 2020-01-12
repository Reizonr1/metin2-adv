// 1) Search:	PyObject * playerGetAlignmentData(PyObject* poSelf, PyObject* poArgs)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
PyObject * playerGetPrestigeData(PyObject* poSelf, PyObject* poArgs)
{
	CInstanceBase * pInstance = CPythonPlayer::Instance().NEW_GetMainActorPtr();
	int iPrestigePoint = 0;
	int iPrestigeGrade = 4;
	if (pInstance)
	{
		iPrestigePoint = pInstance->GetPrestige();
		iPrestigeGrade = pInstance->GetPrestigeGrade();
	}
	return Py_BuildValue("ii", iPrestigePoint, iPrestigeGrade);
}
#endif

// 1) Search:		{ "GetAlignmentData",			playerGetAlignmentData,				METH_VARARGS },
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		{ "GetPrestigeData",			playerGetPrestigeData,				METH_VARARGS },
#endif
