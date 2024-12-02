import random
import threading

titulo = "threads em python"

def selection_sort(lista):
    print('ordenação', titulo)
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
    print('gravar arquivo', titulo, 'inicío')
    with open(filename, 'w') as f:
        for item in lista:
            f.write(f"{item}\n")
    print('gravar arquivo', titulo, 'fim')

def generate_random_numbers(len, lower_bound, upper_bound):
    print(titulo)
    return [random.randint(lower_bound, upper_bound) for _ in range(len)]

def main():
    # Gera 1000 números aleatórios entre 1 e 1000
    numeros = generate_random_numbers(10000, 1, 1000)
    
    # Cria uma thread para ordenar a lista
    sort_thread = threading.Thread(target=selection_sort, args=(numeros,))
    #print('thread de ordenação criada')

    # Cria uma thread para salvar número em arquivo
    sort_thread_gravar = threading.Thread(target=save_to_file, args=(numeros, 'lista_ordenada_por_thread.txt',))
    print("thread de gravar arquivo criada")

    sort_thread_gravar.start()
    print('thread de gravar arquivo iniciada')

    # Inicia a thread de ordenação
    sort_thread.start()
    #print('thread de ordenação solicitada para iniciar a execução')
    

    # Aguarda a conclusão da thread de ordenação
    sort_thread.join()
    #print('thread de ordenação concluída')
    
    sort_thread_gravar.join()
    print('thread de gravar arquivo concluída')

    # Salva a lista ordenada em um arquivo
    #save_to_file(numeros, 'lista_ordenada.txt')
    #print("A lista ordenada foi salva no arquivo 'lista_ordenada.txt'.")

# Executa a função principal
main()
