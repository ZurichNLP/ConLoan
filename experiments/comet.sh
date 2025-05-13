# comet-score -s MT/all/ChiMT/all/Chinese_source_plain.txt nese_source_plain.txt -t MT/all/Chinese_source_plain_translated.txt -r MT/all/Chinese_target.txt  --gpus 0 

# All
# Evaluation of translation of sentences without loanword replacement
comet-score -s MT/all/Chinese_source_plain.txt -t MT/all/Chinese_source_plain_translated.txt -r MT/all/Chinese_target.txt --gpu 0
comet-score -s MT/all/French_source_plain.txt -t MT/all/French_source_plain_translated.txt -r MT/all/French_target.txt --gpu 0
comet-score -s MT/all/German_source_plain.txt -t MT/all/German_source_plain_translated.txt -r MT/all/German_target.txt --gpu 0
comet-score -s MT/all/Greek_source_plain.txt -t MT/all/Greek_source_plain_translated.txt -r MT/all/Greek_target.txt --gpu 0
comet-score -s MT/all/Icelandic_source_plain.txt -t MT/all/Icelandic_source_plain_translated.txt -r MT/all/Icelandic_target.txt --gpu 0
comet-score -s MT/all/Italian_source_plain.txt -t MT/all/Italian_source_plain_translated.txt -r MT/all/Italian_target.txt --gpu 0
comet-score -s MT/all/Northern-Kurdish_source_plain.TXT -t MT/all/Northern-Kurdish_source_plain_translated.txt -r MT/all/Northern-Kurdish_target_GoogleTranslate.txt --gpu 0
comet-score -s MT/all/Portuguese_source_plain.txt -t MT/all/Portuguese_source_plain_translated.txt -r MT/all/Portuguese_target.txt --gpu 0
comet-score -s MT/all/Russian_source_plain.txt -t MT/all/Russian_source_plain_translated.txt -r MT/all/Russian_target.txt --gpu 0
comet-score -s MT/all/Spanish_source_plain.txt -t MT/all/Spanish_source_plain_translated.txt -r MT/all/Spanish_target.txt --gpu 0

# Evaluation of translation of sentences with loanword replacement (including replacement of the loanword by itself)
comet-score -s MT/all/Chinese_source_annotated_plain.txt -t MT/all/Chinese_source_annotated_plain_translated.txt -r MT/all/Chinese_target.txt --gpu 0
comet-score -s MT/all/French_source_annotated_plain.txt -t MT/all/French_source_annotated_plain_translated.txt -r MT/all/French_target.txt --gpu 0
comet-score -s MT/all/German_source_annotated_plain.txt -t MT/all/German_source_annotated_plain_translated.txt -r MT/all/German_target.txt --gpu 0
comet-score -s MT/all/Greek_source_annotated_plain.txt -t MT/all/Greek_source_annotated_plain_translated.txt -r MT/all/Greek_target.txt --gpu 0
comet-score -s MT/all/Icelandic_source_annotated_plain.txt -t MT/all/Icelandic_source_annotated_plain_translated.txt -r MT/all/Icelandic_target.txt --gpu 0
comet-score -s MT/all/Italian_source_annotated_plain.txt -t MT/all/Italian_source_annotated_plain_translated.txt -r MT/all/Italian_target.txt --gpu 0
comet-score -s MT/all/Northern-Kurdish_source_annotated_plain.txt -t MT/all/Northern-Kurdish_source_annotated_plain_translated.txt -r MT/all/Northern-Kurdish_target_GoogleTranslate.txt --gpu 0
comet-score -s MT/all/Portuguese_source_annotated_plain.txt -t MT/all/Portuguese_source_annotated_plain_translated.txt -r MT/all/Portuguese_target.txt --gpu 0
comet-score -s MT/all/Russian_source_annotated_plain.txt -t MT/all/Russian_source_annotated_plain_translated.txt -r MT/all/Russian_target.txt --gpu 0
comet-score -s MT/all/Spanish_source_annotated_plain.txt -t MT/all/Spanish_source_annotated_plain_translated.txt -r MT/all/Spanish_target.txt --gpu 0

# Sentences containing at least one native replacement
Evaluation of translation of sentences that have at least one native replacement but before the loanword replacement
comet-score -s MT/only_loanword/Chinese_only_native_source.txt -t MT/only_loanword/Chinese_only_native_plain_translation.txt -r MT/only_loanword/Chinese_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/French_only_native_source.txt -t MT/only_loanword/French_only_native_plain_translation.txt -r MT/only_loanword/French_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/German_only_native_source.txt -t MT/only_loanword/German_only_native_plain_translation.txt -r MT/only_loanword/German_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Greek_only_native_source.txt -t MT/only_loanword/Greek_only_native_plain_translation.txt -r MT/only_loanword/Greek_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Icelandic_only_native_source.txt -t MT/only_loanword/Icelandic_only_native_plain_translation.txt -r MT/only_loanword/Icelandic_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Italian_only_native_source.txt -t MT/only_loanword/Italian_only_native_plain_translation.txt -r MT/only_loanword/Italian_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Northern-Kurdish_only_native_source.txt -t MT/only_loanword/Northern-Kurdish_only_native_plain_translation.txt -r MT/only_loanword/Northern-Kurdish_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Portuguese_only_native_source.txt -t MT/only_loanword/Portuguese_only_native_plain_translation.txt -r MT/only_loanword/Portuguese_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Russian_only_native_source.txt -t MT/only_loanword/Russian_only_native_plain_translation.txt -r MT/only_loanword/Russian_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Spanish_only_native_source.txt -t MT/only_loanword/Spanish_only_native_plain_translation.txt -r MT/only_loanword/Spanish_only_native_target.txt --gpu 0


# Evaluation of translation of sentences with loanword replacement (excluding replacement of the loanword by itself)
comet-score -s MT/only_loanword/Chinese_only_native_source_annotated.txt -t MT/only_loanword/Chinese_only_native_annotated_translation.txt -r MT/only_loanword/Chinese_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/French_only_native_source_annotated.txt -t MT/only_loanword/French_only_native_annotated_translation.txt -r MT/only_loanword/French_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/German_only_native_source_annotated.txt -t MT/only_loanword/German_only_native_annotated_translation.txt -r MT/only_loanword/German_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Greek_only_native_source_annotated.txt -t MT/only_loanword/Greek_only_native_annotated_translation.txt -r MT/only_loanword/Greek_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Icelandic_only_native_source_annotated.txt -t MT/only_loanword/Icelandic_only_native_annotated_translation.txt -r MT/only_loanword/Icelandic_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Italian_only_native_source_annotated.txt -t MT/only_loanword/Italian_only_native_annotated_translation.txt -r MT/only_loanword/Italian_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Northern-Kurdish_only_native_source_annotated.txt -t MT/only_loanword/Northern-Kurdish_only_native_annotated_translation.txt -r MT/only_loanword/Northern-Kurdish_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Portuguese_only_native_source_annotated.txt -t MT/only_loanword/Portuguese_only_native_annotated_translation.txt -r MT/only_loanword/Portuguese_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Russian_only_native_source_annotated.txt -t MT/only_loanword/Russian_only_native_annotated_translation.txt -r MT/only_loanword/Russian_only_native_target.txt --gpu 0
comet-score -s MT/only_loanword/Spanish_only_native_source_annotated.txt -t MT/only_loanword/Spanish_only_native_annotated_translation.txt -r MT/only_loanword/Spanish_only_native_target.txt --gpu 0

# # Evaluation of English translation of target sentences before annotation 
comet-score -s translations/Chinese_target.txt -t translations/Chinese_translated.txt -r translations/Chinese_source_plain.txt --gpu 0
comet-score -s translations/French_target.txt -t translations/French_translated.txt -r translations/French_source_plain.txt --gpu 0
comet-score -s translations/German_target.txt -t translations/German_translated.txt -r translations/German_source_plain.txt --gpu 1
comet-score -s translations/Greek_target.txt -t translations/Greek_translated.txt -r translations/Greek_source_plain.txt --gpu 1
comet-score -s translations/Icelandic_target.txt -t translations/Icelandic_translated.txt -r translations/Icelandic_source_plain.txt --gpu 1
comet-score -s translations/Italian_target.txt -t translations/Italian_translated.txt -r translations/Italian_source_plain.txt --gpu 1
comet-score -s translations/Northern-Kurdish_target.txt -t translations/Northern-Kurdish_translated.txt -r translations/Northern-Kurdish_source_plain.txt --gpu 1
comet-score -s translations/Portuguese_target.txt -t translations/Portuguese_translated.txt -r translations/Portuguese_source_plain.txt --gpu 1
comet-score -s translations/Russian_target.txt -t translations/Russian_translated.txt -r translations/Russian_source_plain.txt --gpu 1
comet-score -s translations/Spanish_target.txt -t translations/Spanish_translated.txt -r translations/Spanish_source_plain.txt --gpu 1

# # Evaluation of English translation of target sentences after annotation (with loanword replacement - excluding replacement of the loanword by itself)
comet-score -s translations/Chinese_target.txt -t translations/Chinese_translated.txt -r translations/Chinese_source_annotated_plain.txt --gpu 1
comet-score -s translations/French_target.txt -t translations/French_translated.txt -r translations/French_source_annotated_plain.txt --gpu 1
comet-score -s translations/German_target.txt -t translations/German_translated.txt -r translations/German_source_annotated_plain.txt --gpu 1
comet-score -s translations/Greek_target.txt -t translations/Greek_translated.txt -r translations/Greek_source_annotated_plain.txt --gpu 1
comet-score -s translations/Icelandic_target.txt -t translations/Icelandic_translated.txt -r translations/Icelandic_source_annotated_plain.txt --gpu 1
comet-score -s translations/Italian_target.txt -t translations/Italian_translated.txt -r translations/Italian_source_annotated_plain.txt --gpu 1
comet-score -s translations/Northern-Kurdish_target.txt -t translations/Northern-Kurdish_translated.txt -r translations/Northern-Kurdish_source_annotated_plain.txt --gpu 1
comet-score -s translations/Portuguese_target.txt -t translations/Portuguese_translated.txt -r translations/Portuguese_source_annotated_plain.txt --gpu 1
comet-score -s translations/Russian_target.txt -t translations/Russian_translated.txt -r translations/Russian_source_annotated_plain.txt --gpu 1
comet-score -s translations/Spanish_target.txt -t translations/Spanish_translated.txt -r translations/Spanish_source_annotated_plain.txt --gpu 1
