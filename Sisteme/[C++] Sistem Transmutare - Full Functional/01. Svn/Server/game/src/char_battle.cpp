// 1) Search:
	Cube_close(this);
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	ChangeLookWindow(false, true);
#endif


// 1) Search:
	if (IsCubeOpen() == true)
	{
		Cube_close(this);
	}
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	if (IsPC())
		ChangeLookWindow(false, true);
#endif