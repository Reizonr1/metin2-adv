// 1) Search: Cube_close(this);
// 2) After make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	AttrTransfer_close(this);
#endif

// 1) Search: if (m_pkExchange != NULL)
// 2) After their function paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	if (IsAttrTransferOpen() == true)
	{
		AttrTransfer_close(this);
	}
#endif