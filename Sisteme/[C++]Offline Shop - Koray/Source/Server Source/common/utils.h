Search:
inline bool str_to_number (long long& out, const char *in)
{
	if (0==in || 0==in[0])	return false;

	out = (long long)strtoull(in, NULL, 10);
	return true;
}

Add it under:
inline bool str_to_number(unsigned long long& out, const char *in)
{
	if (0 == in || 0 == in[0])	return false;

	out = strtoull(in, NULL, 10);
	return true;
}