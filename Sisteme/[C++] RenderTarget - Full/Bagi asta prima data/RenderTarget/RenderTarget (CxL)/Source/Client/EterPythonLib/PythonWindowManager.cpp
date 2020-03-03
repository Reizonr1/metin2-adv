//1.1 Search:
	CWindow * CWindowManager::RegisterBar(PyObject * po, const char * c_szLayer)

//1.2 Add ABOVE:
	CWindow * CWindowManager::RegisterRenderTarget(PyObject * po, const char * c_szLayer)
	{
		assert(m_LayerWindowMap.end() != m_LayerWindowMap.find(c_szLayer));

		CWindow * pWin = new CUiRenderTarget(po);
		m_LayerWindowMap[c_szLayer]->AddChild(pWin);

#ifdef __WINDOW_LEAK_CHECK__
		gs_kSet_pkWnd.insert(pWin);
#endif
		return pWin;
	}
