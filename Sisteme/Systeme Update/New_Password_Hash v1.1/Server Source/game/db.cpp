Search:
#include "auth_brazil.h"

Add it under:
#include "cryptopp/sha.h"
#include "cryptopp/filters.h"
#include "cryptopp/hex.h"
#include "boost/algorithm/string.hpp"



Search:
void DBManager::AnalyzeReturnQuery(SQLMsg * pMsg)


Find:
[...]
					case QID_AUTH_LOGIN:
[...]
						sys_log(0, "QID_AUTH_LOGIN: SUCCESS %s", pinfo->login);
					}
				}
			}
			break;
[...]
Change:
		case QID_AUTH_LOGIN:
			{
				TPacketCGLogin3 * pinfo = (TPacketCGLogin3 *) qi->pvData;
				LPDESC d = DESC_MANAGER::instance().FindByLoginKey(qi->dwIdent);

				if (!d) {
					M2_DELETE(pinfo);
					break;
				}
				d->SetLogin(pinfo->login);

				sys_log(0, "QID_AUTH_LOGIN: START %u %p", qi->dwIdent, get_pointer(d));

				if (pMsg->Get()->uiNumRows == 0) {
					sys_log(0, "   NOID");
					LoginFailure(d, "NOID");
					M2_DELETE(pinfo);
				}
				else if (!pinfo->passwd){
					LoginFailure(d, "WRONGPWD");
					sys_log(0, "   WRONGPWD");
					M2_DELETE(pinfo);
				}
				else
				{
					MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
					int col = 0;

					DWORD dwID = 0;
					char szEncrytPassword[64];
					char szPassword[64 + 1];
					char szMatrixCode[192 + 1];
					char szSocialID[SOCIAL_ID_MAX_LEN + 1];
					char szStatus[ACCOUNT_STATUS_MAX_LEN + 1];
					std::string szEncryptedPassword;
					char cSHAPassword[64+1];

					if (!row[col])
					{
						sys_err("error column %d", col);
						M2_DELETE(pinfo);
					   	break;
					}

					strlcpy(szEncrytPassword, row[col++], sizeof(szEncrytPassword));

					CryptoPP::SHA256 hash;
					CryptoPP::StringSource(pinfo->passwd, true, new CryptoPP::HashFilter(hash, new CryptoPP::HexEncoder(new CryptoPP::StringSink(szEncryptedPassword))));
					szEncryptedPassword.resize(64);
					sprintf(cSHAPassword, "%s", szEncryptedPassword.c_str());

					if (!row[col])
					{
					   	sys_err("error column %d", col);
						M2_DELETE(pinfo);
					   	break;
				   	}

					strlcpy(szPassword, row[col++], sizeof(szPassword));

					if (!row[col])
					{
						*szMatrixCode = '\0';
						col++;
					}
					else
					{
						strlcpy(szMatrixCode, row[col++], sizeof(szMatrixCode));
					}

					if (!row[col])
				   	{
						sys_err("error column %d", col);
						M2_DELETE(pinfo);
						break;
				   	}

					strlcpy(szSocialID, row[col++], sizeof(szSocialID));

					if (!row[col])
				   	{
					   	sys_err("error column %d", col);
						M2_DELETE(pinfo);
					   	break;
				   	}

					str_to_number(dwID, row[col++]);

					if (!row[col])
					{
					   	sys_err("error column %d", col);
						M2_DELETE(pinfo);
						break;
				   	}

					strlcpy(szStatus, row[col++], sizeof(szStatus));

					BYTE bNotAvail = 0;
					str_to_number(bNotAvail, row[col++]);

					int aiPremiumTimes[PREMIUM_MAX_NUM];
					memset(&aiPremiumTimes, 0, sizeof(aiPremiumTimes));

					char szCreateDate[256] = "00000000";

					{
						str_to_number(aiPremiumTimes[PREMIUM_EXP], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_ITEM], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_SAFEBOX], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_AUTOLOOT], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_FISH_MIND], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_MARRIAGE_FAST], row[col++]);
						str_to_number(aiPremiumTimes[PREMIUM_GOLD], row[col++]);

						{
							long retValue = 0;
							str_to_number(retValue, row[col]);

							time_t create_time = retValue;
							struct tm * tm1;
							tm1 = localtime(&create_time);
							strftime(szCreateDate, 255, "%Y%m%d", tm1);

							sys_log(0, "Create_Time %d %s", retValue, szCreateDate);
							sys_log(0, "Block Time %d ", strncmp(szCreateDate, g_stBlockDate.c_str(), 8));
						}
					}

					int nPasswordDiff = strcmp(szEncrytPassword, szPassword);

					int nPasswordDiff2;
					boost::to_upper(szPassword);
					nPasswordDiff2 = strcmp(cSHAPassword, szPassword);

					if (nPasswordDiff && nPasswordDiff2)
					{
						LoginFailure(d, "WRONGPWD");
						sys_log(0, "   WRONGPWD");
						M2_DELETE(pinfo);
					}
					else if (bNotAvail)
					{
						LoginFailure(d, "NOTAVAIL");
						sys_log(0, "   NOTAVAIL");
						M2_DELETE(pinfo);
					}
					else if (DESC_MANAGER::instance().FindByLoginName(pinfo->login))
					{
						LoginFailure(d, "ALREADY");
						sys_log(0, "   ALREADY");
						M2_DELETE(pinfo);
					}
					else if (strcmp(szStatus, "OK"))
					{
						LoginFailure(d, szStatus);
						sys_log(0, "   STATUS: %s", szStatus);
						M2_DELETE(pinfo);
					}
					else
					{
						if (strncmp(szCreateDate, g_stBlockDate.c_str(), 8) >= 0)
						{
							LoginFailure(d, "BLKLOGIN");
							sys_log(0, "   BLKLOGIN");
							M2_DELETE(pinfo);
							break;
						}

						char szQuery[1024];
						snprintf(szQuery, sizeof(szQuery), "UPDATE account SET last_play=NOW() WHERE id=%u", dwID);
						std::auto_ptr<SQLMsg> msg( DBManager::instance().DirectQuery(szQuery) );

						TAccountTable & r = d->GetAccountTable();

						r.id = dwID;
						trim_and_lower(pinfo->login, r.login, sizeof(r.login));
						strlcpy(r.passwd, pinfo->passwd, sizeof(r.passwd));
						strlcpy(r.social_id, szSocialID, sizeof(r.social_id));
						DESC_MANAGER::instance().ConnectAccount(r.login, d);

						if (!g_bBilling)
						{
							LoginPrepare(BILLING_FREE, 0, 0, d, pinfo->adwClientKey, aiPremiumTimes);
							//By SeMinZ
							M2_DELETE(pinfo);
							break;
						}

						sys_log(0, "QID_AUTH_LOGIN: SUCCESS %s", pinfo->login);
					}
				}
			}
			break;

