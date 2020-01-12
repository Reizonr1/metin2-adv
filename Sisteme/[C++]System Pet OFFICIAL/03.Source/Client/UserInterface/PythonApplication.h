//Search in this file:
#include "PythonShop.h"
#include "PythonExchange.h"
#include "PythonChat.h"
#include "PythonTextTail.h"
#include "PythonSkill.h"

//Add after:
#ifdef NEW_PET_SYSTEM
#include "PythonSkillPet.h"
#endif

//Search in this file:

		CPythonEventManager			m_pyEventManager;
		CPythonBackground			m_pyBackground;
		CPythonSkill				m_pySkill;

//Add after:
#ifdef NEW_PET_SYSTEM
		CPythonSkillPet				m_pySkillPet;
#endif
