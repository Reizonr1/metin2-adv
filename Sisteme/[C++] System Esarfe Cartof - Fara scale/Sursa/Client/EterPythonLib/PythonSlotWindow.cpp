// 1) Search: void CSlotWindow::DeactivateSlot(DWORD dwIndex)
// 2) After their function make a new line and paste:
void CSlotWindow::ActivateAcceSlot(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;
	
	pSlot->bAcceActive = TRUE;
	if (!m_pSlotAcceActiveEffect)
	{
		__CreateAcceSlotEnableEffect();
	}
}

void CSlotWindow::DeactivateAcceSlot(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;
	
	pSlot->bAcceActive = FALSE;
}

// 1) Search: void CSlotWindow::ClearSlot(TSlot * pSlot)
// 2) Delete their function and paste:
void CSlotWindow::ClearSlot(TSlot * pSlot)
{
	pSlot->bActive = FALSE;
	pSlot->bAcceActive = FALSE;
	pSlot->byxPlacedItemSize = 1;
	pSlot->byyPlacedItemSize = 1;
	pSlot->isItem = FALSE;
	pSlot->dwState = 0;
	pSlot->fCoolTime = 0.0f;
	pSlot->fStartCoolTime = 0.0f;
	pSlot->dwCenterSlotNumber = 0xffffffff;
	pSlot->dwItemIndex = 0;
	pSlot->bRenderBaseSlotImage = true;
	
	if (pSlot->pInstance)
	{
		CGraphicImageInstance::Delete(pSlot->pInstance);
		pSlot->pInstance = NULL;
	}
	
	if (pSlot->pCoverButton)
	{
		pSlot->pCoverButton->Hide();
	}
	
	if (pSlot->pSlotButton)
	{
		pSlot->pSlotButton->Hide();
	}
	
	if (pSlot->pSignImage)
	{
 		pSlot->pSignImage->Hide();
	}
	
	if (pSlot->pFinishCoolTimeEffect)
	{
		pSlot->pFinishCoolTimeEffect->Hide();
	}
}

// 1) Search: void CSlotWindow::OnUpdate()
// 2) Delete their function and paste:
void CSlotWindow::OnUpdate()
{
	for (std::deque<DWORD>::iterator itor = m_ReserveDestroyEffectDeque.begin(); itor != m_ReserveDestroyEffectDeque.end(); ++itor)
	{
		DWORD dwSlotIndex = *itor;
		TSlot * pSlot;
		if (!GetSlotPointer(dwSlotIndex, &pSlot))
			continue;
		
		__DestroyFinishCoolTimeEffect(pSlot);
	}
	
	m_ReserveDestroyEffectDeque.clear();
	
	if (m_pSlotActiveEffect)
		m_pSlotActiveEffect->Update();
	
	if (m_pSlotAcceActiveEffect)
		m_pSlotAcceActiveEffect->Update();
}

// 1) Search: void CSlotWindow::OnRender()
// 2) Delete their function and paste:
void CSlotWindow::OnRender()
{
	RenderSlotBaseImage();
	switch (m_dwSlotStyle)
	{
		case SLOT_STYLE_PICK_UP:
			OnRenderPickingSlot();
			break;
		case SLOT_STYLE_SELECT:
			OnRenderSelectedSlot();
			break;
	}
	
	std::for_each(m_pChildList.begin(), m_pChildList.end(), std::void_mem_fun(&CWindow::OnRender));
	TSlotListIterator itor;
#ifdef __RENDER_SLOT_AREA__
	CPythonGraphic::Instance().SetDiffuseColor(0.5f, 0.5f, 0.5f);
	for (itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
	{
		TSlot & rSlot = *itor;
		CPythonGraphic::Instance().RenderBox2d(m_rect.left + rSlot.ixPosition, m_rect.top + rSlot.iyPosition, m_rect.left + rSlot.ixPosition + rSlot.ixCellSize, m_rect.top + rSlot.iyPosition + rSlot.iyCellSize);
	}
	
	CPythonGraphic::Instance().SetDiffuseColor(1.0f, 0.0f, 0.0f, 1.0f);
	CPythonGraphic::Instance().RenderBox2d(m_rect.left, m_rect.top, m_rect.right, m_rect.bottom);
#endif
	
	for (itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
	{
		TSlot & rSlot = *itor;
		if (rSlot.pSlotButton)
		{
			rSlot.pSlotButton->SetPosition(rSlot.ixPosition + 1, rSlot.iyPosition + 19);
		}
		
		if (rSlot.pSignImage)
		{
			rSlot.pSignImage->SetPosition(rSlot.ixPosition - 7, rSlot.iyPosition + 10);
		}
		
		if (rSlot.pInstance)
		{
			rSlot.pInstance->SetPosition(m_rect.left + rSlot.ixPosition, m_rect.top + rSlot.iyPosition);
			rSlot.pInstance->Render();
		}
		
		if (!rSlot.isItem)
		{
			if (IS_SET(rSlot.dwState, SLOT_STATE_ALWAYS_RENDER_COVER))
			{
				rSlot.pCoverButton->Show();
				rSlot.pCoverButton->SetPosition(rSlot.ixPosition, rSlot.iyPosition);
				rSlot.pCoverButton->RenderButton();
			}
			
			continue;
		}
		
		if (IS_SET(rSlot.dwState, SLOT_STATE_DISABLE))
		{
			CPythonGraphic::Instance().SetDiffuseColor(1.0f, 0.0f, 0.0f, 0.3f);
			CPythonGraphic::Instance().RenderBar2d(m_rect.left + rSlot.ixPosition, m_rect.top + rSlot.iyPosition, m_rect.left + rSlot.ixPosition + rSlot.ixCellSize, m_rect.top + rSlot.iyPosition + rSlot.iyCellSize);
		}
		
		if (rSlot.fCoolTime != 0.0f)
		{
			float fcurTime = CTimer::Instance().GetCurrentSecond();
			float fPercentage = (fcurTime - rSlot.fStartCoolTime) / rSlot.fCoolTime;
			CPythonGraphic::Instance().RenderCoolTimeBox(m_rect.left + rSlot.ixPosition + 16.0f, m_rect.top + rSlot.iyPosition + 16.0f, 16.0f, fPercentage);
			if (fcurTime - rSlot.fStartCoolTime >= rSlot.fCoolTime)
			{
				if ((fcurTime - rSlot.fStartCoolTime) - rSlot.fCoolTime < 1.0f)
					__CreateFinishCoolTimeEffect(&rSlot);
				
				rSlot.fCoolTime = 0.0f;
				rSlot.fStartCoolTime = 0.0f;
			}
		}
		
		if (rSlot.pCoverButton)
		{
			rSlot.pCoverButton->SetPosition(rSlot.ixPosition, rSlot.iyPosition);
			rSlot.pCoverButton->RenderButton();
		}
		
		if (rSlot.pNumberLine)
		{
			int ix = rSlot.byxPlacedItemSize*ITEM_WIDTH + rSlot.ixPosition - 4;
			int iy = rSlot.iyPosition + rSlot.byyPlacedItemSize*ITEM_HEIGHT - 12 + 2;
			rSlot.pNumberLine->SetPosition(ix, iy);
			rSlot.pNumberLine->Update();
			rSlot.pNumberLine->Render();
		}
		
		if (rSlot.pFinishCoolTimeEffect)
		{
			rSlot.pFinishCoolTimeEffect->SetPosition(rSlot.ixPosition, rSlot.iyPosition);
			rSlot.pFinishCoolTimeEffect->Update();
			rSlot.pFinishCoolTimeEffect->Render();
		}
		
		if (rSlot.bActive)
		{
			int ix = m_rect.left + rSlot.ixPosition;
			int iy = m_rect.top + rSlot.iyPosition;
			if (m_pSlotActiveEffect)
			{
				m_pSlotActiveEffect->SetPosition(ix, iy);
				m_pSlotActiveEffect->Render();
			}
		}
		
		if (rSlot.bAcceActive)
		{
			int ix = m_rect.left + rSlot.ixPosition;
			int iy = m_rect.top + rSlot.iyPosition;
			if (m_pSlotAcceActiveEffect)
			{
				m_pSlotAcceActiveEffect->SetPosition(ix, iy);
				m_pSlotAcceActiveEffect->Render();
			}
		}
	}
	
	RenderLockedSlot();
}

// 1) Search: void CSlotWindow::__DestroySlotEnableEffect()
// 2) After their function make a new line and paste:
void CSlotWindow::__CreateAcceSlotEnableEffect()
{
	__DestroySlotAcceEnableEffect();
	
	m_pSlotAcceActiveEffect = new CAniImageBox(NULL);
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/00.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/01.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/02.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/03.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/04.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/05.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/06.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/07.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/08.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/09.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/10.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/11.sub");
	m_pSlotAcceActiveEffect->AppendImage("d:/ymir work/ui/slotactiveeffect/acceslot/12.sub");
	m_pSlotAcceActiveEffect->SetRenderingMode(CGraphicExpandedImageInstance::RENDERING_MODE_SCREEN);
	m_pSlotAcceActiveEffect->Show();
}

void CSlotWindow::__DestroySlotAcceEnableEffect()
{
	if (m_pSlotAcceActiveEffect)
	{
		delete m_pSlotAcceActiveEffect;
		m_pSlotAcceActiveEffect = NULL;
	}
}

// 1) Search: void CSlotWindow::__Initialize()
// 2) Delete their function and paste:
void CSlotWindow::__Initialize()
{
	m_dwSlotType = 0;
	m_dwSlotStyle = SLOT_STYLE_PICK_UP;
	m_dwToolTipSlotNumber = SLOT_NUMBER_NONE;
	
	m_isUseMode = FALSE;
	m_isUsableItem = FALSE;
	
	m_pToggleSlotImage = NULL;
	m_pSlotActiveEffect = NULL;
	m_pSlotAcceActiveEffect = NULL;
	m_pBaseImageInstance = NULL;
}

// 1) Search: void CSlotWindow::Destroy()
// 2) Delete their function and paste:
void CSlotWindow::Destroy()
{
	for (TSlotListIterator itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
	{
		TSlot & rSlot = *itor;
		
		ClearSlot(&rSlot);
		if (rSlot.pNumberLine)
		{
			delete rSlot.pNumberLine;
			rSlot.pNumberLine = NULL;
		}
		
		if (rSlot.pCoverButton)
		{
			CWindowManager::Instance().DestroyWindow(rSlot.pCoverButton);
		}
		
		if (rSlot.pSlotButton)
		{
			CWindowManager::Instance().DestroyWindow(rSlot.pSlotButton);
		}
		
		if (rSlot.pSignImage)
		{
			CWindowManager::Instance().DestroyWindow(rSlot.pSignImage);
		}
		
		if (rSlot.pFinishCoolTimeEffect)
		{
			CWindowManager::Instance().DestroyWindow(rSlot.pFinishCoolTimeEffect);
		}
	}
	
	m_SlotList.clear();
	
	__DestroyToggleSlotImage();
	__DestroySlotEnableEffect();
	__DestroySlotAcceEnableEffect();
	__DestroyBaseImage();
	__Initialize();
}