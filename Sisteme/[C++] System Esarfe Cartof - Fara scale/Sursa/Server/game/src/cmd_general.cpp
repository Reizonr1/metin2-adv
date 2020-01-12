// 1) Search: ACMD(do_costume)
// 2) Delete their function and paste:
ACMD(do_costume)
{
	char buf[512];
	const size_t bufferSize = sizeof(buf);
	
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	
	CItem* pBody = ch->GetWear(WEAR_COSTUME_BODY);
	CItem* pHair = ch->GetWear(WEAR_COSTUME_HAIR);
	CItem* pAcce = ch->GetWear(WEAR_COSTUME_ACCE);
	
	ch->ChatPacket(CHAT_TYPE_INFO, "COSTUME status:");
	if (pBody)
	{
		const char* itemName = pBody->GetName();
		ch->ChatPacket(CHAT_TYPE_INFO, "  BODY : %s", itemName);
		
		if (pBody->IsEquipped() && arg1[0] == 'b')
			ch->UnequipItem(pBody);
	}
	
	if (pHair)
	{
		const char* itemName = pHair->GetName();
		ch->ChatPacket(CHAT_TYPE_INFO, "  HAIR : %s", itemName);

		for (int i = 0; i < pHair->GetAttributeCount(); ++i)
		{
			const TPlayerItemAttribute& attr = pHair->GetAttribute(i);
			if (0 < attr.bType)
			{
				snprintf(buf, bufferSize, FN_point_string(attr.bType), attr.sValue);
				ch->ChatPacket(CHAT_TYPE_INFO, "     %s", buf);
			}
		}

		if (pHair->IsEquipped() && arg1[0] == 'h')
			ch->UnequipItem(pHair);
	}
	
	if (pAcce)
	{
		const char* itemName = pAcce->GetName();
		ch->ChatPacket(CHAT_TYPE_INFO, "  Acce : %s", itemName);

		for (int i = 0; i < pAcce->GetAttributeCount(); ++i)
		{
			const TPlayerItemAttribute& attr = pAcce->GetAttribute(i);
			if (0 < attr.bType)
			{
				snprintf(buf, bufferSize, FN_point_string(attr.bType), attr.sValue);
				ch->ChatPacket(CHAT_TYPE_INFO, "     %s", buf);
			}
		}

		if (pAcce->IsEquipped() && arg1[0] == 'a')
			ch->UnequipItem(pAcce);
	}
}

// 1) Search: ACMD(do_inventory)
// 2) After their function paste:
ACMD(do_acce)
{
	if (!ch->CanDoAcce())
		return;
	
	dev_log(LOG_DEB0, "Acce command <%s>: %s", ch->GetName(), argument);
	int acce_index = 0, inven_index = 0;
	const char *line;
	
	char arg1[256], arg2[256], arg3[256];
	line = two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));
	one_argument(line, arg3, sizeof(arg3));
	if (0 == arg1[0])
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Usage: acce open");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce close");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce add <inveltory_index>");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce delete <acce_index>");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce list");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce cancel");
		ch->ChatPacket(CHAT_TYPE_INFO, "       acce make [all]");
		return;
	}
	
	const std::string& strArg1 = std::string(arg1);
	if (strArg1 == "r_info")
	{
		if (0 == arg2[0])
			Acce_request_result_list(ch);
		else
		{
			if (isdigit(*arg2))
			{
				int listIndex = 0, requestCount = 1;
				str_to_number(listIndex, arg2);
				if (0 != arg3[0] && isdigit(*arg3))
					str_to_number(requestCount, arg3);
				
				Acce_request_material_info(ch, listIndex, requestCount);
			}
		}
		
		return;
	}
	else if (strArg1 == "absorption")
	{
		Acce_absorption_make(ch);
		return;
	}
	else if (strArg1 == "open_absorption")
	{
		Acce_absorption_open(ch);
		return;
	}
	
	switch (LOWER(arg1[0]))
	{
		case 'o':
			Acce_open(ch);
			break;
		case 'c':
			Acce_close(ch);
			break;
		case 'l':
			Acce_show_list(ch);
			break;
		case 'a':
			{
				if (0 == arg2[0] || !isdigit(*arg2) || 0 == arg3[0] || !isdigit(*arg3))
					return;
				
				str_to_number(acce_index, arg2);
				str_to_number(inven_index, arg3);
				Acce_add_item (ch, acce_index, inven_index);
			}
			break;
		case 'd':
			{
				if (0 == arg2[0] || !isdigit(*arg2))
					return;
				
				str_to_number(acce_index, arg2);
				Acce_delete_item (ch, acce_index);
			}
			break;
		case 'm':
			if (0 != arg2[0])
			{
				while (true == Acce_make(ch))
					dev_log(LOG_DEB0, "Acce make success!");
			}
			else
				Acce_make(ch);
			break;
		default:
			return;
	}
}