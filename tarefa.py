def selection_sort(lista):
    # Percorre toda a lista
    for i in range(len(lista)):
        # Encontra o menor elemento na parte não ordenada da lista
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[min_index] > lista[j]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Exemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Lista ordenada:", selection_sort(numeros))
