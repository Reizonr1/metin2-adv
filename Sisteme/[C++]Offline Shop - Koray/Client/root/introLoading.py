Search:
		for name, rgb in NAME_COLOR_DICT.items():
			chrmgr.RegisterNameColor(name, rgb[0], rgb[1], rgb[2])

Add it upper:
		if app.ENABLE_OFFLINE_SHOP:
			NAME_COLOR_DICT.update({chrmgr.NAMECOLOR_OFFSHOP : colorInfo.CHR_NAME_RGB_SHOP })
			
https://puu.sh/sgY8e/5510780485.png
			