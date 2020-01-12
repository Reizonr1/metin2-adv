Search:
void CInstanceBase::CreateSpecialEffect(DWORD iEffectIndex)
{
	const D3DXMATRIX & c_rmatGlobal = m_GraphicThingInstance.GetTransform();

	DWORD dwEffectIndex = CEffectManager::Instance().GetEmptyIndex();
	DWORD dwEffectCRC = ms_adwCRCAffectEffect[iEffectIndex];
	CEffectManager::Instance().CreateEffectInstance(dwEffectIndex, dwEffectCRC);
	CEffectManager::Instance().SelectEffectInstance(dwEffectIndex);
	CEffectManager::Instance().SetEffectInstanceGlobalMatrix(c_rmatGlobal);
}

Add it under:
void CInstanceBase::__EffectContainer_Continue()
{
	SEffectContainer::Dict& rkDctEftID = __EffectContainer_GetDict();

	SEffectContainer::Dict::iterator i;
	for (i = rkDctEftID.begin(); i != rkDctEftID.end(); ++i)
		__AttachEffect(i->second);
}

void CInstanceBase::__EffectContainer_Suspend()
{
	SEffectContainer::Dict& rkDctEftID = __EffectContainer_GetDict();

	SEffectContainer::Dict::iterator i;
	for (i = rkDctEftID.begin(); i != rkDctEftID.end(); ++i)
		__DetachEffect(i->second);
}

https://puu.sh/sgKm7/fdb45b1faa.png

---

Search:
UINT CInstanceBase::GetNameColorIndex()
{

Add it under:
#ifdef __OFFLINE_SHOP__
	if (GetRace() >= 30005 && GetRace() <= 30010)
		return NAMECOLOR_OFFSHOP;
#endif

https://puu.sh/sgKnl/8ac85e24b5.png

---

Search:
		case AFFECT_INVISIBILITY:
			// 2004.07.17.levites.isShow¸¦ ViewFrustumCheck·Î º¯°æ
			if (isVisible)
			{
				m_GraphicThingInstance.ClearAttachingEffect();
				__EffectContainer_Destroy();
				DetachTextTail();
			}
			else
			{
				m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
				AttachTextTail();
				RefreshTextTail();
			}
			return;
			break;

Change:
		case AFFECT_INVISIBILITY:
			// 2004.07.17.levites.isShow¸¦ ViewFrustumCheck·Î º¯°æ
			if (isVisible)
			{
				m_GraphicThingInstance.SetDeactiveAllAttachingEffect();
				__EffectContainer_Suspend();
				DetachTextTail();
			}
			else
			{
				m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
				m_GraphicThingInstance.SetActiveAllAttachingEffect();
				//__EffectContainer_Continue();
				AttachTextTail();
				RefreshTextTail();
			}
			return;
			break;

https://puu.sh/sgKpA/7ad85650a8.png
			
