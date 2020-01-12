//Arat
	class FuncWho
///Bu sekilde degistir:
class FuncWho
{
	public:
		int iTotalCount;
		int aiEmpireUserCount[EMPIRE_MAX_NUM];
		int toplam;
		int * Bayrak;
		int asdasdas;

		FuncWho()
		{
			iTotalCount = 0;
			memset(aiEmpireUserCount, 0, sizeof(aiEmpireUserCount));
		}

		void operator() (LPDESC d)
		{
			if (d->GetCharacter())
			{
				++iTotalCount;
				++aiEmpireUserCount[d->GetEmpire()];
				/**
				getusercount'dan getirmeseydim sadece bir kisi,
				icin guncellenecekti.Digerleri guncellenmeyecekti.
				Tecrubeyle sabit.
				*/
				DESC_MANAGER::instance().GetUserCount(toplam, &Bayrak, asdasdas);
				d->ChatPacket(CHAT_TYPE_COMMAND, "black %d %d %d %d", toplam, Bayrak[2], Bayrak[1], Bayrak[3]);
			}
		}
};