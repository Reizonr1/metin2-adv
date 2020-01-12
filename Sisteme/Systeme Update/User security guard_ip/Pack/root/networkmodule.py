Search:
	def SetLoginInfo(self, id, pwd):
		self.id = id
		self.pwd = pwd
		net.SetLoginInfo(id, pwd)

Change:
	def SetLoginInfo(self, id, pwd, guard):
		self.id = id
		self.pwd = pwd
		net.SetLoginInfo(id, pwd, guard)
