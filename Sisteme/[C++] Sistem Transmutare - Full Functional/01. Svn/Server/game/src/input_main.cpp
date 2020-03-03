// 1) Search:
int CInputMain::Analyze(LPDESC d, BYTE bHeader, const char * c_pData)
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
void CInputMain::ChangeLook(LPCHARACTER pkChar, const char* c_pData)
{
	quest::PC * pPC = quest::CQuestManager::instance().GetPCForce(pkChar->GetPlayerID());
	if (pPC->IsRunning())
		return;
	
	TPacketChangeLook * sPacket = (TPacketChangeLook*) c_pData;
	switch (sPacket->subheader)
	{
		case CL_SUBHEADER_CLOSE:
			{
				pkChar->ChangeLookWindow(false);
			}
			break;
		case CL_SUBHEADER_ADD:
			{
				pkChar->AddClMaterial(sPacket->tPos, sPacket->bPos);
			}
			break;
		case CL_SUBHEADER_REMOVE:
			{
				pkChar->RemoveClMaterial(sPacket->bPos);
			}
			break;
		case CL_SUBHEADER_REFINE:
			{
				pkChar->RefineClMaterials();
			}
			break;
		default:
			break;
	}
}
#endif


// 1) Search:
		case HEADER_CG_REFINE:
			Refine(ch, c_pData);
			break;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		case HEADER_CG_CL:
			{
				ChangeLook(ch, c_pData);
			}
			break;
#endif