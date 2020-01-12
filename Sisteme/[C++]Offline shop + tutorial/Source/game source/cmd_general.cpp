Arat ;
#ifdef __AUCTION__
#include "auction_manager.h"
#endif

Altına Ekle ;
#include "offlineshop_manager.h"






Arat ;
	AuctionManager::instance().bid_cancel (ch, strtoul(arg1, NULL, 10));
}
#endif

Altına Ekle ;
ACMD(do_open_offline_shop)
{
	// If character is dead, return false
	if (ch->IsDead())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Ölüyken pazar açamassın.");
		return;
	}

	// If character is exchanging with someone, return false
	if (ch->GetExchange())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Biriyle alışveriş yapıyorsun. İlk önce pencereye yaklaşın!");
		return;
	}

	// If character has a private shop, return false
	if (ch->GetMyShop())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Açık özel dükkânın vardı. İlk bakışta bu özel dükkana yakın olmanız lazım!");
		return;
	}

	// If character is look at one offline shop, return false
	if (ch->GetOfflineShop())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Zaten bir çevrimdışı mağazaya baktığınızdan çevrimdışı mağazayı açamazsınız.");
		return;
	}

	// If cube window is open, return false
	if (ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Küp pencereniz açık olduğu için çevrimdışı mağazayı açamazsınız");
		return;
	}

	// If character's safebox is open, return false
	if (ch->IsOpenSafebox())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Kasa kutusu penceresi açık olduğundan çevrimdışı mağazayı açamazsınız!");
		return;
	}

	// If character's shop window is open, return false
	if (ch->GetShop())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Dükkan pencereniz açık olduğu için çevrimdışı mağazayı açamazsınız!");
		return;
	}

	// Send the command to client.
	ch->ChatPacket(CHAT_TYPE_COMMAND, "OpenOfflineShop");
}