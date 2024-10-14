class PilhaProntuario:

    def __init__(self):
        """Cria a pilha de prontuarios"""
        self.prontuarios = []

    def adicionar_prontuario(self, prontuario):
        """Adiciona um novo prontuario a pilha"""
        self.prontuarios.append(prontuario)

    def remover_prontuario(self):
        """Remove um prontuario do topo da pilha, se a pilha não estiver vazia"""
        if self.prontuarios:
            return self.prontuarios.pop()
        return None

    def ultimo_prontuario(self):
        """Retorna o prontuario do topo da pilha, se a pilha não estiver vazia"""
        if self.prontuarios:
            return self.prontuarios[-1]
        return None
    
    def __repr__(self):
        """Exibe todos os prontuários"""
        return f"Prontuarios: {self.prontuarios}"