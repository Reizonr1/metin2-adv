//1.1 Search:
void CGraphicImageInstance::OnRender()
	
//1.2 Replace complete function with:
void CGraphicImageInstance::OnRender()
{
	CGraphicTexture* graphicTexture = m_roImage->GetTexturePointer();

	float fimgWidth = m_roImage->GetWidth() * m_v2Scale.x;
	float fimgHeight = m_roImage->GetHeight() * m_v2Scale.y;

	const RECT& c_rRect = m_roImage->GetRectReference();
	float texReverseWidth = 1.0f / float(graphicTexture->GetWidth());
	float texReverseHeight = 1.0f / float(graphicTexture->GetHeight());
	float su = c_rRect.left * texReverseWidth;
	float sv = c_rRect.top * texReverseHeight;
	float eu = (c_rRect.left + (c_rRect.right - c_rRect.left)) * texReverseWidth;
	float ev = (c_rRect.top + (c_rRect.bottom - c_rRect.top)) * texReverseHeight;


	TPDTVertex vertices[4];
	vertices[0].position.x = m_v2Position.x - 0.5f;
	vertices[0].position.y = m_v2Position.y - 0.5f;
	vertices[0].position.z = 0.0f;
	vertices[0].texCoord = TTextureCoordinate(su, sv);
	vertices[0].diffuse = m_DiffuseColor;

	vertices[1].position.x = m_v2Position.x + fimgWidth - 0.5f;
	vertices[1].position.y = m_v2Position.y - 0.5f;
	vertices[1].position.z = 0.0f;
	vertices[1].texCoord = TTextureCoordinate(eu, sv);
	vertices[1].diffuse = m_DiffuseColor;

	vertices[2].position.x = m_v2Position.x - 0.5f;
	vertices[2].position.y = m_v2Position.y + fimgHeight - 0.5f;
	vertices[2].position.z = 0.0f;
	vertices[2].texCoord = TTextureCoordinate(su, ev);
	vertices[2].diffuse = m_DiffuseColor;

	vertices[3].position.x = m_v2Position.x + fimgWidth - 0.5f;
	vertices[3].position.y = m_v2Position.y + fimgHeight - 0.5f;
	vertices[3].position.z = 0.0f;
	vertices[3].texCoord = TTextureCoordinate(eu, ev);
	vertices[3].diffuse = m_DiffuseColor;

	if (CGraphicBase::SetPDTStream(vertices, 4))
	{
		CGraphicBase::SetDefaultIndexBuffer(CGraphicBase::DEFAULT_IB_FILL_RECT);

		STATEMANAGER.SetTexture(0, graphicTexture->GetD3DTexture());
		STATEMANAGER.SetTexture(1, NULL);
		STATEMANAGER.SetVertexShader(D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1);
		STATEMANAGER.DrawIndexedPrimitive(D3DPT_TRIANGLELIST, 0, 4, 0, 2);
	}
}


//2.1 Search:
void CGraphicImageInstance::SetPosition(float fx, float fy)

//2.2 Add before:
void CGraphicImageInstance::SetScale(float fx, float fy)
{
	m_v2Scale.x = fx;
	m_v2Scale.y = fy;
}


//3.1 Search:
	m_v2Position.x = m_v2Position.y = 0.0f;

//3.2 Add after:
	m_v2Scale.x = m_v2Scale.y = 1.0f;
