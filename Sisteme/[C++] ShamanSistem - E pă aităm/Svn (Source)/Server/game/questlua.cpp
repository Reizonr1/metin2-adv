// Check this:

		RegisterHorseFunctionTable();
		
// Add under:

#ifdef ENABLE_SUPPORT_SYSTEM
		RegisterSupportFunctionTable();
#endif