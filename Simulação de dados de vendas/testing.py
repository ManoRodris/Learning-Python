import plotly.express as px

# Exemplo de dados
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
}

# Criando o gráfico
fig = px.scatter(data_frame=data, x='x', y='y', title='Gráfico de Dispersão')

# Exibindo o gráfico
fig.show()