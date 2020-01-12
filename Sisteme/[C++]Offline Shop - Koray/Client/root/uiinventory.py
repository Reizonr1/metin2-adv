Search:
			self.dlgPickMoney.SetMax(7) # ÀÎº¥Åä¸® 990000 Á¦ÇÑ ¹ö±× ¼öÁ¤

Change:
			if app.ENABLE_OFFLINE_SHOP:
				self.dlgPickMoney.SetMax(11) # ÀÎº¥Åä¸® 990000 Á¦ÇÑ ¹ö±× ¼öÁ¤
			else:
				self.dlgPickMoney.SetMax(7) # ÀÎº¥Åä¸® 990000 Á¦ÇÑ ¹ö±× ¼öÁ¤


https://puu.sh/sgWV3/2337b0f975.png


Search:
			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

Change:
			itemPrice = player.GetISellItemPrice(itemSlotPos)



https://puu.sh/sgXaD/a572cad541.png

