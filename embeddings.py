from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Используем модель для получения эмбеддингов (например, "sentence-transformers/all-MiniLM-L6-v2")
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
model = AutoModel.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings[0].numpy()




def compare_texts(text1, text2):
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    similarity = cosine_similarity([emb1], [emb2])[0][0]
    return similarity


print(compare_texts("кошка","кот"))