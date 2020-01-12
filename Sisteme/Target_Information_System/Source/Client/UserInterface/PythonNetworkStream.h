// Search for:
		bool RecvDamageInfoPacket();

// Add (Under):
#ifdef ENABLE_SEND_TARGET_INFO
		bool RecvTargetInfoPacket();

		public:
			bool SendTargetInfoLoadPacket(DWORD dwVID);

		protected:
#endif
