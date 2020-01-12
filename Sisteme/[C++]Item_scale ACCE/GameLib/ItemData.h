// // arat

void SetItemTableScaleData(int dwJob, int dwSex, float fSca

// alt©¥na ekle

		D3DXVECTOR3 & GetItemScalePosition(int dwJob, int dwSex);
		D3DXVECTOR3 & GetItemScale(int dwJob, int dwSex);

// arat

		TItemTable m_ItemTable;

// alt©¥na ekle

		TItemScaleTable m_ItemScaleTable;

// arat

		} TItemTable;

// alt©¥na ekle

		typedef struct SItemScaleTable
		{
			D3DXVECTOR3 scalePos[2][5];
			D3DXVECTOR3 scale[2][5];

		} TItemScaleTable;

