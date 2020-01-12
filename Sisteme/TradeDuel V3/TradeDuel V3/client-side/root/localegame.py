import app
import constInfo
import serverInfo

class Game_Fatihbab34:
	__IS_TURKCE = "1"
	if __IS_TURKCE:
		__IS_TURKCE = TRUE
	
	if 12580>15477:
		print"is Updating..."

class Game_Test:
	print"--------------------------------------- GAME ~ PRINT"

__IS_TURKCE		= "TURKCE" == app.GetLocaleServiceName()
__IS_ENGLISH	= "ENGLISH" == app.GetLocaleServiceName()
__IS_EUROPE		= "EUROPE" == app.GetLocaleServiceName()		
__IS_CANADA		= "locale/ca" == app.GetLocalePath()

if __IS_CANADA:
	__IS_EUROPE = TRUE

def SNA(text):	
	def f(x):
		return text
	return f

def SA(text):
	def f(x):
		return text % x
	return f

def LoadLocaleFile(gelenDosya, kelime):

	funcDict = {"SA":SA, "SNA":SNA}

	yer = 1

	try:
		ac = pack_open(gelenDosya, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("Beklenmeyen Hata(%(gelenDosya)s)" % locals())
		app.Abort()

	for i in ac:
		try:		
			tokens = i[:-1].split("\t")
			if len(tokens) == 2:
				kelime[tokens[0]] = tokens[1]		
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					kelime[tokens[0]] = funcDict[type](tokens[1])
				else:
					kelime[tokens[0]] = tokens[1]
			else:
				raise RuntimeError, "Belirsiz Token kodu tespit edildi!"

			yer += 1
		except:
			import dbg
			dbg.LogBox("%s: Bulunan Satır(%d): %s" % (gelenDosya, yer, i), "localegame[game.txt]")
			raise

def GetTimeModule(time): #app.GetGlobalTimeStamp()
    d, s = divmod(time, 60)
    ss, d = divmod(d, 60)
    return "%02d:%02d" % (d, s)

def GetTimeModuleEx(time):
    d, s2 = divmod(time, 10)
    ss2, d = divmod(d, 10)
    return "%d" % (s2)

def GetAuxiliaryWordType(text):

	textLength = len(text)

	if textLength > 1:

		singleWord = text[-1]

		if (singleWord >= '0' and singleWord <= '9') or\
			(singleWord >= 'a' and singleWord <= 'z') or\
			(singleWord >= 'A' and singleWord <= 'Z'):
			if not dictSingleWord.has_key(singleWord):
				return 1

		elif dictDoubleWord.has_key(text[-2:]):
			return 1

	return 0



def CutMoneyString(sourceText, startIndex, endIndex, insertingText, backText):

	sourceLength = len(sourceText)

	if sourceLength < startIndex:
		return backText

	text = sourceText[max(0, sourceLength-endIndex):sourceLength-startIndex]

	if not text:
		return backText

	if int(text) <= 0:
		return backText

	text = str(int(text))

	if backText:
		backText = " " + backText

	return text + insertingText + backText

def SecondToDHM(time):

	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + DAY
		text += " "

	if hour > 0:
		text += str(hour) + HOUR
		text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToHM(time):

	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

LOGOM = "locale/turkey/fatihbab34/ingamesrc/test.mse"
LOCALE_FILE_NAME = "%s/game.txt" % app.GetLocalePath()
constInfo.IN_GAME_SHOP_ENABLE = 0

LoadLocaleFile(LOCALE_FILE_NAME, locals())
