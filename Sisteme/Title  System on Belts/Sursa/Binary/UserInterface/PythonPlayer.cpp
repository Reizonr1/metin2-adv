// 1) Search: const DWORD POINT_MAGIC_NUMBER = 0xe73ac1da;
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
void CPythonPlayer::RequestChangeTitle(int iTitle)
{
	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendChangeTitle((int)iTitle);
}
#endif