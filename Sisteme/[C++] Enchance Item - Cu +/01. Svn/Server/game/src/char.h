// 1) Search: int	GetSyncHackCount() { return m_iSyncHackCount; }
// 2) After this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
	private:
		DWORD	dw_EnchantAttr;
		BYTE	newEnchant_type1, newEnchant_type2, newEnchant_type3, newEnchant_type4, newEnchant_type5;
		int		newEnchant_value1, newEnchant_value2, newEnchant_value3, newEnchant_value4, newEnchant_value5;
	public:
		DWORD	GetEnchantAttr() {return dw_EnchantAttr;}
		void	SetEnchantAttr(DWORD dwValue) {dw_EnchantAttr = dwValue;}
		void	PrepareEnchantAttr(int iAttribute, int iIdx, int iVal);
		int		GetEnchantType1() {return newEnchant_type1;}
		int		GetEnchantValue1() {return newEnchant_value1;}
		int		GetEnchantType2() {return newEnchant_type2;}
		int		GetEnchantValue2() {return newEnchant_value2;}
		int		GetEnchantType3() {return newEnchant_type3;}
		int		GetEnchantValue3() {return newEnchant_value3;}
		int		GetEnchantType4() {return newEnchant_type4;}
		int		GetEnchantValue4() {return newEnchant_value4;}
		int		GetEnchantType5() {return newEnchant_type5;}
		int		GetEnchantValue5() {return newEnchant_value5;}
#endif