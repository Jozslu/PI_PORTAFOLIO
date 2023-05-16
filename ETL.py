import pandas as pd 
import numpy as np 
import ast

#Cargando el dataset
df_movie  = pd.read_csv("Data/movies_dataset.csv", index_col= False, sep=",", header= 0)

# Creando las funciones para responder las transformaciones sugeridas.

# Transformacion 1 
def desanidar(obj): 
    """
    Esta función permite desanidar los datos de una fila en formato de listas.
    """
    if isinstance(obj, str) and "{" in obj:
        Nombres=[]
        for elemento in ast.literal_eval(obj):
            Nombres.append(elemento["name"]);
        return Nombres
    
def desanidar_2(obj): 
    """
    Esta función permite desanidar los datos de una fila en formato diccionario.
    """
    if isinstance(obj, str) and "{" in obj:
        dic = ast.literal_eval(obj)
        return dic["name"]

# Transformacion 2
def reemplazar_nulos(df= pd.DataFrame()):
    """
    Esta función reemplaza los valores nulos del campo "revenue" y "budget" por el número "0" en el dataframe.
    """
    df["revenue"] = pd.to_numeric(df["revenue"], errors='coerce').fillna(0) 
    df["budget"] = pd.to_numeric(df["budget"], errors='coerce').fillna(0) 

# Transformacion 3
def eliminar_nulos(df= pd.DataFrame()):
    """
    Esta función eliminará los valores nulos del campo "release_date" en el dataframe.
    """
    df = df.dropna(subset=["release_date"], inplace=True)

# Transformacion 4
def formato_fecha(df= pd.DataFrame(),campo= str()):
    """
    Esta función normalizará en el formato fecha: "AAAA-mm-dd" del campo solicitado en el dataframe y creará la columna release_year.
    """
    df[campo] = pd.to_datetime(df[campo], errors="coerce")#.dt.strftime("%Y- %m- %d")
    df["release_year"] = df[campo].dt.year

# Transformacion 5
def columna_return(df= pd.DataFrame()):
    """
    Esta función creará la columna "return" y obtendrá como valor, el resultado de dividir: "revenue / budget", y si no hay datos disponibles para calcularlo, deberá tomar el valor 0.
    """
    df["budget"] = df["budget"].astype(float)
    df["return"] = df.apply(lambda row: row["revenue"] / row["budget"] if row["budget"] else 0, axis=1)
    df["return"] = df["return"].fillna(0)

# Transformacion 6
def eliminar_columnas(df= pd.DataFrame()):
    """
    Esta función eliminará las columnas que no serán utilizadas: video,imdb_id,adult,original_title,vote_count,poster_path y homepage.
    """ 
    df = df.drop(columns=["video", "imdb_id", "adult", "original_title", "vote_count", "poster_path", "homepage"], inplace= True)

# Normalizando el dataset con las funciones.
df_movie["genres"]                = df_movie["genres"].apply(desanidar)
df_movie["belongs_to_collection"] = df_movie["belongs_to_collection"].apply(desanidar_2)
df_movie["production_companies"]  = df_movie["production_companies"].apply(desanidar)
df_movie["production_countries"]  = df_movie["production_countries"].apply(desanidar)
df_movie["spoken_languages"]      = df_movie["spoken_languages"].apply(desanidar)

reemplazar_nulos(df_movie)
eliminar_nulos(df_movie)
formato_fecha(df_movie,"release_date")
columna_return(df_movie)
eliminar_columnas(df_movie)
df_movie = df_movie.dropna(subset=["release_year"])

# Guardando todas las transformaciones en un nuevo archivo csv.
df_movie.to_csv("data_actualizada.csv")

