""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# def __LoadGameEffect(): Bulunur Ve ��erisinde : 
# chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+37, "", "d:/ymir work/effect/etc/guild_war_flag/flag_yellow.mse")
# Alt�na Eklenir :

	if app.ENABLE_GM_AFFECTS:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+42, "Bip01", localeInfo.FN_MOD_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+43, "Bip01", localeInfo.FN_SGM_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+44, "Bip01", localeInfo.FN_GA_MARK)
		
# E�er Ondan Evvel Ba�ka Bir Affect Eklediyseniz Affect kodlar�n� +1 artt�rarak ilerletin. �rne�in :
	
	if app.ENABLE_GM_AFFECTS:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+51, "Bip01", localeInfo.FN_MOD_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+52, "Bip01", localeInfo.FN_SGM_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+53, "Bip01", localeInfo.FN_GA_MARK)
		
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""