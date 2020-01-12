Search:
	default:
		sys_err ("Invalid Inventory type %d", window_type);
		return;
	}

Add it upper:
#ifdef __OFFLINE_SHOP__
	case OFFLINE_SHOP:
		m_pointsInstant.pItems[wCell] = pItem;
		break;
#endif

https://puu.sh/sgFhv/26fcc25039.png

---

Search:
			ChatPacket(CHAT_TYPE_COMMAND, "OpenPrivateShop");
			break;

Change:
#ifdef __OFFLINE_SHOP__
			ChatPacket(CHAT_TYPE_COMMAND, "OpenPrivateShop %d %d %d", __OFFLINE_SHOP_ALLOW_COIN__, __OFFLINE_SHOP_ALLOW_GOLDBAR__, __OFFLINE_SHOP_ALLOW_WON__);
#else
			ChatPacket(CHAT_TYPE_COMMAND, "OpenPrivateShop");
#endif
			break;

https://puu.sh/sgFjc/7ce83808fe.png

