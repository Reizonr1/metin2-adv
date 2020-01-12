#1.) Search:
	def ResizeToolTip(self):
		self.SetSize(self.toolTipWidth, self.TOOL_TIP_HEIGHT + self.toolTipHeight)
#2.) Add after:
	if app.ENABLE_FEATURES_OXEVENT:
		def AppendPlayersDesc(self, name, level, guild, empire, job, date, correct_answers):

			def IsExistKey(name):
				return (job == localeInfo.OXEVENT_TOOLTIP_EMPTY)
				
			if not IsExistKey(job):
				self.ClearToolTip()

				itemImage = ui.ImageBox()
				itemImage.SetParent(self)
				itemImage.LoadImage(job)
				itemImage.SetPosition(itemImage.GetWidth()/2 + 50, self.toolTipHeight)
				itemImage.Show()

				self.mainDescription = [
					name,
					level,
					guild,
					empire,
					date,
					correct_answers
				]			
						
				self.AppendSpace(50)	
				for i in xrange(len(self.mainDescription)):
					self.AppendTextLine(self.mainDescription[i], self.SPECIAL_POSITIVE_COLOR)

				self.toolTipHeight += 16
				self.childrenList.append(itemImage)
				self.ResizeToolTip()
			else:
				self.HideToolTip()