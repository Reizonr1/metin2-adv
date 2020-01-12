// Suche :
#include "MarkManager.h"
// Füge darunter das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
#include "Colors.h"

#define PRESTIGECOLOR MSG_COLOR_BLUE
#endif
// Suche : 
void CPythonTextTail::AttachLevel(DWORD dwVID, const char * c_szText, const D3DXCOLOR & c_rColor)
// Ersetze die ganze Funktion mit : 
void CPythonTextTail::AttachLevel(DWORD dwVID, const char * c_szText, const D3DXCOLOR & c_rColor)
{
	CInstanceBase * pCharacterInstance = CPythonCharacterManager::Instance().GetInstancePtr(dwVID);
	if (!pCharacterInstance)
		return;

	if (!bPKTitleEnable)
		return;

	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;

	TTextTail * pTextTail = itor->second;

	CGraphicTextInstance *& prLevel = pTextTail->pLevelTextInstance;
	if (!prLevel)
	{
		prLevel = CGraphicTextInstance::New();
		prLevel->SetTextPointer(ms_pFont);
		prLevel->SetOutline(true);

		prLevel->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_RIGHT);
		prLevel->SetVerticalAlign(CGraphicTextInstance::VERTICAL_ALIGN_BOTTOM);
	}
#if ENABLE_NEW_PRESTIGE_SYSTEM == 2
	if (pCharacterInstance->IsPC() && pCharacterInstance->GetPrestigeLevel())
	{
		char szPrestige[500 + 1];
		if (bPrestige < PRESTIGE_MAX)
			snprintf(szPrestige, sizeof(szPrestige), "[Prestige%d] %s", pCharacterInstance->GetPrestigeLevel(), c_szText);
		else
			snprintf(szPrestige, sizeof(szPrestige), "[Prestige Master] %s",c_szText);

		const char * c_szNewText = szPrestige;
		prLevel->SetValue(c_szNewText);
	}
	else
		prLevel->SetValue(c_szText);
#else
	prLevel->SetValue(c_szText);
#endif

	prLevel->SetColor(c_rColor.r, c_rColor.g, c_rColor.b);
	prLevel->Update();
}

// Suche :
void CPythonTextTail::RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight)
// Ersete das mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
void CPythonTextTail::RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight, BYTE bPrestige)
#else
void CPythonTextTail::RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight)
#endif

// Ersetze das :
	TTextTail * pTextTail = RegisterTextTail(dwVirtualID,
		pCharacterInstance->GetNameString(),
		pCharacterInstance->GetGraphicThingInstancePtr(),
		pCharacterInstance->GetGraphicThingInstanceRef().GetHeight() + fAddHeight,
		c_rColor);
	
// Mit :

#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
	char szNameTextTail[5000 + 1];

	if (pCharacterInstance->IsPC() && bPrestige)
	{
		if (bPrestige < PRESTIGE_MAX)
			snprintf(szNameTextTail, sizeof(szNameTextTail), "[Prestige%d]%s", bPrestige, pCharacterInstance->GetNameString());
		else
			snprintf(szNameTextTail, sizeof(szNameTextTail), "[Prestige Master]%s", pCharacterInstance->GetNameString());
	}
	else
		snprintf(szNameTextTail, sizeof(szNameTextTail), "%s", pCharacterInstance->GetNameString());

	TTextTail * pTextTail = RegisterTextTail(dwVirtualID,
		szNameTextTail,
		pCharacterInstance->GetGraphicThingInstancePtr(),
		pCharacterInstance->GetGraphicThingInstanceRef().GetHeight() + fAddHeight,
		c_rColor);

#else
	TTextTail * pTextTail = RegisterTextTail(dwVirtualID,
		pCharacterInstance->GetNameString(),
		pCharacterInstance->GetGraphicThingInstancePtr(),
		pCharacterInstance->GetGraphicThingInstanceRef().GetHeight() + fAddHeight,
		c_rColor);
#endif

// Suche :

void CPythonTextTail::AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor)

// Ersetze die ganze Funktion mit :

#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
void CPythonTextTail::AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor, BYTE bPrestige)
#else
void CPythonTextTail::AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor)
#endif
{
	if (!bPKTitleEnable)
		return;


	TTextTailMap::iterator itor = m_CharacterTextTailMap.find(dwVID);
	if (m_CharacterTextTailMap.end() == itor)
		return;

	TTextTail * pTextTail = itor->second;

	CGraphicTextInstance *& prTitle = pTextTail->pTitleTextInstance;
	if (!prTitle)
	{
		prTitle = CGraphicTextInstance::New();
		prTitle->SetTextPointer(ms_pFont);
		prTitle->SetOutline(true);

		if (LocaleService_IsEUROPE())
			prTitle->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_RIGHT);
		else
			prTitle->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_CENTER);
		prTitle->SetVerticalAlign(CGraphicTextInstance::VERTICAL_ALIGN_BOTTOM);
	}
#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
	std::string s_Prestige = "";
	const char * c_szEmpty = "";
	if (c_szName != c_szEmpty)
	{
		s_Prestige = " ";
		s_Prestige += c_szName;
	}

	if (bPrestige > 0)
	{
		char szColor[50 + 1];
		if (c_szName != c_szEmpty)
			snprintf(szColor, sizeof(szColor), " %s[", PRESTIGECOLOR);
		else
			snprintf(szColor, sizeof(szColor), "%s[", PRESTIGECOLOR);

		s_Prestige += szColor;
		if (bPrestige < PRESTIGE_MAX)
		{
			char szText[256];
			sprintf(szText, "Prestige %d", bPrestige);
			s_Prestige += szText;
		}
		else
			s_Prestige += "Prestige Master";
		
		s_Prestige += "]";
	}
	prTitle->SetValue(s_Prestige.c_str());
#else
	prTitle->SetValue(c_szName);
#endif
	prTitle->SetColor(c_rColor.r, c_rColor.g, c_rColor.b);
	prTitle->Update();
}