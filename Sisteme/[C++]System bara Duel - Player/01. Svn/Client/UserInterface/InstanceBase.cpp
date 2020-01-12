// 1) Search: if (rkInstVictim.IsEnemy())
// 2) Be sure is member of: bool CInstanceBase::CanViewTargetHP(CInstanceBase& rkInstVictim)
// 2) After this make a new line and paste:
#ifdef ENABLE_VIEW_TARGET_PLAYER_HP
	if (rkInstVictim.IsPC())
		return true;
#endif