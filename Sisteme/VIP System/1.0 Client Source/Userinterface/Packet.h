//1.0 suchen:
typedef struct packet_char_additional_info
{
	....
	
	short   sAlignment; //¼±¾ÇÄ¡
	
//1.0 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	short   sVip; 
#endif	

//1.1 suchen:
typedef struct packet_add_char2
{
    ....
	
    short       sAlignment;

//1.1 dahinter:
#ifdef ENABLE_VIP_SYSTEM
    short       sVip;
#endif	

//1.2 suchen:
typedef struct packet_update_char
{
    ....
	
    short       sAlignment;

//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
    short       sVip;
#endif	

//1.3 suchen:
typedef struct packet_update_char2
{
    ....
	
    short       sAlignment;

//1.3 dahinter:
#ifdef ENABLE_VIP_SYSTEM
    short       sVip;
#endif	

