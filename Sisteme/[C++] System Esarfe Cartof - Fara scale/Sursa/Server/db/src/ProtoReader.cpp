// 1) Search: static string arSub28[]
// 2) After change the entire string with:
	static string arSub28[] = {"COSTUME_BODY", "COSTUME_HAIR", "COSTUME_ACCE"};

// 1) Search: int get_Item_WearFlag_Value(string inputString)
// 2) Delete their function and paste:
int get_Item_WearFlag_Value(string inputString) 
{
	string arWearrFlag[] = {"WEAR_BODY", "WEAR_HEAD", "WEAR_FOOTS", "WEAR_WRIST", "WEAR_WEAPON", "WEAR_NECK", "WEAR_EAR", "WEAR_SHIELD", "WEAR_UNIQUE", "WEAR_ARROW", "WEAR_HAIR", "WEAR_ABILITY", "WEAR_COSTUME_BODY", "WEAR_COSTUME_HAIR", "WEAR_COSTUME_ACCE", "WEAR_COSTUME_MOUNT"};
	int retValue = 0;
	string* arInputString = StringSplit(inputString, "|");
	for(int i =0;i<sizeof(arWearrFlag)/sizeof(arWearrFlag[0]);i++)
	{
		string tempString = arWearrFlag[i];
		for (int j=0; j<30 ; j++)
		{
			string tempString2 = arInputString[j];
			if (tempString2.compare(tempString)==0)
			{
				retValue = retValue + pow((float)2,(float)i);
			}
			
			if(tempString2.compare("") == 0)
				break;
		}
	}
	
	delete []arInputString;
	return retValue;
}