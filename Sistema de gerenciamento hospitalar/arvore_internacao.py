class NoPaciente:
    def __init__(self, paciente):
        """Cria um nó da árvore binária de busca, armazenando um paciente"""
        self.paciente = paciente
        self.esquerda = None
        self.direita = None

class ArvoreInternacao:
    def __init__(self):
        """Inicia a árvore"""
        self.raiz = None

    def inserir(self, paciente):
        """Insere um novo paciente na árvore binária de busca."""
        if self.raiz is None:
            self.raiz = NoPaciente(paciente)
        else:
            self._inserir_recursivo(self.raiz, paciente)

    def _inserir_recursivo(self, no_atual, paciente):
        """Função auxiliar recursiva para encontrar a posição de inserção."""
        if paciente.id < no_atual.paciente.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoPaciente(paciente)
            else:
                self._inserir_recursivo(no_atual.esquerda, paciente)
        elif paciente.id > no_atual.paciente.id:
            if no_atual.direita is None:
                no_atual.direita = NoPaciente(paciente)
            else:
                self._inserir_recursivo(no_atual.direita, paciente)

    def buscar(self, id_paciente):
        """Busca um paciente pelo id na árvore binária de busca."""
        return self._buscar_recursivo(self.raiz, id_paciente)

    def _buscar_recursivo(self, no_atual, id_paciente):
        """Função auxiliar recursiva para busca."""
        if no_atual is None or no_atual.paciente.id == id_paciente:
            return no_atual
        if id_paciente < no_atual.paciente.id:
            return self._buscar_recursivo(no_atual.esquerda, id_paciente)
        else:
            return self._buscar_recursivo(no_atual.direita, id_paciente)

    def __repr__(self):
        """Exibe todos os pacientes internados"""
        pacientes = []
        self._in_order(self.raiz, pacientes)
        return f"Árvore de internação: {pacientes}"
    
    def _in_order(self, no_atual, pacientes):
        """Ordena os pacientes na árvore"""
        if no_atual is not None:
            self._in_order(no_atual.esquerda, pacientes)
            pacientes.append(no_atual.paciente)
            self._in_order(no_atual.direita, pacientes)
