[..]
class CClientManager : public CNetBase, public singleton<CClientManager>
{
 
#ifdef OFFLINE_SHOP
	void		ShopName(CPeer * peer, TPacketShopName * p);
	void		ShopClose(CPeer * peer, TPacketShopClose *p);
	void		ShopUpdateItem(CPeer * peer, TPacketShopUpdateItem *p);
#endif
	
[..]