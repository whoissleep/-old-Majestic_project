from model_from_hugging_face import encoding
from tqdm import tqdm
import json
from database import insert_data

def sent_2_vec_for_languages(list_of_sents: list) -> dict:
    vectors_of_sentences = []
    vector2sent = {}
    
    for sentence in tqdm(list_of_sents):
        vectors_of_sentences.append(encoding(sentence))
     
    for i in range(len(list_of_sents)):
        vector2sent[list_of_sents[i]] = vectors_of_sentences[i]
    
    return vector2sent

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/ru_preproc.json', 'r', encoding='utf-8') as file:
    data_ru = json.load(file)
    
with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/ukr_preproc.json', 'r', encoding='utf-8') as file:
    data_ukr = json.load(file)

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/pt_preproc.json', 'r', encoding='utf-8') as file:
    data_pt = json.load(file)

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/pl_preproc.json', 'r', encoding='utf-8') as file:
    data_pl = json.load(file)

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/de_preproc.json', 'r', encoding='utf-8') as file:
    data_de = json.load(file)
    
with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/en_preproc.json', 'r', encoding='utf-8') as file:
    data_en = json.load(file)
    
ru_text_for_preproc = [x.lower() for x in list(data_ru.keys())]
de_text_for_preproc = [x.lower() for x in list(data_de.keys())]
en_text_for_preproc = [x.lower() for x in list(data_en.keys())]
pt_text_for_preproc = [x.lower() for x in list(data_pt.keys())]
uk_text_for_preproc = [x.lower() for x in list(data_ukr.keys())]
pl_text_for_preproc = [x.lower() for x in list(data_pl.keys())]

vectors_for_db = sent_2_vec_for_languages(ru_text_for_preproc) #heres name of need file
insert_data("pl", vectors_for_db.keys(), vectors_for_db.values())