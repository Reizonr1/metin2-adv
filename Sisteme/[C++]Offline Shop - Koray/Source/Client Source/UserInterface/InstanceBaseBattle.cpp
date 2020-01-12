Search:
void CInstanceBase::Hide()
{
	m_GraphicThingInstance.SetAlphaValue(0.0f);
	m_GraphicThingInstance.BlendAlphaValue(0.0f, 0.1f);
}

void CInstanceBase::Show()
{
	m_GraphicThingInstance.SetAlphaValue(1.0f);
	m_GraphicThingInstance.BlendAlphaValue(1.0f, 0.1f);
}

Change:
void CInstanceBase::Hide()
{
	m_bIsHidden = true;
	m_GraphicThingInstance.SetAlphaValue(0.0f);
	m_GraphicThingInstance.BlendAlphaValue(0.0f, 0.1f);
}

void CInstanceBase::Show()
{
	m_bIsHidden = false;
	m_GraphicThingInstance.SetAlphaValue(1.0f);
	m_GraphicThingInstance.BlendAlphaValue(1.0f, 0.1f);
}

bool CInstanceBase::IsHidden()
{
	return m_bIsHidden;
}

https://puu.sh/sgKkc/12a37e5e2c.png