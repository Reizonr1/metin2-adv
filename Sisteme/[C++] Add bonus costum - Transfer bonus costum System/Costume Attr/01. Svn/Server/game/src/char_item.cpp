// 1) Search: case USE_BAIT:
// 2) Before this make a new line and paste:
#ifdef __COSTUME_ATTR_SYSTEM__
					case USE_COSTUME_ENCHANT:
					case USE_COSTUME_TRANSFORM:
						{
							LPITEM item2;
							if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
								return false;
							
							if (item2->IsEquipped())
							{
								BuffOnAttr_RemoveBuffsFromItem(item2);
							}
							
							if (item2->IsExchanging() || item2->IsEquipped())
								return false;
							
							if (item2->GetType() != ITEM_COSTUME)
							{
								ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can use this just on costumes."));
								return false;
							}
							
							if (item2->GetAttributeCount() == 0)
							{
								ChatPacket(CHAT_TYPE_INFO, LC_TEXT("This costume doesn't have any bonus."));
								return false;
							}
							
							switch (item->GetSubType())
							{
								case USE_COSTUME_ENCHANT:
									{
										int aiChangeProb[ITEM_ATTRIBUTE_MAX_LEVEL] = {100, 100, 100, 100, 100};
										item2->ChangeAttribute(aiChangeProb);
										ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You enchant succesfully the costume."));
										{
											char buf[21];
											snprintf(buf, sizeof(buf), "%u", item2->GetID());
											LogManager::instance().ItemLog(this, item, "USE_COSTUME_ENCHANT", buf);
										}
										
										item->SetCount(item->GetCount() - 1);
									}
									break;
								case USE_COSTUME_TRANSFORM:
									{
										item2->ClearAttribute();
										int iCostumePercent = number(1, 3);
										for (int i = 0; i < iCostumePercent; ++i)
										{
											item2->AddAttribute();
										}
										
										int aiChangeProb[ITEM_ATTRIBUTE_MAX_LEVEL] = {100, 100, 100, 100, 100};
										item2->ChangeAttribute(aiChangeProb);
										ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You transform succesfully the costume."));
										{
											char buf[21];
											snprintf(buf, sizeof(buf), "%u", item2->GetID());
											LogManager::instance().ItemLog(this, item, "USE_COSTUME_TRANSFORM", buf);
										}
										
										item->SetCount(item->GetCount() - 1);
									}
									break;
							}
						}
						break;
#endif