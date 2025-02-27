import streamlit as st
import plotly.express as px
from eda import *

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
col3 = st.columns(1)

fig_loja = px.bar(lojas_faturamento, x='loja', y='valor_total', title='Receita total por loja', labels={
    'loja': 'Loja', 'valor_total': 'Faturamento'})
col1.plotly_chart(fig_loja)

fig_categoria = px.pie(categorias_vendas, names='categoria', values='quantidade', title='Percentual de vendas por categoria')
fig_categoria.update_traces(textinfo='percent+label')
col2.plotly_chart(fig_categoria)

fig_mensal = px.line(df_mensal, y='valor_total', x='ano_mes', title='Evolução das vendas ao longo do tempo', labels={
    'ano_mes': 'Ano-Mês'})

# fig_mais_vendido = px.bar(produtos_vendas, x='produto', y='quantidade', title='Receita total por loja')

# col3.plotly_chart(fig_mensal)
# col4.plotly_chart(fig_mais_vendido)