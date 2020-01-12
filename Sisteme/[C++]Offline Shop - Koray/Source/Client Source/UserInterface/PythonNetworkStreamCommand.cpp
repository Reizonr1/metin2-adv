Search:
void CPythonNetworkStream::ServerCommand(char * c_szCommand)

Add it upper:
#ifdef __OFFLINE_SHOP__
void CPythonNetworkStream::SetShopMoveMode(int iType)
{
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_SetOfflineShopMoveMode", Py_BuildValue("(i)", iType));
}
#endif

https://puu.sh/sgLqK/fe2cc50cc7.png