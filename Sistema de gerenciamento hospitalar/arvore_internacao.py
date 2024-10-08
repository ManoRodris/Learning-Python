class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Insere um novo valor na árvore binária de busca."""
        novo_no = No(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, no_atual, novo_no):
        """Função auxiliar recursiva para encontrar a posição de inserção."""
        if novo_no.valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir_recursivo(no_atual.direita, novo_no)

    def buscar(self, valor):
        """Busca um valor na árvore binária de busca."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no_atual, valor):
        """Função auxiliar recursiva para busca."""
        if no_atual is None:
            return False  # O valor não foi encontrado.
        if valor == no_atual.valor:
            return True  # Valor encontrado.
        elif valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

    def travessia_em_ordem(self):
        """Realiza uma travessia em ordem (in-order) e retorna os nós da árvore."""
        elementos = []
        self._travessia_em_ordem_recursiva(self.raiz, elementos)
        return elementos

    def _travessia_em_ordem_recursiva(self, no_atual, elementos):
        """Função auxiliar para a travessia em ordem."""
        if no_atual:
            self._travessia_em_ordem_recursiva(no_atual.esquerda, elementos)
            elementos.append(no_atual.valor)
            self._travessia_em_ordem_recursiva(no_atual.direita, elementos)
