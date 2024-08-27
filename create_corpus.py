from GlotScript import sp
import wn
from wn.morphy import Morphy
import jieba
import json

def check_sentence(text, script) -> bool:
	# check code-switching
	try:
		if script in sp(text)[-1]["details"] and sp(text)[-1]["details"][script] == 1:
			return True
	except:
		return False
	return False

with open("data.json", "r") as f:
	files = json.load(f)

for lang_pair in files:
	with open(files[lang_pair]["source_file"], "r") as f:
		source = f.read().splitlines()

	with open(files[lang_pair]["target_file"], "r") as f:
		target = f.read().splitlines()

	with open(files[lang_pair]["loanwords_file"], "r") as f:
		loanwords = set([i.split("\t")[0] for i in f.read().splitlines()])

	print("Files read.")
	new_dataset, new_dataset_tool = list(), list()

	if files[lang_pair]["wordnet"] != False:
		wordnet = wn.Wordnet(files[lang_pair]["wordnet"], lemmatizer=Morphy())

	seen_words = list() # to diversify words

	for sentence, t_sentence in zip(source, target):
		# clean sentences
		sentence = sentence.replace("\t", " ").replace('"', " ")
		t_sentence = t_sentence.replace("\t", " ").replace('"', " ")

		# print(sp(sentence)[-1]["details"])
		if check_sentence(sentence, files[lang_pair]["script"]) and len(sentence) < 500 and len(sentence) > 40: # check if the sentence can be a good candidate
			new_sent = list()
			annot_sent = list()
			synonyms = list()
			flag = False
			counter = 1

			# word segmentation depending on the script
			if files[lang_pair]["script"] == "Hani":
				sentence_tokens = jieba.lcut(sentence)
			else:
				sentence_tokens = sentence.split()

			for i in sentence_tokens:
				# select a word only if it's a loanword, hasn't been seen and is not a named-entity

				if i in loanwords and i not in seen_words and not i.istitle():
					flag = True
					new_sent.append('<L%s>%s</L%s>'%(str(counter), i, str(counter)))
					annot_sent.append('<N%s></N%s>'%(str(counter),str(counter)))

					if files[lang_pair]["wordnet"] != False:
						syns = wordnet.synsets(i)
					else:
						syns = []

					if len(syns):
						synonyms = list(set([" ".join(i.lemmas()) for i in syns]))
						
						if i in synonyms:
							synonyms.remove(i)
						
					seen_words.append(i)
					counter += 1

				else:
					new_sent.append(i)
					annot_sent.append(i)

			if flag: # save only those that contain a loanword
				new_dataset.append(" ".join(new_sent) + "\t" + t_sentence + '\t' + " | ".join(synonyms)+ "\n" + " ".join(annot_sent) + "\t" + t_sentence + "\n\n")
				new_dataset_tool.append((sentence, t_sentence))

	print("%s collected."%len(new_dataset))
	with open("selected_corpora/%s.tsv"%lang_pair, "w") as f:
		f.write("\n".join(new_dataset))

	with open("selected_corpora/%s.src"%lang_pair, "w") as f:
		f.write("\n".join([i[0] for i in new_dataset_tool]))
	with open("selected_corpora/%s.tgt"%lang_pair, "w") as f:
		f.write("\n".join([i[1] for i in new_dataset_tool]))

