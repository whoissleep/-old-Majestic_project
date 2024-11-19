import json

with open('/home/whoissleep/Документы/VS_CODE/Majestic_project/poland.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def extract_clothing_paths(data):
    clothing_paths = {}

    def extract_paths_helper(data, path=''):
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f"{path}/{key}" if path else key
                extract_paths_helper(value, new_path)
        elif isinstance(data, str):
            clothing_name = data
            if clothing_name not in clothing_paths:
                clothing_paths[clothing_name] = []
            clothing_paths[clothing_name].append(path)

    extract_paths_helper(data['clothes'])
    return clothing_paths

clothing_data = extract_clothing_paths(data)

output_file = 'pl_preproc.json' #here is name of your json file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(clothing_data, file, ensure_ascii=False, indent=4)

print(f"Results saved to {output_file}")