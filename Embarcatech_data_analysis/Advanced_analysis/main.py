from tabula import read_pdf
import pandas

def creating_csv_files(name_of_pdf, name_of_csv, from_page, to_page, lattice_parameter):
    table = read_pdf(input_path=name_of_pdf, pages=f'{from_page}-{to_page}', multiple_tables=False,
                                  lattice=lattice_parameter)
    combined_dfs = pandas.concat(table)
    combined_dfs.to_csv(name_of_csv)

# creating_csv_files("../PDF_Data/Resultado_Final_homologacao_TIC37.pdf", "subscribers_embarcatech.csv", 2, 42, False)
# creating_csv_files("../PDF_Data/Resultado_Preliminar_Prova_TIC37.pdf", "classified_embarcatech.csv", 2, 29, True)
# creating_csv_files("../PDF_Data/Resultado_Preliminar_Prova_TIC37.pdf", "declassified_embarcatech.csv", 30, 47, True)