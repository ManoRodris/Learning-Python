def merge_sort(prontuarios, key):
    """Ordena usando Merge Sort, usa o parâmetro 'key' para ordenar"""
    
    # Caso base: Se a lista tiver 0 ou 1 elementos, já está ordenada
    if len(prontuarios) <= 1:
        return prontuarios
    
    # Divide a lista ao meio
    meio = len(prontuarios) // 2
    esquerda = merge_sort(prontuarios[:meio], key)
    direita = merge_sort(prontuarios[meio:], key)
    
    # Mescla as duas metades ordenadas
    return merge(esquerda, direita, key)

def merge(esquerda, direita, key):
    """Mescla duas listas ordenadas em uma única lista ordenada."""
    
    resultado = []
    i = 0  # Índice da lista da esquerda
    j = 0  # Índice da lista da direita
    
    # Mescla as duas listas enquanto houver elementos em ambas
    while i < len(esquerda) and j < len(direita):
        if getattr(esquerda[i], key) <= getattr(direita[j], key):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes da lista esquerda (se houver)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Adiciona os elementos restantes da lista direita (se houver)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado


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
