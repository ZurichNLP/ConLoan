# All
# Evaluation of translation of sentences without loanword replacement
sacrebleu MT/all/Chinese_source_plain_translated.txt -i MT/all/Chinese_target.txt -m bleu chrf
sacrebleu MT/all/French_source_plain_translated.txt -i MT/all/French_target.txt -m bleu chrf
sacrebleu MT/all/German_source_plain_translated.txt -i MT/all/German_target.txt -m bleu chrf
sacrebleu MT/all/Greek_source_plain_translated.txt -i MT/all/Greek_target.txt -m bleu chrf
sacrebleu MT/all/Icelandic_source_plain_translated.txt -i MT/all/Icelandic_target.txt -m bleu chrf
sacrebleu MT/all/Italian_source_plain_translated.txt -i MT/all/Italian_target.txt -m bleu chrf
sacrebleu MT/all/Northern-Kurdish_source_plain_translated.txt -i MT/all/Northern-Kurdish_target_GoogleTranslate.txt -m bleu chrf
sacrebleu MT/all/Portuguese_source_plain_translated.txt -i MT/all/Portuguese_target.txt -m bleu chrf
sacrebleu MT/all/Russian_source_plain_translated.txt -i MT/all/Russian_target.txt -m bleu chrf
sacrebleu MT/all/Spanish_source_plain_translated.txt -i MT/all/Spanish_target.txt -m bleu chrf

# Evaluation of translation of sentences with loanword replacement (including replacement of the loanword by itself)
sacrebleu MT/all/Chinese_source_annotated_plain_translated.txt -i MT/all/Chinese_target.txt -m bleu chrf
sacrebleu MT/all/French_source_annotated_plain_translated.txt -i MT/all/French_target.txt -m bleu chrf
sacrebleu MT/all/German_source_annotated_plain_translated.txt -i MT/all/German_target.txt -m bleu chrf
sacrebleu MT/all/Greek_source_annotated_plain_translated.txt -i MT/all/Greek_target.txt -m bleu chrf
sacrebleu MT/all/Icelandic_source_annotated_plain_translated.txt -i MT/all/Icelandic_target.txt -m bleu chrf
sacrebleu MT/all/Italian_source_annotated_plain_translated.txt -i MT/all/Italian_target.txt -m bleu chrf
sacrebleu MT/all/Northern-Kurdish_source_annotated_plain_translated.txt -i MT/all/Northern-Kurdish_target_GoogleTranslate.txt -m bleu chrf
sacrebleu MT/all/Portuguese_source_annotated_plain_translated.txt -i MT/all/Portuguese_target.txt -m bleu chrf
sacrebleu MT/all/Russian_source_annotated_plain_translated.txt -i MT/all/Russian_target.txt -m bleu chrf
sacrebleu MT/all/Spanish_source_annotated_plain_translated.txt -i MT/all/Spanish_target.txt -m bleu chrf

# Sentences containing at least one native replacement
# Evaluation of translation of sentences that have at least one native replacement but before the loanword replacement
sacrebleu MT/only_loanword/Chinese_only_native_plain_translation.txt -i MT/only_loanword/Chinese_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/French_only_native_plain_translation.txt -i MT/only_loanword/French_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/German_only_native_plain_translation.txt -i MT/only_loanword/German_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Greek_only_native_plain_translation.txt -i MT/only_loanword/Greek_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Icelandic_only_native_plain_translation.txt -i MT/only_loanword/Icelandic_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Italian_only_native_plain_translation.txt -i MT/only_loanword/Italian_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Northern-Kurdish_only_native_plain_translation.txt -i MT/only_loanword/Northern-Kurdish_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Portuguese_only_native_plain_translation.txt -i MT/only_loanword/Portuguese_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Russian_only_native_plain_translation.txt -i MT/only_loanword/Russian_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Spanish_only_native_plain_translation.txt -i MT/only_loanword/Spanish_only_native_target.txt -m bleu chrf

# Evaluation of translation of sentences with loanword replacement (excluding replacement of the loanword by itself)
sacrebleu MT/only_loanword/Chinese_only_native_annotated_translation.txt -i MT/only_loanword/Chinese_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/French_only_native_annotated_translation.txt -i MT/only_loanword/French_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/German_only_native_annotated_translation.txt -i MT/only_loanword/German_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Greek_only_native_annotated_translation.txt -i MT/only_loanword/Greek_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Icelandic_only_native_annotated_translation.txt -i MT/only_loanword/Icelandic_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Italian_only_native_annotated_translation.txt -i MT/only_loanword/Italian_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Northern-Kurdish_only_native_annotated_translation.txt -i MT/only_loanword/Northern-Kurdish_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Portuguese_only_native_annotated_translation.txt -i MT/only_loanword/Portuguese_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Russian_only_native_annotated_translation.txt -i MT/only_loanword/Russian_only_native_target.txt -m bleu chrf
sacrebleu MT/only_loanword/Spanish_only_native_annotated_translation.txt -i MT/only_loanword/Spanish_only_native_target.txt -m bleu chrf