from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

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


def get_recomendation(title):
    id = indices[title]

    coseno = np.zeros(len(data))

    for i in range(num_batches):
        start = i * batch_size
        end = (i + 1) * batch_size

        if end > len(data):
            end = len(data)

        batch_coseno = cosine_similarity(
            vector_matriz[start:end], vector_matriz
        )

        coseno[start:end] = batch_coseno[:, id].flatten()

    x1 = list(enumerate(coseno))
    x1 = sorted(x1, key=lambda x: x[1], reverse=True)
    # Obtenemos los 5 primeros.
    x1 = x1[1:6]

    movie_index = [i[0] for i in x1]
    # Devolvera los 5 primeros.
    return data["title"].iloc[movie_index].to_list()[:5]
#print(get_recomendation('Minions'))
# primer modelo optimizado
@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str):
    id = indices[titulo]
    coseno = np.zeros(len(df))

    for i in range(num_batches):
        start = i * batch_size
        end = (i + 1) * batch_size

        if end > len(df):
            end = len(df)

        batch_coseno = cosine_similarity(vector_matriz[start:end], vector_matriz)
        coseno[start:end] = batch_coseno[:, id].flatten()

    x1 = list(enumerate(coseno))
    x1 = sorted(x1, key=lambda x: x[1], reverse=True)
    # Obtenemos los 5 primeros.
    x1 = x1[1:6]

    movie_index = [i[0] for i in x1]

    movie_titles = []

    for index in movie_index:
        movie_titles.append(df["title"].iloc[index])

    return movie_titles
# segundo modelo optimizado
import heapq

@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str):
    id = indices[titulo]
    coseno = []

    for i in range(num_batches):
        start = i * batch_size
        end = (i + 1) * batch_size

        if end > len(df):
            end = len(df)

        batch_coseno = cosine_similarity(vector_matriz[start:end], vector_matriz)
        coseno.extend(batch_coseno[:, id].flatten())

    movie_index = heapq.nlargest(6, range(1, len(coseno)), key=coseno.__getitem__)
    movie_titles = [df["title"].iloc[index] for index in movie_index if index != id][:5]

    return movie_titles
