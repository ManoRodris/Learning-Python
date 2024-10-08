from collections import deque

class FilaAtendimento:

    def __init__(self):
        """Instancia a fila de atendimento"""
        self.fila = deque()

    def adicionar_paciente(self, paciente):
        """Adiciona pacientes a fila de atendimento"""
        self.fila.append(paciente)

    def remover_paciente(self):
        """Remove pacientes da fila de atendimento"""
        self.fila.popleft()
