# PI_Henry

## Proyecto Individual - MLOPS

Alumno: José Luis Martínez Chávez


> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API y 
> el Sistema de Recomendación que se solicitó desarrollar.


**MENU:** 
 _dataset trabajada desde 0._ en _"[https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view)"_

* **EDA_1.ipynb** - _notebook, con la exploración y visualización de la data sin modificar._
* **EDA_2.ipynb** - _notebook, con la exploración y visualización de la data mdificada._
* **ETL.py** - _notebook con las transformaciones sugeridas._
* **README** - _Instrucciones de uso._
* **data_actualizada.csv** - _data limpia que usamos para las consultas y para el sistema de recomedación._
* **requirements.txt** - _dependencias necesarias para que funcione la API._
* **API** - _es una carpeta que contiene el llamado de la APi._
* **main.py** - _contiene las funciones de las queries pedidas y el sistema de recomendación._
* **Sistema_Recomendacion**- _es una carpeta que contiene la creación del modelo del Sistema de Recomendación._
* **query_modelo.py** - _contiene las funciones de las queries pedidas y el sistema de recomendación._


**Las funciones que componen la API  y sus respectivas consutas deployadas en render**

-  Obtener la cantidad de películas que se estrenaron en un determinado mes.
    Ejemplo: mes = 'septiembre'. <br>
https://pi04-henry.onrender.com/peliculas_mes/septiembre

-  Obtener la cantidad de películas que se estrenaron en un determinado día.
    Ejemplo: dia = 'viernes'. <br>
https://pi04-henry.onrender.com/peliculas_dia/viernes

-  Obtener la cantidad de películas, ganancia total y promedio de una franquicia.
    Ejemplo: franquicia = 'James Bond Collection'. <br>
https://pi04-henry.onrender.com/franquicia/James%20Bond%20Collection

-  Obtener la cantidad de películas producidas en un determinado país.
    Ejemplo: pais = 'United States of America'. <br>
https://pi04-henry.onrender.com/peliculas_pais/United%20States%20of%20America

-  Obtener la ganancia total y la cantidad de películas producidas por una determinada productora.
    Ejemplo: productora = 'Warner Bros'. <br>
https://pi04-henry.onrender.com/productoras/Warner%20Bros

-  Obtener la inversión, ganancia, retorno y año de una determinada película.
    Ejemplo: pelicula = 'Jumanji' <br>
https://pi04-henry.onrender.com/retorno/Jumanji


Machine Learning

Ya los datos están limpios, investigamos las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías , y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior, para ello realizamos un Análisis Exploratorio de Datos-EDA.

Por terminar desarrollamos nuestro Sistema de Recomendación basado a dos variables "title" y "overview " y 
en en este caso nos basamos en las librerías TfidfVectorizer y cosine_similarity.

** Aquí adjuntaria el link del modelo deployado pero tuve problemas con la capacidad de memoria de 512MB que te proporciona Render.

** El Sistema de Recomedación se visualizará en el link del video, allí comprobarán su ejecución de manera local.  
https://drive.google.com/drive/folders/1YsjWcYGJIbTtxexjklncLxAoiQ-0HhDP?usp=share_link

