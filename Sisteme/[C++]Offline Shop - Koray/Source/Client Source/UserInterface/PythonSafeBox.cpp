Search:
void CPythonSafeBox::SetMoney(DWORD dwMoney)
{
	m_dwMoney = dwMoney;
}

DWORD CPythonSafeBox::GetMoney()
{
	return m_dwMoney;
}

Change:
#ifdef __OFFLINE_SHOP__
void CPythonSafeBox::SetMoney(uint64_t dwMoney)
{
	m_dwMoney = dwMoney;
}

uint64_t CPythonSafeBox::GetMoney()
{
	return m_dwMoney;
}
#else
void CPythonSafeBox::SetMoney(DWORD dwMoney)
{
	m_dwMoney = dwMoney;
}

DWORD CPythonSafeBox::GetMoney()
{
	return m_dwMoney;
}
#endif

https://puu.sh/sgMho/da2b5b14ff.png

---

Search:
PyObject * safeboxGetMoney(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSafeBox::Instance().GetMoney());
}

Change:
PyObject * safeboxGetMoney(PyObject * poSelf, PyObject * poArgs)
{
#ifdef __OFFLINE_SHOP__
	return PyLong_FromUnsignedLongLong(CPythonSafeBox::Instance().GetMoney());
#else
	return Py_BuildValue("i", CPythonSafeBox::Instance().GetMoney());
#endif
}

https://puu.sh/sgMj9/7ecef4106c.png
