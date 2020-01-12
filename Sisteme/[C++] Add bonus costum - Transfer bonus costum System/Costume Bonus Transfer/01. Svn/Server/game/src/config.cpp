// 1) Search: bool	g_BlockCharCreation = false;
// 2) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
int	gAttrTransferLimit = 0;
#endif

// 1) Search: TOKEN("pk_protect_level")
// 2) After their definition make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
		TOKEN("ATTR_TRANSFER_LIMIT")
		{
			str_to_number(gAttrTransferLimit, value_string);
			fprintf(stderr, "ATTR_TRANSFER_LIMIT: %d\n", gAttrTransferLimit);
			continue;
		}
#endif