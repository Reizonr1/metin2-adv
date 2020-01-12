//Aratýn
	// GIFT NOTIFY
	else if (!strcmpi(szCmd, "gift"))
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "Gift_Show", Py_BuildValue("()")); 	
	}
	
//Altýna Ekleyin
	///Blackkkk
	else if (!strcmpi(szCmd, "black"))
	{
		UINT black 		= atoi(TokenVector[1].c_str()); //toplam
		UINT sari 		= atoi(TokenVector[2].c_str());
		UINT kirmizi 	= atoi(TokenVector[3].c_str());
		UINT mavi 		= atoi(TokenVector[4].c_str());
		//elleme
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "oyuncu_black", Py_BuildValue("(iiii)", black, sari, kirmizi, mavi));
	}