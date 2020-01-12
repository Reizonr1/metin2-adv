// 1) Search: (if you not have that you can step)
				snprintf(buf, sizeof(buf), "%s %lld %d %ld %d", 
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment());
// 2) Delete their function and change with this:
#ifdef ENABLE_TITLE_SYSTEM
				snprintf(buf, sizeof(buf), "%s %lld %d %ld %d %d", 			
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment(), ch->GetTitle());
#else		
				snprintf(buf, sizeof(buf), "%s %lld %d %ld %d", 
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment());
#endif	
"""""""""""""""""""""""""""""""""""""""""