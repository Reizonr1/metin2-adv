// 1) Search: CItem::GetAttributeCount()
// 2) After their function make a new line and paste:
int CItem::GetAcceAttributeCount()
{
	int i;
	int c = 0;
	for (i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
	{
		if (GetAttributeType(i) != 0)
			c = c + 1;
	}
	
	return c;
}