//1.) Search:
#define UPPER(c)		(((c) >= 'a' && (c) <= 'z') ? ((c) + ('A' - 'a')) : (c))
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	#include "PythonOxEvent.h"
#endif

//1.) Search:
	else if (!strcmpi(szCmd, "ObserverTeamInfo"))
	{		
	}
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT	
	else if (!strcmpi(szCmd, "oxevent_manager"))
	{
		 if ("open" == TokenVector[1])
		 {
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OxEvent_Append", Py_BuildValue("(iii)", APPEND_WINDOW, 0, 0));
		 }
		 if ("refresh" == TokenVector[1])
		 {
			int participantsCount = atoi(TokenVector[2].c_str());
			int observersCount = atoi(TokenVector[3].c_str());
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OxEvent_Append", Py_BuildValue("(iii)", APPEND_REFRESH, participantsCount, observersCount));
		 }		 
		 
	}
#endif