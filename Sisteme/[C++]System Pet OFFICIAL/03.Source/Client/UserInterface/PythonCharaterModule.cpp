//Search in this file:
#include "PythonCharacterManager.h"

//Add after:
#ifdef NEW_PET_SYSTEM
#include "PythonNetworkStream.h"
#include "PythonPlayer.h"
#endif

//Search in this file:
PyObject * chrRaceToSex(PyObject * poSelf, PyObject * poArgs)
{
	int race;
	if (!PyTuple_GetInteger(poArgs, 0, &race))
		return Py_BuildException();

	return Py_BuildValue("i", RaceToSex(race));
}

//Add after:
#ifdef NEW_PET_SYSTEM
PyObject* braveRequestPetName(PyObject* poSelf, PyObject* poArgs)
{
	const char * petname;

	if (!PyArg_ParseTuple(poArgs, "s", &petname)) {
		return Py_BuildException();
	}

	if (strlen(petname) > 12 || strlen(petname) < 4) {
		TraceError("RequestPetName: petname lenght not allowed!");
		return Py_BuildNone();
	}
	
	CPythonNetworkStream& rns = CPythonNetworkStream::Instance();
	rns.PetSetNamePacket(petname);
	return Py_BuildNone();
}
#endif

//Search in this file:
		{ "Revive",						chrRevive,							METH_VARARGS },
		{ "Die",						chrDie,								METH_VARARGS },

//Add after:
#ifdef NEW_PET_SYSTEM
		{ "RequestPetName",				braveRequestPetName,				METH_VARARGS },
#endif