// 1) Search:
					case USE_PUT_INTO_BELT_SOCKET:
					case USE_PUT_INTO_RING_SOCKET:
					case USE_PUT_INTO_ACCESSORY_SOCKET:
					case USE_ADD_ACCESSORY_SOCKET:
					case USE_CLEAN_SOCKET:
					case USE_CHANGE_ATTRIBUTE:
					case USE_CHANGE_ATTRIBUTE2:
					case USE_ADD_ATTRIBUTE:
					case USE_ADD_ATTRIBUTE2:
// 2) Before:
					case USE_PUT_INTO_BELT_SOCKET:
// 3) Make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
					case USE_CHANGE_ATTRIBUTE3:
					{
						if (GetEnchantAttr() < 5555)
							return false;
						
						LPITEM item2;
						if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
							return false;
						
						if (item2->IsEquipped())
							BuffOnAttr_RemoveBuffsFromItem(item2);
						
#ifdef __SOULBINDING_SYSTEM__
						if (item2->IsBind() && item->GetSubType() != USE_PUT_INTO_BELT_SOCKET && item->GetSubType() != USE_PUT_INTO_RING_SOCKET && item->GetSubType() != USE_PUT_INTO_ACCESSORY_SOCKET && item->GetSubType() != USE_ADD_ACCESSORY_SOCKET)
						{
							ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't do this because this item is binded."));
							return false;
						}
						
						if (item2->IsUntilBind() && item->GetSubType() != USE_PUT_INTO_BELT_SOCKET && item->GetSubType() != USE_PUT_INTO_RING_SOCKET && item->GetSubType() != USE_PUT_INTO_ACCESSORY_SOCKET && item->GetSubType() != USE_ADD_ACCESSORY_SOCKET)
						{
							ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't do this because this until unbind process."));
							return false;
						}
#endif
						
						if (ITEM_COSTUME == item2->GetType())
						{
							ChatPacket(CHAT_TYPE_INFO, LC_TEXT("속성을 변경할 수 없는 아이템입니다."));
							return false;
						}
						
						if (item2->IsExchanging() || item2->IsEquipped())
							return false;
						
						if (item2->GetAttributeSetIndex() == -1)
						{
							ChatPacket(CHAT_TYPE_INFO, LC_TEXT("속성을 변경할 수 없는 아이템입니다."));
							return false;
						}
						
						if (item2->GetAttributeCount() == 0)
						{
							ChatPacket(CHAT_TYPE_INFO, LC_TEXT("변경할 속성이 없습니다."));
							return false;
						}
#ifdef __USE_TESTSERVER__
						if ((GM_PLAYER == GetGMLevel()) && (false == test_server) && (false == g_bDisableItemBonusChangeTime))
#else
						if ((GM_PLAYER == GetGMLevel()) && (false == g_bDisableItemBonusChangeTime))
#endif
						{
							DWORD dwChangeItemAttrCycle = quest::CQuestManager::instance().GetEventFlag(msc_szChangeItemAttrCycleFlag);
							if (dwChangeItemAttrCycle < msc_dwDefaultChangeItemAttrCycle)
								dwChangeItemAttrCycle = msc_dwDefaultChangeItemAttrCycle;
							
							quest::PC* pPC = quest::CQuestManager::instance().GetPC(GetPlayerID());
							if (pPC)
							{
								DWORD dwNowMin = get_global_time() / 60;
								DWORD dwLastChangeItemAttrMin = pPC->GetFlag(msc_szLastChangeItemAttrFlag);
								if (dwLastChangeItemAttrMin + dwChangeItemAttrCycle > dwNowMin)
								{
									ChatPacket(CHAT_TYPE_INFO, LC_TEXT("속성을 바꾼지 %d분 이내에는 다시 변경할 수 없습니다.(%d 분 남음)"), dwChangeItemAttrCycle, dwChangeItemAttrCycle - (dwNowMin - dwLastChangeItemAttrMin));
									return false;
								}
								
								pPC->SetFlag(msc_szLastChangeItemAttrFlag, dwNowMin);
							}
						}
						
						newEnchant_type1 = 0;
						newEnchant_value1 = 0;
						newEnchant_type2 = 0;
						newEnchant_value2 = 0;
						newEnchant_type3 = 0;
						newEnchant_value3 = 0;
						newEnchant_type4 = 0;
						newEnchant_value4 = 0;
						newEnchant_type5 = 0;
						newEnchant_value5 = 0;
						SetEnchantAttr(item2->GetCell());
						item2->PrepareAttribute();
						ChatPacket(CHAT_TYPE_COMMAND, "EnchantAttr_open #%d#%d#%d#%d#%d#%d#%d#%d#%d#%d#%d#", DestCell.cell, newEnchant_type1, newEnchant_value1, newEnchant_type2, newEnchant_value2, newEnchant_type3, newEnchant_value3, newEnchant_type4, newEnchant_value4, newEnchant_type5, newEnchant_value5);
						{
							char buf[128];
							snprintf(buf, sizeof(buf), "%u", item2->GetID());
							LogManager::instance().ItemLog(this, item, "CHANGE_ATTRIBUTE3 WAIT_PLAYER", buf);
						}
						
						item2->Lock(true);
						item->SetCount(item->GetCount() - 1);
					}
					break;
#endif