""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# def __LoadGameEffect(): Bulunur Ve Ýçerisinde : 
# chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+37, "", "d:/ymir work/effect/etc/guild_war_flag/flag_yellow.mse")
# Altýna Eklenir :

	if app.ENABLE_GM_AFFECTS:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+42, "Bip01", localeInfo.FN_MOD_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+43, "Bip01", localeInfo.FN_SGM_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+44, "Bip01", localeInfo.FN_GA_MARK)
		
# Eðer Ondan Evvel Baþka Bir Affect Eklediyseniz Affect kodlarýný +1 arttýrarak ilerletin. Örneðin :
	
	if app.ENABLE_GM_AFFECTS:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+51, "Bip01", localeInfo.FN_MOD_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+52, "Bip01", localeInfo.FN_SGM_MARK)
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+53, "Bip01", localeInfo.FN_GA_MARK)
		
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""