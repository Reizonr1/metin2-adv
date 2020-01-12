####Find all functions and make changes like this

	def __init__(self, stream):
		[..]
		
		self.uiNewShopCreate = None
		self.uiNewShop = None
		
		
	def OnRender(self):
		[..]
#Search: self.PickingItemIndex = textTail.Pick(x, y)
#After this make a new line and paste:
		if systemSetting.IsShowSalesText():
			uiPrivateShopBuilder.UpdateADBoard()

	def Open(self):
		[..]
		
		import uiNewShop
		self.uiNewShop = uiNewShop.ShopDialog()
		self.uiNewShop.Close()
		self.uiNewShopCreate = uiNewShop.ShopDialogCreate()
		self.uiNewShopCreate.Hide()
		
	def Close(self):
		[..]
		self.uiNewShop.Hide()
		self.uiNewShopCreate.Hide()
		uiPrivateShopBuilder.Clear()
	
	## PrivateShop
	def __PrivateShop_Open(self):
		#self.interface.OpenPrivateShopInputNameDialog()
		self.uiNewShop.Show()

	def BINARY_PrivateShop_Appear(self, vid, text):
		if chr.GetInstanceType(vid) in [chr.INSTANCE_TYPE_PLAYER, chr.INSTANCE_TYPE_NPC]:
			self.interface.AppearPrivateShop(vid, text)

	## BINARY CALLBACK
	######################################################################################

	def __ServerCommand_Build(self):
		serverCommandList = {
		[..]
			
			##NEW SHOP
			"shop"		:self.NewShop,
			"shop_clear"		:self.ShopClear,
			"shop_add"		:self.ShopAdd,
			"shop_item"		:self.ShopItem,
			"shop_cost"		:self.ShopCost,
			"shop_cost_clear"		:self.ShopCostClear,
			"shop_item_clear"	:self.ShopItemClear,
			
			#####GIFT SYSTEM
			"gift_clear"		:self.gift_clear,
			"gift_item"		:self.gift_item,
			"gift_info"		:self.gift_show,
			"gift_load"		:self.gift_load,
			###
		}
		
		####SHOP SYSTEM#####
	def NewShop(self):
		if self.uiNewShop:
			self.uiNewShop.Show()
	
	def ShopClear(self):
		if self.uiNewShop:
			self.uiNewShop.HideAll()
		constInfo.MyShops=[]
	def ShopCostClear(self):
		constInfo.shop_cost=[]
	def ShopCost(self,id,time,time_val,price):
		constInfo.shop_cost.append({"id":int(id),"time":int(time),"time_val":int(time_val),"price":int(price)})
	def ShopAdd(self,shop_id,shop_vid,szSign,gold,count,sold,days,date_close):
		if self.uiNewShop:
			shop={
				"id":shop_id,
				"vid":shop_vid,
				"name":szSign.replace("\\"," ").replace("_","#"),
				"gold":gold,
				"sold":sold,
				"items":int(count)-int(sold),
				"days":days,
				"time":date_close
			}
			self.uiNewShop.Load(shop)
			constInfo.MyShops.append(shop)
	def ShopItemClear(self):
		if self.uiNewShop:
			self.uiNewShop.ClearItems()
	def ShopItem(self,data):
		d=data.split("#")
		id=d[0]
		vnum=d[1]
		count=d[2]
		slot=d[3]
		price=d[4]
		s=d[5]
		a=d[6]
		sockets=[]
		for key in s.split("|"):
			sockets.append(int(key))
	
		attrs=[]
		for key in a.split("|"):
			a=key.split(",")
			attrs.append([int(a[0]),int(a[1])])
		if self.uiNewShop:
			self.uiNewShop.AddItem(slot,{"id":id,"vnum":vnum,"count":count,"price":price,"sockets":sockets,"attrs":attrs})
		
	####GIFT SYSTEM#####
	def gift_clear(self):
		constInfo.gift_items={}
		self.interface.ClearGift()
	def gift_item(self, id, vnum, count, pos, date_add, give, reason, szSockets, szAttrs):
		sockets=[]
		for key in szSockets.split("|"):
			sockets.append(int(key))
	 
		attrs=[]
		for key in szAttrs.split("|"):
			a=key.split(",")
			attrs.append([int(a[0]),int(a[1])])
		constInfo.gift_items[int(pos)]={"id":int(id),"vnum":int(vnum),"count":int(count),"pos":int(pos),"date_add":int(date_add),"reason":reason.replace("_"," "),"give":give.replace("_"," "),"sockets":sockets,"attrs":attrs}
	def gift_load(self):
		self.interface.wndGiftBox.Refresh()
	def gift_show(self,pages):
		self.interface.wndGiftBox.pageNum=int(pages)
		self.interface.OpenGift()	
		
[..]