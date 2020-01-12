// Search for:
void CSlotWindow::SetSlotCoolTime(DWORD dwIndex, float fCoolTime, float fElapsedTime)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->fCoolTime = fCoolTime;
	pSlot->fStartCoolTime = CTimer::Instance().GetCurrentSecond() - fElapsedTime;
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CSlotWindow::EnableSlotCoverImage(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->bSlotCoverImage = TRUE;

	if (!m_pSlotCoverImage)
	{
		__CreateSlotCoverImage();
	}
}

void CSlotWindow::DisableSlotCoverImage(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->bSlotCoverImage = FALSE;
}
#endif

// Search for:
void CSlotWindow::DeactivateSlot(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->bActive = FALSE;
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CSlotWindow::ActivateChangeLookSlot(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->bChangeLookActive = TRUE;

	if (!m_pSlotChangeLookActiveEffect[0] || !m_pSlotChangeLookActiveEffect[1] || !m_pSlotChangeLookActiveEffect[2])
	{
		__CreateSlotChangeLookEnableEffect();
	}
}

void CSlotWindow::DeactivateChangeLookSlot(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	pSlot->bChangeLookActive = FALSE;
}
#endif

// Search for:
	pSlot->bActive = FALSE;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	pSlot->bChangeLookActive = FALSE;
	pSlot->bSlotCoverImage = FALSE;
#endif

// Search for:
	if (m_pSlotActiveEffect)
		m_pSlotActiveEffect->Update();

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	for (int i = 0; i < 3; ++i)
	{
		if (m_pSlotChangeLookActiveEffect[i])
			m_pSlotChangeLookActiveEffect[i]->Update();
	}

	if (m_pSlotCoverImage)
		m_pSlotCoverImage->Update();
#endif

// Search for:
		if (rSlot.bActive)
		{
			if (m_pSlotActiveEffect)
			{
				m_pSlotActiveEffect->SetPosition(ix, iy);
				m_pSlotActiveEffect->Render();
			}
		}

// Add Under:

#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		if (rSlot.bChangeLookActive)
		{
			int ix = m_rect.left + rSlot.ixPosition;
			int iy = m_rect.top + rSlot.iyPosition;
			int size = rSlot.byyPlacedItemSize;

			if (size == 1)
			{
				m_pSlotChangeLookActiveEffect[0]->Show();
				m_pSlotChangeLookActiveEffect[0]->SetPosition(ix, iy);
				m_pSlotChangeLookActiveEffect[0]->Render();
			}

			if (size == 2)
			{
				m_pSlotChangeLookActiveEffect[1]->Show();
				m_pSlotChangeLookActiveEffect[1]->SetPosition(ix, iy);
				m_pSlotChangeLookActiveEffect[1]->Render();
			}

			if (size == 3)
			{
				m_pSlotChangeLookActiveEffect[2]->Show();
				m_pSlotChangeLookActiveEffect[2]->SetPosition(ix, iy);
				m_pSlotChangeLookActiveEffect[2]->Render();
			}
		}

		if (rSlot.bSlotCoverImage)
		{
			if (m_pSlotCoverImage)
			{
				int ix = m_rect.left + rSlot.ixPosition;
				int iy = m_rect.top + rSlot.iyPosition;

				m_pSlotCoverImage->SetPosition(ix, iy);
				m_pSlotCoverImage->Render();
			}
		}
#endif

// Search for:
void CSlotWindow::__CreateToggleSlotImage()
{
	__DestroyToggleSlotImage();

	m_pToggleSlotImage = new CImageBox(NULL);
	m_pToggleSlotImage->LoadImage("d:/ymir work/ui/public/slot_toggle.sub");
	m_pToggleSlotImage->Show();
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CSlotWindow::__CreateSlotCoverImage()
{
	__DestroySlotCoverImage();

	m_pSlotCoverImage = new CAniImageBox(NULL);
	m_pSlotCoverImage->AppendImage("icon/item/ingame_convert_mark.tga");
	m_pSlotCoverImage->Show();
}

void CSlotWindow::__DestroySlotCoverImage()
{
	if (m_pSlotCoverImage)
	{
		delete m_pSlotCoverImage;
		m_pSlotCoverImage = NULL;
	}
}
#endif

// Search for:
void CSlotWindow::__DestroySlotEnableEffect()
{
	if (m_pSlotActiveEffect)
	{
		delete m_pSlotActiveEffect;
		m_pSlotActiveEffect = NULL;
	}
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CSlotWindow::__CreateSlotChangeLookEnableEffect()
{
	__DestroySlotChangeLookEnableEffect();

	for (int i = 0; i < 3; ++i)
	{
		CAniImageBox* pEff = new CAniImageBox(NULL);
		for (int j = 0; j <= 12; ++j)
		{
			char buf[64 + 1];
			sprintf_s(buf, "d:/ymir work/ui/public/slotactiveeffect/slot%d/%02d.sub", (i + 1), j);
			pEff->SetSlotDiffuseColor(buf);
		}

		pEff->SetRenderingMode(CGraphicExpandedImageInstance::RENDERING_MODE_SCREEN);
		m_pSlotChangeLookActiveEffect[i] = pEff;
	}
}

void CSlotWindow::__DestroySlotChangeLookEnableEffect()
{
	for (int i = 0; i < 3; ++i)
	{
		if (m_pSlotChangeLookActiveEffect[i])
		{
			delete m_pSlotChangeLookActiveEffect[i];
			m_pSlotChangeLookActiveEffect[i] = NULL;
		}
	}
}
#endif

// Search for:
// void CSlotWindow::__Initialize()
	m_pSlotActiveEffect = NULL;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	for (int i = 0; i < 3; ++i)
	{
		m_pSlotChangeLookActiveEffect[i] = NULL;
	}

	m_pSlotCoverImage = NULL;
#endif

// Search for:
	__DestroySlotEnableEffect();

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	__DestroySlotChangeLookEnableEffect();
	__DestroySlotCoverImage();
#endif
