import re

files = {
	"ckb": {
		"other-script": "selected_corpora/Central-Kurdish/KASET-ckb_code-switching-other-script.txt",
		"same-script": "selected_corpora/Central-Kurdish/KASET-ckb_code-switching-same-script.txt"
	},
	"kmr": {
		"other-script":"selected_corpora/Northern-Kurdish/KASET-kmr-code-switching-other-script.txt",
		"same-script":"selected_corpora/Northern-Kurdish/KASET-kmr-code-switching-same-script.txt"
	}
}

def process_sentence(sentence):
	# Check for unclosed tags
	open_tags = re.findall(r"<foreign\s+lang=\".*?\">", sentence)
	close_tags = re.findall(r"</foreign>", sentence)
	
	if len(open_tags) != len(close_tags):
		raise ValueError("There is an unclosed <foreign> tag in the sentence.")
	
	# Step 1: Replace <foreign> tags with <F_i>
	foreign_index = 1
	def replace_with_F(match):
		nonlocal foreign_index
		lang = match.group(1)
		content = match.group(2)
		replacement = f'<F{foreign_index} lang="{lang}">{content}</F{foreign_index}>'
		foreign_index += 1
		return replacement

	# Original sentence with F1, F2, ...
	step_1_sentence = re.sub(r"<foreign lang=\"(.*?)\">(.*?)</foreign>", replace_with_F, sentence)

	# Step 2: Replace <F_i> tags with empty <N_i> tags
	final_sentence = re.sub(r"<F(\d+) lang=\"(.*?)\">(.*?)</F\1>", r"<N\1></N\1>", step_1_sentence)

	# Step 3: Remove all tags, leaving only the content
	no_tag_sentence = re.sub(r"<.*?>", "", step_1_sentence)
	
	return step_1_sentence, final_sentence, no_tag_sentence


for dialect in files:
	for script_mode in files[dialect]:
		with open(files[dialect][script_mode], "r") as f:
			data = f.read().splitlines()

		sentences = list()
		for i in data:
			i = i.strip()
			# print(i)
			s, t, p = process_sentence(i)
			
			if t != "<N1></N1>" and t !="<N1></N1>." and len(t) > 13:
				sentences.append(p + "\n" + s + "\n" + t + "\n")
			
		with open("selected_corpora/" + dialect + "_" + script_mode + ".tsv", "w") as f:
			f.write("\n".join(sentences))
