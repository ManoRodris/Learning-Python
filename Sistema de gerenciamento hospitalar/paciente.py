class Paciente:
    
    def __init__(self, nome, idade, id_paciente, status):
        """Inicia os atributos do paciente"""
        self.nome = nome
        self.idade = idade
        self.id = id_paciente
        self.status = status 
    
    def __repr__(self):
        """Exibe os atributos do paciente"""
        return f"Paciente(Nome: {self.nome}, ID: {self.id}, Idade: {self.idade}, Status: {self.status})"
