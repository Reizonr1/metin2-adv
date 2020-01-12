Search:
	if (!pkInstTarget->IsPC() && !pkInstTarget->IsBuilding())
		return;

Change:
	if (!pkInstTarget->IsPC() && !pkInstTarget->IsBuilding() && (pkInstTarget->GetVirtualNumber() < 30005 || pkInstTarget->GetVirtualNumber() > 30010))
		return;


https://puu.sh/sgMdj/c8ad39dd6b.png
