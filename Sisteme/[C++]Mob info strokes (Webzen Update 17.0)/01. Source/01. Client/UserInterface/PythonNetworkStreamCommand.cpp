//1.) Search for:
	else if (!strcmpi(szCmd, "ObserverTeamInfo"))
	{		
	}
//2.) Add after:
#ifdef WJ_SHOW_STROKE_INFO
	else if (!strcmpi(szCmd, "RegisterStroke"))
	{
		int targetVID = atoi(TokenVector[1].c_str());
		int value = atoi(TokenVector[2].c_str());
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RegisterStroke", Py_BuildValue("(ii)", targetVID, value));
	}
#endif