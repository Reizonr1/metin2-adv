//find function GetNameColorIndex and make changes like this
UINT CInstanceBase::GetNameColorIndex()
{
//before if (IsPC()) add:
#ifdef ENABLE_OFFLINE_SHOP
		if (GetRace() == 30000)
			return NAMECOLOR_SHOP;
#endif


//find function CInstanceBase::SetEmoticon and replace with this:
void CInstanceBase::SetEmoticon(UINT eEmoticon)
{

	if (eEmoticon >= EMOTICON_NUM)
	{
		TraceError("CInstanceBase[VID:%d]::SetEmoticon(eEmoticon:%d<EMOTICON_NUM:%d, isVisible=%d)",
			GetVirtualID(), eEmoticon);
		return;
	}
#ifdef ENABLE_OFFLINE_SHOP
	if (GetRace() == 30000)
		return;
#endif
	if (IsPossibleEmoticon())
	{
		D3DXVECTOR3 v3Pos = m_GraphicThingInstance.GetPosition();
		v3Pos.z += float(m_GraphicThingInstance.GetHeight());

		//CEffectManager& rkEftMgr=CEffectManager::Instance();
		CCamera * pCamera = CCameraManager::Instance().GetCurrentCamera();

		D3DXVECTOR3 v3Dir = (pCamera->GetEye() - v3Pos) * 9 / 10;
		v3Pos = pCamera->GetEye() - v3Dir;

		v3Pos = D3DXVECTOR3(0, 0, 0);
		v3Pos.z += float(m_GraphicThingInstance.GetHeight());

		//rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[EFFECT_EMOTICON+eEmoticon],v3Pos,D3DXVECTOR3(0,0,0));
		m_GraphicThingInstance.AttachEffectByID(0, NULL, ms_adwCRCAffectEffect[EFFECT_EMOTICON + eEmoticon], &v3Pos);
		m_dwEmoticonTime = ELTimer_GetMSec();
	}
}