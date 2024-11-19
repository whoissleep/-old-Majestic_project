import json
import re
from pylev import levenshtein as Lev

def T9_preprocc(json_file: json) -> list:
    text_for_t9 = list(json_file)
    word_corpus = []

    for sent in text_for_t9:
        words = sent.split()
        for word in words:
            cleaned_word = re.sub(r'\([^)]*\)', '', word).strip()
            cleaned_word = cleaned_word.replace('"', '').replace("«", "").replace("»", "").strip()
            if cleaned_word and len(cleaned_word) >= 3:
                word_corpus.append(cleaned_word.lower())

    word_corpus = list(set(word_corpus))
    print(word_corpus)
    return word_corpus

def T9_with_Lev(sent: str, lang_T9_corpus: list) -> list:
    distance_of_Lev = []
    words = sent.lower().split()
    new_choose = []
    fin_choose = []

    for word in words:
        min_dist = 100000
        best_word = word
        
        for curr_word in lang_T9_corpus:
            dist = Lev(word, curr_word)
            if dist < min_dist:
                min_dist = dist
                best_word = curr_word
            elif dist == min_dist + 1:
                new_choose.append(curr_word)
        
        if new_choose:
            print("Choose the word you want:")
            print(f"1. {best_word}")
            for num, opt in enumerate(new_choose, start=2):
                print(f"{num}. {opt}")
            user_choice = int(input())
            if user_choice == 1:
                fin_choose.append(best_word)
            else:
                fin_choose.append(new_choose[user_choice - 2])
        else:
            fin_choose.append(best_word)
        
        new_choose.clear()

    print(fin_choose)
    return fin_choose

