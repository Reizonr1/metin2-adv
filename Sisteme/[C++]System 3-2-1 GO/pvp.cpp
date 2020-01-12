Intram in pvp.cpp
cautam void CPVPManager::Insert(LPCHARACTER pkChr, LPCHARACTER pkVictim) si inlocuim toata functia cu:
EVENTINFO(start_duel_efect_info)
{
   LPCHARACTER ch1;
   LPCHARACTER ch2;
   CPVP * pkPVP;
   BYTE state;

   start_duel_efect_info() 
   : ch1( NULL )
   ,ch2( NULL )
   ,pkPVP( NULL )
   ,state( 0 )
   {
   }
};
   
EVENTFUNC(start_duel_efect)
{
   start_duel_efect_info * info = dynamic_cast<start_duel_efect_info *>(event->info);

   if ((info == NULL) || (info->ch1 == NULL) || (info->ch2 == NULL) || (info->pkPVP == NULL)) return 0;
   
   switch (info->state)
   {
      case 0:
      {
         info->ch1->SpecificEffectPacket("d:/ymir work/effect/pvp/3.mse");
         info->ch2->SpecificEffectPacket("d:/ymir work/effect/pvp/3.mse");
         info->state++;
         return PASSES_PER_SEC(1);
         break;
      }
      case 1:
      {
         info->ch1->SpecificEffectPacket("d:/ymir work/effect/pvp/2.mse");
         info->ch2->SpecificEffectPacket("d:/ymir work/effect/pvp/2.mse");
         info->state++;
         return PASSES_PER_SEC(1);
         break;
      }
      case 2:
      {
         info->ch1->SpecificEffectPacket("d:/ymir work/effect/pvp/1.mse");
         info->ch2->SpecificEffectPacket("d:/ymir work/effect/pvp/1.mse");
         info->state++;
         return PASSES_PER_SEC(1);
         break;
      }
      case 3:
      {
         info->ch1->SpecificEffectPacket("d:/ymir work/effect/pvp/go.mse");
         info->ch2->SpecificEffectPacket("d:/ymir work/effect/pvp/go.mse");
         if ((info->pkPVP->Agree(info->ch1->GetPlayerID())) && (!info->pvp_event))
         {
            info->ch2->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s님과의 대결 시작!"), info->ch1->GetName());
            info->ch1->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s님과의 대결 시작!"), info->ch2->GetName());
         }
         return 0;
         break;
      }
   }
   return 0;
}

void CPVPManager::Insert(LPCHARACTER pkChr, LPCHARACTER pkVictim)
{
   if (pkChr->IsDead() || pkVictim->IsDead() || pkChr->FindAffect(AFFECT_PVP_START))
      return;   
   
   CPVP kPVP(pkChr->GetPlayerID(), pkVictim->GetPlayerID());

   CPVP * pkPVP;
   
   if (pkPVP = Find(kPVP.m_dwCRC))
   {
      start_duel_efect_info * info = AllocEventInfo<start_duel_efect_info>();
      info->ch1 = pkChr;
      info->ch2 = pkVictim;
      info->pkPVP = pkPVP;
      info->state = 0;
      pkChr->AddAffect(AFFECT_PVP_START, APPLY_NONE, 0, 0, 5, 0, false);
      event_create(start_duel_efect, info, 0);
      return;
   }

   pkPVP = M2_NEW CPVP(kPVP);

   pkPVP->SetVID(pkChr->GetPlayerID(), pkChr->GetVID());
   pkPVP->SetVID(pkVictim->GetPlayerID(), pkVictim->GetVID());

   m_map_pkPVP.insert(map<DWORD, CPVP *>::value_type(pkPVP->m_dwCRC, pkPVP));

   m_map_pkPVPSetByID[pkChr->GetPlayerID()].insert(pkPVP);
   m_map_pkPVPSetByID[pkVictim->GetPlayerID()].insert(pkPVP);

   pkPVP->Packet();

   
   char msg[CHAT_MAX_LEN + 1];
   snprintf(msg, sizeof(msg), LC_TEXT("%s님이 대결신청을 했습니다. 승낙하려면 대결동의를 하세요."), pkChr->GetName());
      
   pkVictim->ChatPacket(CHAT_TYPE_INFO, msg);
   pkChr->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s에게 대결신청을 했습니다."), pkVictim->GetName());
      
   // NOTIFY_PVP_MESSAGE
   LPDESC pkVictimDesc = pkVictim->GetDesc();
   if (pkVictimDesc)
   {
      TPacketGCWhisper pack;

      int len = MIN(CHAT_MAX_LEN, strlen(msg) + 1);

      pack.bHeader = HEADER_GC_WHISPER;
      pack.wSize = sizeof(TPacketGCWhisper) + len;
      pack.bType = WHISPER_TYPE_SYSTEM;
      strlcpy(pack.szNameFrom, pkChr->GetName(), sizeof(pack.szNameFrom));

      TEMP_BUFFER buf;

      buf.write(&pack, sizeof(TPacketGCWhisper));
      buf.write(msg, len);

      pkVictimDesc->Packet(buf.read_peek(), buf.size());
   }   
   // END_OF_NOTIFY_PVP_MESSAGE
}

cautam bool CPVPManager::Dead(LPCHARACTER pkChr, DWORD dwKillerPID) si inlocuim toata functia cu:
bool CPVPManager::Dead(LPCHARACTER pkChr, DWORD dwKillerPID)
{
   CPVPSetMap::iterator it = m_map_pkPVPSetByID.find(pkChr->GetPlayerID());

   if (it == m_map_pkPVPSetByID.end())
      return false;

   bool found = false;

   sys_log(1, "PVPManager::Dead %d", pkChr->GetPlayerID());
   TR1_NS::unordered_set<CPVP*>::iterator it2 = it->second.begin();

   while (it2 != it->second.end())
   {
      CPVP * pkPVP = *it2++;

      DWORD dwCompanionPID;

      if (pkPVP->m_players[0].dwPID == pkChr->GetPlayerID())
         dwCompanionPID = pkPVP->m_players[1].dwPID;
      else
         dwCompanionPID = pkPVP->m_players[0].dwPID;

      if (dwCompanionPID == dwKillerPID)
      {
         if (pkPVP->IsFight())
         {
            pkPVP->SetLastFightTime();
            pkPVP->Win(dwKillerPID);
            found = true;
            break;
         }
         else if (get_dword_time() - pkPVP->GetLastFightTime() <= 15000)
         {
            found = true;
            break;
         }
      }
   }
   
   LPCHARACTER pkChrW = CHARACTER_MANAGER::instance().FindByPID(dwKillerPID);
   pkChrW->SpecificEffectPacket("d:/ymir work/effect/pvp/win.mse");
   
   return found;
}

Intram in affect.h
cautam AFFECT_DRAGON_SOUL_DECK_1 = 542, si sub adaugam:
   AFFECT_PVP_START = 543,
   AFFECT_PVP_WIN = 544,

cautam AFF_BITS_MAX si deasupra adaugam:
   AFF_PVP_START,
   AFF_PVP_WIN,
   
info->ch2->ChatPacket(CHAT_TYPE_INFO, "Duelul cu: %s a inceput!", info->ch1->GetName());
info->ch1->ChatPacket(CHAT_TYPE_INFO, "Duelul cu: %s a inceput!", info->ch2->GetName());

char msg[CHAT_MAX_LEN + 1];
snprintf(msg, sizeof(msg), "Ai fost provocat la duel de: %s.", pkChr->GetName()); //e el

pkVictim->ChatPacket(CHAT_TYPE_INFO, msg);
pkChr->ChatPacket(CHAT_TYPE_INFO, "L-ai provocat la duel pe: %s.", pkVictim->GetName()); //is eu


if (info->pkPVP->Agree(info->ch1->GetPlayerID()))