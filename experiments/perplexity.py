import json
from evaluate import load

perplexity = load("perplexity", module_type="metric")
# input_texts = ["lorem ipsum", "Happy Birthday!", "Bienvenue"]
# results = perplexity.compute(model_id='sharpbai/Llama-2-7b-hf', batch_size=4, add_start_token=False, predictions=input_texts)


files = {
	"Chinese": "../datasets/Chinese.json",
	"French": "../datasets/French.json",
	"German": "../datasets/German.json",
	"Greek": "../datasets/Greek.json",
	"Icelandic": "../datasets/Icelandic.json",
	"Italian": "../datasets/Italian.json",
	"Northern-Kurdish": "../datasets/Northern-Kurdish.json",
	"Portuguese": "../datasets/Portuguese.json",
	"Spanish": "../datasets/Spanish.json",
	"Russian": "../datasets/Russian.json",
}

for language in files:

	with open(files[language], "r") as f:
		dataset = json.load(f)

	source, source_annotated = list(), list()
	only_native_source, only_native_source_annotated = list(), list()

	counter = 0
	for i in dataset:
		source.append(i["source_plain"])
		source_annotated.append(i["source_annotated_plain"])

		l_tags = set(i["words_in_L_tags"].values())
		N_tags = set(i["words_in_N_tags"].values())

		if len(l_tags & N_tags) < len(N_tags): # there is at least one element that is different in the loanword and replacement sets
			only_native_source.append(i["source_plain"])
			only_native_source_annotated.append(i["source_annotated_plain"])

	print(language)
	results = perplexity.compute(model_id='sharpbai/Llama-2-7b-hf', add_start_token=False, predictions=source)
	print("All - original")
	print(round(results["mean_perplexity"], 2))
	print(round(results["perplexities"][0], 2))

	results_all_source_annotated = perplexity.compute(model_id='sharpbai/Llama-2-7b-hf', batch_size=4, add_start_token=False, predictions=source_annotated)
	print("All - annotated")
	print(round(results["mean_perplexity"], 2))
	print(round(results["perplexities"][0], 2))

	results_only_native_source = perplexity.compute(model_id='sharpbai/Llama-2-7b-hf', batch_size=4, add_start_token=False, predictions=only_native_source)
	print("Native - original")
	print(round(results["mean_perplexity"], 2))
	print(round(results["perplexities"][0], 2))

	results_only_native_source_annotated = perplexity.compute(model_id='sharpbai/Llama-2-7b-hf', batch_size=4, add_start_token=False, predictions=only_native_source_annotated)
	print("Native - annotated")
	print(round(results["mean_perplexity"], 2))
	print(round(results["perplexities"][0], 2))


	

