//1.) Search:
#include "ProcessCRC.h"
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	#include "PythonOxEvent.h"
#endif

//1.) Search:
			case HEADER_GC_MOUNT:
				ret = RecvMountPacket();
				break;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
			case HEADER_GC_OXEVENT:
				ret = RecvOxEventPacket();
				break;
#endif

//1.) Search:
void CPythonNetworkStream::__TEST_SetSkillGroupFake(int iIndex)
{
	m_dwMainActorSkillGroup = DWORD(iIndex);

	CPythonPlayer::Instance().NEW_ClearSkillData();
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshCharacter", Py_BuildValue("()"));
}
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
bool CPythonNetworkStream::RecvOxEventPacket()
{
	TPacketCGOxEventData p;
	if (!Recv(sizeof(TPacketCGOxEventData), &p))
	{
		Tracen("Recv Ox Event Packet Error");
		return false;
	}

	CPythonOxEvent::instance()->Initialize(p);
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OxEvent_Append", Py_BuildValue("(iii)", APPEND_WINNERS, 0, 0));
	return true;
}

bool CPythonNetworkStream::SendOxEventManagerPacket(int type, const char* c_szPassword, int vnum, int count)
{
	TPacketCGOxEventManager p;
	p.header = HEADER_CG_OXEVENT_MANAGER;
	p.type	 = type;
	strncpy(p.password, c_szPassword, sizeof(p.password));
	p.vnum	 = vnum;
	p.count	 = count;

	if (!Send(sizeof(p), &p))
		return false;

	return SendSequence();
}
#endif