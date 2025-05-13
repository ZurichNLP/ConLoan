# Loanword Annotation Guide

Sina Ahmadi ([sina.ahmadi@uzh.ch](mailto:sina.ahmadi@uzh.ch))   
Created on June 25th, 2024   
Last Updated on July 15th, 2024

Thanks for participating in the plenary session. If you could not attend that session, please have a look at the [slides](https://sinaahmadi.github.io/docs/slides/Loanwords\_annotation\_slides.pdf) (or [handout](https://sinaahmadi.github.io/docs/slides/Loanwords\_annotation\_handout.pdf)) of the plenary session. Don't hesitate to reach out if you have any questions.

This document provides some information on the annotation task. 

# **Corpus selection**

After having collected a list of loanwords in the target languages (mostly from Wiktionary like [this one](https://en.wiktionary.org/wiki/Category:Serbo-Croatian\_terms\_borrowed\_from\_English)), I then sampled sentences containing loanwords from a few parallel corpora. Additionally, a few other criteria are considered in the candidate sentence selection as in excluding those containing code-switching. You can find your folder on Google Drive (please request access to make sure you are the only one having access).

# **Annotation**

## **CLoAn**

As you know, we have a specific tool for annotating loanwords called CLoAn: [https://github.com/chamisshe/CLoAn](https://github.com/chamisshe/CLoAn) You can install the tool and refer to the annotation guide to learn about all the nice functionalities at [https://github.com/chamisshe/CLoAn/blob/main/annotation\_guide.md](https://github.com/chamisshe/CLoAn/blob/main/annotation\_guide.md)

## **Google Spreadsheet (RECOMMENDED)**

I understand that some of you might not be comfortable with the command-line interface. If so, you can also use Google Spreadsheet for the annotation task. It's the same data but sentences are enriched with a few tags that would hopefully make the annotation process easier. This is how the spreadsheet looks like:

| Source | Target (Don't change ⚠️) | Suggestions | Comments? |
| ----- | :---- | :---- | :---- |
| Το **\<L1\>χιούμορ\</L1\>** *μοιάζει να* απευθύνεται σε παιδιά και όχι σε ενήλικες και, κατά τη γνώμη μου | The humour feels as if it is pitched at kids rather than adults |  |  |
| Ο **\<N1\>αστεϊσμός\</N1\>** *μοιάζει να* απευθύνεται σε παιδιά και όχι σε ενήλικες και, κατά τη γνώμη μου  | The humour feels as if it is pitched at kids rather than adults |  |  |
| CHECKBOX |  |  |  |

* **Original sentence:** Given a sentence, some loanwords are detected and marked with enumerated \<L\*\>\</L\*\> tags. Depending on the number of loanwords, the tags are numbered; like in the example where **\<L1\>χιούμορ\</L1\>** (humor) is tagged in Greek. Please note that the sentence might contain additional loanwords that are not tagged; make sure to read all the sentence. If so, feel free to add a new tag around other loanwords (like **\<L2\>word\</L2\>**).  
* **Your annotation:** In the next row of the same column, the same sentence is provided but with the loanword replaced with the **\<N\*\>\</N\*\>** tags. The tag number refers to that of the loanword in the original sentence. Your task is to insert the native alternative in between the **\<N\*\>\</N\>** tags. To draw your attention to case agreement, two preceding and succeeding tokens are set in *italics*. If you added a new tag in the original sentence, add the native alternative with the same tag number (as **\<N2\>word\_native\_alternative\</N2\>**). If the loanword cannot be replaced by any other alternative, you can simply add the loanword again. Otherwise, insert the native one.  
* **Translations:** the translation of the sentences in English are provided in the following column. If the translation doesn't correspond to the original sentence, skip it. There is no need to correct the translation. Please do not change it.  
* **Suggestions column:** To facilitate your task, we provide synonyms for the loanwords in that column based on WordNet. Regardless, you should consult other resources, like online dictionaries or thesauri, to come up with good replacements. (This column is empty for Ukranian and Russian; the first doesn't have a wordnet and the latter doesn't have an open-source one.)  
* **Comments column:** Any interesting phenomena or issue? Write them there for future consultation.  
* **Checkbox:** Finally, in the last row, there is a checkbox. Make sure to check it if you validate your annotation. If the sentence doesn't make sense, doesn’t contain any loanword or you want to skip it for any reason, don't check the button. Unchecked checkboxes won't be included in the final dataset. 

Each sentence is separated by two blank rows. Going back to the example above, a correct annotation would look like this:

| Source |
| :---- |
| Το **\<L1\>χιούμορ\</L1\>** *μοιάζει να* απευθύνεται σε παιδιά και όχι σε ενήλικες και |
| Ο **\<N1\>αστεϊσμός\</N1\>** *μοιάζει να* απευθύνεται σε παιδιά και όχι σε ενήλικες και |

Note that in the last column, you can see the number of your annotation 🙂 Here is the spreadsheet for Danish: [https://docs.google.com/spreadsheets/d/177lZPdiOjiFcXt15CRovBe50ZC6LKqKtEHc0k912ZIc/edit?usp=sharing](https://docs.google.com/spreadsheets/d/177lZPdiOjiFcXt15CRovBe50ZC6LKqKtEHc0k912ZIc/edit?usp=sharing)

## **Annotation procedure**

Based on what we discussed about loanwords, if you believe that a loanword in a given sentence cannot be replaced (or you don't know of any native replacement), simply ignore them. Otherwise, add the native alternative (or select one from the choices using CLoAn). If you use the spreadsheet, I'll identify your replacements by checking non-empty **\<N\*\>\</N\*\>** tags.

# **What you should do:**

Please consider the following steps:

1. After getting access to your folder on Google Drive, check the quality of the corpus. If you think the sentences are not very useful for our task, i.e. don't contain many replaceable loanwords, simply let me know and I'll generate a new sample for you.  
2. If you are happy with the corpus, please proceed with the annotation. You can do it with either CLoAn or the spreadsheet. For the first option, the corpora and loanword list are also provided in your folder.  
3. In replacing the loanword, read the original sentence and its translation first. If the translation pair is correct, then replace the loanword if possible and check the checkbox. Otherwise, simply move to the next one.  
4. Don't forget to locally backup you work as you proceed.  
5. I'll make sure to check your spreadsheet every now and then and I'll let you know if I come across any issue. Do let me know if you need additional assistance from my side.  
6. Depending on your availability, we accept 10 to 15 hours of work. Once done, let me know, please.

# Frequently Asked Questions

1. If I substitute the loanword with a word that has different morphological gender, should I make the necessary changes to the annotated sentence to make gender agreement work?  
   **Exactly\! Feel free to change the sentence such that the native alternative is syntactically correct.**  
     
2. I see that some \<L1\> tags surround a token of what indeed is a multitoken loanword. For instance: *Así que sobre ello no tengo absolutamente ningún hard \<L1\>feeling\</L1\>*. Only *feeling* is tagged, although the full loanword is *hard feeling*. Can I move the \<L1\> tag so it includes *hard (Así que sobre ello no tengo absolutamente ningún \<L1\>hard feeling\</L1\>)*? (The alternative would be creating a \<L2\> tag for *hard*, but the thing is that the Spanish alternative to "hard feeling" would be one word only, there would only be a \<N1\>).  
   **Totally\! You are in full control of moving the tags in the sentences in your language. The only thing that is not supposed to be changed is the translations.**   
     
3. If a sentence has no loanwords whatsoever (the word tagged as \<L1\> is not actually a loanword) but the sentence is correct, should I still validate the sentence and check the checkbox?  
   **We validate the annotations by checking the checkbox for cases where there is at least one loanword in the original sentence. If you notice no loanwords, no need for annotation or validation.**  
     
4. What should I do if something is marked as a loanword, but it isn't actually a loanword. Should I delete the \<L\> tags, or  leave the \<N\> tags unfilled?   
   **Please skip such cases\! We only focus on loanwords. When you don’t check a checkbox, we assume that one of the followings has happened:**  
* **The sentence in a language other than yours**  
* **The sentence has encoding issues or is not readable**  
* **The translation doesn’t correspond to the original sentence**  
* **There is no loanword in the sentence: In this case, you can leave a comment in the comment section, e.g. “not loanword”**  
    
5. Should we only check the checkbox if we provided a replacement for the loanword? If no replacement was provided (because there is no good alternative, or because the word is not truly a loanword), should I leave the checkbox blank?   
   **If you check a sentence and decide not to replace anything, you can still validate it. This way, we will know that the sentence is actually fine, but you decided not to replace it. The checkbox will be left unchecked for sentences not containing a loanword or wrong cases only (like sentences not in Spanish, sentences having HTML tags and etc.).**  
     
6. I skimmed quickly through the spreadsheet and didn't see too many sentences with loanwords (the words marked with \<L\> tags are not loanwords in most cases). Is that expected?  
   **Yes\! The loanword list that I collected is based on Wiktionary. So, it is totally possible that there are fewer cases there. That said, if you think the cases are very sparse, I can sample from another corpus. Please let me know.**  
     
7. Some loanwords will have a very natural alternative in my language, others may have an alternative but they may be less frequent or will make the sentence sound less natural than the loanword would. Should I sacrifice naturalness for the sake of using a native alternative?   
   **Yes\! How you feel comfortable about the usage of a word with its potential connotations goes beyond the scope of this task. That said, we are aware that language purism is not perceived in a positive way by many.**  
8. I know more than one native alternative for a loanword in my language. What should I do?   
   **Feel free to select any of them. It is recommended to select the one that sounds most natural and more well-known to you.**   
   

If you have any questions, please let me know.   
Many thanks\!
