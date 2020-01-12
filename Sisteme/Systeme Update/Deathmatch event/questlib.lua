Search:
function resetdelay(v) raw_script("[/DELAY]") end

Add it under:
function say_npc()
 say_title(""..mob_name(npc.get_race()).."")
end
