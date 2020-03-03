#ifndef	__HEADER_SUPPORT_SYSTEM__
#define	__HEADER_SUPPORT_SYSTEM__


class CHARACTER;


struct SShamanAbility
{
};

/**
*/
class CSupportActor //: public CHARACTER
{
public:
	enum EShamanOptions
	{
		ESupportOption_Followable		= 1 << 0,
		ESupportOption_Mountable		= 1 << 1,
		ESupportOption_Summonable		= 1 << 2,
		ESupportOption_Combatable		= 1 << 3,		
	};


protected:
	friend class CSupportSystem;

	CSupportActor(LPCHARACTER owner, DWORD vnum, DWORD options = ESupportOption_Followable | ESupportOption_Summonable);


	virtual ~CSupportActor();

	virtual bool	Update(DWORD deltaTime);

protected:
	virtual bool	_UpdateFollowAI();				///< ������ ����ٴϴ� AI ó��
	virtual bool	_UpdatAloneActionAI(float fMinDist, float fMaxDist);			///< ���� ��ó���� ȥ�� ��� AI ó��


private:
	bool Follow(float fMinDistance = 50.f);

public:
	LPCHARACTER		GetCharacter()	const					{ return m_pkChar; }
	LPCHARACTER		GetOwner()	const						{ return m_pkOwner; }
	DWORD			GetVID() const							{ return m_dwVID; }
	DWORD			GetVnum() const							{ return m_dwVnum; }

	bool			HasOption(EShamanOptions option) const		{ return m_dwOptions & option; }

	void			SetName();
	void			SetLevel(DWORD level);

	bool			Mount();
	void			Unmount();

	DWORD			Summon(const char* supportName, LPITEM pSummonItem, bool bSpawnFar = false);
	void			Unsummon();

	bool			IsSummoned() const			{ return 0 != m_pkChar; }
	void			SetSummonItem (LPITEM pItem);
	DWORD			GetLevel() { return m_dwlevel; }
	void			SetLastSkillTime(DWORD time)	{ m_dwLastSkillTime = time; }
	void			SetCostume();
	void			SetHair();
	void			SetWeapon();
	DWORD			GetLastSkillTime()	{ return m_dwLastSkillTime; }
	void			SetLastExpUpdate(DWORD time)	{ m_dwLastExpUpdateTime = time; }
	DWORD			GetLastExpUpdate()	{ return m_dwLastExpUpdateTime; }
	void			SetExp(DWORD exp);
	void			UpdateItemExp();
	void			UpdatePacketsupportActor();
	void			RefreshCostume();
	DWORD			GetExp() { return m_dwExp; }
	void			SetNextExp(int nextExp);
	int				GetNextExp() { return m_dwNextExp; }
	int				GetIntSkill();
	int				GetSupportVID();			
	void			UseSkill();
	void			SetIntSkill();
	DWORD			GetSummonItemVID () { return m_dwSummonItemVID; }

	void			GiveBuff();
	void			ClearBuff();

private:
	DWORD			m_dwVnum;
	DWORD			m_dwVID;
	DWORD			m_dwOptions;
	DWORD			m_dwLastActionTime;
	DWORD			m_dwSummonItemVID;
	DWORD			m_dwSummonItemVnum;
	DWORD			m_dwExp;
	DWORD			m_dwLastSkillTime;
	DWORD			m_dwLastExpUpdateTime;
	DWORD			m_dwIntSkill;
	DWORD			m_dwlevel;
	DWORD			m_dwNextExp;
	short			m_originalMoveSpeed;
	
	std::string		first_name;
	std::string		second_name;
	std::string		m_speciality;
	LPCHARACTER		m_pkChar;
	LPCHARACTER		m_pkOwner;


};

/**
*/
class CSupportSystem
{
public:
	typedef	boost::unordered_map<DWORD,	CSupportActor*>		TsupportActorMap;		

public:
	CSupportSystem(LPCHARACTER owner);
	virtual ~CSupportSystem();

	CSupportActor*	GetByVID(DWORD vid) const;
	CSupportActor*	GetByVnum(DWORD vnum) const;

	bool		Update(DWORD deltaTime);
	void		Destroy();

	size_t		CountSummoned() const;

	
public:
	void		SetUpdatePeriod(DWORD ms);

	CSupportActor*	Summon(DWORD mobVnum, LPITEM pSummonItem, const char* supportName, bool bSpawnFar, DWORD options = CSupportActor::ESupportOption_Followable | CSupportActor::ESupportOption_Summonable);

	void		Unsummon(DWORD mobVnum, bool bDeleteFromList = false);
	void		Unsummon(CSupportActor* supportActor, bool bDeleteFromList = false);
	void		SetExp(int iExp);
	int			GetLevel();
	int			GetExp();
	bool		IsActiveSupport();
	CSupportActor*   GetActiveSupport();
	CSupportActor*	AddShaman(DWORD mobVnum, const char* supportName, const SShamanAbility& ability, DWORD options = CSupportActor::ESupportOption_Followable | CSupportActor::ESupportOption_Summonable | CSupportActor::ESupportOption_Combatable);

	void		DeleteSupport(DWORD mobVnum);
	void		DeleteSupport(CSupportActor* supportActor);
	void		RefreshBuff();
	
private:
	TsupportActorMap	m_supportActorMap;
	LPCHARACTER		m_pkOwner;					
	DWORD			m_dwUpdatePeriod;			
	DWORD			m_dwLastUpdateTime;
	LPEVENT			m_pksupportSystemUpdateEvent;
};



#endif	//__HEADER_SUPPORT_SYSTEM__