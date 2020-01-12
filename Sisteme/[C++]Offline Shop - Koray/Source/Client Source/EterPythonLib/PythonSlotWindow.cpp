Search:
void CSlotWindow::SetCoverButton(DWORD dwIndex, const char * c_szUpImageName, const char * c_szOverImageName, const char * c_szDownImageName, const char * c_szDisableImageName, BOOL bLeftButtonEnable, BOOL bRightButtonEnable)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	CCoverButton *& rpCoverButton = pSlot->pCoverButton;

	if (!rpCoverButton)
	{
		rpCoverButton = new CCoverButton(CSlotButton::SLOT_BUTTON_TYPE_COVER, pSlot->dwSlotNumber, this);
		CWindowManager::Instance().SetParent(rpCoverButton, this);
	}

	rpCoverButton->SetLeftButtonEnable(bLeftButtonEnable);
	rpCoverButton->SetRightButtonEnable(bRightButtonEnable);
	rpCoverButton->SetUpVisual(c_szUpImageName);
	rpCoverButton->SetOverVisual(c_szOverImageName);
	rpCoverButton->SetDownVisual(c_szDownImageName);
	rpCoverButton->SetDisableVisual(c_szDisableImageName);
	rpCoverButton->Enable();
	rpCoverButton->Show();

	// NOTE : Cover ¹öÆ°ÀÌ Plus ¹öÆ°À» °¡·Á¹ö·Á¼­ ÀÓ½Ã ÄÚµå¸¦..
	if (pSlot->pSlotButton)
	{
		SetTop(pSlot->pSlotButton);
	}
}


Add it under:
void CSlotWindow::DeleteCoverButton(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	CCoverButton *& rpCoverButton = pSlot->pCoverButton;
	if (!rpCoverButton)
		return;

	rpCoverButton->Hide();
	rpCoverButton->Disable();
	rpCoverButton->DestroyHandle();
}

bool CSlotWindow::HasCoverButton(DWORD dwIndex)
{
	TSlot * pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return false;

	CCoverButton *& rpCoverButton = pSlot->pCoverButton;
	return rpCoverButton ? true : false;
}

https://puu.sh/sgJYz/487c6d96ea.png