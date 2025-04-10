from PyPDF2 import PdfReader, PdfWriter

leitor = PdfReader(r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Cortador de PDF\Tese Teofilo Galvao.pdf")
escritor = PdfWriter()

# Pega as páginas de 10 a 20 (lembrando que o índice começa do 0)
for i in range(113, 218):
    escritor.add_page(leitor.pages[i])

with open("capitulo 4 - Tese Teofilo Galvao.pdf", "wb") as saida:
    escritor.write(saida)
