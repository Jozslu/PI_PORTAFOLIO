from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import heapq

# Sistema de recomendación:
# Elimina las palabras comunes en inglés
vector = TfidfVectorizer(stop_words="english")

# Cargamos el dataset
data = pd.read_csv("data_actualizada.csv", index_col=False, sep=",", header=0)

data["overview"] = data["overview"].replace(np.nan, "")

vector_matriz = vector.fit_transform(data["overview"])

batch_size = 1000  # Tamaño de lote
num_batches = len(data) // batch_size + 1

indices = pd.Series(data.index, index=data["title"]).drop_duplicates()


# Creamos la función de recomendación

def recomendacion(titulo: str):
    id = indices[titulo]
    coseno = []

    for i in range(num_batches):
        start = i * batch_size
        end = (i + 1) * batch_size

        if end > len(data):
            end = len(data)

        batch_coseno = cosine_similarity(vector_matriz[start:end], vector_matriz)
        coseno.extend(batch_coseno[:, id].flatten())

    movie_index = heapq.nlargest(6, range(1, len(coseno)), key=coseno.__getitem__)
    movie_titles = [data["title"].iloc[index] for index in movie_index if index != id][:5]

    return movie_titles
#print(recomendacion('Minions'))
