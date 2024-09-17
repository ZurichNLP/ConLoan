import json

files = {
	"Chinese": {
			"dataset": "../datasets/Chinese.json",
			"plain_translation": "MT/all/Chinese_source_plain_translated.txt",
			"annotated_translation": "MT/all/Chinese_source_annotated_plain_translated.txt",
			"target": "MT/all/Chinese_target.txt",
			"source": "MT/all/Chinese_source_plain.txt"
	},
	"French": {
			"dataset": "../datasets/French.json",
			"plain_translation": "MT/all/French_source_plain_translated.txt",
			"annotated_translation": "MT/all/French_source_annotated_plain_translated.txt",
			"target": "MT/all/French_target.txt",
			"source": "MT/all/French_source_plain.txt"
	},
	"German": {
			"dataset": "../datasets/German.json",
			"plain_translation": "MT/all/German_source_plain_translated.txt",
			"annotated_translation": "MT/all/German_source_annotated_plain_translated.txt",
			"target": "MT/all/German_target.txt",
			"source": "MT/all/German_source_plain.txt"
	},
	"Greek": {
			"dataset": "../datasets/Greek.json",
			"plain_translation": "MT/all/Greek_source_plain_translated.txt",
			"annotated_translation": "MT/all/Greek_source_annotated_plain_translated.txt",
			"target": "MT/all/Greek_target.txt",
			"source": "MT/all/Greek_source_plain.txt"
	},
	"Icelandic": {
			"dataset": "../datasets/Icelandic.json",
			"plain_translation": "MT/all/Icelandic_source_plain_translated.txt",
			"annotated_translation": "MT/all/Icelandic_source_annotated_plain_translated.txt",
			"target": "MT/all/Icelandic_target.txt",
			"source": "MT/all/Icelandic_source_plain.txt"
	},
	"Italian": {
			"dataset": "../datasets/Italian.json",
			"plain_translation": "MT/all/Italian_source_plain_translated.txt",
			"annotated_translation": "MT/all/Italian_source_annotated_plain_translated.txt",
			"target": "MT/all/Italian_target.txt",
			"source": "MT/all/Italian_source_plain.txt"
	},
	"Northern-Kurdish": {
			"dataset": "../datasets/Northern-Kurdish.json",
			"plain_translation": "MT/all/Northern-Kurdish_source_plain_translated.txt",
			"annotated_translation": "MT/all/Northern-Kurdish_source_annotated_plain_translated.txt",
			"target": "MT/all/Northern_target.txt",
			"source": "MT/all/Northern-Kurdish_source_plain.txt"
	},
	"Portuguese": {
			"dataset": "../datasets/Portuguese.json",
			"plain_translation": "MT/all/Portuguese_source_plain_translated.txt",
			"annotated_translation": "MT/all/Portuguese_source_annotated_plain_translated.txt",
			"target": "MT/all/Portuguese_target.txt",
			"source": "MT/all/Portuguese_source_plain.txt"
	},
	"Spanish": {
			"dataset": "../datasets/Spanish.json",
			"plain_translation": "MT/all/Spanish_source_plain_translated.txt",
			"annotated_translation": "MT/all/Spanish_source_annotated_plain_translated.txt",
			"target": "MT/all/Spanish_target.txt",
			"source": "MT/all/Spanish_source_plain.txt"
	},
	"Russian": {
			"dataset": "../datasets/Russian.json",
			"plain_translation": "MT/all/Russian_source_plain_translated.txt",
			"annotated_translation": "MT/all/Russian_source_annotated_plain_translated.txt",
			"target": "MT/all/Russian_target.txt",
			"source": "MT/all/Russian_source_plain.txt"
	},
}

for language in files:

	with open(files[language]["dataset"], "r") as f:
		dataset = json.load(f)

	with open(files[language]["plain_translation"], "r") as f:
		plain_trans = f.read().splitlines()

	with open(files[language]["annotated_translation"], "r") as f:
		annotated_trans = f.read().splitlines()

	with open(files[language]["source"], "r") as f:
		source = f.read().splitlines()

	print(language)
	# print(len([i["source_plain"] for i in dataset]))
	# print(len(plain_trans))
	# print(len(annotated_trans))
	# print()

	only_native_source, only_native_source_annotated, only_native_target = list(), list(), list()
	only_native_plain_translation, only_native_annotated_translation = list(), list()
	
	counter = 0
	identical = 0
	for i in dataset:
		l_tags = set(i["words_in_L_tags"].values())
		N_tags = set(i["words_in_N_tags"].values())

		if len(l_tags & N_tags) < len(N_tags): # there is at least one element that is different in the loanword and replacement sets
			# if i["source_plain"] != source[counter]:
			# 	print("no")
			only_native_source.append(i["source_plain"])
			only_native_source_annotated.append(i["source_annotated_plain"])
			only_native_target.append(i["target"])
			
			only_native_plain_translation.append(plain_trans[counter])
			only_native_annotated_translation.append(annotated_trans[counter])

		counter += 1

		if i["source_plain"] == i["source_annotated_plain"]:
			identical += 1

	print(f"In {language}, among {counter}, {identical} are identical.")

	# with open("MT/only_loanword/" + language + "_only_native_source.txt", "w") as f:
	# 	f.write("\n".join(only_native_source))

	# with open("MT/only_loanword/" + language + "_only_native_source_annotated.txt", "w") as f:
	# 	f.write("\n".join(only_native_source_annotated))

	# with open("MT/only_loanword/" + language + "_only_native_target.txt", "w") as f:
	# 	f.write("\n".join(only_native_target))

	# with open("MT/only_loanword/" + language + "_only_native_plain_translation.txt", "w") as f:
	# 	f.write("\n".join(only_native_plain_translation))

	# with open("MT/only_loanword/" + language + "_only_native_annotated_translation.txt", "w") as f:
	# 	f.write("\n".join(only_native_annotated_translation))










