import pandas as pd

df = pd.read_csv("dados_vendas.csv")

# print(df.describe())
# print(df.info())

categorias_vendas = df.groupby('categoria')['quantidade'].sum()
lojas_faturamento = df.groupby('loja')['valor_total'].sum()
print(categorias_vendas)
print(lojas_faturamento)

