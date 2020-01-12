import dbg
import app
import net

import ui, wndMgr, linecache, chr, player

###################################################################################################
## Restart


class kolorDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "interfececolor.py")
		except Exception, msg:
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("kolorDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		try:
			self.zapiszn=self.GetChild("ok")
			self.domyslne=self.GetChild("no")
		except:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		self.interfacelist2= (self.GetChild("board").Corners[0],
							self.GetChild("board").Corners[1],
							self.GetChild("board").Corners[2],
							self.GetChild("board").Corners[3],
							self.GetChild("board").Lines[0],
							self.GetChild("board").Lines[1],
							self.GetChild("board").Lines[2],
							self.GetChild("board").Lines[3],
							self.GetChild("board").Base,
							self.GetChild("board").titleBar.imgLeft,
							self.GetChild("board").titleBar.imgCenter,
							self.GetChild("board").titleBar.imgRight,
		)
		self.GetChild("board").SetCloseEvent(self.Close)
		self.zapiszn.SetEvent(ui.__mem_func__(self.ok))
		self.domyslne.SetEvent(ui.__mem_func__(self.Restart))
		z = open('lib/color').readlines()
		self.GetChild("r").SetSliderPos(float(z[0]))
		self.GetChild("g").SetSliderPos(float(z[1]))
		self.GetChild("b").SetSliderPos(float(z[2]))
		self.GetChild("a").SetSliderPos((float(z[3])-0.5)*2)
		self.OnUpdate()

		return 1
	def ok(self):
		r = self.GetChild("r").GetSliderPos()
		g = self.GetChild("g").GetSliderPos()
		b = self.GetChild("b").GetSliderPos()
		a = self.GetChild("a").GetSliderPos()
		ui.zmiengrafike(r, g, b, (a/2)+0.5)
		i = player.GetTargetVID()
		#chr.testSetModulateRenderModeRGB(i, r, g, b)
		plik = open('lib/color', 'wb')
		plik.write(str(r)+"\n"+str(g)+"\n"+str(b)+"\n"+str((a/2)+0.5)+"\n")
		plik.close()
		pass
	def Restart(self):
		self.GetChild("r").SetSliderPos(1.0)
		self.GetChild("g").SetSliderPos(1.0)
		self.GetChild("b").SetSliderPos(1.0)
		self.GetChild("a").SetSliderPos(1.0)
		self.OnUpdate()
		pass
	def OnUpdate(self):
		r = self.GetChild("r").GetSliderPos()
		g = self.GetChild("g").GetSliderPos()
		b = self.GetChild("b").GetSliderPos()
		a = self.GetChild("a").GetSliderPos()
		for x in self.interfacelist2:
			wndMgr.SetDiffuseColor(x.hWnd, r, g, b, (a/2)+0.5)
		r = str(r*255).split('.')
		g = str(g*255).split('.')
		b = str(b*255).split('.')
		a = str(a*100).split('.')

		self.GetChild("rt").SetText(r[0])
		self.GetChild("gt").SetText(g[0])
		self.GetChild("bt").SetText(b[0])
		self.GetChild("at").SetText(a[0]+"%")

		pass
	def Destroy(self):
		self.restartHereButton=0
		self.restartTownButton=0

	def OpenDialog(self):
		if self.IsShow():
			self.Close()
		else:
			z = open('lib/color').readlines()
			self.GetChild("r").SetSliderPos(float(z[0]))
			self.GetChild("g").SetSliderPos(float(z[1]))
			self.GetChild("b").SetSliderPos(float(z[2]))
			self.GetChild("a").SetSliderPos((float(z[3])-0.5)*2)
			self.Show()

	def Close(self):
		self.Hide()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE

	def OnPressEscapeKey(self):
		#self.interfacelist2.Hide()
		self.Hide()
		self.Close()
		return TRUE
