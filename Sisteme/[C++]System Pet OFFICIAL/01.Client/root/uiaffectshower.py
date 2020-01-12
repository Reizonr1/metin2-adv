#Search :
	if app.ENABLE_DRAGON_SOUL_SYSTEM:
		# ¿ëÈ¥¼® Ãµ, Áö µ¦.
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK1] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK1, "d:/ymir work/ui/dragonsoul/buff_ds_sky1.tga")
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK2] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK2, "d:/ymir work/ui/dragonsoul/buff_ds_land1.tga")

#Add After:
	AFFECT_PET_DATA_DICT ={
		5401 : ("Rezistenta (Razboinic)", "d:/ymir work/ui/skill/pet/jijoong.sub"),
		5402 : ("Rezistenta (Sura)", "d:/ymir work/ui/skill/pet/jijoong.sub"),
		5403 : ("Rezistenta (Ninja)", "d:/ymir work/ui/skill/pet/jijoong.sub"),
		5404 : ("Rezistenta (Saman)", "d:/ymir work/ui/skill/pet/jijoong.sub"),
		5405 : ("Rezistenta (Lycan)", "d:/ymir work/ui/skill/pet/jijoong.sub"),
		5406 : ("Berserker", "d:/ymir work/ui/skill/pet/pacheon.sub"),
		5407 : ("Anti-Magie", "d:/ymir work/ui/skill/pet/cheonryeong.sub"),
		5408 : ("Graba", "d:/ymir work/ui/skill/pet/banya.sub"),
		5409 : ("Antrenament", "d:/ymir work/ui/skill/pet/choehoenbimu.sub"),
		5410 : ("Restaurare", "d:/ymir work/ui/skill/pet/heal.sub"),
		5411 : ("Vampirism", "d:/ymir work/ui/skill/pet/stealhp.sub"),
		5412 : ("Spiritism", "d:/ymir work/ui/skill/pet/stealmp.sub"),
		5413 : ("Obstructie", "d:/ymir work/ui/skill/pet/block.sub"),
		5414 : ("Reflexie", "d:/ymir work/ui/skill/pet/reflect_melee.sub"),
		5415 : ("Drop Yang", "d:/ymir work/ui/skill/pet/gold_drop.sub"),
		5416 : ("Distanta", "d:/ymir work/ui/skill/pet/bow_distance.sub"),
		5417 : ("Imortalitate", "d:/ymir work/ui/skill/pet/invincibility.sub"),
		5418 : ("Remediu", "d:/ymir work/ui/skill/pet/removal.sub"),
	}
	
#Search:
		if not self.AFFECT_DATA_DICT.has_key(affect):
			return

#Replace With:

		if not self.AFFECT_DATA_DICT.has_key(affect) and not self.AFFECT_PET_DATA_DICT.has_key(affect):
			return

#Search:
		affectData = self.AFFECT_DATA_DICT[affect]

#Replace Wich:

		if affect >= 5400 and affect <= 5419:
			affectData = self.AFFECT_PET_DATA_DICT[affect]
		else:
			affectData = self.AFFECT_DATA_DICT[affect]

#Search:
			if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:

#Replace Wtih:
			if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY and not self.AFFECT_PET_DATA_DICT.has_key(affect):
