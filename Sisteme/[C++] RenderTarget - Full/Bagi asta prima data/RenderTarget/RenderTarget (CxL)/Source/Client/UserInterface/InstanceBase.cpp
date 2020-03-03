//1.1 Search:
bool CInstanceBase::__CanRender()

//1.2 Replace complete method with:
bool CInstanceBase::__CanRender()
{
	if (IsAlwaysRender())
	{
		return true;
	}

	if (!__IsInViewFrustum())
		return false;
	if (IsAffect(AFFECT_INVISIBILITY))
		return false;

	return true;
}


//2.1 Search:
	m_dwEmoticonTime = 0;

//2.1 Add after:
	m_IsAlwaysRender = false;


//3.1 Search:
void CInstanceBase::GetBoundBox(D3DXVECTOR3 * vtMin, D3DXVECTOR3 * vtMax)

//3.2 Add BEFORE:
bool CInstanceBase::IsAlwaysRender()
{
	return m_IsAlwaysRender;
}

void CInstanceBase::SetAlwaysRender(bool val)
{
	m_IsAlwaysRender = val;
}

