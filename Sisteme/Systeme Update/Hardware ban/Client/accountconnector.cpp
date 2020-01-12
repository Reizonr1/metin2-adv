Find:
#include "../EterPack/EterPackManager.h"

Add it under:
#include <intrin.h>
#include <Iphlpapi.h>
#pragma comment(lib, "iphlpapi.lib")

---

Find:
bool CAccountConnector::__AuthState_RecvEmpty()
{
	BYTE byEmpty;
	Recv(sizeof(BYTE), &byEmpty);
	return true;
}

Add it under:
const char* GetMacAddress(){
	PIP_ADAPTER_INFO AdapterInfo;
	DWORD dwBufLen = sizeof(AdapterInfo);
	char *mac_addr = (char*)malloc(17);

	AdapterInfo = (IP_ADAPTER_INFO *)malloc(sizeof(IP_ADAPTER_INFO));
	if (!AdapterInfo) {
		//printf("Error allocating memory needed to call GetAdaptersinfo\n");
		return "";
	}

	// Make an initial call to GetAdaptersInfo to get the necessary size into the dwBufLen     variable
	if (GetAdaptersInfo(AdapterInfo, &dwBufLen) == ERROR_BUFFER_OVERFLOW) {

		AdapterInfo = (IP_ADAPTER_INFO *)malloc(dwBufLen);
		if (!AdapterInfo) {
			//printf("Error allocating memory needed to call GetAdaptersinfo\n");
			return "";
		}
	}

	CHAR _MACFORMAT[] = { '%', '0', '2', 'X', ':', '%', '0', '2', 'X', ':', '%', '0', '2', 'X', ':', '%', '0', '2', 'X', ':', '%', '0', '2', 'X', ':', '%', '0', '2', 'X', 0x0 }; //"%02X:%02X:%02X:%02X:%02X:%02X"
	if (GetAdaptersInfo(AdapterInfo, &dwBufLen) == NO_ERROR) {
		PIP_ADAPTER_INFO pAdapterInfo = AdapterInfo;// Contains pointer to current adapter info
		do {
			sprintf(mac_addr, _MACFORMAT,
				pAdapterInfo->Address[0], pAdapterInfo->Address[1],
				pAdapterInfo->Address[2], pAdapterInfo->Address[3],
				pAdapterInfo->Address[4], pAdapterInfo->Address[5]);
			return mac_addr;

			pAdapterInfo = pAdapterInfo->Next;
		} while (pAdapterInfo);
	}
	free(AdapterInfo);
}

---

Find:
strncpy(LoginPacket.pwd, m_strPassword.c_str(), PASS_MAX_NUM);

Add it under:
strncpy(LoginPacket.cHWInfo, GetMacAddress(), sizeof(LoginPacket.cHWInfo) - 1);

---

Find:
LoginPacket.pwd[PASS_MAX_NUM] = '\0';

Add it under:
LoginPacket.cHWInfo[255] = '\0';
