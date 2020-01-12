//1.0 suchen:
typedef struct packet_char_additional_info
{
	....
	short	sAlignment;
//.0 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	short	sVip;
#endif	

//1.1 suchen:
typedef struct packet_update_char
{
	....
	short	sAlignment;
//dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	short	sVip;
#endif	
