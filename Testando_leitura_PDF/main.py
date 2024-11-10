import fitz  # PyMuPDF

# Abre o PDF
pdf_document = fitz.open("Resultado_Final_homologacao_TIC37.pdf")

# Inicializa a contagem
count = 0

# Itera por cada página do PDF
for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    text = page.get_text("text")  # Extrai o texto da página
    count += text.count("Feira de Santana")  # Conta as ocorrências na página

# Fecha o PDF
pdf_document.close()

print(f"Total de candidatos em Feira de Santana: {count}")
