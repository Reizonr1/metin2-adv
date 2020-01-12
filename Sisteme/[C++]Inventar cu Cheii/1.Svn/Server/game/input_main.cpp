//Find
void CInputMain::ItemMove(LPCHARACTER ch, const char * data)
{
	struct command_item_move * pinfo = (struct command_item_move *) data;

	if (ch)
		ch->MoveItem(pinfo->Cell, pinfo->CellTo, pinfo->count);
}

///Add
#ifdef NEW_ADD_INVENTORY
void CInputMain::Envanter_pakettiii(LPCHARACTER ch, const char * data)
{
    if (ch)
        ch->Envanter_update();
}
#endif

//Find
case HEADER_CG_ITEM_MOVE:
	if (!ch->IsObserverMode())
		ItemMove(ch, c_pData);
	break;
	
///Add
#ifdef NEW_ADD_INVENTORY
	case ENVANTER_BLACK:
		if (!ch->IsObserverMode())
			Envanter_pakettiii(ch, c_pData);
	break;
#endif