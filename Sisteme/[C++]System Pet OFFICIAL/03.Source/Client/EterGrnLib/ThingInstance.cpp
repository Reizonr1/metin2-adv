//Search this function
void CGraphicThingInstance::DeformNoSkin()

//Replace their function with:
void CGraphicThingInstance::DeformNoSkin()
{
	m_bUpdated = true;

	for (std::vector<CGrannyLODController*>::size_type i = 0; i != m_LODControllerVector.size(); i++)
	{
		CGrannyLODController* pkLOD = m_LODControllerVector[i];
		if (pkLOD->isModelInstance())
			pkLOD->DeformNoSkin(&m_matAbsoluteTrans);
	}
}

//Search this funtion:

void CGraphicThingInstance::OnDeform()

//Replac their function with:

void CGraphicThingInstance::OnDeform()
{
	m_bUpdated = true;

	for (std::vector<CGrannyLODController*>::size_type i = 0; i != m_LODControllerVector.size(); i++)
	{
		CGrannyLODController* pkLOD = m_LODControllerVector[i];
		if (pkLOD->isModelInstance())
			pkLOD->Deform(&m_matAbsoluteTrans);
	}
}
