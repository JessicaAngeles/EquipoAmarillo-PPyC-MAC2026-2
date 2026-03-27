import requests
import queue
import threading
import time

LIMITE_CHISTES = 50
TIEMPO_EJECUCION = 5

buffer = queue.Queue(maxsize=20)
total_generados = 0

lock = threading.Lock()
evento_fin = threading.Event()

def generar(id_gen):
    global total_generados
    url_api = "https://api.chucknorris.io/jokes/random"

    while not evento_fin.is_set():
        try:
            respuesta = requests.get(url_api, timeout=3)
            dato = respuesta.json()['value']

            buffer.put(dato)

            with lock:
                total_generados += 1
                if total_generados >= LIMITE_CHISTES:
                    evento_fin.set()

            print(f"Generador {id_gen} obtuvo chiste")
        except Exception as err:
            print("Fallo en request:", err)

def procesar(id_proc):
    nombre_archivo = f"salida_{id_proc}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        while True:
            item = buffer.get()

            if item is None:
                break

            archivo.write(item + "\n\n")
            print(f"Procesador {id_proc} escribió chiste")

            buffer.task_done()

if __name__ == "__main__":
    lista_generadores = []
    lista_procesadores = []

    tiempo_inicio = time.time()

    for i in range(3):
        hilo = threading.Thread(target=procesar, args=(i,))
        lista_procesadores.append(hilo)
        hilo.start()

    for i in range(2):
        hilo = threading.Thread(target=generar, args=(i,))
        lista_generadores.append(hilo)
        hilo.start()

    while time.time() - tiempo_inicio < TIEMPO_EJECUCION:
        if evento_fin.is_set():
            break
        time.sleep(0.1)

    evento_fin.set()

    for hilo in lista_generadores:
        hilo.join()

    for _ in lista_procesadores:
        buffer.put(None)

    for hilo in lista_procesadores:
        hilo.join()

    print("\nEjecución finalizada.")
    print(f"Cantidad total de chistes: {total_generados}")