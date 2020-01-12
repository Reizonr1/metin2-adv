// 1) Search: m_dwHair = src.m_dwHair;
// 2) After make a new line and paste:
	m_dwAcce = src.m_dwAcce;

// 1) Search: m_dwHair=0;
// 2) After make a new line and paste:
	m_dwAcce=0;

// 1) Search: kCreateData.m_dwHair=rkNetActorData.m_dwHair;
// 2) After make a new line and paste:
	kCreateData.m_dwAcce=rkNetActorData.m_dwAcce;

// 1) Search: pkInstFind->ChangeHair(c_rkNetUpdateActorData.m_dwHair);
// 2) After make a new line and paste:
		pkInstFind->ChangeAcce(c_rkNetUpdateActorData.m_dwAcce);

// 1) Search: rkNetActorData.m_dwHair=c_rkNetUpdateActorData.m_dwHair;
// 2) After make a new line and paste:
	rkNetActorData.m_dwAcce=c_rkNetUpdateActorData.m_dwAcce;