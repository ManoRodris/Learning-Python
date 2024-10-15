from fila_atendimento import FilaAtendimento
from pilha_prontuario import PilhaProntuario
from arvore_internacao import ArvoreInternacao
from algoritmos import merge_sort, quick_sort, busca_binaria

class Hospital:

    def __init__(self):
        self.fila_atendimento = FilaAtendimento()
        self.pilha_prontuario = PilhaProntuario()
        self.arvore_internacao = ArvoreInternacao()

        # Métodos para gerenciar o fluxo de pacientes e prontuários

    def adicionar_paciente_fila(self, paciente):
        """Adiciona o paciente a fila de atendimento"""
        self.fila_atendimento.adicionar_paciente(paciente)

    def atender_paciente(self):
        """Atende o próximo paciente da fila de atendimento, em seguida insere o prontuário na pilha"""
        paciente = self.fila_atendimento.remover_paciente()
        if paciente:
            paciente.status = "alta" 
            self.pilha_prontuario.adicionar_prontuario(paciente)
            print(f"Paciente {paciente.nome} foi atendido")
        else:
            print("Não há pacientes na fila para atendimento")

    def internar_paciente(self, paciente):
        """Interna o paciente, inserindo-o na árvore"""
        paciente.status = "internado"
        self.arvore_internacao.inserir(paciente)

    def buscar_paciente_internado(self, id_paciente):
        """Busca um paciente pelo ID na árvore"""
        paciente_buscado = self.arvore_internacao.buscar(id_paciente)
        if paciente_buscado:
            return f"Paciente encontrado na árvore: {paciente_buscado.paciente}"
        else:
            return "Paciente não encontrado na árvore"
    
    def ordenar_prontuarios(self, key):
        """Ordena os prontuários armazenados na pilha por um atributo especificado."""
        prontuarios = list(self.pilha_prontuario.pilha)  
        
        if len(prontuarios) <= 1000:
            # Se o número de prontuários for pequeno, usa Merge Sort
            return merge_sort(prontuarios, key)
        else:
            # Para grandes volumes, usa Quick Sort
            return quick_sort(prontuarios, key)

    def buscar_prontuario(self, key, valor):
        """Ordena os prontuários por um atributo especificado para então realizar a busca binária."""
        prontuarios = self.ordenar_prontuarios(key)
        prontuario_buscado = busca_binaria(prontuarios, key, valor)
        if prontuario_buscado:
            return prontuario_buscado
        else:
            return "Prontuário não encontrado"
