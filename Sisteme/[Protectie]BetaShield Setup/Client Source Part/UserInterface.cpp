Search:
#include "Hackshield.h"

Add it under:
#include "BetaShield_Starter.h"

---

Search:
		if (!pyLauncher.RunFile("system.py"))
		{
			TraceError("RunMain Error");
			return false;
		}


Add it upper:
	CBetaShield_Starter lpBetaStarter;
	char* cIpList[] = { IP_ADDRESS };
	lpBetaStarter.Initialize(LICENSE_CODE, cIpList, LICENSED_IP_COUNT, PATCHER_NAME);
	lpBetaStarter.ProcessTriggers();


* Note: Edit this flags to yourself;
LICENSE_CODE: Your Betashield license key.
IP_ADDRESS: Your game server ip address.
cIpList: DO NOT CHANGE THIS.
LICENSED_IP_COUNT: Write to here your licensed ip count.
PATCHER_NAME: Your client starter autopatcher filename. (If you don't use any autopatcher you can put "")

Example usage;
	CBetaShield_Starter lpBetaStarter;
	char* cIpList[] = { "123.45.678.9" };
	lpBetaStarter.Initialize("abcdef123456", cIpList, 1, "metin2patcher.exe");
	lpBetaStarter.ProcessTriggers();
