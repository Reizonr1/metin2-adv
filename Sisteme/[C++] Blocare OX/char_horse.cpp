Caută:
void CHARACTER::HorseSummon(bool bSummon, bool bFromFar, DWORD dwVnum, const char* pPetName)
{
Aici găsește:
if (IsRiding())
			return;
Adaugă sub:
#ifdef ENABLE_OX_HORSE_BLOCK
		if (GetMapIndex() == 113)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("hydra_cannot_use_ride"));
			return;
		}
#endif