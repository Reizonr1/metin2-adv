//Search in this file:

		void					SetRotationQuaternion(const D3DXQUATERNION &q);
		void					SetRotationMatrix(const D3DXMATRIX & m);

//Add after:

		void					SetScaleNew(float x, float y, float z);
		void					SetScaleNew(const D3DXVECTOR3 & newscale);
		void					SetScalePosition(float x, float y, float z);
		void					SetScalePosition(const D3DXVECTOR3 & newposition);

//Search in this file:

		// Bounding Box
		D3DXVECTOR4				m_v4TBBox[8];
		D3DXVECTOR3				m_v3TBBoxMin, m_v3TBBoxMax;
		D3DXVECTOR3				m_v3BBoxMin, m_v3BBoxMax;

		// Portal
		BYTE					m_abyPortalID[PORTAL_ID_MAX_NUM];

//Add after:

		D3DXVECTOR3				m_vecScalePos;
		D3DXVECTOR3				m_vecScaleNew;
		D3DXMATRIX				m_matAbsoluteTrans;
		D3DXMATRIX				m_matScale;
		D3DXMATRIX				m_matPositon;
