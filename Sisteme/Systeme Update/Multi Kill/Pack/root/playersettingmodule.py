Search:
	EmoticonStr = "d:/ymir work/effect/etc/emoticon/"
	
Add it under:
	BuffStr = "d:/ymir work/effect/etc/buffnew/"

---
	
NOTE: If you have new emotions after fish change emotion numbers with +1
Search:
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+11, "", EmoticonStr+"fish.mse")
	net.RegisterEmoticonString("(fish)")

Add it under:	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+12, "", BuffStr+"1x_kill.mse")
	net.RegisterEmoticonString("(kill1)")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+13, "", BuffStr+"2x_kill.mse")
	net.RegisterEmoticonString("(kill2)")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+14, "", BuffStr+"3x_kill.mse")
	net.RegisterEmoticonString("(kill3)")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+15, "", BuffStr+"4x_kill.mse")
	net.RegisterEmoticonString("(kill4)")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+16, "", BuffStr+"5x_kill.mse")
	net.RegisterEmoticonString("(kill5)")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+17, "", BuffStr+"6x_kill.mse")
	net.RegisterEmoticonString("(kill6)")	
	