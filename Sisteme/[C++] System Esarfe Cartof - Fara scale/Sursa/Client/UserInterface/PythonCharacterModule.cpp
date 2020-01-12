// 1) Search: kCreateData.m_dwHair=0;
// 2) After make a new line and paste:
		kCreateData.m_dwAcce=0;

// 1) Search: PyObject * chrChangeHair(PyObject* poSelf, PyObject* poArgs)
// 2) After make a new line and paste:
PyObject * chrSetAcce(PyObject* poSelf, PyObject* poArgs)
{
	int iRace;
	if (!PyTuple_GetInteger(poArgs, 0, &iRace))
		return Py_BuildException();
	
	CInstanceBase * pkInst = CPythonCharacterManager::Instance().GetSelectedInstancePtr();
	if (!pkInst)
		return Py_BuildNone();
	
	pkInst->SetAcce(iRace);
	return Py_BuildNone();
}

PyObject * chrChangeAcce(PyObject* poSelf, PyObject* poArgs)
{
	int iAcce;

	if (!PyTuple_GetInteger(poArgs, 0, &iAcce))
		return Py_BuildException();
	
	CInstanceBase * pkInst = CPythonCharacterManager::Instance().GetSelectedInstancePtr();
	if (!pkInst)
		return Py_BuildNone();
	
	pkInst->ChangeAcce(iAcce);
	return Py_BuildNone();
}

// 1) Search: kCreateData.m_dwHair = 100;
// 2) After make a new line and paste:
	kCreateData.m_dwAcce = 100;

// 1) Search: {"ChangeHair", chrChangeHair, METH_VARARGS},
// 2) After make a new line and paste:
		{"SetAcce", chrSetAcce, METH_VARARGS},
		{"ChangeAcce", chrChangeAcce, METH_VARARGS},

// 1) Search: PyModule_AddIntConstant(poModule, "PART_WEAPON_LEFT", CRaceData::PART_WEAPON_LEFT);
// 2) After make a new line and paste:
		PyModule_AddIntConstant(poModule, "PART_ACCE", CRaceData::PART_ACCE);