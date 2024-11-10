import fitz

def abrir_arquivo(arquivo):
    arquivo = open(arquivo, 'rb').read()
    return fitz.Document(stream=arquivo, filetype="pdf")

documento = abrir_arquivo('Resultado_Final_homologacao_TIC37.pdf')
qtd_de_inscritos = 0

for paginas in documento:
    for linhas in paginas.get_text("dict")['blocks']:
        qtd_de_inscritos += linhas.count("Feira de Santana")

print(qtd_de_inscritos)

