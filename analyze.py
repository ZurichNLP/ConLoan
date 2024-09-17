import re
import json

def clean_sentence(text):
	return text.replace("\t", "")

def extract_tagged_words(sentence, tag_prefix):
	pattern = fr"<{tag_prefix}(\d+)>(.*?)</{tag_prefix}\1>"
	matches = re.findall(pattern, sentence)
	return {int(num): word for num, word in matches}


files = {
	"Portuguese": {
		"annotations": "annotations/Portuguese1.tsv", 
		"loanwords": "loanwords/Portuguese_loanwords_Wiktionary.tsv"
	},
	"Icelandic": {
		"annotations": "annotations/Icelandic1.tsv", 
		"loanwords": "loanwords/Icelandic_Morphology_database_words-forms.tsv"
	},
	# "Italian1": {
	# 	"annotations": "annotations/Italian1.tsv", 
	# 	"loanwords": "loanwords/Italian_loanwords_Wiktionary.tsv"
	# },
	# "Italian2": {
	# 	"annotations": "annotations/Italian2.tsv", 
	# 	"loanwords": "loanwords/Italian_loanwords_Wiktionary.tsv"
	# },
	"Italian": {
		"annotations": "annotations/Italian_merged.tsv", 
		"loanwords": "loanwords/Italian_loanwords_Wiktionary.tsv"
	},
	"German1": {
		"annotations": "annotations/German1.tsv", 
		"loanwords": "loanwords/German_loanwords.tsv"
	},
	"German": {
		"annotations": "annotations/German.tsv", 
		"loanwords": "loanwords/German_loanwords.tsv"
	},
	# "Chinese1": {
	# 	"annotations": "annotations/Chinese1.tsv", 
	# 	"loanwords": "loanwords/Chinese_loanwords_Wiktionary.tsv"
	# },
	# "Chinese2": {
	# 	"annotations": "annotations/Chinese2.tsv", 
	# 	"loanwords": "loanwords/Chinese_loanwords_Wiktionary.tsv"
	# }
	# "Chinese3": {
	# 	"annotations": "annotations/Chinese3.tsv", 
	# 	"loanwords": "loanwords/Chinese_loanwords_Wiktionary.tsv"
	# }
	"Chinese": {
		"annotations": "annotations/Chinese_merged.tsv", 
		"loanwords": "loanwords/Chinese_loanwords_Wiktionary.tsv"
	},
	"German2": {
		"annotations": "annotations/German2.tsv", 
		"loanwords": "loanwords/German_loanwords.tsv"
	},
	# "Greek2": {
	# 	"annotations": "annotations/Greek2.tsv", 
	# 	"loanwords": "loanwords/Greek_loanwords.tsv"
	# },
	# "Greek1": {
	# 	"annotations": "annotations/Greek1.tsv", 
	# 	"loanwords": "loanwords/Greek_loanwords.tsv"
	# },
	"Greek": {
		"annotations": "annotations/Greek_merged.tsv", 
		"loanwords": "loanwords/Greek_loanwords.tsv"
	},
	"Spanish": {
		"annotations": "annotations/Spanish.tsv", 
		"loanwords": "loanwords/Spanish_loanwords.tsv"
	},
	"French": {
		"annotations": "annotations/French1.tsv", 
		"loanwords": "loanwords/French_loanwords_Wiktionary.tsv"
	},
	"Russian": {
		"annotations": "annotations/Russian2.tsv", 
		"loanwords": "loanwords/Russian_loanwords_Wiktionary.tsv"
	}
}

for language in files:
	json_output = list()
	with open(files[language]["annotations"], "r") as f:
		data = f.read().split("\t\t\t\t\t\n\t\t\t\t\t")

	with open(files[language]["loanwords"], "r") as f:
		loanwords = {i.split("\t")[0]: i.split("\t")[1] for i in f.read().splitlines()}

	all_cells, validated_cells = 0, 0
	replacements, replaced_loanwords = list(), list()

	for i in data:
		flagged = False
		cells = i.splitlines()

		if len(cells) == 4:
			sentence_1, target_1 = clean_sentence(cells[1].split("\t")[0]), clean_sentence(cells[1].split("\t")[1])
			annot_sent_1, target_2 = clean_sentence(cells[2].split("\t")[0]), clean_sentence(cells[2].split("\t")[1])

			all_cells += 1

			if target_1 != target_2:
				flagged = True

			if cells[-1] == "TRUE" or cells[-1] == "TRUE\t":
				validated_cells += 1
				if flagged:
					print("Unmatching translations")
					print("\t", cells)
				else:
					# print(sentence_1)
					pass

					# Extract words from tags in both sentences
					words_in_L_tags = extract_tagged_words(sentence_1, 'L')
					words_in_N_tags = extract_tagged_words(annot_sent_1, 'N')			

					# Check for missing or empty tags
					for key in words_in_L_tags:
						if key not in words_in_N_tags:
							raise ValueError(f"Error: Tag <L{key}> does not have a corresponding <N{key}> tag.")
						if not words_in_L_tags[key]:
							raise ValueError(f"Error: Tag <L{key}> is empty.")
						if not words_in_N_tags[key]:
							raise ValueError(f"Error: Tag <N{key}> is empty.")

					corresponding_words = {key: (words_in_L_tags[key], words_in_N_tags[key]) for key in words_in_L_tags}
					
					for i in corresponding_words:
						replacements.append(corresponding_words[i])
						if corresponding_words[i][0] != corresponding_words[i][1]:
							replaced_loanwords.append(corresponding_words[i])
					# break

					json_output.append({
						"source_annotated_loanwords": sentence_1,
						"source_annotated_loanwords_replaced": annot_sent_1,
						"target": target_1,
						"source_plain": re.sub(r'</?[NL]\d?>', '', sentence_1),
						"source_annotated_plain": re.sub(r'</?[NL]\d?>', '', annot_sent_1),
						"words_in_L_tags": words_in_L_tags,
						"words_in_N_tags": words_in_N_tags,
						"corresponding_words": corresponding_words
					})

		elif len(cells):
			print("Suspicious cells")
			print("\t", cells)

	print(language)
	print("Number of all sentence pairs:", all_cells)
	print("Number of all validated cells (checked checkbox):", validated_cells)
	print("Number of annotated instances:", len(replacements))
	print("Number of loanwords replaced by native alternatives:", len(replaced_loanwords))
	print()

	with open("datasets/%s_all_replacements.tsv"%language, "w") as f:
		f.write("\n".join(["\t".join(i) + "\t" + loanwords.get(i[0], "") for i in replacements]))

	with open("datasets/%s_replaced_loanwords.tsv"%language, "w") as f:
		f.write("\n".join(["\t".join(i) + "\t" + loanwords.get(i[0], "") for i in replaced_loanwords]))

	# with open("datasets/%s.json"%language, "w") as f:
	# 	json.dump(json_output, f, ensure_ascii=False, indent=4)