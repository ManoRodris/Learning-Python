class PilhaProntuario:

    def __init__(self):
        self.prontuarios = []

    def adicionar_prontuario(self, prontuario):
        self.prontuarios.append(prontuario)

    def remover_prontuario(self):
        self.prontuarios.pop()

    def ultimo_prontuario(self):
        return self.prontuarios[-1]