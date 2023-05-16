# PI_Henry

## Proyecto Individual - MLOPS

Alumno: José Luis Martínez Chávez


> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API y el Sistema de Recomendación que se solicitó desarrollar.


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

* **queries.py** - _contiene las funciones de las queries pedidas y el sistema de recomendación._



**Las funciones que componen la API  y sus respectivas consutas deployadas en render**

-  Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. <br>
https://pi-henry-t1tx.onrender.com/get_max_duration/2020/netflix/min
-  Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. <br>
https://pi-henry-t1tx.onrender.com/get_score_count/amazon/3.4/2019.
-  Cantidad de películas por plataforma con filtro de PLATAFORMA. <br>
https://pi-henry-t1tx.onrender.com/get_count_platform/hulu
- Actor que más se repite según plataforma y año. <br>
https://pi-henry-t1tx.onrender.com/get_actor/disney/2020
- Cantidad de contenidos/productos que se publicó por país y año. <br>
https://pi-henry-t1tx.onrender.com/prod_per_county/movie/india/2018
-  Cantidad de contenidos/productos según el rating de audiencia dado. <br>
https://pi-henry-t1tx.onrender.com/get_contents/18%2B
