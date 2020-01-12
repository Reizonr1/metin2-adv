### GUIA ###

#--- ***** game.py:

import uiHabilidades


		self.habis = uiHabilidades.Habilidades()
		self.habis.Close()
		

			# HABILIDADES
			"HABILIDADES"			: self.__Habilidades,
			# END_OF_HABILIDADES
			
			
	### HABILIDADES ###
	
	def __Habilidades(self, cmd):
		shang = cmd.split("|")
		if shang[0] == "RAZA":
			self.habis.Open(int(shang[1]))
		elif shang[0] == "GRUPO":
			net.SendQuestInputStringPacket(str(constInfo.Habilidades["HABSTR"]))
			constInfo.Habilidades["HABSTR"] = ""
		elif shang[0] == "QID":
			constInfo.Habilidades["qid"] = int(shang[1])
		
	### END_HABILIDADES ###
	
#--- ***** constInfo.py:

Habilidades = {
	"HABSTR" : "",
	"qid" : 0,
}