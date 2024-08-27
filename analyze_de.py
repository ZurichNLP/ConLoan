import json
import re

with open("annotations/OUT_FLORES+devtest_german.json", "r") as f:
	data = json.load(f)

with open("/Users/sina/Bucket/Parallel/floresp-v2.0-rc.2/devtest/devtest.deu_Latn", "r") as f:
	deu = f.read().splitlines()

with open("/Users/sina/Bucket/Parallel/floresp-v2.0-rc.2/devtest/devtest.eng_Latn", "r") as f:
	eng = f.read().splitlines()

with open("loanwords/German_loanwords.tsv", "r") as f:
	loanwords = {i.split("\t")[0]: i.split("\t")[1] for i in f.read().splitlines()}

inflected_replacements = {
	"Vorsitzender": "Vorsitzenden",
	"ausgezeichnetes": "ausgezeichnete",
	"Wiederherstellungschirurgischer Eingriff": "Wiederherstellungschirurgischen",
	"leitete in die Wege": "leitete",
	"Überschuss": "Überschüsse",
	"Umstand": "Umstände",
	"annehmen": "anzunehmen",
	"hängt zusammen": "hängt",
	"ausrichten": "richten",
	"Vorgesetzter": "Manager",
	"streng beurteilendes": "streng beurteilende",
	"festlegen": "legen",
	"fachkundiges": "fachkundige"
}

parallel_corpus = {i: j for i, j in zip(deu, eng)}

json_output = list()
words_in_L_tags, words_in_N_tags, corresponding_words = dict(), dict(), dict()
replacements, replaced_loanwords = list(), list()
for i in data:
	source_annotated, source_annotated_native = data[i]["original_sentence"], data[i]["original_sentence"]
	tag_id = 0
	
	for j in data[i]["changes-loan-to-native"]:
		if j not in source_annotated:
			print(j, source_annotated)			
		else:
			source_annotated = source_annotated.replace(j, "<L%s>%s</L%s>"%(str(tag_id), j, str(tag_id)))
			if data[i]["changes-loan-to-native"][j] in data[i]["only_native_sentence"]:
				source_annotated_native = source_annotated_native.replace(j, "<N%s>%s</N%s>"%(str(tag_id), data[i]["changes-loan-to-native"][j], str(tag_id)))
			else:
				source_annotated_native = source_annotated_native.replace(j, "<N%s>%s</N%s>"%(str(tag_id), inflected_replacements[data[i]["changes-loan-to-native"][j]], str(tag_id)))
			
			tag_id += 1

		words_in_L_tags.update({tag_id: j})
		words_in_N_tags.update({tag_id: data[i]["changes-loan-to-native"][j]})
		corresponding_words.update({tag_id: (j, data[i]["changes-loan-to-native"][j])})
		replacements.append((j, data[i]["changes-loan-to-native"][j]))
		if j != data[i]["changes-loan-to-native"][j]:
			replaced_loanwords.append((j, data[i]["changes-loan-to-native"][j]))
	
	json_output.append({
		"source_annotated_loanwords": source_annotated,
		"source_annotated_loanwords_replaced": source_annotated_native,
		"target": parallel_corpus[data[i]["original_sentence"]],
		"source_plain": data[i]["original_sentence"],
		"source_annotated_plain": data[i]["only_native_sentence"],
		"words_in_L_tags": words_in_L_tags,
		"words_in_N_tags": words_in_N_tags,
		"corresponding_words": corresponding_words
	})

print("Number of all validated cells (checked checkbox):", len(data))
print("Number of annotated instances:", len(replacements))
print("Number of loanwords replaced by native alternatives:", len(replaced_loanwords))

language = "German_0"
with open("analysis/%s.json"%language, "w") as f:
	json.dump(json_output, f, ensure_ascii=False, indent=4)

with open("analysis/%s_all_replacements.tsv"%language, "w") as f:
	f.write("\n".join(["\t".join(i) + "\t" + loanwords.get(i[0], "") for i in replacements]))

with open("analysis/%s_replaced_loanwords.tsv"%language, "w") as f:
	f.write("\n".join(["\t".join(i) + "\t" + loanwords.get(i[0], "") for i in replaced_loanwords]))

