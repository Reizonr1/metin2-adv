Find - Bul:
bool SendSelectCharacterPacket(BYTE account_Index);

Add it under- Altına ekle:
bool SendCharacterPinPacket(BYTE index, int pin);


http://puu.sh/jS0uE/8136bc9273.png


Find - Bul:
bool SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byStat1, BYTE byStat2, BYTE byStat3, BYTE byStat4);

Change - Değiştir:
bool SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byStat1, BYTE byStat2, BYTE byStat3, BYTE byStat4, int character_pin);


http://puu.sh/jSEdl/963cb9725d.png