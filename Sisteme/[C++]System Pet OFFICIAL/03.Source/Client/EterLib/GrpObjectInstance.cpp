//Search in this file:

	m_v3Position.x = m_v3Position.y = m_v3Position.z = 0.0f;
	m_v3Scale.x = m_v3Scale.y = m_v3Scale.z = 0.0f;
	//m_fRotation = 0.0f;
	m_fYaw = m_fPitch = m_fRoll = 0.0f;
	D3DXMatrixIdentity(&m_worldMatrix);

//Add after:
	m_vecScalePos.x = m_vecScalePos.y = m_vecScalePos.z = 0.0f;
	m_vecScaleNew.x = m_vecScaleNew.y = m_vecScaleNew.z = 0.0f;

	D3DXMatrixIdentity(&m_matAbsoluteTrans);
	D3DXMatrixIdentity(&m_matScale);
	D3DXMatrixIdentity(&m_matPositon);

//Search this funtion:
void CGraphicObjectInstance::Transform()

//Replace their function with this:

void CGraphicObjectInstance::Transform()
{
	D3DXMATRIX temp;
	D3DXMatrixMultiply(&temp, &m_matPositon, &m_mRotation);

	m_worldMatrix = temp;

	m_worldMatrix._41 += m_v3Position.x;
	m_worldMatrix._42 += m_v3Position.y;
	m_worldMatrix._43 += m_v3Position.z;

	D3DXMatrixMultiply(&temp, &m_matPositon, &m_matScale);

	D3DXMATRIX temp2;
	D3DXMatrixMultiply(&temp2, &temp, &m_mRotation);

	m_matAbsoluteTrans = temp2;
	m_matAbsoluteTrans._41 = m_vecScalePos.x + m_v3Position.x + m_matAbsoluteTrans._41;
	m_matAbsoluteTrans._42 = m_vecScalePos.y + m_v3Position.y + m_matAbsoluteTrans._42;
	m_matAbsoluteTrans._43 = m_vecScalePos.z + m_v3Position.z + m_matAbsoluteTrans._43;

}

//Search in this file:
void CGraphicObjectInstance::SetScale(float x, float y, float z)
{
	m_v3Scale.x = x;
	m_v3Scale.y = y;
	m_v3Scale.z = z;
}

//Add after:
void CGraphicObjectInstance::SetScaleNew(float x, float y, float z)
{
	m_vecScaleNew.x = x;
	m_vecScaleNew.y = y;
	m_vecScaleNew.z = z;
	D3DXMatrixScaling(&m_matScale, x, y, z);
}

void CGraphicObjectInstance::SetScaleNew(const D3DXVECTOR3 & newscale)
{
	m_vecScaleNew = newscale;
	D3DXMatrixScaling(&m_matScale, m_vecScaleNew.x, m_vecScaleNew.y, m_vecScaleNew.z);
}

void CGraphicObjectInstance::SetScalePosition(float x, float y, float z)
{
	m_vecScalePos.x = x;
	m_vecScalePos.y = y;
	m_vecScalePos.z = z;
}

void CGraphicObjectInstance::SetScalePosition(const D3DXVECTOR3 & newposition)
{
	m_vecScalePos = newposition;
}

//Search in this file:
	m_v3Position.x = m_v3Position.y = m_v3Position.z = 0.0f;
	m_v3Scale.x = m_v3Scale.y = m_v3Scale.z = 0.0f;
	m_fYaw = m_fPitch = m_fRoll = 0.0f;

	D3DXMatrixIdentity(&m_worldMatrix);
	D3DXMatrixIdentity(&m_mRotation);

//Add after:

	m_vecScalePos.x = m_vecScalePos.y = m_vecScalePos.z = 0.0f;
	m_vecScaleNew.x = m_vecScaleNew.y = m_vecScaleNew.z = 0.0f;

	D3DXMatrixIdentity(&m_matAbsoluteTrans);
	D3DXMatrixIdentity(&m_matScale);
	D3DXMatrixIdentity(&m_matPositon);
