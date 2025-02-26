import pandas as pd

df = pd.read_csv("dados_vendas.csv")

# print(df.describe())
# print(df.info())

categorias_vendas = df.groupby('categoria')['quantidade'].sum().reset_index()
lojas_faturamento = df.groupby('loja')['valor_total'].sum().reset_index()
produtos_vendas = df.groupby('produto')['quantidade'].sum().reset_index()
produto_mais_vendido = produtos_vendas.sort_values(by=["quantidade"], ascending=False).head(1)
ticket_medio = round(df['valor_total'].mean(), 2)
receita_por_categoria = df.groupby('categoria')['valor_total'].sum().reset_index()

# print(categorias_vendas)
# print(lojas_faturamento)
# print(produto_mais_vendido)
# print(ticket_medio)
print(receita_por_categoria)

