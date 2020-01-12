
// arat:
void CItemData::Clear()

// ustune ekle


D3DXVECTOR3 & CItemData::GetItemScalePosition(int dwJob, int dwSex)
{
	return m_ItemScaleTable.scalePos[dwSex][dwJob];
}

D3DXVECTOR3 & CItemData::GetItemScale(int dwJob, int dwSex)
{
	return m_ItemScaleTable.scale[dwSex][dwJob];

}

void CItemData::SetItemTableScaleData(int dwJob, int dwSex, float fScaleX, float fScaleY, float fScaleZ, float fScalePosX, float fScalePosY, float fScalePosZ)
{
	
	m_ItemScaleTable.scale[dwSex][dwJob].x = fScaleX;
	m_ItemScaleTable.scale[dwSex][dwJob].y = fScaleY;
	m_ItemScaleTable.scale[dwSex][dwJob].z = fScaleZ;
	//TraceError("Scale-itemData: %d - %d - %d", fScaleX, fScaleY, fScaleZ);

	m_ItemScaleTable.scalePos[dwSex][dwJob].x = fScalePosX;
	m_ItemScaleTable.scalePos[dwSex][dwJob].y = fScalePosY;
	m_ItemScaleTable.scalePos[dwSex][dwJob].z = fScalePosZ;
	//TraceError("scalePos-itemData: %d - %d - %d", fScalePosX, fScalePosY, fScalePosZ);
}
