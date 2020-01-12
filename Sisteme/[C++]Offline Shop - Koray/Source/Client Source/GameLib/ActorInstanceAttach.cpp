Search:
void CActorInstance::ShowAllAttachingEffect()
{
	std::list<TAttachingEffect>::iterator it;
	for(it = m_AttachingEffectList.begin(); it!= m_AttachingEffectList.end();++it)
	{
		CEffectManager::Instance().SelectEffectInstance(it->dwEffectIndex);
		CEffectManager::Instance().ShowEffect();
	}
}

Add it upper:
void CActorInstance::SetActiveAllAttachingEffect()
{
	std::list<TAttachingEffect>::iterator it;
	for (it = m_AttachingEffectList.begin(); it != m_AttachingEffectList.end(); ++it)
	{
		CEffectManager::Instance().ActiveEffectInstance(it->dwEffectIndex);
	}
}

void CActorInstance::SetDeactiveAllAttachingEffect()
{
	std::list<TAttachingEffect>::iterator it;
	for (it = m_AttachingEffectList.begin(); it != m_AttachingEffectList.end(); ++it)
	{
		CEffectManager::Instance().DeactiveEffectInstance(it->dwEffectIndex);
	}
}

https://puu.sh/sgK2T/8257998561.png