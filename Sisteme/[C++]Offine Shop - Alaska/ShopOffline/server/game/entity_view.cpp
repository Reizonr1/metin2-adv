//find class CFuncViewInsert and replace
#include "questmanager.h"
class CFuncViewInsert
{
	private:
		int dwViewRange;

	public:
		LPENTITY m_me;

		CFuncViewInsert(LPENTITY ent) :
			dwViewRange(VIEW_RANGE + VIEW_BONUS_RANGE),
			m_me(ent)
		{
		}

		void operator () (LPENTITY ent)
		{
			// żŔşęÁ§Ć®°ˇ ľĆ´Ń °ÍŔş °Ĺ¸®¸¦ °č»ęÇĎż© °Ĺ¸®°ˇ ¸Ö¸é Ăß°ˇÇĎÁö ľĘ´Â´Ů.
			if (!ent->IsType(ENTITY_OBJECT))
				if (DISTANCE_APPROX(ent->GetX() - m_me->GetX(), ent->GetY() - m_me->GetY()) > dwViewRange)
					return;
#ifdef SHOP_DISTANCE
			if (ent->IsType(ENTITY_CHARACTER) && m_me->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER chMe = (LPCHARACTER)m_me;
				LPCHARACTER chEnt = (LPCHARACTER)ent;
				DWORD ViewRange = quest::CQuestManager::instance().GetEventFlag("shop_dist");
				if (ViewRange>0 && DISTANCE_APPROX(ent->GetX() - m_me->GetX(), ent->GetY() - m_me->GetY()) > ViewRange &&
					chMe->IsPC() && chEnt->IsNPC() && chEnt->GetRaceNum() == 30000)
					return;
			}
#endif
			// łŞ¸¦ ´ë»óżˇ Ăß°ˇ
			m_me->ViewInsert(ent);

			// µŃ´Ů Äł¸ŻĹÍ¸é
			if (ent->IsType(ENTITY_CHARACTER) && m_me->IsType(ENTITY_CHARACTER))
			{
				LPCHARACTER chMe = (LPCHARACTER) m_me;
				LPCHARACTER chEnt = (LPCHARACTER) ent;

				// ´ë»óŔĚ NPC¸é StateMachineŔ» Ĺ˛´Ů.
				if (chMe->IsPC() && !chEnt->IsPC() && !chEnt->IsWarp() && !chEnt->IsGoto())
					chEnt->StartStateMachine();
			}
		}
};
