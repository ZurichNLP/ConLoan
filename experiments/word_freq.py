import json
from wordfreq import word_frequency

files = {
	"Chinese": "/home/user/ahmadi/ConLoan/Chinese.json",
	"French": "/home/user/ahmadi/ConLoan/French.json",
	"German": "/home/user/ahmadi/ConLoan/German.json",
	"Greek": "/home/user/ahmadi/ConLoan/Greek.json",
	"Icelandic": "/home/user/ahmadi/ConLoan/Icelandic.json",
	"Italian": "/home/user/ahmadi/ConLoan/Italian.json",
	# "Northern-Kurdish": "/home/user/ahmadi/ConLoan/Northern-Kurdish.json",
	"Portuguese": "/home/user/ahmadi/ConLoan/Portuguese.json",
	"Spanish": "/home/user/ahmadi/ConLoan/Spanish.json",
	"Russian": "/home/user/ahmadi/ConLoan/Russian.json"
}

lang_code = {
	"Chinese": "zh",
	"French": "fr",
	"German": "de",
	"Greek": "el",
	"Icelandic": "is",
	"Italian": "it",
	"Northern-Kurdish": "ku",
	"Portuguese": "pt",
	"Spanish": "es",
	"Russian": "ru"
}

for language in files:
	# print("Processing", language)
	with open(files[language], "r") as f:
		dataset = json.load(f)

	loanword_native = list()
	freq_table = list()
	loan_freq_bigger_than_native_freq = 0

	for entry in dataset:
		for i in entry["corresponding_words"]:
			if entry["corresponding_words"][i][0] != entry["corresponding_words"][i][1]:
				if (entry["corresponding_words"][i][0], entry["corresponding_words"][i][1]) not in loanword_native:
					loanword_native.append((entry["corresponding_words"][i][0].strip(), entry["corresponding_words"][i][1].strip()))

	loanword_native = set(loanword_native)
	# with open("/home/user/ahmadi/ConLoan/frequencies/%s-loanword-native.tsv"%language, "w") as f:
	# 	f.write("\n".join(loanword_native))
	
	for word in loanword_native:
		loanword_freq = word_frequency(word[0], lang_code[language])
		native_freq = word_frequency(word[1], lang_code[language])

		if loanword_freq > native_freq:
			loan_freq_bigger_than_native_freq += 1

		freq_table.append(f"{word[0]}\t{word[1]}\t{loanword_freq}\t{native_freq}")

	if len(loanword_native)-loan_freq_bigger_than_native_freq > loan_freq_bigger_than_native_freq:
		print(language, "more frequent: native")
	else:
		print(language, "more frequent: loanwords")

	with open(f"/home/user/ahmadi/ConLoan/frequencies/{language}_frequencies.tsv", "w") as f:
		f.write("\n".join(freq_table))