//1.1 Search:
float CGraphicBase::GetFOV()
{
	return ms_fFieldOfView;
}
	
//1.2 Replace with:

float CGraphicBase::GetFOV() const
{
	return ms_fFieldOfView;
}

float CGraphicBase::GetAspect() const
{
	return ms_fAspect;
}

float CGraphicBase::GetNear() const
{
	return ms_fNearY;
}

float CGraphicBase::GetFar() const
{

	return ms_fFarY;
}

