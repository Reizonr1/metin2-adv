Find - Bul:
HEADER_CG_CHARACTER_SELECT			= 6,

Add it under- Altına ekle:
HEADER_CG_PLAYER_PIN				= 21,

http://puu.sh/jRZT4/0a4e354e77.png


Find - Bul:
typedef struct command_player_select
{
	BYTE	header;
	BYTE	index;
} TPacketCGPlayerSelect;

Add it under- Altına ekle:
typedef struct command_player_pin
{
	BYTE	header;
	BYTE	index;
	int		character_pin;
} TPacketCGPinCharacter;


http://puu.sh/jRZWS/607439cc05.png


Find - Bul:
typedef struct command_player_create
{
	BYTE        header;
	BYTE        index;
	char        name[CHARACTER_NAME_MAX_LEN + 1];
	WORD        job;
	BYTE	shape;
	BYTE	Con;
	BYTE	Int;
	BYTE	Str;
	BYTE	Dex;
} TPacketCGPlayerCreate;

Change - Değiştir:
typedef struct command_player_create
{
	BYTE        header;
	BYTE        index;
	char        name[CHARACTER_NAME_MAX_LEN + 1];
	WORD        job;
	BYTE	shape;
	BYTE	Con;
	BYTE	Int;
	BYTE	Str;
	BYTE	Dex;
	int		character_pin; //M2_CHARACTER_PIN
} TPacketCGPlayerCreate;


http://puu.sh/jSEtR/5797c19344.png