###########################################################
#					   WikiBoard by .Kori				  #
###########################################################
import player
import app
lastupdate = 0
Funkton = 0
VIP = 0
	
Wiki1 = []
Wiki1.append("Name:" + " " + player.GetName() + "#")
Wiki1.append("Level:" + str(player.GetStatus(player.LEVEL)) + "#")
Wiki1.append("Aktuelle Spielzeit:" + " " + str(player.GetPlayTime()) + "" +"Minuten#")

News = []
News.append("Last Update: 24.06.2014#")
News.append("Login-Interface Fertiggestellt#")
News.append("Character-Select Fertiggestellt#")
News.append("Neue Items Eingef�gt:				Biologen Items#")
News.append("											Waffen & R�stungen#")
News.append("#")
News.append("#")
News.append("Mit Freundlichen Gr��en das Age of Platon Team.#")