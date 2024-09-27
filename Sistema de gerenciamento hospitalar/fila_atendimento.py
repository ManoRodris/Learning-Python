from collections import deque

class FilaAtendimento:

    def __init__(self):
        self.fila = deque()

    def adicionar_paciente(self, paciente):
        self.fila.append(paciente)

    def remover_paciente(self):
        self.fila.popleft()
