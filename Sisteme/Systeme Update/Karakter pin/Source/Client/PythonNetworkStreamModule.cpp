Find - Bul:
PyObject* netSendChangeNamePacket(PyObject* poSelf, PyObject* poArgs)

Add it upper - Üstüne ekle:
PyObject* netSendCharacterPinPacket(PyObject* poSelf, PyObject* poArgs)
{
	int Index;
	if (!PyTuple_GetInteger(poArgs, 0, &Index))
		return Py_BuildException();

	int iPin;
	if (!PyTuple_GetInteger(poArgs, 1, &iPin))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendCharacterPinPacket(Index, iPin);
	return Py_BuildNone();
}


http://puu.sh/jS0Dt/8cf6be29c2.png



Find - Bul:
{ "SendSelectCharacterPacket",			netSendSelectCharacterPacket,			METH_VARARGS },

Add it upper - Üstüne ekle:
{ "SendCharacterPinPacket",				netSendCharacterPinPacket,				METH_VARARGS },


http://puu.sh/jS0G7/d0226af520.png


Find - Bul:
int stat4;
if (!PyTuple_GetInteger(poArgs, 7, &stat4))
	return Py_BuildException();

Add it under- Altına ekle:
int character_pin;
if (!PyTuple_GetInteger(poArgs, 8, &character_pin))
	return Py_BuildException();

http://puu.sh/jSEko/b1852b2c3c.png


Find - Bul:
rkNetStream.SendCreateCharacterPacket((BYTE) index, name, (BYTE) job, (BYTE) shape, stat1, stat2, stat3, stat4);

Change - Değiştir:
rkNetStream.SendCreateCharacterPacket((BYTE)index, name, (BYTE)job, (BYTE)shape, stat1, stat2, stat3, stat4, character_pin);


http://puu.sh/jSEm1/c1b3606d1d.png

