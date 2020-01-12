Find - Bul:
bool CPythonNetworkStream::SendSelectCharacterPacket(BYTE Index)

Add it upper - Üstüne ekle:
bool CPythonNetworkStream::SendCharacterPinPacket(BYTE index, int pin){
	if (m_strPhase == "Select"){
		TPacketCGPinCharacter CharacterPinPacket;

		CharacterPinPacket.header = HEADER_CG_PLAYER_PIN;
		CharacterPinPacket.index = index;
		CharacterPinPacket.character_pin = pin;

		if (!Send(sizeof(TPacketCGPinCharacter), &CharacterPinPacket))
		{
			Tracen("CharacterPinPacket - Error");
			return false;
		}
	}
	else {
		Tracen("CPythonNetworkStream::SendCharacterPinPacket Wrong Phase - Error");
		return false;
	}

	return SendSequence();
}


http://puu.sh/jS0IP/3e9ec93b0c.png


Find - Bul:
bool CPythonNetworkStream::SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byCON, BYTE byINT, BYTE bySTR, BYTE byDEX)

Change - Değiştir:
bool CPythonNetworkStream::SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byCON, BYTE byINT, BYTE bySTR, BYTE byDEX, int character_pin)


http://puu.sh/jSEbn/a88dcd261a.png


Find - Bul:
createCharacterPacket.DEX = byDEX;

Add it under- Altına ekle:
createCharacterPacket.character_pin = character_pin;


http://puu.sh/jSEgz/4f052bdfd5.png
