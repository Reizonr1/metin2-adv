Inventory Slot Marking System

You can compare every files with the original(unmodified from dev branch) files to see the differences,
where I made my modifications. There are many compare tools to check these, if something makes trouble. 
This system is not exactly same with official, but almost =D
The name of the macro of the system is WJ_ENABLE_TRADABLE_ICON.
I made the grayscale for shops, private shop builds, exchange, safebox, but you can easily extend the system for your
custom systems too if you want it or necessary, because you can query type, subtype or the antiflag of an item by slot with
my new functions, which are reversed from official binary.
The redglow is done for exchange, private shop builds(attached items get red glow), refine of an item, attaching stone into item
and (a not included) Enchant Item+.

If you found a bug please tells me as soon as possible, I will fix it.


Mark for can't make acts with the item by index:
	- wndMgr.SetCantMouseEventSlot(localSlotIndex[0..45]) --> Sets the red glow, and disable all mouse button events on the invenslot by localSlotIndex.
	- wndMgr.SetCanMouseEventSlot(localSlotIndex[0..45])  --> Release the red glow, and enable the mouse button events on the invenslot by localSlotIndex.

Mark for can't attach to target window or enything else what dismissed:
	- wndMgr.SetUnusableSlotOnTopWnd(localSlotIndex[0..45]) --> Sets the greyscale on the invenlot by localSlotIndex.
	- wndMgr.SetUsableSlotOnTopWnd(localSlotIndex[0..45])   --> Release the greyscale from the invenslot if it was set.


!!!IMPORTANT!!!!
Some updates were made about costume and sealbind in uiInventory.py but I didn't made in tutorial.
So after when you done with the tut, check the UPDATE.py file, and try to understand the differences and take a look for the macro also.
app.ENABLE_SEALBIND_SYSTEM - may be other name!
