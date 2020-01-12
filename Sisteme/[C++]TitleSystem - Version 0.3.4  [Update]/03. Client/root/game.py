#.1.) Search:
		self.affectShower = uiAffectShower.AffectShower()
#2.) Add bellow:
		if app.ENABLE_TITLE_SYSTEM:
			import title_system
			self.wndTitleSystem = title_system.Title_System()
""""""""""""""""""""""""""""""""""""""""""
#.1.) Search:	
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
#2.) Add bellow:
		if app.ENABLE_TITLE_SYSTEM:	
			onPressKeyDict[app.DIK_F5]		= lambda : self.OpenTitleSystem()
""""""""""""""""""""""""""""""""""""""""""
#.1.) Search:	
	def	__ReleaseGKey(self):
		app.PitchCamera(app.CAMERA_STOP)
#2.) Add bellow:	
	if app.ENABLE_TITLE_SYSTEM:	
		def OpenTitleSystem(self):		
			self.wndTitleSystem.OpenWindow()
""""""""""""""""""""""""""""""""""""""""""	
#.1.) Search:	
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None
#2.) Add bellow:
		if app.ENABLE_TITLE_SYSTEM:			
			self.wndTitleSystem.Close()
""""""""""""""""""""""""""""""""""""""""""		
#.1.) Search:			
	def OnUpdate(self):		
		app.UpdateGame()
#2.) Add bellow:	
		if app.ENABLE_TITLE_SYSTEM:		
			self.wndTitleSystem.OnUpdate()	
""""""""""""""""""""""""""""""""""""""""""