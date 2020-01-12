Find - Bul:
HEADER_CG_PLAYER_SELECT						= 6,

Add it under- Altına ekle:
HEADER_CG_PLAYER_PIN						= 21,


http://puu.sh/jS0mQ/a4bb84e5b9.png


Find - Bul:
typedef struct command_player_select
{
	BYTE	header;
	BYTE	player_index;
} TPacketCGSelectCharacter;

Add it under- Altına ekle:
typedef struct command_player_pin
{
	BYTE	header;
	BYTE	index;
	int		character_pin;
} TPacketCGPinCharacter;


http://puu.sh/jS0qH/25f2018c5c.png

Find - Bul:
typedef struct command_player_create
{
	BYTE        header;
	BYTE        index;
	char        name[CHARACTER_NAME_MAX_LEN + 1];
	WORD        job;
	BYTE		shape;
	BYTE		CON;
	BYTE		INT;
	BYTE		STR;
	BYTE		DEX;
} TPacketCGCreateCharacter;

Change - Değiştir:
typedef struct command_player_create
{
	BYTE        header;
	BYTE        index;
	char        name[CHARACTER_NAME_MAX_LEN + 1];
	WORD        job;
	BYTE		shape;
	BYTE		CON;
	BYTE		INT;
	BYTE		STR;
	BYTE		DEX;
	int			character_pin; //M2_CHARACTER_PIN
} TPacketCGCreateCharacter;


http://puu.sh/jSE7R/46e78f9321.png


