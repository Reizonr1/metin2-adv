// 1) Search: ACMD(do_cube)
// 2) Before this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
ACMD(do_enchant_new)
{
	if (!ch)
		return;
	
	if (ch->GetEnchantAttr() == 5555)
		return;
	
	LPITEM itemTarget = ch->GetInventoryItem(ch->GetEnchantAttr());
	if (itemTarget == NULL)
		return;
	
	ch->SetEnchantAttr(5555);
	itemTarget->SetForceAttribute(0, ch->GetEnchantType1(), ch->GetEnchantValue1());
	itemTarget->SetForceAttribute(1, ch->GetEnchantType2(), ch->GetEnchantValue2());
	itemTarget->SetForceAttribute(2, ch->GetEnchantType3(), ch->GetEnchantValue3());
	itemTarget->SetForceAttribute(3, ch->GetEnchantType4(), ch->GetEnchantValue4());
	itemTarget->SetForceAttribute(4, ch->GetEnchantType5(), ch->GetEnchantValue5());
	itemTarget->Lock(false);
	
	ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You choose to take the new bonuses."));
	{
		char buf[128];
		snprintf(buf, sizeof(buf), "%u", itemTarget->GetID());
		LogManager::instance().ItemLog(ch, itemTarget, "CHANGE_ATTRIBUTE3 ANSWER_YES", buf);
	}
	
	ch->Save();
}

ACMD(do_enchant_old)
{
	if (!ch)
		return;
	
	if (ch->GetEnchantAttr() == 5555)
		return;
	
	LPITEM itemTarget = ch->GetInventoryItem(ch->GetEnchantAttr());
	if (itemTarget == NULL)
		return;
	
	ch->SetEnchantAttr(5555);
	itemTarget->Lock(false);
	
	ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You choose to take the old bonuses."));
	{
		char buf[128];
		snprintf(buf, sizeof(buf), "%u", itemTarget->GetID());
		LogManager::instance().ItemLog(ch, itemTarget, "CHANGE_ATTRIBUTE3 ANSWER_NO", buf);
	}
}
#endif