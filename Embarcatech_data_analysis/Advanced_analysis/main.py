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

inscriptions_embarcatech = pandas.read_csv("subscribers_embarcatech.csv")

total_subscribers = len(inscriptions_embarcatech)
total_fsa = len(inscriptions_embarcatech[inscriptions_embarcatech["Pólo"] == "Feira de Santana"])
total_bjl = len(inscriptions_embarcatech[inscriptions_embarcatech["Pólo"] == "Bom Jesus da Lapa"])
total_ii = len(inscriptions_embarcatech[inscriptions_embarcatech["Pólo"] == "Ilhéus/Itabuna"])
total_j = len(inscriptions_embarcatech[inscriptions_embarcatech["Pólo"] == "Juazeiro"])
total_vc = len(inscriptions_embarcatech[inscriptions_embarcatech["Pólo"] == "Vitória da Conquista"])

if __name__ == "__main__":
    print("===========================================================")
    print(f"Total of submissions in the Embarcatech: {total_subscribers}")
    print(f"Total of submissions in Feira de Santana: {total_fsa}")
    print(f"Total of submissions in Bom Jesus da Lapa: {total_bjl}")
    print(f"Total of submissions in Ilhéus/Itabuna: {total_ii}")
    print(f"Total of submissions in Juazeiro: {total_j}")
    print(f"Total of submissions in Vitória da Conquista: {total_vc}")

classified_embarcatech = pandas.read_csv("classified_embarcatech.csv")

total_classified = len(classified_embarcatech[classified_embarcatech["Status"] == "Classificado"])
total_fsa_classified = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Feira de Santana") &
    (classified_embarcatech["Status"] == "Classificado")
])
total_bjl_classified = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Bom Jesus da Lapa") &
    (classified_embarcatech["Status"] == "Classificado")
])

total_ii_classified = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Ilhéus/Itabuna") &
    (classified_embarcatech["Status"] == "Classificado")
])

total_j_classified = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Juazeiro") &
    (classified_embarcatech["Status"] == "Classificado")
])

total_vc_classified = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Vitória da Conquista") &
    (classified_embarcatech["Status"] == "Classificado")
])


if __name__ == "__main__":
    print("===========================================================")
    print(f"Total of students classified in the Embarcatech: {total_classified}")
    print(f"Total of students classified in Feira de Santana: {total_fsa_classified}")
    print(f"Total of students classified in Bom Jesus da Lapa: {total_bjl_classified}")
    print(f"Total of students classified in Ilhéus/Itabuna: {total_ii_classified}")
    print(f"Total of students classified in Juazeiro: {total_j_classified}")
    print(f"Total of students classified in Vitória da Conquista: {total_vc_classified}")

total_summoned = len(classified_embarcatech[classified_embarcatech["Status"] == "Convocado"])
total_fsa_summoned = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Feira de Santana") &
    (classified_embarcatech["Status"] == "Convocado")
])

total_bjl_summoned = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Bom Jesus da Lapa") &
    (classified_embarcatech["Status"] == "Convocado")
])

total_ii_summoned = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Ilhéus/Itabuna") &
    (classified_embarcatech["Status"] == "Convocado")
])

total_j_summoned = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Juazeiro") &
    (classified_embarcatech["Status"] == "Convocado")
])

total_vc_summoned = len(classified_embarcatech[
    (classified_embarcatech["Polo"] == "Vitória da Conquista") &
    (classified_embarcatech["Status"] == "Convocado")
])

if __name__ == "__main__":
    print("===========================================================")
    print(f"Total of students summoned in the Embarcatech: {total_summoned}")
    print(f"Total of students summoned in Feira de Santana: {total_fsa_summoned}")
    print(f"Total of students summoned in Bom Jesus da Lapa: {total_bjl_summoned}")
    print(f"Total of students summoned in Ilhéus/Itabuna: {total_ii_summoned}")
    print(f"Total of students summoned in Juazeiro: {total_j_summoned}")
    print(f"Total of students summoned in Vitória da Conquista: {total_vc_summoned}")

declassified_embarcatech = pandas.read_csv("declassified_embarcatech.csv")

total_declassified = len(declassified_embarcatech)
total_fsa_declassified = len(declassified_embarcatech[declassified_embarcatech["Polo"] == "Feira de Santana"])
total_bjl_declassified = len(declassified_embarcatech[declassified_embarcatech["Polo"] == "Bom Jesus da Lapa"])
total_ii_declassified = len(declassified_embarcatech[declassified_embarcatech["Polo"] == "Ilhéus/Itabuna"])
total_j_declassified = len(declassified_embarcatech[declassified_embarcatech["Polo"] == "Juazeiro"])
total_vc_declassified = len(declassified_embarcatech[declassified_embarcatech["Polo"] == "Vitória da Conquista"])

if __name__ == "__main__":
    print("===========================================================")
    print(f"Total of students declassified in the Embarcatech: {total_declassified}")
    print(f"Total of students declassified in Feira de Santana: {total_fsa_declassified}")
    print(f"Total of students declassified in Bom Jesus da Lapa: {total_bjl_declassified}")
    print(f"Total of students declassified in Ilhéus/Itabuna: {total_ii_declassified}")
    print(f"Total of students declassified in Juazeiro: {total_j_declassified}")
    print(f"Total of students declassified in Vitória da Conquista: {total_vc_declassified}")

