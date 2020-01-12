#include "StdAfx.h"
#include "BetaShield_Starter.h"
#include <comutil.h>
#include <Windows.h>
#include <iostream>
#include <fstream>
#include <conio.h>
#include <ctime>
#include <stdlib.h>
#include <io.h>


using namespace std;

#pragma warning(disable:4172)
inline bool is_file_exist(const std::string& name) {
	std::ifstream infile(name.c_str());
	return infile.good();
}

__forceinline void __exit() {
	PostQuitMessage(0);
	TerminateProcess((HANDLE)-1, -1);

	CHAR __ntdlldll[] = { 'n', 't', 'd', 'l', 'l', '.', 'd', 'l', 'l', 0x0 }; // ntdll.dll
	CHAR __NtRaiseException[] = { 'N', 't', 'R', 'a', 'i', 's', 'e', 'E', 'x', 'c', 'e', 'p', 't', 'i', 'o', 'n', 0x0 }; //NtRaiseException
	DWORD adr = (DWORD)GetProcAddress(GetModuleHandleA(__ntdlldll), __NtRaiseException);
	__asm {
		mov ESP, 0
		jmp dword ptr adr
	};

	__asm {
		xor eax, eax
		leave
		ret
	}

	while (1) {}
}
__forceinline void close(const char* cArgFormat, ...) {
	char cTmpString[2000];
	CHAR _Filename[] = { 's', 'y', 's', 'e', 'r', 'r', '.', 't', 'x', 't', 0x0 };

	va_list vaArgList;
	va_start(vaArgList, cArgFormat);
	wvsprintfA(cTmpString, cArgFormat, vaArgList);
	va_end(vaArgList);

	time_t ct = time(0);
	struct tm ctm = *localtime(&ct);

	CHAR __timeformat[] = { '%', '0', '2', 'd', ':', '%', '0', '2', 'd', ':', '%', '0', '2', 'd', ' ', '-', ' ', '%', '0', '2', 'd', ':', '%', '0', '2', 'd', ':', '%', 'd', ' ', ':', ':', ' ', 0x0 }; // %02d:%02d:%02d - %02d:%02d:%d ::
	char cTimeBuf[1250];
	sprintf(cTimeBuf, __timeformat,
		ctm.tm_hour,
		ctm.tm_min,
		ctm.tm_sec,
		ctm.tm_mday,
		ctm.tm_mon + 1,
		1900 + ctm.tm_year);

	std::ofstream f(_Filename, std::ofstream::out | std::ofstream::app);
	f << cTimeBuf << cTmpString << '\n' << std::endl;
	f.close();

	__exit();
}


HMODULE hAntiModule;
void CBetaShield_Starter::Initialize(const char* c_szLicenseCode, char* cIpList[], int iIpCount, const char* c_szPatcherName) {
	CHAR __Filename[] = { 'B', 'e', 't', 'a', 'S', 'h', 'i', 'e', 'l', 'd', '/', '/', 'B', 'e', 't', 'a', 'C', 'o', 'r', 'e', '.', 'd', 'l', 'l', 0x0 }; // BetaShield//BetaCore.dll
	CHAR __Filenotfound[] = { 'A', 'n', 't', 'i', 'c', 'h', 'e', 'a', 't', ' ', 'f', 'i', 'l', 'e', ' ', 'd', 'o', 'e', 's', 'n', ' ', 't', ' ', 'f', 'o', 'u', 'n', 'd', 0x0 }; // Anticheat file doesn't found
	CHAR __LoadFail[] = { 'A', 'n', 't', 'i', 'c', 'h', 'e', 'a', 't', ' ', 'm', 'o', 'd', 'u', 'l', 'e', ' ', 'd', 'o', 'e', 's', 'n', ' ', 't', ' ', 'l', 'o', 'a', 'd', 'e', 'd', 0x0 }; // Anticheat module doesn't loaded
	CHAR __Apiname[] = { 'I', 'n', 'i', 't', 'i', 'a', 'l', 'i', 'z', 'e', 0x0 }; // Initialize
	CHAR __exportfail[] = { 'A', 'n', 't', 'i', 'c', 'h', 'e', 'a', 't', ' ', 'c', 'o', 'u', 'l', 'd', ' ', 'n', 'o', 't', ' ', 'l', 'o', 'c', 'a', 't', 'e', ' ', 't', 'h', 'e', ' ', 'I', 'n', 'i', 't', 'i', 'a', 'l', 'i', 'z', 'e', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', 0x0 }; // Anticheat could not locate the Initialize function

	if (!is_file_exist(__Filename))
		close(__Filenotfound);

	HMODULE hGetProcIDDLL = LoadLibraryA(__Filename);
	if (!hGetProcIDDLL)
		close(__LoadFail);
	hAntiModule = hGetProcIDDLL;

	typedef int(__cdecl* lpFuncition)(const char* c_szLicenseCode, char* r_cIpList[], int iIpCount, const char* c_szPatcherName, int x);
	lpFuncition DLL_Wrapper_Func = (lpFuncition)GetProcAddress(hGetProcIDDLL, __Apiname);
	if (!DLL_Wrapper_Func)
		close(__exportfail);

	DLL_Wrapper_Func(c_szLicenseCode, cIpList, iIpCount, c_szPatcherName, 1903);
}

#include "../EterPack/EterPackManager.h"
#include "PythonPlayer.h"
#include "PythonNetworkStream.h"

bool TRAMPOLINE_CEterPackManager_isExist(const char* c_szFileName){
	return CEterPackManager::Instance().isExist(c_szFileName);
}
const char* TRAMPOLINE_CPythonPlayer_GetName() {
	return CPythonPlayer::Instance().GetName();
}
DWORD TRAMPOLINE_GetHashFromMappedFile(const char* c_szFileName) {
	CMappedFile file;
	const void * pData = NULL;

	if (CEterPackManager::Instance().GetFromPack(file, c_szFileName, &pData))
		return GetCRC32((const char*)pData, file.Size());

	return -1;
}


void CBetaShield_Starter::ProcessTriggers() {
	CHAR __exportfail[] = { 'A', 'n', 't', 'i', 'c', 'h', 'e', 'a', 't', ' ', 'c', 'o', 'u', 'l', 'd', ' ', 'n', 'o', 't', ' ', 'l', 'o', 'c', 'a', 't', 'e', ' ', 't', 'h', 'e', ' ', 'I', 'n', 'i', 't', 'i', 'a', 'l', 'i', 'z', 'e', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', 0x0 }; // Anticheat could not locate the Initialize function
	CHAR __FunctionTrigger[] = { 'F', 'u', 'n', 'c', 't', 'i', 'o', 'n', 'T', 'r', 'i', 'g', 'g', 'e', 'r', 0x0 }; // FunctionTrigger

	typedef void(__cdecl* lpFuncition)(void * lpTarget, int iType);
	lpFuncition DLL_Wrapper_Func = (lpFuncition)GetProcAddress(hAntiModule, __FunctionTrigger);
	if (!DLL_Wrapper_Func)
		close(__exportfail);

	DLL_Wrapper_Func(&TraceError, 1);
	DLL_Wrapper_Func(&TRAMPOLINE_CEterPackManager_isExist, 2);
	DLL_Wrapper_Func(&TRAMPOLINE_CPythonPlayer_GetName, 3);
	DLL_Wrapper_Func(&TRAMPOLINE_GetHashFromMappedFile, 6);
}
