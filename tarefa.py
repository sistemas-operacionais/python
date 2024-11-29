import random

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

def save_to_file(lista, filename):
    with open(filename, 'w') as f:
        for item in lista:
            f.write(f"{item}\n")

def generate_random_numbers(len, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(len)]

# Gera 1000 números aleatórios entre 1 e 1000
print('gerando lista de números aleatórios')
numeros = generate_random_numbers(10000, 1, 100000)

# ordena lista de números
lista_ordenada = selection_sort(numeros)
print("Lista foi ordenada!")

# Salva a lista ordenada em um arquivo
save_to_file(lista_ordenada, 'lista_ordenada.txt')
print("A lista ordenada foi salva no arquivo 'lista_ordenada.txt'.")
