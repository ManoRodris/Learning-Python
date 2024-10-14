from collections import deque

class FilaAtendimento:

    def __init__(self):
        """Cria a fila de atendimento"""
        self.pacientes = deque()

    def adicionar_paciente(self, paciente):
        """Adiciona pacientes a fila de atendimento"""
        self.pacientes.append(paciente)

    def remover_paciente(self):
        """Se houver pacientes na fila, remove o primeiro da fila de atendimento"""
        if self.pacientes:
            return self.pacientes.popleft()
        return None
    
    def buscar_paciente(self, nome):
        """Busca um paciente na fila a partir do seu nome (busca sequencial)"""
        for paciente in self.pacientes:
            if paciente.nome == nome:
                return paciente
        return None

    def __repr__(self):
        """Exibe a fila de atendimento"""
        return f"Fila de atendimento: {list(self.pacientes)}"