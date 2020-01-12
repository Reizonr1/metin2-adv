#define DEATMATCH_MAP_INDEX 200

/*
Deathmatch mode;

saldýrýlabilirlik, girince attan ve binekten indirme, confige map index, do_ride,
party_req_accep, party_req, pvp, restart, horse_ride, poly, pazar, oto pk,
pk deðiþtirme, alignment olayý, 180saniyede doðma(?), girildiðinde bufflar silinir
alignmentten kaynaklý item düþmez, autopot, evlilik yüzüðü çalýþmaz,
china firework, full hp baþlar, 20 snde bir baþlar, þebnem ve bazý eþyalar engelli
þaman baþkasýna buf veremez, gmye saldýrýlamaz, oyundan çýkýldýðýnda savaþtan çýkar


Hedef oyuncu saldýran oyuncudan 2 kat daha fazla kill aldýysa %5, 3 kat fazla ise %10, 4 kat fazla kill ise %20 ekstra hasar
Hedef oyuncu saldýran oyuncudan 2 kat daha fazla kill aldýysa +2, 3 kat fazla ise +3, 4 kat fazla kill ise +5 ekstra kill

*/

enum DeathMatchStatus
{
	DEATHMATCH_FINISH = 0,
	DEATHMATCH_OPEN = 1,	//stundan önce
	DEATHMATCH_STARTED = 2, //stundan sonra event aktif
	DEATHMATCH_CLOSE = 3,

	DEATHMATCH_ERR = 0xff
};

class CDeathMatchManager : public singleton<CDeathMatchManager>
{
	private:
		std::map<DWORD, DWORD> m_map_char; //Aktif eventtekiler
		std::map<DWORD, DWORD> m_map_miss; //Ölen izleyiciler
		DWORD dwWinnerPID;

	protected:
		bool EnterAttender(LPCHARACTER pChar);

	public:
		bool Initialize();
		void Destroy();

		DeathMatchStatus GetStatus();
		void SetStatus(DeathMatchStatus status);
		void CheckEventStatus();

		bool Enter(LPCHARACTER pChar);
		bool StartEvent();
		bool CloseEvent();

		bool EnterSpectator(LPCHARACTER pChar);
		bool SwitchToSpectator(LPCHARACTER pChar);
		void RemoveFromEvent(LPCHARACTER x_pkChar);

		void RemoveStuns();
		void SpawnRandomPos(LPCHARACTER pkChar);

		int GetScore(DWORD dwPID);
		void SetScore(DWORD dwPID, int iNewScore);
		void NoticeScore(DWORD dwPID, int iScore);
		void SendScoreInfo(DWORD dwPID, int iScore);
		void ResetScore(LPCHARACTER pkChar);

		int GetHighScore();
		DWORD GetHighScoreOwner();
		void SetHighScore(DWORD dwPID, int iNewScore);
		void CheckHighScore(DWORD dwPID);
		
		void SetWinner(LPCHARACTER x_pkChar);
		bool LogWinner();
		bool GiveItemToAttender(DWORD dwItemVnum, BYTE count);

		bool IsLimitedItem(DWORD dwVnum);

		DWORD GetAttenderCount() { return m_map_char.size(); }
		DWORD GetSpectatorCount() { return m_map_miss.size(); }
};

