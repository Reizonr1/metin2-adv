#pragma once

class CBetaShield_Starter {
	public:
		void Initialize(const char* c_szLicenseCode, char* cIpList[], int iIpCount, const char* c_szPatcherName);
		void ProcessTriggers();
};
