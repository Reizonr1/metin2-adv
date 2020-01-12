/*********************************************************************
* date        : 2016.08.31
* durate_time : 20 min
* file        : commandTeleporter_vegas.h
* author      : VegaS
* description : Command teleporter with argument's
*/

#define NUMBER_MAX_MAPS 13
#define ENABLE_TRANSLATE_LC_ENGLISH

/**********************
* Example for configuration table:
* coordantes_x : 473900
* coordantes_y : 954600
* level_minim : 1
* level_maxim : 105
*/	
	int szTeleportConfig[NUMBER_MAX_MAPS + 1][4] = 
	{
		{	NULL, NULL, NULL, NULL},
		{	473900,	954600,	1,	105	},	// metin2_map_a1                (idxMapIndex: 1)
		{	352300,	882700,	1,	105	},	// metin2_map_a3                (idxMapIndex: 3)
		{	63200,	166700,	1,	105	},	// metin2_map_b1                (idxMapIndex: 21)
		{	145700,	239800,	1,	105	},	// metin2_map_b3                (idxMapIndex: 23)
		{	959600,	269700,	1,	105	},	// metin2_map_c1                (idxMapIndex: 41)
		{	863800,	246000,	1,	105	},	// metin2_map_c3                (idxMapIndex: 43)	
		{	436300, 215700,	10,	105	},	// map_n_snowm_01               (idxMapIndex: 61)
		{	270400, 739900,	15,	105	},	// map_n_threeway               (idxMapIndex: 64)
		{	600900, 687500,	20,	105	},	// metin2_map_n_flame_01        (idxMapIndex: 62)
		{	217800, 627200,	25,	75	},	// metin2_map_n_desert_01       (idxMapIndex: 63)
		{	60000, 	496600, 30,	85	},	// metin2_map_spiderdungeon     (idxMapIndex: 10)
		{	553600,	144900, 35,	95	},	// metin2_map_milgyo            (idxMapIndex: 65)
		{	284200,	809600, 45,	105	}	// metin2_map_skipia_dungeon_01 (idxMapIndex: 72)
	};
	
	char* szTableNameMaps[] =
	{
		NULL,
		"<1> Map1 Shinshoo            (Lv. min.%d) | | (Lv. max.%d)", 
		"<2> Map2 Shinshoo            (Lv. min.%d) | | (Lv. max.%d)", 
		"<3> Map1 Chunjo              (Lv. min.%d) | | (Lv. max.%d)", 
		"<4> Map2 Chunjo              (Lv. min.%d) | | (Lv. max.%d)", 
		"<5> Map1 Jinno               (Lv. min.%d) | | (Lv. max.%d)", 
		"<6> Map2 Jinno               (Lv. min.%d) | | (Lv. max.%d)", 
		"<7> Mount Sohan              (Lv. min.%d) | | (Lv. max.%d)", 
		"<8> Valley of Seungryong     (Lv. min.%d) | | (Lv. max.%d)", 
		"<9> Doyyumhwaji              (Lv. min.%d) | | (Lv. max.%d)", 
		"<10> Yongbi Desert           (Lv. min.%d) | | (Lv. max.%d)", 	
		"<11> Spiders Dungeon 1       (Lv. min.%d) | | (Lv. max.%d)", 
		"<12> Hwang Temple            (Lv. min.%d) | | (Lv. max.%d)", 
		"<13> Skipia Dungeon 1        (Lv. min.%d) | | (Lv. max.%d)"
	};	
	
#ifdef ENABLE_TRANSLATE_LC_ENGLISH
	const char* szTableTranslate[] = {
		"You are in observation mode, you can not do that.",
		"You're dead, you can not do that.",
		"You're dizzy, you can not do that.",
		"You're a store, you can not do that.",
		"You're in a dungeon, you can not do that.",
		"Have a malicious window open, please close it then you can do this.",
		"You can not enter a smaller number like 1.",
		"You can not enter a higher number as [%d].",
		"You you cannot teleport in this map because you're too weak, you need level min: [%d].",
		"You you cannot teleport in this map because you're too big, you need level max: [%d].",
		"You chose number: [%d].",
		"USAGE : /teleport <number>",
		"List with map's active for teleport with number:"
	};	
#endif
#ifdef ENABLE_TRANSLATE_LC_POLAND
	const char* szTableTranslate[] = {"Jeste? w trybie obserwacji, nie mo?na tego zrobi?.",	"Jeste? martwy, nie mo?na tego zrobi?.",	"Jeste? w g≥owie, ?e nie mog? tego zrobi?.",	"Jeste? sklep, nie mo?na tego zrobi?.",	"Jeste? w lochu, nie mo?na tego zrobi?.",	"Maj? szkodliwy okno otwarte, zamknij go, a nast?pnie mo?na to zrobi?.",	"Nie mo?na wprowadzi? mniejsz? liczb? jak 1.",	"Nie mo?na wprowadzi? wi?ksz? liczb? jako [%d].",	"Ty nie mo?na teleportowa? si? w tej mapie, bo jeste? zbyt s≥aby, trzeba poziomu MIN: [%d].",	"Ty nie mo?na teleportowa? si? w tej mapie, bo jeste? zbyt du?e, trzeba Maksymalny poziom: [%d].",	"Wybrano numer: [%d].",	"STOSOWANIE : /teleport <numer>",	"List z aktywno?ci? mapy do teleportu z numerem:"};	
#endif
#ifdef ENABLE_TRANSLATE_LC_GERMANY
	const char* szTableTranslate[] = {"Sie befinden sich in Beobachtungsmodus , konnen Sie das nicht konnen.",	"Du bist tot, du kannst das nicht tun.",	"Du bist schwindelig, man kann das nicht tun.",	"Sie sind ein Speicher, konnen Sie das nicht tun.",	"Du bist in einem Kerker, konnen Sie das nicht tun.",	"Haben Sie ein bosartiger Fenster geoffnet, bitte schlieﬂen Sie es dann konnen Sie dies tun.",	"Sie konnen nicht eine kleinere Zahl wie 1 eingeben.",	"Sie konnen nicht eine hohere Zahl eingeben, wie [%d].",	"Sie konnen nicht in dieser Karte teleportieren , weil du zu schwach sind, dann mussen Sie Level min: [%d].",	"Sie konnen nicht in dieser Karte teleportieren , weil Sie zu groﬂ, du Level max brauchen: [%d].",	"Sie wahlten Nummer: [%d].",	"VERWENDUNG : /teleport <nummer>",	"Liste mit Karte Tatigkeit fur Teleport mit der Nummer:"};	
#endif
#ifdef ENABLE_TRANSLATE_LC_SPAIN
	const char* szTableTranslate[] = {"Usted esta en modo de observacion, no se puede hacer eso.",	"Estas muerto, no se puede hacer eso.",	"Estas mareada, no se puede hacer eso.",	"Eres una tienda, no se puede hacer eso.",	"Estas en un calabozo, no se puede hacer eso.",	"Tener una ventana abierta maliciosos, por favor cerrarla entonces usted puede hacer esto.",	"No se puede introducir un numero mas pequeno como 1.",	"No se puede introducir un numero mas alto como [%d].",	"Usted no puede teletransportarse en este mapa porque esta demasiado debil, que necesita el nivel min: [%d].",	"Usted no puede teletransportarse en este mapa porque estas demasiado grande, se necesita el nivel maximo: [%d].",	"Elegiste numero: [%d].",	"USO : /teleport <numero>",	"Una lista con actividad mapa de teletransporte con el numero:"};	
#endif