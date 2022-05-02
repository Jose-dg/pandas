import numpy as np
import pandas as pd

datos1 = {'Celular':['314','315','320','322'], 'Número de pago' : ['234242','23244','23242','243535']}
datos2 = {'Número de pago' : ['234242','23244','23242','234242','23244','23242','243535'], 'Valor' : ['100.34','200.43','300.54','400','120','2323','2321']}

dataframe1 = pd.DataFrame(datos1)
dataframe2 = pd.DataFrame(datos2)
print(dataframe1)
print(dataframe2)

dataframe2.Valor = dataframe2.Valor.astype(float)
resultado = pd.merge(dataframe1,dataframe2,on='Número de pago',how='inner').groupby('Celular').Valor.sum().reset_index()

print(resultado)


