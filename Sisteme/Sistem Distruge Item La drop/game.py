"ITEMZER"				: self.itemselectzer,





cauta                 dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

constInfo.itemzerst["select"] = ""
constInfo.itemzerst["select"] = "DELETE|"+str(attachedItemSlotPos)+"|"+str(attachedItemIndex)

cauta                     ##Dialog

itemDropQuestionDialog = uiCommon.QuestionDialogItem()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetDestroyEvent(lambda arg=True: self.DestroyItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog
				
				
cauta                       dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)





## Dialog
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetDestroyEvent(lambda arg=True: self.DestroyItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog
				
				
sfârºit game.py


	def itemselectzer(self, cmd):
		cmd = cmd.split("|")
		if cmd[0] == "QID":
			constInfo.itemzerst["QID"] = int(cmd[1])
		elif cmd[0] == "SELECT":
			net.SendQuestInputStringPacket(str(constInfo.itemzerst["select"]))
			constInfo.itemzerst["select"] = ""

	def DestroyItem(self, arg):
		if arg:
			event.QuestButtonClick(constInfo.itemzerst["QID"])
		# self.RemoveQuestion.Close()
		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)















