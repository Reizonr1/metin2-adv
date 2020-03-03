//1.1 Search:
			float fAspect=m_kWndMgr.GetAspect();

//1.2 add before:
			m_kRenderTargetManager.RenderBackgrounds();
		

//2.1 Search:
		m_kEftMgr.Update();

//2.2 Add After:
		m_kRenderTargetManager.DeformModels();


//3.1 Search:
		m_kChrMgr.Render();

//3.2 Add after:
		m_kRenderTargetManager.RenderModels();


//4.1 Search:
	DWORD t3=ELTimer_GetMSec();
	TPixelPosition kPPosMainActor;

//4.2 Add BEFORE:
	m_kRenderTargetManager.UpdateModels();


//5.1 Search:
				rkBG.ReleaseCharacterShadowTexture();

//5.2 add after:
				CRenderTargetManager::Instance().ReleaseRenderTargetTextures();


//6.1 Search:
				if (m_pyGraphic.RestoreDevice())					
					rkBG.CreateCharacterShadowTexture();
				else
					canRender = false;				
//6.2 replace with:
				if (m_pyGraphic.RestoreDevice())					
				{
					CRenderTargetManager::Instance().CreateRenderTargetTextures();
					rkBG.CreateCharacterShadowTexture();
				}
				else
					canRender = false;				

//7.1 Search:
	CPythonSystem::Instance().SaveConfig();
	
//7.2 Add after:
	m_kRenderTargetManager.Destroy();
