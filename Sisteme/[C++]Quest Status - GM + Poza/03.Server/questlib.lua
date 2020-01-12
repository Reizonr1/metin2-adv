#En Alta Ekle: (questcategory.txt quest dizinine atılacak (questlib.lua'nın bulunduğu bölüme))


function string:split(delimiter)
	local result = {}
	local from = 1
	local delim_from, delim_to = string.find(self, delimiter, from)

	while delim_from do
		table.insert(result, string.sub(self, from , delim_from-1))
		from = delim_to + 1
		delim_from, delim_to = string.find(self, delimiter, from)
	end
	table.insert(result, string.sub(self, from))
	return result
end

q = q or {}

q["category_num"] = {"MAIN_QUEST", "SUB_QUEST", "COLLECT_QUEST", "LEVELUP_QUEST", "SCROLL_QUEST", "SYSTEM_QUEST", "NONE_TYPE_QUEST"}
q["category_map"] = {}

function q.GetCategoryIndex(category)
	for i = 1, 6 do
		if q["category_num"][i] == category then
			return (i-1)
		end
	end
	return 5
end

function q.GetQuestCategory()
	local qName = q.getcurrentquestname()
	for questName, questCategory in pairs(q["category_map"]) do
		--syschat(questName.." "..questCategory)
		if questName == qName then
			return questCategory
		end
	end
	return 5
end

function ReadQuestCategoryFile()
	for line in io.lines(get_locale_base_path().."/quest/questcategory.txt") do
		local tokens = string.split(line, "\t")
		local qName = tokens[1] or ""
		local category = string.gsub(tokens[2], "%s", "") or ""

		q["category_map"][qName] = q.GetCategoryIndex(category)
	end
end

function send_letter(text, cat)
	cat = cat or q.GetQuestCategory()
	text = cat..text
	makequestbutton(text) 
	set_skin(NOWINDOW) 
	q.set_title(text)
	q.start()
end

ReadQuestCategoryFile()

