#include "stdafx.h"
#include "questmanager.h"
#include "char.h"
#include "item.h"
#include "item_manager.h"
#include "over9refine.h"
#include "log.h"
#include "refine.h"

#undef sys_err
#ifndef __WIN32__
#define sys_err(fmt, args...) quest::CQuestManager::instance().QuestError(__FUNCTION__, __LINE__, fmt, ##args)
#else
#define sys_err(fmt, ...) quest::CQuestManager::instance().QuestError(__FUNCTION__, __LINE__, fmt, __VA_ARGS__)
#endif

namespace quest
{
	//
	// "item_get_id" under!
	//

	int item_get_attribute_type(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		LPITEM item = q.GetCurrentItem();

		if (item == NULL)
		{
			sys_err("item_get_attribute_type::can not find given item index");
			lua_pushnumber(L, 0);
			return 1;
		}

		if (!lua_isnumber(L, 1))
		{
			sys_err("item_get_attribute_type::number is not given!!!");
			lua_pushnumber(L, 0);
			return 1;
		}

		int iAttrIndex = (int)lua_tonumber(L, 1);

		if (iAttrIndex < 0 || iAttrIndex >= ITEM_ATTRIBUTE_MAX_NUM)
		{
			sys_err("item_get_attribute_type::given attribute index is out of range: %d", iAttrIndex);
			lua_pushnumber(L, 0);
			return 1;
		}

		const TPlayerItemAttribute& attrItem = item->GetAttribute(iAttrIndex);

		lua_pushnumber(L, attrItem.bType);

		return 1;
	}
	
	int item_get_attribute_value(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		LPITEM item = q.GetCurrentItem();

		if (item == NULL)
		{
			sys_err("item_get_attribute_value::can not find given item index");
			lua_pushnumber(L, 0);
			return 1;
		}

		if (!lua_isnumber(L, 1))
		{
			sys_err("item_get_attribute_value::number is not given!!!");
			lua_pushnumber(L, 0);
			return 1;
		}

		int iAttrIndex = (int)lua_tonumber(L, 1);

		if (iAttrIndex < 0 || iAttrIndex >= ITEM_ATTRIBUTE_MAX_NUM)
		{
			sys_err("item_get_attribute_value::given attribute index is out of range: %d", iAttrIndex);
			lua_pushnumber(L, 0);
			return 1;
		}

		const TPlayerItemAttribute& attrItem = item->GetAttribute(iAttrIndex);

		lua_pushnumber(L, attrItem.sValue);

		return 1;
	}

    int item_get_attribute(lua_State* L)
    {
        LPITEM item = CQuestManager::instance().GetCurrentItem();
 
        if (!item) return 0;
 
        if (!lua_isnumber(L, 1))
        {
            sys_err("Wrong argument, need a number from range(0..%d)!", ITEM_ATTRIBUTE_MAX_NUM-2);
            lua_pushnumber(L, 0);
            return 1;
        }
 
        int iAttrIndex = (int)lua_tonumber(L, 1);
        if (iAttrIndex < 0 || iAttrIndex >= ITEM_ATTRIBUTE_MAX_NUM-2)
        {
            sys_err("Invalid index %d. Index out of range(0..%d)", iAttrIndex, ITEM_ATTRIBUTE_MAX_NUM-2);
            lua_pushnumber(L, 0);
            return 1;
        }
 
        const TPlayerItemAttribute& AttrItem = item->GetAttribute(iAttrIndex);
 
        lua_newtable(L);
 
        lua_pushnumber(L, AttrItem.bType);
        lua_rawseti(L, -2, 1);
 
        lua_pushnumber(L, AttrItem.sValue);
        lua_rawseti(L, -2, 2);
        return 1;
    }
 
	int item_set_attribute(lua_State* L)
    {
        LPITEM item = CQuestManager::instance().GetCurrentItem();
 
        if (!item) return 0;
        if (item->GetType() == ITEM_COSTUME)
        {
            lua_pushboolean(L, false);
            return 1;
        }
 
        if (!lua_isnumber(L, 1))
        {
            sys_err("Wrong argument[AttrIdx] #1.");
            lua_pushboolean(L, false);
            return 1;
        }
        else if (!lua_isnumber(L, 2))
        {
            sys_err("Wrong argument[AttrType] #2.");
            lua_pushboolean(L, false);
            return 1;
        }
        else if (!lua_isnumber(L, 3))
        {
            sys_err("Wrong argument[AttrValue] #3.");
            lua_pushboolean(L, false);
            return 1;
        }
 
        int bAttrIndex = (int)lua_tonumber(L, 1);
        if (bAttrIndex < 0 || bAttrIndex >= ITEM_ATTRIBUTE_MAX_NUM-2)
        {
            sys_err("Invalid AttrIndex %d. AttrIndex out of range(0..4)", bAttrIndex);
            lua_pushboolean(L, false);
            return 1;
        }
 
        int bAttrType = (int)lua_tonumber(L, 2);
        if (bAttrType < 1 || bAttrType >= MAX_APPLY_NUM)
        {
            sys_err("Invalid AttrType %d. AttrType out of range(1..%d)", MAX_APPLY_NUM);
            lua_pushboolean(L, false);
            return 1;
        }
 
        if (item->HasAttr(bAttrType) && (item->GetAttribute(bAttrIndex).bType != bAttrType))
        {
            sys_err("AttrType[%d] multiplicated.", bAttrType);
            lua_pushboolean(L, false);
            return 1;
        }
 
        int bAttrValue = (int)lua_tonumber(L, 3);
        if (bAttrValue < 1 || bAttrValue >= 32768)
        {
            sys_err("Invalid AttrValue %d. AttrValue should be between 1 and 32767!", bAttrValue);
            lua_pushboolean(L, false);
            return 1;
        }
 
        bool bRet = TRUE;
        int bAttrCount = item->GetAttributeCount();
        if (bAttrCount <= 4 && bAttrCount >= 0)
        {
            if (bAttrCount < bAttrIndex)
                bAttrIndex = bAttrCount;
 
            item->SetForceAttribute(bAttrIndex, bAttrType, bAttrValue);
        }
        else
            bRet = FALSE;
 
        lua_pushboolean(L, bRet);
        return 1;
    }
 
 
	/* add to list! */
	
	void RegisterITEMFunctionTable()
	{

		luaL_reg item_functions[] =
		{
			
			{ "get_attribute",				item_get_attribute					},
			{ "set_attribute",		                item_set_attribute					},
			{ "get_attribute_type",		item_get_attribute_type		},
			{ "get_attribute_value",		item_get_attribute_value		},
			{ NULL,			NULL			}
		};
		CQuestManager::instance().AddLuaFunctionTable("item", item_functions);
	}
}
