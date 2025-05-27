# ConLoan: A Contrastive Multilingual Dataset for Evaluating Loanwords

<p align="center" width="100%">
<img width="40%" src="loanwords_meme.png" alt="loanwords">
</p>

---

## What if English sounded completely different?

Consider this familiar opening from the U.S. Constitution:

<table>
<tr>
<td width="50%">

**🏛️ Standard English (with loanwords)**
> "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defense, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

</td>
<td width="50%">

**⚔️ "Pure" English (native words only)**
> "We the Folk of the Foroned Riches, to make a more flawless oneship, build rightness, bring frith and stillness to our land, shield one another, uphold the overall welfare, and hold fast the Blessings of Freedom to ourselves and our offspring, do foresay and lay down this lawbook for the foroned riches of Americksland."

</td>
</tr>
</table>

The second version uses predominantly Germanic roots, avoiding Latin and French borrowings that entered English over centuries. This isn't just a linguistic curiosity; there's even a movement called [**Anglish**](https://anglish.org/wiki/Anglish) dedicated to this approach!

## ConLoan

While the "pure English" example might seem amusing, **loanword integration is happening right now, in every language, every day**. From "WiFi" entering global vocabularies to "kawaii" spreading beyond Japanese, languages constantly borrow and adapt words from each other. **But how does modern language technology handle this linguistic reality?**

This is exactly what we try to answer with ConLoan. ConLoan is a novel contrastive dataset comprising sentences with and without loanwords across 10 languages, namely **Chinese, French, German, Greek, Icelandic, Italian, Northern Kurdish, Portuguese, Russian** and **Spanish**. 

<!-- This repository contains the data, code, and resources from the paper "ConLoan – A Contrastive Multilingual Dataset for Evaluating Loanwords" published at ACL 2025. -->

## Dataset Overview

ConLoan contains sentences having one or more loanwords along with their equivalents where the loanwords are manually replaced by native alternatives. Here is an example:

| **sentence with loanwords** | **equivalent with native replacements** |
|---------------------------|------------------------------|
| Mais tout ceci ne nous empêche pas de constater que nous sommes relativement impuissants, car lorsque les négociateurs des deux parties prendront l'avion ce **<span style="color: red;">week-end</span>** pour retourner aux États-Unis, nous ne pourrons nous empêcher de penser qu'à chaque fois que cent dollars sont dépensés pour le processus de paix dans la région, 60 dollars sont payés par l'Union européenne. | Mais tout ceci ne nous empêche pas de constater que nous sommes relativement impuissants, car lorsque les négociateurs des deux parties prendront l'avion cette **<span style="color: blue;">fin de semaine</span>** pour retourner aux États-Unis, nous ne pourrons nous empêcher de penser qu'à chaque fois que cent dollars sont dépensés pour le processus de paix dans la région, 60 dollars sont payés par l'Union européenne. |
| Cela impliquerait également tous les frais de transaction occasionnés par la vente de vos actions, puis par leur rachat après le **<span style="color: red;">crack</span>** boursier. | Cela impliquerait également tous les frais de transaction occasionnés par la vente de vos actions, puis par leur rachat après la **<span style="color: blue;">débacle</span>** boursière. |
| Les propositions de la Commission dont nous discutons ici permettent le **<span style="color: red;">lifting</span>** dont elle a besoin. | Les propositions de la Commission dont nous discutons ici permettent le **<span style="color: blue;">lissage</span>** dont elle a besoin. |

This table clearly shows the contrast between borrowed words (in red) and their native French alternatives (in blue), demonstrating how ConLoan provides parallel sentences that differ only in their use of loanwords versus native vocabulary. The dataset also provides translations in English with other meta-data.

In this repository, you can find two main data folders:

- [**`annotations/`**](annotations/): Raw annotations from individual annotators (per language)
- [**`datasets/`**](datasets/): Processed contrastive sentence pairs in JSON format and TSV files with replacements. Here are the data files per Language:
  - **JSON files**: Contain contrastive sentence pairs with loanwords and their native replacements
  - **`*_all_replacements.tsv`**: All annotated loanword replacements, including cases where loanwords were not replaced
  - **`*_replaced_loanwords.tsv`**: Only cases where loanwords were successfully replaced with native alternatives

| Language | Annotations (JSON) | All Replacements (TSV) | Replaced Loanwords (TSV) |
|----------|-----------|------------------------|--------------------------|
| Chinese | [`Chinese.json`](datasets/Chinese.json) | [`Chinese_all_replacements.tsv`](datasets/Chinese_all_replacements.tsv) | [`Chinese_replaced_loanwords.tsv`](datasets/Chinese_replaced_loanwords.tsv) |
| French | [`French.json`](datasets/French.json) | [`French_all_replacements.tsv`](datasets/French_all_replacements.tsv) | [`French_replaced_loanwords.tsv`](datasets/French_replaced_loanwords.tsv) |
| German | [`German.json`](datasets/German.json) | [`German_all_replacements.tsv`](datasets/German_all_replacements.tsv) | [`German_replaced_loanwords.tsv`](datasets/German_replaced_loanwords.tsv) |
| Greek | [`Greek.json`](datasets/Greek.json) | [`Greek_all_replacements.tsv`](datasets/Greek_all_replacements.tsv) | [`Greek_replaced_loanwords.tsv`](datasets/Greek_replaced_loanwords.tsv) |
| Icelandic | [`Icelandic.json`](datasets/Icelandic.json) | [`Icelandic_all_replacements.tsv`](datasets/Icelandic_all_replacements.tsv) | [`Icelandic_replaced_loanwords.tsv`](datasets/Icelandic_replaced_loanwords.tsv) |
| Italian | [`Italian.json`](datasets/Italian.json) | [`Italian_all_replacements.tsv`](datasets/Italian_all_replacements.tsv) | [`Italian_replaced_loanwords.tsv`](datasets/Italian_replaced_loanwords.tsv) |
| Northern Kurdish | [`Northern-Kurdish.json`](datasets/Northern-Kurdish.json) | [`Northern-Kurdish_all_replacements.tsv`](datasets/Northern-Kurdish_all_replacements.tsv) | [`Northern-Kurdish_replaced_loanwords.tsv`](datasets/Northern-Kurdish_replaced_loanwords.tsv) |
| Portuguese | [`Portuguese.json`](datasets/Portuguese.json) | [`Portuguese_all_replacements.tsv`](datasets/Portuguese_all_replacements.tsv) | [`Portuguese_replaced_loanwords.tsv`](datasets/Portuguese_replaced_loanwords.tsv) |
| Russian | [`Russian.json`](datasets/Russian.json) | [`Russian_all_replacements.tsv`](datasets/Russian_all_replacements.tsv) | [`Russian_replaced_loanwords.tsv`](datasets/Russian_replaced_loanwords.tsv) |
| Spanish | [`Spanish.json`](datasets/Spanish.json) | [`Spanish_all_replacements.tsv`](datasets/Spanish_all_replacements.tsv) | [`datasets/Spanish_replaced_loanwords.tsv`](datasets/Spanish_replaced_loanwords.tsv) |

You can also find the loanword lists collected per language from sources reported in the paper (mainly Wiktionary) in the [**`loanwords/`**](loanwords/) folder.

## Annotation Guidelines

For detailed information about the annotation process and guidelines used in creating this dataset, see [`loanword_annotation_guide.md`](loanword_annotation_guide.md).

## Code Files

| File | Description |
|------|-------------|
| [`analyze.py`](analyze.py) | General analysis utilities for the ConLoan dataset |
| [`create_corpus.py`](create_corpus.py) | Script for creating the corpus from raw annotations |
| [`donor.py`](donor.py) | Analysis of donor language distributions |
| [`data.json`](data.json) | Configuration file or metadata |
| [`AppScripts/`](AppScripts/) | Google Apps Script code used for annotation spreadsheets |
| [`experiments/surprisal.py`](experiments/surprisal.py) | Language model surprisal analysis |
| [`experiments/t-test.py`](experiments/t-test.py) | Statistical significance testing for surprisal differences |
| [`experiments/ridge_plot.R`](experiments/ridge_plot.R) | R script for creating ridge plots (density visualizations) |

The [`experiments/`](experiments/) folder contains scripts and results for the experiments described in the paper.

## Citation

If you're using this project, please cite [this paper]():

```
  @inproceedings{ahmadi2025conloan,
   title = {ConLoan--A Contrastive Multilingual Dataset for Evaluating Loanwords},
   author = {
    Ahmadi, Sina and,
    Hess, Micha David  and,
    Álvarez Mellado, Elena  and,
    Battisti, Alessia and,
    Ding, Cui and,
    Göhring, Anne and,
    Gao, Yingqiang and,
    Jiang, Zifan and,
    Michail, Andrianos and,
    Morad, Peshmerge and,
    Niklaus, Joel and,
    Panagiotopoulou, Maria Christina and,
    Perrella, Stefano and,
    Opitz, Juri and,
    Shaitarova, Anastassia and,
    Sennrich, Rico
    },
   publisher = {Association for Computational Linguistics},
   year = {2025},
}
```

## License

This project is fully open-source with the permissive [MIT license](LICENSE).
