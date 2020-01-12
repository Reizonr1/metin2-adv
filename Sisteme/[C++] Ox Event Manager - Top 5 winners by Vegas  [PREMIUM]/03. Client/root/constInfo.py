#Add on first line:
import app, os
if app.ENABLE_FEATURES_OXEVENT:
	if not os.path.exists("lib\item_proto_list.py"):
		fileName = file("lib\item_proto_list.py", "w")