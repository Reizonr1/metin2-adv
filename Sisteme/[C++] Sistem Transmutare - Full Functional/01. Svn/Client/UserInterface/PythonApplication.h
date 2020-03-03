// 1) Search:
#include "MovieMan.h"
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
#include "PythonChangeLook.h"
#endif


// 1) Search:
		CGuildMarkManager			m_kGuildMarkManager;
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		CPythonChangeLook	m_pyChangeLook;
#endif