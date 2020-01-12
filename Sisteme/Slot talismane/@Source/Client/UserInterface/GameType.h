// Search :

	const DWORD c_New_Equipment_Count = 4; //maybe this value can be different.
	
// Replace with :


#ifdef ENABLE_PENDANT
	const DWORD c_New_Equipment_Count = 5;
#else
	const DWORD c_New_Equipment_Count = 4;  
#endif



// How it's work ? Old value +1 , in this case 4 +1 , 3 old , 1 new , final value 5.

// Search this :

const DWORD c_Equipment_Belt  = c_New_Equipment_Start + 2;

// Add this :

#ifdef ENABLE_PENDANT
	const DWORD c_Equipment_Pendant  = c_New_Equipment_Start + 4; // change the value , if the last is two , change with three. 
#endif

