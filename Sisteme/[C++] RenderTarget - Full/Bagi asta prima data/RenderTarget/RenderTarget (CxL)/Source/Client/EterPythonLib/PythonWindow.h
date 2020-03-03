//1.1 Search:
#include "../eterBase/Utils.h"

//1.2 Add ABOVE:
#include <cstdint>


//2.1 Search:
	class CBox : public CWindow

//2.2 Add ABOVE:
	class CUiRenderTarget : public CWindow
	{
	public:
		CUiRenderTarget(PyObject * ppyObject);
		virtual ~CUiRenderTarget();

		bool SetRenderTarget(uint8_t index);

	protected:
		DWORD m_dwIndex;
		void OnRender();
	};
