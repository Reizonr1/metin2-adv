#define DEATMATCH_MAP_INDEX 200

/*
Deathmatch mode;

sald�r�labilirlik, girince attan ve binekten indirme, confige map index, do_ride,
party_req_accep, party_req, pvp, restart, horse_ride, poly, pazar, oto pk,
pk de�i�tirme, alignment olay�, 180saniyede do�ma(?), girildi�inde bufflar silinir
alignmentten kaynakl� item d��mez, autopot, evlilik y�z��� �al��maz,
china firework, full hp ba�lar, 20 snde bir ba�lar, �ebnem ve baz� e�yalar engelli
�aman ba�kas�na buf veremez, gmye sald�r�lamaz, oyundan ��k�ld���nda sava�tan ��kar


Hedef oyuncu sald�ran oyuncudan 2 kat daha fazla kill ald�ysa %5, 3 kat fazla ise %10, 4 kat fazla kill ise %20 ekstra hasar
Hedef oyuncu sald�ran oyuncudan 2 kat daha fazla kill ald�ysa +2, 3 kat fazla ise +3, 4 kat fazla kill ise +5 ekstra kill

*/

enum DeathMatchStatus
{
	DEATHMATCH_FINISH = 0,
	DEATHMATCH_OPEN = 1,	//stundan �nce
	DEATHMATCH_STARTED = 2, //stundan sonra event aktif
	DEATHMATCH_CLOSE = 3,

	DEATHMATCH_ERR = 0xff
};

class CDeathMatchManager : public singleton<CDeathMatchManager>
{
	private:
		std::map<DWORD, DWORD> m_map_char; //Aktif eventtekiler
		std::map<DWORD, DWORD> m_map_miss; //�len izleyiciler
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

