// 1) Search: PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_MaterialInfo", Py_BuildValue("(iis)", requestStartIndex, resultCount, TokenVector[4].c_str()));
// 2) After "}}" make a new line and paste:
#ifdef ENABLE_ATTR_TRANSFER_SYSTEM
	else if (!strcmpi(szCmd, "attrtransfer"))
	{
		if (TokenVector.size() < 2)
		{
			TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
			return;
		}
		
		if ("open" == TokenVector[1])
		{
			if (TokenVector.size() < 2)
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
			
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AttrTransfer_Open", Py_BuildValue("()"));
		}
		else if ("close" == TokenVector[1])
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AttrTransfer_Close", Py_BuildValue("()"));
		}
		else if ("success" == TokenVector[1])
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AttrTransfer_Success", Py_BuildValue("()"));
		}
	}
#endif