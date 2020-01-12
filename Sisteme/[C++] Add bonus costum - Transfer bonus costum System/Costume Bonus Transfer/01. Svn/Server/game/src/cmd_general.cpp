// 1) Search: ACMD(do_inventory)
// 2) After their function make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
ACMD(do_attr_transfer)
{
	if (!ch->CanDoAttrTransfer())
		return;
	
	sys_log(1, "%s has used an Attr Transfer command: %s.", ch->GetName(), argument);
	
	int w_index = 0, i_index = 0;
	const char *line;
	char arg1[256], arg2[256], arg3[256];
	line = two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));
	one_argument(line, arg3, sizeof(arg3));
	if (0 == arg1[0])
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Usage:");
		ch->ChatPacket(CHAT_TYPE_INFO, "- attrtransfer open");
		ch->ChatPacket(CHAT_TYPE_INFO, "- attrtransfer close");
		ch->ChatPacket(CHAT_TYPE_INFO, "- attrtransfer add <attr_transfer_slot> <inventory_slot>");
		ch->ChatPacket(CHAT_TYPE_INFO, "- attrtransfer delete <attr_transfer_slot>");
		return;
	}
	
	const std::string& strArg1 = std::string(arg1);
	if (strArg1 == "open")
	{
		AttrTransfer_open(ch);
		return;
	}
	else if (strArg1 == "close")
	{
		AttrTransfer_close(ch);
		return;
	}
	else if (strArg1 == "make")
	{
		AttrTransfer_make(ch);
		return;
	}
	else if (strArg1 == "add")
	{
		if (0 == arg2[0] || !isdigit(*arg2) || 0 == arg3[0] || !isdigit(*arg3))
			return;
		
		str_to_number(w_index, arg2);
		str_to_number(i_index, arg3);
		AttrTransfer_add_item(ch, w_index, i_index);
		return;
	}
	else if (strArg1 == "delete")
	{
		if (0 == arg2[0] || !isdigit(*arg2))
			return;
		
		str_to_number(w_index, arg2);
		AttrTransfer_delete_item(ch, w_index);
		return;
	}
	
	switch (LOWER(arg1[0]))
	{
		case 'o':
			AttrTransfer_open(ch);
			break;
		case 'c':
			AttrTransfer_close(ch);
			break;
		case 'm':
			AttrTransfer_make(ch);
			break;
		case 'a':
			{
				if (0 == arg2[0] || !isdigit(*arg2) || 0 == arg3[0] || !isdigit(*arg3))
					return;
				
				str_to_number(w_index, arg2);
				str_to_number(i_index, arg3);
				AttrTransfer_add_item(ch, w_index, i_index);
			}
			break;
		case 'd':
			{
				if (0 == arg2[0] || !isdigit(*arg2))
					return;
				
				str_to_number(w_index, arg2);
				AttrTransfer_delete_item(ch, w_index);
			}
			break;
		default:
			return;
	}
}
#endif