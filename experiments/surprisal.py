import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Check if a GPU is available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load a pre-trained GPT or LLaMA model (example uses GPT-2 here)
model_name = "sharpbai/Llama-2-7b-hf"  # You can use LLaMA or GPT model names gpt2
# model_llama_3 = "meta-llama/Meta-Llama-3-8B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Switch to evaluation mode
model.eval()

files = {
	"Chinese": "ConLoan/Chinese.json",
	"French": "ConLoan/French.json",
	"German": "ConLoan/German.json",
	"Greek": "ConLoan/Greek.json",
	"Icelandic": "ConLoan/Icelandic.json",
	"Italian": "ConLoan/Italian.json",
	"Northern-Kurdish": "ConLoan/Northern-Kurdish.json",
	"Portuguese": "ConLoan/Portuguese.json",
	"Spanish": "ConLoan/Spanish.json",
	"Russian": "ConLoan/Russian.json"
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

		if len(l_tags & N_tags) < len(N_tags):  # there is at least one element that is different in the loanword and replacement sets
			only_native_source.append(i["source_plain"])
			only_native_source_annotated.append(i["source_annotated_plain"])

	# Disable gradient calculation for faster inference
	datasets = {"only_native_source": only_native_source, "only_native_source_annotated": only_native_source_annotated}
	with torch.no_grad():
		for dataset_label in datasets:
			print(language, dataset_label)
			perplexities = []  # To store perplexities of each sentence
			for text in datasets[dataset_label]:
				# Tokenize each text string
				inputs = tokenizer(text, return_tensors="pt")
				input_ids = inputs["input_ids"]
				
				# Get model output
				outputs = model(input_ids, labels=input_ids)
				loss = outputs.loss
				
				# Multiply by the number of tokens to get sentence-level loss (undo normalization)
				sentence_loss = loss * input_ids.size(1)  # input_ids.size(1) gives the number of tokens in the sentence
				
				# Calculate sentence-level perplexity (without normalizing by the number of tokens)
				# perplexity = torch.exp(sentence_loss).item()
				# + "\t" + str(perplexity
				text_ppl = text + "\t" + str(sentence_loss.item())
				print(language + "\t", text_ppl)
				perplexities.append(text_ppl)

				# print(f"Perplexity for '{text}': {perplexity}")
			
			# # calculate the average perplexity across all texts
			# # print(perplexities)
			# # average_perplexity = sum(perplexities) / len(perplexities)
			# # print(f"Average Perplexity: {average_perplexity}")
			# # perplexities.append(str(average_perplexity))
			# # print("Average Perplexity - native: " + str(sum(perplexities_source_native) / len(perplexities_source_native)))

			with open("surprisal/%s_%s_sentence.tsv"%(dataset_label, language), "w") as f:
				f.write("\n".join(perplexities))