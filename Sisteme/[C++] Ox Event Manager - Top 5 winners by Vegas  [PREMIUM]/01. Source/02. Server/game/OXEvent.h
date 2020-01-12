//1.) Search:
#define OXEVENT_MAP_INDEX 113
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT

	#define PASSWORD_MANAGER "metin2team" // Change here password for login in event manager.

	enum TypeInfo
	{
		OXEVENT_TOP_LIMIT = 5,
		OXEVENT_FIRST_ANSWER = 1,
		OXEVENT_NO_DATA = 999,
		OXEVENT_OPEN_LOGIN = 0,
		OXEVENT_OPEN_EVENT = 1,
		OXEVENT_CLOSE_GATES = 2,
		OXEVENT_CLOSE_EVENT = 3,
		OXEVENT_REWARD_PLAYERS = 4,
		OXEVENT_ASK_QUESTION = 5,
		OXEVENT_FORCE_CLOSE_EVENT = 6,
	};
#endif

//1.) Search:
		std::map<DWORD, DWORD> m_map_miss;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		std::map<DWORD, DWORD> m_map_answers;
#endif

//1.) Search:
		LPEVENT m_timedEvent;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		LPEVENT m_counterEvent;
#endif

//1.) Search:
		bool ShowQuizList(LPCHARACTER pChar);
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		DWORD GetObserverCount() { return (m_map_char.size() - m_map_attender.size() > 0) ? m_map_char.size() - m_map_attender.size() : 0; }
		std::string GetGuildWinner(LPCHARACTER pkChar);

		bool IsExistVnum(DWORD dwItemVnum);
		bool IsExistCount(BYTE count);
		bool IsExistKeyAnswers(LPCHARACTER pChar, int * keyAnswers);
		//bool CheckPassword(LPCHARACTER pChar, const char* c_szPassword);
		
		bool IsLastManStanding();
		void InsertAnswers(LPCHARACTER pChar);
		void TruncateAnswers(LPCHARACTER pChar);
		void RegisterWinner();
		void InitializePacket(LPCHARACTER pChar);
		
		void RefreshWinners();
		void OpenGui(LPCHARACTER pChar);
		void Disconnect(LPCHARACTER pChar);
		
		void GetErrByStatus(LPCHARACTER pChar, int key);

		void NoticeAll(std::string msg);
		void Manager(LPCHARACTER ch, const char* c_pData);
#endif