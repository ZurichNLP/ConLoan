datasets = {
	"Chinese": "/home/user/ahmadi/perplexities/only_native_source_Chinese.tsv",
	"French": "/home/user/ahmadi/perplexities/only_native_source_French.tsv",
	"German": "/home/user/ahmadi/perplexities/only_native_source_German.tsv",
	"Greek": "/home/user/ahmadi/perplexities/only_native_source_Greek.tsv",
	"Icelandic": "/home/user/ahmadi/perplexities/only_native_source_Icelandic.tsv",
	"Italian": "/home/user/ahmadi/perplexities/only_native_source_Italian.tsv",
	"Northern-Kurdish": "/home/user/ahmadi/perplexities/only_native_source_Northern-Kurdish.tsv",
	"Portuguese": "/home/user/ahmadi/perplexities/only_native_source_Portuguese.tsv",
	"Russian": "/home/user/ahmadi/perplexities/only_native_source_Russian.tsv",
	"Spanish": "/home/user/ahmadi/perplexities/only_native_source_Spanish.tsv"
}

for language in datasets:
	with open(datasets[language].replace(".tsv", "_sentence.tsv"), "r") as f:
		source = f.read().splitlines()
	
	annotated_file_name = "/home/user/ahmadi/perplexities/only_native_source_annotated_%s_sentence.tsv"%language
	print(annotated_file_name)
	with open(annotated_file_name, "r") as f:
		annotated = f.read().splitlines()

	ppl_source_all, ppl_annotated_all = list(), list()
	for i, j in zip(source, annotated):
		ppl_source, ppl_annotated = i.split("\t")[1], j.split("\t")[1]
		# print(float(ppl_source), float(ppl_annotated))
		ppl_source_all.append(float(ppl_source))
		ppl_annotated_all.append(float(ppl_annotated))

	print(language, len(ppl_source_all), len(ppl_annotated_all))
	print("Source perplexity:", sum(ppl_source_all) / len(ppl_source_all))
	print("Native (annotated) perplexity:", sum(ppl_annotated_all) / len(ppl_annotated_all))