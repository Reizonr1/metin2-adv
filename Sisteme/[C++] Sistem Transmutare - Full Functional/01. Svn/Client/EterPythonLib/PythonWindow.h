// 1) Search:
#include "../eterBase/Utils.h"
// 2) After this make a new line and paste:
#include "../UserInterface/defines.h"


// 1) Search:
			void	AppendImage(const char * c_szFileName);
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			void	AppendImage(const char * c_szFileName, float r = 1.0, float g = 1.0, float b = 1.0, float a = 1.0);
#else
			void	AppendImage(const char * c_szFileName);
#endif