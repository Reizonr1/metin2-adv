// 1) Search:
	Slot.pFinishCoolTimeEffect = NULL;
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	for (int i = 0; i < 3; ++i)
	{
		Slot.pActiveSlotEffect[i] = NULL;
	}
#endif


// 1) Search:
	if (pSlot->pFinishCoolTimeEffect)
	{
		pSlot->pFinishCoolTimeEffect->Hide();
	}
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	for (int i = 0; i < 3; ++i)
	{
		if (pSlot->pActiveSlotEffect[i])
			pSlot->pActiveSlotEffect[i]->Hide();
	}
#endif


// 1) Search:
	for (std::deque<DWORD>::iterator itor = m_ReserveDestroyEffectDeque.begin(); itor != m_ReserveDestroyEffectDeque.end(); ++itor)
	{
		DWORD dwSlotIndex = *itor;
		TSlot * pSlot;
		if (!GetSlotPointer(dwSlotIndex, &pSlot))
			continue;
		
		__DestroyFinishCoolTimeEffect(pSlot);
	}
// 2) Replace with:
	for (std::deque<DWORD>::iterator itor = m_ReserveDestroyEffectDeque.begin(); itor != m_ReserveDestroyEffectDeque.end(); ++itor)
	{
		DWORD dwSlotIndex = *itor;
		TSlot * pSlot;
		if (!GetSlotPointer(dwSlotIndex, &pSlot))
			continue;
		
		__DestroyFinishCoolTimeEffect(pSlot);
#ifdef ENABLE_CHANGELOOK_SYSTEM
		for (int i = 0; i < 3; ++i)
		{
			if (pSlot->pActiveSlotEffect[i])
			{
				delete pSlot->pActiveSlotEffect[i];
				pSlot->pActiveSlotEffect[i] = NULL;
			}
		}
#endif
	}


// 1) Search:
		if (rSlot.pFinishCoolTimeEffect)
		{
			rSlot.pFinishCoolTimeEffect->SetPosition(rSlot.ixPosition, rSlot.iyPosition);
			rSlot.pFinishCoolTimeEffect->Update();
			rSlot.pFinishCoolTimeEffect->Render();
		}
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{
			int iX = m_rect.left + rSlot.ixPosition, iY = m_rect.top + rSlot.iyPosition, iItemYSize = rSlot.byyPlacedItemSize;
			for (int i = 0; i < 3; ++i)
			{
				if ((rSlot.pActiveSlotEffect[i]) && (iItemYSize == i + 1))
				{
					rSlot.pActiveSlotEffect[i]->Show();
					rSlot.pActiveSlotEffect[i]->SetPosition(iX, iY);
					rSlot.pActiveSlotEffect[i]->Update();
					rSlot.pActiveSlotEffect[i]->Render();
				}
			}
		}
#endif


// 1) Search:
DWORD CSlotWindow::Type()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
void CSlotWindow::ActivateEffect(DWORD dwSlotIndex, float r, float g, float b, float a)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwSlotIndex, &pSlot))
		return;
	
	for (int i = 0; i < 3; ++i)
	{
		if (pSlot->pActiveSlotEffect[i])
		{
			delete pSlot->pActiveSlotEffect[i];
			pSlot->pActiveSlotEffect[i] = NULL;
		}
		
		CAniImageBox * pEff = new CAniImageBox(NULL);
		for (int j = 0; j <= 12; ++j)
		{
			char cBuf[72];
			sprintf_s(cBuf, "d:/ymir work/ui/public/slotactiveeffect/slot%d/%02d.sub", (i + 1), j);
			pEff->AppendImage(cBuf, r, g, b, a);
		}
		
		pEff->SetRenderingMode(CGraphicExpandedImageInstance::RENDERING_MODE_SCREEN);
		pSlot->pActiveSlotEffect[i] = pEff;
	}
}

void CSlotWindow::DeactivateEffect(DWORD dwSlotIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwSlotIndex, &pSlot))
		return;
	
	for (int i = 0; i < 3; ++i)
	{
		if (pSlot->pActiveSlotEffect[i])
		{
			delete pSlot->pActiveSlotEffect[i];
			pSlot->pActiveSlotEffect[i] = NULL;
		}
	}
}
#endif


// 1) Search:
		if (rSlot.pFinishCoolTimeEffect)
		{
			CWindowManager::Instance().DestroyWindow(rSlot.pFinishCoolTimeEffect);
		}
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		for (int i = 0; i < 3; ++i)
		{
			if (rSlot.pActiveSlotEffect[i])
				CWindowManager::Instance().DestroyWindow(rSlot.pActiveSlotEffect[i]);
		}
#endif