// 1. Caută:

void CInstanceBase::__Assassin_SetEunhyeongAffect(bool isVisible)

// 1. Schimbă funcția în:

void CInstanceBase::__Assassin_SetEunhyeongAffect(bool isVisible)
{
	if (isVisible)
	{
		if (IsWearingDress())
			return;

		if (__IsMainInstance() || __MainCanSeeHiddenThing())
		{
			m_GraphicThingInstance.BlendAlphaValue(0.5f, 1.0f);
		}
		else
		{
			m_GraphicThingInstance.BlendAlphaValue(0.0f, 1.0f);
			m_GraphicThingInstance.HideAllAttachingEffect();
		}
	}
	else
	{
#ifdef ENABLE_CANSEEHIDDENTHING_FOR_GM
		if (IsAffect(AFFECT_INVISIBILITY) && __MainCanSeeHiddenThing())
			return;
#endif
		m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);	
		m_GraphicThingInstance.ShowAllAttachingEffect();
	}
}

// 2. Caută

case AFFECT_YMIR: // în funcția: void CInstanceBase::__SetAffect(UINT eAffect, bool isVisible)

// 2. Schimbă tot case-ul în:

		case AFFECT_YMIR:
#ifdef ENABLE_CANSEEHIDDENTHING_FOR_GM
			if (IsAffect(AFFECT_INVISIBILITY) && !__MainCanSeeHiddenThing())
				return;
#else
			if (IsAffect(AFFECT_INVISIBILITY))
				return;
#endif

// 3. Caută

case AFFECT_INVISIBILITY: // în funcția: void CInstanceBase::__SetAffect(UINT eAffect, bool isVisible)

// 3. Schimbă tot case-ul în:

		case AFFECT_INVISIBILITY:
#ifdef ENABLE_CANSEEHIDDENTHING_FOR_GM
			if (__MainCanSeeHiddenThing())
			{
				if (isVisible)
					m_GraphicThingInstance.BlendAlphaValue(0.5f, 1.0f);
				else
					m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
				break;
			}
#endif
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
			
// 4. Caută 

	if (IsAffect(AFFECT_INVISIBILITY)) // în functia : DWORD CInstanceBase::__AttachEffect(UINT eEftType)
		return 0;
	
// 4. Schimbă în:

#ifdef ENABLE_CANSEEHIDDENTHING_FOR_GM
	if (IsAffect(AFFECT_INVISIBILITY) && !__MainCanSeeHiddenThing())
		return 0;
#else
	if (IsAffect(AFFECT_INVISIBILITY))
		return 0;
#endif