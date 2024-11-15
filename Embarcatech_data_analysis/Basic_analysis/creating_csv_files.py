from tabula import read_pdf
import pandas

# Caminho do PDF
table_inscriptions_path = "../PDF_Data/Resultado_Final_homologacao_TIC37.pdf"
table_results_path = "../PDF_Data/Resultado_Preliminar_Prova_TIC37.pdf"

# Extrai a tabela do PDF, a partir da página que inicia a tabela, para criar uma lista de DataFrames
table_inscriptions = read_pdf(input_path=table_inscriptions_path, pages='2-42', multiple_tables=False, lattice=False)
table_results = read_pdf(input_path=table_results_path, pages='2-29', multiple_tables=False, lattice=True)

# Concatena os DataFrames e cria um arquivo CSV
combined_df_1 = pandas.concat(table_inscriptions)
combined_df_1.to_csv("inscriptions_embarcatech.csv")

combined_df_2 = pandas.concat(table_results)
combined_df_2.to_csv("results_embarcatech.csv")



