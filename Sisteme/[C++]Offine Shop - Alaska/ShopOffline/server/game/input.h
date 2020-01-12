[..]
class CInputDB : public CInputProcessor
{
#ifdef OFFLINE_SHOP
	public:
	void		ShopName(const char * c_pData);
	void		ShopClose(const char * c_pData);
	void		ShopUpdateItem(const char * c_pData);

#endif
