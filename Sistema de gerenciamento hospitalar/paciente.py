class Paciente:

    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id
        self.status = ["esperando", "internado", "alta"]