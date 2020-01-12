// 1) Search: Cube_close(this);
// 2) After make a new line and paste:
	Acce_close(this);

// 1) Search: if (m_pkExchange != NULL)
// 2) After their function paste:
	if (IsAcceOpen() == true)
	{
		Acce_close(this);
	}