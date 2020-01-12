##1.0 suchen:	
	## 34 Polymoph
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+35, "", "d:/ymir work/effect/etc/guild_war_flag/flag_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+36, "", "d:/ymir work/effect/etc/guild_war_flag/flag_blue.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+37, "", "d:/ymir work/effect/etc/guild_war_flag/flag_yellow.mse")
##1.0 dahinter:	
	if app.ENABLE_VIP_SYSTEM:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+45, "Bip01", "locale/de/effect/vip.mse")
		