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
        
    def remover(self, id_paciente):
        """Remove um paciente internado com base no ID."""
        self.raiz = self._remover_recursivo(self.raiz, id_paciente)
    
    def _remover_recursivo(self, no_atual, id_paciente):
        """Função auxiliar recursiva para remover pacientes internados"""
        if no_atual is None:
            return no_atual
        if id_paciente < no_atual.paciente.id:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, id_paciente)
        elif id_paciente > no_atual.paciente.id:
            no_atual.direita = self._remover_recursivo(no_atual.direita, id_paciente)
        else:
            # Caso 1: Nó a ser removido não tem filhos (é uma folha)
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
            # Caso 2: Nó a ser removido tem apenas um filho
            elif no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            # Caso 3: Nó a ser removido tem dois filhos
            else:
                sucessor = self._buscar_menor(no_atual.direita)
                no_atual.paciente = sucessor.paciente
                no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.paciente.id)
        return no_atual

    def _buscar_menor(self, no):
        """Encontra o menor valor da subárvore à direita."""
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

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
