// Check this:

	extern void RegisterHorseFunctionTable();

	
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
	extern void RegisterSupportFunctionTable();
#endif