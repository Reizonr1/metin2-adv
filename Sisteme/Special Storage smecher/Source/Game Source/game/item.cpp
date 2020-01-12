Cauta ---------

if (false == cell.IsDefaultInventoryPosition() && false == cell.IsBeltInventoryPosition()

Adauga sub -------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
					&& false == cell.IsSkillBookInventoryPosition() && false == cell.IsUpgradeItemsInventoryPosition() && false == cell.IsStoneInventoryPosition() && false == cell.IsSandikInventoryPosition()
#endif


Cauta ------

bool CItem::IsSameSpecialGroup(const LPITEM item) const

Adauga sub ------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
bool CItem::IsSkillBook()
{
	return GetType() == ITEM_SKILLBOOK;
}

bool CItem::IsUpgradeItem()
{
	switch (GetVnum())
	{
		case 30003:
		case 30004:
		case 30005:
		case 30006:
		case 30007:
		case 30008:
		case 30009:
		case 30010:
		case 30011:
		case 30014:
		case 30015:
		case 30016:
		case 30017:
		case 30018:
		case 30019:
		case 30021:
		case 30022:
		case 30023:
		case 30025:
		case 30027:
		case 30028:
		case 30030:
		case 30031:
		case 30032:
		case 30033:
		case 30034:
		case 30035:
		case 30037:
		case 30038:
		case 30039:
		case 30040:
		case 30041:
		case 30042:
		case 30045:
		case 30046:
		case 30047:
		case 30048:
		case 30049:
		case 30050:
		case 30051:
		case 30052:
		case 30053:
		case 30055:
		case 30056:
		case 30057:
		case 30058:
		case 30059:
		case 30060:
		case 30061:
		case 30067:
		case 30069:
		case 30070:
		case 30071:
		case 30072:
		case 30073:
		case 30074:
		case 30075:
		case 30076:
		case 30077:
		case 30078:
		case 30079:
		case 30080:
		case 30081:
		case 30082:
		case 30083:
		case 30084:
		case 30085:
		case 30086:
		case 30087:
		case 30088:
		case 30089:
		case 30090:
		case 30091:
		case 30092:
		case 30192:
		case 30193:
		case 30194:
		case 30195:
		case 30196:
		case 30197:
		case 30198:
		case 30199:
		case 30500:
		case 30501:
		case 30502:
		case 30503:
		case 30504:
		case 30505:
		case 30506:
		case 30507:
		case 30508:
		case 30509:
		case 30510:
		case 30511:
		case 30512:
		case 30513:
		case 30514:
		case 30515:
		case 30516:
		case 30517:
		case 30518:
		case 30519:
		case 30520:
		case 30521:
		case 30522:
		case 30523:
		case 30524:
		case 30525:
		case 30600:
		case 30601:
		case 30602:
		case 30603:
		case 30604:
		case 30605:
		case 30606:
		case 30607:
		case 30608:
		case 30609:
		case 30610:
		case 30611:
		case 30612:
		case 30613:
		case 30614:
		case 30615:
		case 30616:
		case 30617:
		case 30618:
		case 30619:
			return true;
	}
	
	return false;
}

bool CItem::IsStone()
{
	return GetType() == ITEM_METIN;
}

bool CItem::IsSandik()
{
	switch (GetVnum())
	{
		case 38050:
		case 38052:
		case 38053:
		case 38054:
		case 38055:
		case 38056:
		case 50006:
		case 50007:
		case 50011:
		case 50012:
		case 50013:
		case 50070:
		case 50071:
		case 50072:
		case 50073:
		case 50074:
		case 50075:
		case 50076:
		case 50077:
		case 50078:
		case 50079:
		case 50080:
		case 50081:
		case 50082:
		case 50090:
		case 50109:
		case 50110:
		case 50111:
		case 50112:
		case 50113:
		case 50114:
		case 50127:
		case 50128:
		case 50129:
		case 50130:
		case 50131:
		case 50132:
		case 50133:
		case 50134:
		case 50135:
		case 50136:
		case 50137:
		case 50182:
		case 50186:
		case 50215:
		case 50249:
		case 50254:
		case 50270:
		case 50271:
		case 50272:
		case 50273:
		case 50323:
		case 50324:
		case 53505:
		case 53506:
		case 53507:
		case 53508:
		case 53509:
		case 53510:
		case 53511:
		case 53512:
		case 53513:
		case 53514:
		case 53515:
		case 55009:
		case 71159:
		case 71160:
		case 80022:
		case 80023:
		case 80024:
		case 80025:
		case 80026:
		case 80027:
		case 80028:
		case 80029:
		case 80030:
		case 80031:
		case 80032:
		case 80033:
		case 80034:
		case 80035:
		case 80036:
		case 80037:
		case 80038:
		case 30118:
		case 38057:
		case 50034:
		case 50033:
		case 50117:
			return true;
	}
	
	return false;
}

#endif
