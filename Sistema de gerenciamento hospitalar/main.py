from hospital import Hospital
from paciente import Paciente

hospital = Hospital()

# Testando a inserção e remoção de pacientes na fila.

paciente1 = Paciente("Rodrigo", 22, 1, "aguardando")
paciente2 = Paciente("Helder", 20, 2, "aguardando")
paciente3 = Paciente("Pedro", 19, 3, "aguardando")
paciente4 = Paciente("Gabi", 23, 4, "aguardando")

hospital.adicionar_paciente_fila(paciente1) 
hospital.adicionar_paciente_fila(paciente2)
hospital.adicionar_paciente_fila(paciente3)
hospital.adicionar_paciente_fila(paciente4)

print(hospital.fila_atendimento.__repr__()) # Exibe toda a fila, após a inserção dos pacientes

hospital.atender_paciente() # Atende o paciente, removendo-o da fila de atendimento

print(hospital.fila_atendimento.__repr__()) # Exibe toda a fila, após o ultimo atendimento

# Testando a pilha de prontuários e o acesso ao último prontuário.

hospital.atender_paciente() # Remove da fila e adiciona a pilha de prontuários

print(hospital.pilha_prontuario.ultimo_prontuario()) # Exibe o ultimo prontuario, ilustrando que o status do paciente agora é "alta"

# Validando a inserção, busca e remoção de pacientes internados na árvore.

paciente5 = Paciente("Jorge", 27, 5, "aguardando")
paciente6 = Paciente("Arthur", 22, 6, "aguardando")
paciente7 = Paciente("Alberto", 26, 7, "aguardando")
paciente8 = Paciente("Fabio", 17, 8, "aguardando")

# Inserção

hospital.internar_paciente(paciente5)
hospital.internar_paciente(paciente6)
hospital.internar_paciente(paciente7)
hospital.internar_paciente(paciente8)

print(hospital.arvore_internacao.__repr__()) # Exibe a árvore após a internação dos pacientes

# Busca

print(hospital.buscar_paciente_internado(7)) # Teste com paciente que realmente está na árvore
print(hospital.buscar_paciente_internado(9)) # Teste com paciente que não está na árvore

# Remoção 

hospital.atender_paciente_internado(6) # Teste com paciente que realmente está na árvore
hospital.atender_paciente_internado(3) # Teste com paciente que não está na árvore

print(hospital.arvore_internacao.__repr__()) # Exibe a árvore após o atendimento dos pacientes internados

# Testando os algoritmos de busca e ordenação nos prontuários.

hospital.atender_paciente() # Teste com penúltimo paciente que está na fila
hospital.atender_paciente() # Teste com último paciente que está na fila
hospital.atender_paciente() # Teste após não haver mais pacientes na fila

prontuarios_ordenados_por_nome = hospital.ordenar_prontuarios("nome") # Ordenando por nome

print(prontuarios_ordenados_por_nome)

prontuarios_ordenados_por_id = hospital.ordenar_prontuarios("id") # Ordenando por ID

print(prontuarios_ordenados_por_id)

print(hospital.buscar_prontuario("id", 4)) # Busca por ID da paciente Gabi
print(hospital.buscar_prontuario("nome", "Helder")) # Busca por nome do paciente Helder
print(hospital.buscar_prontuario("nome", "Adalberto")) # Busca por nome de um paciente que não está dentre os prontuários





