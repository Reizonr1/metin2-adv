# Search def HideAllWindows(self): and replace

		if self.wndCharacter:
			self.wndCharacter.Hide()

# with

		if self.wndCharacter:
			self.wndCharacter.Close()

# Search if state == self.wndCharacter.GetState(): and replace

		self.wndCharacter.Hide()

# with

		self.wndCharacter.Close()