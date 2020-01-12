#Search :

				else:					
					self.wndItem.SetUseMode(False)

				snd.PlaySound("sound/ui/pick.wav")

#ADd After:
				
	def UseTransportBox(self):
		self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
		self.OnCloseQuestionDialog()
	
	def UseProtein(self):
		self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
		self.OnCloseQuestionDialog()
		
#Search:
	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if srcItemSlotPos == dstItemSlotPos:
			return

#Add After:

		if srcItemVID >= 55701 and srcItemVID <= 55704 and player.GetItemIndex(dstItemSlotPos) == 55002:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Vrei sa adaugi insotitorul in cutia de transport?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseTransportBox))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
			
		if srcItemVID == 55001 and player.GetItemIndex(dstItemSlotPos) >= 55701 and player.GetItemIndex(dstItemSlotPos) <= 55704:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Vrei sa hranesti insotitorul?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseProtein))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
					
#Search:
	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		"다른 아이템에 사용할 수 있는 아이템인가?"

#ADD AFTER:
		
		if srcItemVNum >= 55701 and srcItemVNum <= 55704:
			return True
		
		if srcItemVNum == 55001:
			return True
#Search
	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		"대상 아이템에 사용할 수 있는가?"

		if srcSlotPos == dstSlotPos:
			return False

#ADD After:
		if srcItemVNum >= 55701 and  srcItemVNum <= 55704 and player.GetItemIndex(dstSlotPos) == 55002:			
			return True		
		
		if srcItemVNum == 55001 and player.GetItemIndex(dstSlotPos) >= 55701 and player.GetItemIndex(dstSlotPos) <= 55704:			
			return True


