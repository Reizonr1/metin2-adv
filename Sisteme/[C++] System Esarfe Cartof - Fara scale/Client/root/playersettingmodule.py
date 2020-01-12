""""""
#1) Search: chrmgr.RegisterCacheEffect(chrmgr.EFFECT_LOVE_PENDANT_EQUIP, "", "d:/ymir work/effect/etc/buff/buff_item4.mse")
#2) Make a new line and paste:
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_SUCCEDED_1, "", "d:/ymir work/effect/etc/buff/buff_item6.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_EQUIP_ACCE_1, "", "d:/ymir work/effect/etc/buff/buff_item7.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_EQUIP_ACCE_2, "", "d:/ymir work/effect/etc/buff/buff_item7.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_EQUIP_ACCE_3, "", "d:/ymir work/effect/etc/buff/buff_item7.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_EQUIP_ACCE_4, "", "d:/ymir work/effect/etc/buff/buff_item7.mse")
""""""

""""""
#1) Search: chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+20, "Bip01", "D:/ymir work/pc/common/effect/armor/armor-4-2-2.mse")
#2) Make a new line and paste:
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+21, "PART_ACCE", "D:/ymir work/pc/common/effect/sword/sword_9_b.mse")
""""""

""""""
#1) Search: chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right_hand")
#2) Make a new line and paste:
	chrmgr.RegisterAttachingBoneName(chr.PART_ACCE, "Bip01 Head")
""""""

""""""
#1) Search: chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left")
#2) Make a new line and paste:
	chrmgr.RegisterAttachingBoneName(chr.PART_ACCE, "Bip01 Head")
""""""

""""""
#1) Search: chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right")
#2) Make a new line and paste:
	chrmgr.RegisterAttachingBoneName(chr.PART_ACCE, "Bip01 Head")
""""""

""""""
#1) Search: chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left")
#2) Make a new line and paste:
	chrmgr.RegisterAttachingBoneName(chr.PART_ACCE, "Bip01 Head")
""""""

""""""
#1) Search: chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left_weapon")
#2) Make a new line and paste:
	chrmgr.RegisterAttachingBoneName(chr.PART_ACCE, "Bip01 Head")
""""""