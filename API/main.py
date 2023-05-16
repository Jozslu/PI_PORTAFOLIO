from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Crear la aplicación FastAPI
app = FastAPI()
df = pd.read_csv("../data_actualizada.csv", index_col=False, sep=",", header=0)

# Query 1
@app.get('/peliculas_mes/{mes}')
async def peliculas_mes(mes: str):
    """
    Obtener la cantidad de películas que se estrenaron en un determinado mes.
    Ejemplo: mes = 'septiembre'.
    """
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    
    if mes.lower() not in meses:
        return {'error': 'Mes inválido'}
    
    mes_numerico = str(meses.index(mes) + 1).zfill(2)
    df['release_date'] = pd.to_datetime(df['release_date'])
    cantidad = df[df['release_date'].dt.month == int(mes_numerico)].shape[0]

    return {'mes': mes, 'cantidad': cantidad}
#print(peliculas_mes('septiembre'))

# Query 2
@app.get('/peliculas_dia/{dia}')
async def peliculas_dia(dia: str):
    """
    Obtener la cantidad de películas que se estrenaron en un determinado día.\n
    Ejemplo: dia = 'viernes'.
    """
    dias_dict = {'lunes': 0,'martes': 1,'miércoles': 2,'miercoles': 2,'jueves': 3,'viernes': 4,'sábado': 5,'sabado': 5,  'domingo': 6}
    dia_numerico = dias_dict.get(dia.lower())
    if dia_numerico is None:
        return {'error': 'Día inválido'}
    
    df['release_date'] = pd.to_datetime(df['release_date'])
    cantidad = df[df['release_date'].dt.dayofweek == dia_numerico].shape[0]

    return {'dia': dia, 'cantidad': cantidad}
#print(peliculas_dia('lunes'))

# Query 3
@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia: str):
    """
    Obtener la cantidad de películas, ganancia total y promedio de una franquicia.\n
    Ejemplo: franquicia = 'James Bond Collection'.
    """
    franquicia_df = df[df['belongs_to_collection'].apply(lambda x: franquicia in x if isinstance(x, str) else False)]
    cantidad = franquicia_df.shape[0]
    ganancia_total = franquicia_df['revenue'].sum().round()
    ganancia_promedio = franquicia_df['revenue'].mean().round()

    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}
#print(franquicia('James Bond Collection'))

# Query 4
@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais: str):
    """
    Obtener la cantidad de películas producidas en un determinado país.\n
    Ejemplo: pais = 'United States of America'.
    """
    df['production_countries'] = df['production_countries'].replace(np.nan, '')
    filtered_df = df[df['production_countries'].str.contains(pais)]
    cantidad = len(filtered_df)
    
    return {'pais': pais, 'cantidad': cantidad}
#print(peliculas_pais('United States of America'))

# Query 5
@app.get('/productoras/{productora}')
async def productoras(productora: str):
    """
    Obtener la ganancia total y la cantidad de películas producidas por una determinada productora.\n
    Ejemplo: productora = 'Warner Bros'.
    """
    df['production_companies'] = df['production_companies'].replace(np.nan,'')
    productora_df = df[df['production_companies'].apply(lambda x: productora in x)]
    ganancia_total = productora_df['revenue'].sum()
    cantidad = productora_df.shape[0]

    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}
#print(productoras('Warner Bros'))

# Query 6
@app.get('/retorno/{pelicula}')
async def retorno(pelicula: str):
    """
    Obtener la inversión, ganancia, retorno y año de una determinada película.
    Ejemplo: pelicula = 'Jumanji'
    """
    pelicula_df = df[df['title'].str.contains(pelicula, na=False)]
    inversion = pelicula_df.loc[pelicula_df['title'].str.contains(pelicula), 'budget'].values[0]
    ganancia = pelicula_df.loc[pelicula_df['title'].str.contains(pelicula), 'revenue'].values[0]
    retorno = pelicula_df.loc[pelicula_df['title'].str.contains(pelicula), 'return'].values[0]
    anio = pelicula_df.loc[pelicula_df['title'].str.contains(pelicula), 'release_year'].values[0]
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}
#print(retorno('Jumanji'))

####################################               SISTEMA DE RECOMENDACIÓN               ################################################

vector = TfidfVectorizer(stop_words="english")
df["overview"] = df["overview"].replace(np.nan, "")
vector_matriz = vector.fit_transform(df["overview"])

batch_size = 1000  
num_batches = len(df) // batch_size + 1
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

# Query 7
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
#print(get_recomendation('Minions'))

