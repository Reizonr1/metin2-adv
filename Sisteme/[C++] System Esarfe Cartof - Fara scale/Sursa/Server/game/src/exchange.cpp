// 1) Search: if (IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen())
// 2) Delete this line and paste:
	if (IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen() || IsAcceOpen())

// 1) Search: if (victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen())
// 2) Delete this line and paste:
	if (victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen() || victim->IsAcceOpen())