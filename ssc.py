import pandas as pd

dfs = pd.read_excel('mercadopago_febrero_2022.xlsx', sheet_name='1')
mercadago_date = pd.DataFrame(dfs)
df_ng = list(mercadago_date['NÚMERO DE IDENTIFICACIÓN'])
df_monto_neto = list(mercadago_date['MONTO NETO DE OPERACIÓN'])
valor = [mercadago_date.loc[(mercadago_date['NÚMERO DE IDENTIFICACIÓN'] == df_ng[i]),'MONTO NETO DE OPERACIÓN'].sum() for i in range(mercadago_date.shape[0])]
mercadago_date["Valor"]= valor
out4 = mercadago_date.iloc[:, [27, 0]]
dataframe2 = pd.DataFrame(out4.drop_duplicates())
print(dataframe2)


dfs2 = pd.read_excel('view_pago_febrero_2022.xls', sheet_name='filter')
view_pago_date = pd.DataFrame(dfs2)
df_ng2 = list(view_pago_date['NÚMERO DE IDENTIFICACIÓN'])
dataframe1 = pd.DataFrame(view_pago_date.iloc[:, [1, 14]])
print(dataframe1)

dataframe2.Valor = dataframe2.Valor.astype(float)
dataframe2.Valor = dataframe2.Valor.astype(float)
dataframe2.Valor = dataframe2.Valor.astype(float)
resultado = pd.merge(dataframe2,dataframe1,on='NÚMERO DE IDENTIFICACIÓN',how='inner').groupby('Celular').Valor.sum().reset_index()

print(resultado)