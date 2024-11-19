from T9_Lev import T9_with_Lev, T9_preprocc
from model_from_hugging_face import encoding, cosine_similarity
import json
import torch
from database import fetch_data

def convert_keys_to_lowercase(obj):
    if isinstance(obj, dict):
        return {k.lower(): convert_keys_to_lowercase(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys_to_lowercase(item) for item in obj]
    else:
        return obj
    
def make_prediction(some_text: str, data_for_Lev: list, vectors: dict) -> list:
    list_of_sims = []
    top_10_clothes = []
    new_str = ""

    vectors_of_clothes = list(vectors.values())
    names_of_clothes = list(vectors.keys())

    choose_for_model = T9_with_Lev(some_text, T9_preprocc(data_for_Lev))


    for i in range(len(choose_for_model)):
        new_str += " " + choose_for_model[i]
    new_str = new_str.lstrip()

    print(new_str)

    vector_of_sent = encoding(new_str)

    for i in range(len(vectors_of_clothes)):
        similar = cosine_similarity(torch.tensor(vector_of_sent), torch.tensor(vectors_of_clothes[i]))
        list_of_sims.append([similar, names_of_clothes[i]])
    list_of_sims = sorted(list_of_sims)[::-1]
    for i in range(len(list_of_sims[:10])):
        top_10_clothes.extend(data_for_Lev[list_of_sims[i][1]])

    return top_10_clothes
    
with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/ru_preproc.json', 'r', encoding='utf-8') as file:
    data_ru = convert_keys_to_lowercase(json.load(file))
    
with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/ukr_preproc.json', 'r', encoding='utf-8') as file:
    data_ukr = convert_keys_to_lowercase(json.load(file))

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/pt_preproc.json', 'r', encoding='utf-8') as file:
    data_pt = convert_keys_to_lowercase(json.load(file))

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/pl_preproc.json', 'r', encoding='utf-8') as file:
    data_pl = convert_keys_to_lowercase(json.load(file))

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/de_preproc.json', 'r', encoding='utf-8') as file:
    data_de = convert_keys_to_lowercase(json.load(file))
    
with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/en_preproc.json', 'r', encoding='utf-8') as file:
    data_en = convert_keys_to_lowercase(json.load(file))

state = "ru" # тут нужно будет получать какого языка у нас интерфейс
user_input = input().lower()

match state:
    case "ru":
        vectors_ru = fetch_data("ru")
        print(make_prediction(user_input, data_ru, vectors_ru))
    case "ukr":
        vectors_ukr = fetch_data("ukr")
        print(make_prediction(user_input, data_ukr, vectors_ukr))
    case "en":
        vectors_en = fetch_data("en")
        print(make_prediction(user_input, data_en, vectors_en))
    case "pl":
        vectors_pl = fetch_data("pl")
        print(make_prediction(user_input, data_pl, vectors_pl))
    case "pt":
        vectors_pt = fetch_data("pt")
        print(make_prediction(user_input, data_pt, vectors_pt))
    case "de":
        vectors_de = fetch_data("de")
        print(make_prediction(user_input, data_de, vectors_de))     
