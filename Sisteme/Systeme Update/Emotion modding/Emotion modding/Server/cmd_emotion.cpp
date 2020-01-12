Search:
	TPacketGCChat pack_chat;
	pack_chat.header = HEADER_GC_CHAT;
	pack_chat.size = sizeof(TPacketGCChat) + len;
	pack_chat.type = CHAT_TYPE_COMMAND;
	pack_chat.id = 0;
	TEMP_BUFFER buf;
	buf.write(&pack_chat, sizeof(TPacketGCChat));
	buf.write(chatbuf, len);

	ch->PacketAround(buf.read_peek(), buf.size());

Add it under:
	if (victim)
	{
		if (victim->IsBlockMode(BLOCK_EMOITION_REQUEST){
			ch->ChatPacket(CHAT_TYPE_INFO, "%s is blocked emotion requests", victim->GetName());
			return;
		}

		LPDESC pkVictimDesc = victim->GetDesc();
		if (pkVictimDesc)
		{
			TPacketGCWhisper pack;

			char msg[450];
			sprintf(msg, "You challenged %s for a emotion.", ch->GetName());

			int len = MIN(CHAT_MAX_LEN, strlen(msg) + 1);

			pack.bHeader = HEADER_GC_WHISPER;
			pack.wSize = sizeof(TPacketGCWhisper)+len;
			pack.bType = WHISPER_TYPE_SYSTEM;
			strlcpy(pack.szNameFrom, ch->GetName(), sizeof(pack.szNameFrom));

			TEMP_BUFFER buf_wh;

			buf_wh.write(&pack, sizeof(TPacketGCWhisper));
			buf_wh.write(msg, len);

			ch->PacketAround(buf_wh.read_peek(), buf_wh.size());
		}
	}
