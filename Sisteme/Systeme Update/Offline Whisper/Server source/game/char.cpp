Search:
#include "buff_on_attributes.h"

Add it under:
#ifdef OFFLINE_MESSAGE
#include "fstream"
#endif

---

Search:
int	CHARACTER::GetSkillPowerByLevel(int level, bool bMob) const
{
	return CTableBySkill::instance().GetSkillPowerByLevelFromType(GetJob(), GetSkillGroup(), MINMAX(0, level, SKILL_MAX_LEVEL), bMob);
}

Add it under:
#ifdef OFFLINE_MESSAGE
static bool file_is_empty(std::ifstream& pFile)
{
	return pFile.peek() == std::ifstream::traits_type::eof();
}

void CHARACTER::SaveOfflineMessage(const char* szMsg, DWORD dwTargetPID)
{
	// create filename
	char szFileName[500];
	sprintf(szFileName, "%s/quest/game_api/off_msg/%u.txt", LocaleService_GetBasePath().c_str(), dwTargetPID);

	// open target file
	FILE *fp = 0;
	fp = fopen(szFileName, "a");

	if (0 == fp){
		sys_err("File: %s couldn't readed", szFileName);
		return;
	}

	std::ifstream fFile(szFileName);
	if (!fFile.is_open()){
		sys_err("File: %s couldn't opened", szFileName);
		return;
	}

	// write offline msg
	if (file_is_empty(fFile))
		fprintf(fp, "%s", szMsg);
	else
		fprintf(fp, "\n%s", szMsg);

	// close target file
	fclose(fp);
	fFile.close();

	// log
	if (test_server)
		sys_log(0, "%s writed to %s file", szMsg, szFileName);
}

void CHARACTER::ClearOfflineMessageBox(DWORD dwTargetPID)
{
	// create filename
	char szFileName[500];
	sprintf(szFileName, "%s/quest/game_api/off_msg/%u.txt", LocaleService_GetBasePath().c_str(), dwTargetPID);

	// open target file
	FILE *fp = 0;
	fp = fopen(szFileName, "w");

	if (0 == fp){
		sys_err("File: %s couldn't readed", szFileName);
		return;
	}

	// write offline msg
	fprintf(fp, "");

	// close target file
	fclose(fp);

	// log
	if (test_server)
		sys_log(0, "cleaned offline messagebox file: %s", szFileName);
}


void CHARACTER::ReadOfflineMessageBox()
{
	// create filename
	char szFileName[500];
	sprintf(szFileName, "%s/quest/game_api/off_msg/%u.txt", LocaleService_GetBasePath().c_str(), GetPlayerID());

	// reader
	int i = 0;
	std::string tmpString;
	std::ifstream File(szFileName);

	if (!File.is_open())
	{
		if (test_server)
			sys_log(0, "WARNING: cannot open %s", szFileName);
		return;
	}

	if (file_is_empty(File))
	{
		if (test_server)
			sys_log(0, "WARNING: file %s is empty", szFileName);
		return;
	}

	while (!File.eof())
	{
		File >> tmpString;
		ChatPacket(CHAT_TYPE_COMMAND, "OFFMSG %s", tmpString.c_str());
	}

	File.close();
}
#endif
