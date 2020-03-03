// Check this:

		void			SendMovePacket(BYTE bFunc, BYTE bArg, DWORD x, DWORD y, DWORD dwDuration, DWORD dwTime=0, int iRot=-1);
		
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
		void			SendSupportSkillPacket(DWORD skill_vnum);
		DWORD			SupportGetNextExp() const;
#endif

// Check this:

		LPCHARACTER			GetHorse() const			{ return m_chHorse; }	 // ?? ???? ?
		LPCHARACTER			GetRider() const; // rider on horse
		void				SetRider(LPCHARACTER ch);

		bool				IsRiding() const;
		
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	public:
		CSupportSystem*			GetSupportSystem()				{ return m_supportSystem; }

	protected:
		CSupportSystem*			m_supportSystem;

	public:
#endif 

// Check this:

	public:
		void SetArmada() { cannot_dead = true; }
		void ResetArmada() { cannot_dead = false; }
	private:
		bool cannot_dead;
		
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	private:
		bool m_bIsSupport;
		LPCHARACTER m_Owner;
		DWORD m_dwSupportCostume;
		DWORD m_dwSupportHair;
		DWORD m_dwSupportWeapon;
		DWORD m_dwSupportInt;
	public:
		void SetSupport() { m_bIsSupport = true; }
		bool IsSupport() { return m_bIsSupport; }
		void SetSupportArmor(int vnum) { m_dwSupportCostume = vnum; }
		void SetSupportHair(int vnum) { m_dwSupportHair = vnum; }
		void SetSupportWeapon(int vnum) { m_dwSupportWeapon = vnum; }
		DWORD GetSupportArmor() { return m_dwSupportCostume; }
		DWORD GetSupportHair() { return m_dwSupportHair; }
		DWORD GetSupportWeapon() { return m_dwSupportWeapon; }
		void SetOwner(LPCHARACTER owner) { m_Owner = owner; }
		LPCHARACTER GetOwner() { return m_Owner; }
		void SetSupportInt(int count) { m_dwSupportInt = count; }
		DWORD GetSupportInt() { return m_dwSupportInt; }
#endif
