def bubble_sort(prontuarios, key):
    """Ordena usando Bubble Sort, usa o parâmetro 'key' para ordenar"""
    n = len(prontuarios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if getattr(prontuarios[j], key) > getattr(prontuarios[j + 1], key):
                prontuarios[j], prontuarios[j + 1] = prontuarios[j + 1], prontuarios[j]
    return prontuarios

def quick_sort(prontuarios, key):
    """Ordena usando Quick Sort, usa o parâmetro 'key' para ordenar"""
    if len(prontuarios) <= 1:
        return prontuarios
    else:
        pivot = prontuarios[len(prontuarios) // 2]
        menores = [x for x in prontuarios if getattr(x, key) < getattr(pivot, key)]
        iguais = [x for x in prontuarios if getattr(x, key) == getattr(pivot, key)]
        maiores = [x for x in prontuarios if getattr(x, key) > getattr(pivot, key)]
        return quick_sort(menores, key) + iguais + quick_sort(maiores, key)

def busca_binaria(prontuarios, key, valor):
    """Realiza busca binária em uma lista de prontuários ordenados pelo 'key' especificado.
    O parâmetro 'valor' é o valor buscado."""
    inicio = 0
    fim = len(prontuarios) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if getattr(prontuarios[meio], key) == valor:
            return prontuarios[meio]
        elif getattr(prontuarios[meio], key) < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return None
