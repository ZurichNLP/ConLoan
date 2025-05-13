#!/bin/bash
declare -A lang_codes=(
    ["Northern-Kurdish"]="ku"
)

process_language() {
    local lang=$1
    local lang_code=${lang_codes[$lang]}
    local pairs_file="${lang}-loanword-native.tsv"
    local corpus_path="/local/scratch/ahmadi/OSCAR/original/txt/${lang_code}.txt"
    
    echo "Processing $lang ($lang_code)..."
    
    # Get total words in corpus first
    echo "Counting total words in corpus..."
    total_words=$(wc -w < "$corpus_path")
    echo "Total words in corpus: $total_words"
    
    # Create a temporary file with all words to count, adding word boundaries
    cut -f1 "$pairs_file" | sed 's/^/ /' | sed 's/$/ /' > words_to_count.tmp
    cut -f2 "$pairs_file" | sed 's/^/ /' | sed 's/$/ /' >> words_to_count.tmp
    
    # Count all words in one pass
    echo "Counting words..."
    tr '[:upper:]' '[:lower:]' < "$corpus_path" |
    sed 's/^/ /' | sed 's/$/ /' |
    grep -of words_to_count.tmp |
    tr -d ' ' |
    sort | uniq -c > counts.tmp
    
    # Modified output header with normalized frequencies only
    echo -e "Loanword\tNative\tRel_Loan_Freq\tRel_Native_Freq" > "${lang}_frequencies.tsv"
    
    while IFS=$'\t' read -r loanword native; do
        loanword_lower=$(echo "$loanword" | tr '[:upper:]' '[:lower:]')
        native_lower=$(echo "$native" | tr '[:upper:]' '[:lower:]')
        
        loan_freq=$(awk -v word="$loanword_lower" '$2==word {print $1}' counts.tmp)
        native_freq=$(awk -v word="$native_lower" '$2==word {print $1}' counts.tmp)
        
        loan_freq=${loan_freq:-0}
        native_freq=${native_freq:-0}
        
        # Calculate relative frequencies
        rel_loan=$(awk -v freq="$loan_freq" -v total="$total_words" 'BEGIN {printf "%.10f", freq/total}')
        rel_native=$(awk -v freq="$native_freq" -v total="$total_words" 'BEGIN {printf "%.10f", freq/total}')
        
        echo -e "$loanword\t$native\t$rel_loan\t$rel_native" >> "${lang}_frequencies.tsv"
    done < "$pairs_file"
    
    # Clean up
    rm words_to_count.tmp counts.tmp
}

# Process each language
for lang in "${!lang_codes[@]}"; do
    process_language "$lang"
done
