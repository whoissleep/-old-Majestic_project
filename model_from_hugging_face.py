from sentence_transformers import SentenceTransformer
import torch

def encoding(sent):
    return model.encode(sent)

def cosine_similarity(vec1, vec2):
    return torch.cosine_similarity(torch.tensor(vec1.reshape(1, -1)), torch.tensor(vec2.reshape(1, -1))).item()

path_to_model = 'sentence-transformers/LaBSE' #тут нужен путь до модели

model = SentenceTransformer(path_to_model)
    
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
