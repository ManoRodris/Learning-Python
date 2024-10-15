class PilhaProntuario:

    def __init__(self):
        """Cria a pilha de prontuarios"""
        self.pilha = []

    def adicionar_prontuario(self, prontuario):
        """Adiciona um novo prontuario a pilha"""
        self.pilha.append(prontuario)

    def remover_prontuario(self):
        """Remove um prontuario do topo da pilha, se a pilha não estiver vazia"""
        if self.pilha:
            return self.pilha.pop()
        return None

    def ultimo_prontuario(self):
        """Retorna o prontuario do topo da pilha, se a pilha não estiver vazia"""
        if self.pilha:
            return self.pilha[-1]
        return None
    
    def __repr__(self):
        """Exibe todos os prontuários"""
        return f"Prontuários: {self.pilha}"