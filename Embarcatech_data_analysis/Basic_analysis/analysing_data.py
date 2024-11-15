import pandas

# Faz a leitura dos dados de cada arquivo CSV
inscriptions_data = pandas.read_csv("inscriptions_embarcatech.csv")
results_data = pandas.read_csv("results_embarcatech.csv")

# Faz a leitura de quantos inscritos há em Feira de Santana
inscriptions_feira_de_santana = len(inscriptions_data[inscriptions_data["Pólo"] == "Feira de Santana"])

# Faz a leitura de quantos candidatos em Feira de Santana foram classificados/convocados
results_feira_de_santana = len(results_data[results_data["Polo"] == "Feira de Santana"])

# Calcula a porcentagem de quantos candidatos de Feira de Santana se classificaram/foram convocados
percentage = round((results_feira_de_santana/inscriptions_feira_de_santana) * 100)

# Exibe os dados
print(f"Amount of inscriptions in Feira de Santana: {inscriptions_feira_de_santana}")
print(f"Amount of people who was classified: {results_feira_de_santana}")
print(f"Percentage of people who was classified based on the subscribers: {percentage}%")