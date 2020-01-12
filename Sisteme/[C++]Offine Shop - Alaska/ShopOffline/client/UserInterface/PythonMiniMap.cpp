//Find function:
void CPythonMiniMap::Update(float fCenterX, float fCenterY)

//Find this line:
 else if (pkInstEach->IsNPC())
//And replace with:

#ifdef ENABLE_OFFLINE_SHOP
		else if (pkInstEach->GetRace()==30000)
		{
			aMarkPosition.m_fX = ( m_fWidth - (float)m_WhiteMark.GetWidth() ) / 2.0f + fDistanceFromCenterX + m_fScreenX;
			aMarkPosition.m_fY = ( m_fHeight - (float)m_WhiteMark.GetHeight() ) / 2.0f + fDistanceFromCenterY + m_fScreenY;
			aMarkPosition.m_eNameColor = pkInstEach->GetNameColorIndex();
			m_NPCPositionVector.push_back(aMarkPosition);		
		}
#endif
		else if (pkInstEach->IsNPC())
		