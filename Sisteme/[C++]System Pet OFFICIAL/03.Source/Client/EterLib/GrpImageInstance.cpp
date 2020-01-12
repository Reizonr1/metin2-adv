//Search in this file:
	float fimgWidth = pImage->GetWidth();
	float fimgHeight = pImage->GetHeight();

//Replace with:

	float fimgWidth = pImage->GetWidth()*m_vScale;
	float fimgHeight = pImage->GetHeight()*m_vScale;

//Search in this file:

void CGraphicImageInstance::SetPosition(float fx, float fy)
{
	m_v2Position.x = fx;
	m_v2Position.y = fy;
}

//Add after:

void CGraphicImageInstance::SetScale(float fx, float fy) {
	m_vScale = fx;
}

//Search this funtion:
void CGraphicImageInstance::Initialize()
{
	m_DiffuseColor.r = m_DiffuseColor.g = m_DiffuseColor.b = m_DiffuseColor.a = 1.0f;
	m_v2Position.x = m_v2Position.y = 0.0f;
}

//Replace with:
void CGraphicImageInstance::Initialize()
{
	m_DiffuseColor.r = m_DiffuseColor.g = m_DiffuseColor.b = m_DiffuseColor.a = 1.0f;
	m_v2Position.x = m_v2Position.y = 0.0f;
	m_vScale = 1.0f;
}
