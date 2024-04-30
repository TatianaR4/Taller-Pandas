# -*- coding: utf-8 -*-
"""dataframes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dpo6S528P9NSV4PMMlrmbRbCwm1p8d5c
"""

!PIP INSTALL PANDAS

!pip install pandas

import pandas as pd

#crear una serie
#arreglo unidimensional de datos

miSerie=pd.Series([34,56,78,23,34])
miSerie

#diccionarios en python
#Estructura que guarda datos de forma de objetos de llave-valor

miDiccionario={"nombre":"casa1","área":32,"baños":5,"propietarios":["casandrra", "juan", "leandra"],"barrio":{"nombre":["gran britalia","fontibon","bosa"]}}
miDiccionario

#Dataframe
#estructura de datos de formato tabla.
#La forma mas simple de crear un dataframe es apartir de un diccionario, otra forma es desde la hoja de calculo, desde archivo json, desde archivos csv

miDataframe =pd.DataFrame({"si":[10,15],"no":[50,68]})
miDataframe



"""#otro dataframe
#encuuesta es otro datframe de pandas
"""

encuesta=pd.DataFrame(
    {
        "Julia":["me gusto","fue horrible"],
        "Pedro":["me delicioso","No estuvo mal"],
    },
    index=["Restaurante_1","Restaurante_2"]
)
encuesta

#leer el archivo Csv

miTitanic=pd.read_csv("titanic.csv")

miTitanic

miTitanic.head()

"""# Sección nueva"""



miTitanic.describe()

miTitanic.rename(columns= {"Survived": "Sobreviviente"},inplace=True)

import pandas as pd

miTitanic.head()

misSobrevivientes= miTitanic["Sobreviviente"]
misSobrevivientes.count()

misSobrevivientes.product()

miTitanicFiltrado=miTitanic[miTitanic["Sobreviviente"]==1]
miTitanicFiltrado.count()

total_sobrevivientes = miTitanicFiltrado["Sobreviviente"].sum()
total_sobrevivientes



