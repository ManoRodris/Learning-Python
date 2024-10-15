from hospital import Hospital
from paciente import Paciente

hospital = Hospital()

paciente1 = Paciente("Rodrigo", 22, 1, "aguardando")
paciente2 = Paciente("Helder", 20, 2, "aguardando")
paciente3 = Paciente("Pedro", 19, 3, "aguardando")
paciente4 = Paciente("Gabi", 23, 4, "aguardando")

# Testando a inserção e remoção de pacientes na fila.

hospital.adicionar_paciente_fila(paciente1)
hospital.adicionar_paciente_fila(paciente2)
hospital.adicionar_paciente_fila(paciente3)
hospital.adicionar_paciente_fila(paciente4)

print(hospital.fila_atendimento.__repr__())

hospital.atender_paciente()

print(hospital.fila_atendimento.__repr__())

# Testando a pilha de prontuários e o acesso ao último prontuário.

hospital.atender_paciente()

print(hospital.pilha_prontuario.ultimo_prontuario())

# Validando a inserção, busca e remoção de pacientes internados na árvore.

paciente5 = Paciente("Jorge", 27, 5, "aguardando")
paciente6 = Paciente("Arthur", 22, 6, "aguardando")
paciente7 = Paciente("Alberto", 26, 7, "aguardando")
paciente8 = Paciente("Fabio", 17, 8, "aguardando")

hospital.internar_paciente(paciente5)
hospital.internar_paciente(paciente6)
hospital.internar_paciente(paciente7)
hospital.internar_paciente(paciente8)

print(hospital.arvore_internacao.__repr__())

print(hospital.buscar_paciente_internado(7))
print(hospital.buscar_paciente_internado(9))

# Testando os algoritmos de busca e ordenação nos prontuários.

hospital.atender_paciente()
hospital.atender_paciente()
hospital.atender_paciente()
hospital.atender_paciente()

prontuarios_ordenados_por_nome = hospital.ordenar_prontuarios("nome")

print(prontuarios_ordenados_por_nome)

prontuarios_ordenados_por_id = hospital.ordenar_prontuarios("id")

print(prontuarios_ordenados_por_id)

print(hospital.buscar_prontuario("id", 4))
print(hospital.buscar_prontuario("nome", "Helder"))
print(hospital.buscar_prontuario("nome", "Adalberto"))





