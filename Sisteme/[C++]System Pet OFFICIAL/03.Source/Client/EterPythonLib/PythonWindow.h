//Search in this file:

			BOOL LoadImage(const char * c_szFileName);
			void SetDiffuseColor(float fr, float fg, float fb, float fa);

//Add after:
			void SetScale(float sx, float sy);

//Search in this file:

			void SetDelay(int iDelay);
			void AppendImage(const char * c_szFileName);

//Add after:

			void AppendImageScale(const char * c_szFileName, float scale_x, float scale_y);
