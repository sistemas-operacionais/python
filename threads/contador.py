import threading
import time

# Recurso compartilhado
contador = 0
# Lock para sincronização
lock = threading.Lock()

def incrementar(nome):
    global contador
    for _ in range(10):
        # Adquirir o lock antes de modificar o recurso compartilhado
        print(f'acesso - solicitado - {nome}')
        lock.acquire()
        print(f'acesso - concedido - {nome}')
        contador += 1
        time.sleep(5)
        # Liberar o lock após a modificação
        lock.release()
        print(f'liberado - {nome}')

# Criando threads
thread1 = threading.Thread(target=incrementar, args=("Thread 1",))
thread2 = threading.Thread(target=incrementar, args=("Thread 2",))

# Iniciando threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

print(f"Valor final do contador: {contador}")