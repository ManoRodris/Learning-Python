import pandas as pd
import numpy as np

# Definir categorias de produtos e lojas
produtos = [
    ("Notebook", "Eletrônicos"), ("Smartphone", "Eletrônicos"), ("Tablet", "Eletrônicos"),
    ("Cadeira Gamer", "Móveis"), ("Mesa de Escritório", "Móveis"), ("Monitor", "Eletrônicos"),
    ("Teclado Mecânico", "Acessórios"), ("Mouse Gamer", "Acessórios"), ("Headset", "Acessórios"),
    ("Impressora", "Periféricos"), ("Câmera de Segurança", "Periféricos")
]

lojas = ["Loja Centro", "Loja Norte", "Loja Sul", "Loja Leste"]

# Gerar 500 vendas fictícias
np.random.seed(42)  # Para reprodutibilidade
num_vendas = 500

dados = {
    "id_venda": np.arange(1, num_vendas + 1),
    "data": pd.date_range(start="2023-01-01", periods=num_vendas, freq="D"),
    "produto": np.random.choice([p[0] for p in produtos], num_vendas),
    "categoria": np.random.choice([p[1] for p in produtos], num_vendas),
    "preco_unitario": np.random.uniform(50, 5000, num_vendas).round(2),
    "quantidade": np.random.randint(1, 10, num_vendas),
    "loja": np.random.choice(lojas, num_vendas),
}

# Criar DataFrame
df = pd.DataFrame(dados)
df["valor_total"] = df["preco_unitario"] * df["quantidade"]

# Exibir as primeiras linhas
print(df.head())

# Salvar em CSV para futuras análises
df.to_csv("dados_vendas.csv", index=False)
