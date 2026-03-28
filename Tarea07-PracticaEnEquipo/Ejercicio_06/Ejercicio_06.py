import requests
import threading
import time

archivos = [
    "https://erg.abdn.ac.uk/test/1KB.txt",                    
    "https://erg.abdn.ac.uk/test/10KB.txt",                   
    "https://www.gutenberg.org/cache/epub/11/pg11.txt",       
    "https://www.gutenberg.org/cache/epub/84/pg84.txt",       
    "https://jsonplaceholder.typicode.com/posts",             
]

def descargar_archivo(url, nombre_salida):
    respuesta = requests.get(url, timeout=20)
    with open(nombre_salida, 'wb') as archivo:
        archivo.write(respuesta.content)


def descargar_con_hilo(url, indice):
    nombre = f"archivo_hilo_{indice+1}.txt"
    print(f"Hilo {indice+1} descargando {url}")
    descargar_archivo(url, nombre)
    print(f"Hilo {indice+1} terminó")

# Secuencial
print("="*20)
print("Descarga secuencial")
inicio = time.time()

for i, url in enumerate(archivos):
    nombre = f"archivo_{i+1}.txt"
    print(f"Descargando {url}...")
    descargar_archivo(url, nombre)
    print(f"Guardado como {nombre}")

fin = time.time()
print(f"Tiempo total: {fin - inicio:.2f} segundos")

#Hilos
print("Descarga con hilos")
inicio_2 = time.time()

hilos = []
for i, url in enumerate(archivos):
    hilo = threading.Thread(target=descargar_con_hilo, args=(url, i))
    hilos.append(hilo)

for hilo in hilos:
    hilo.start()  # Iniciar el hilo

for hilo in hilos:
    hilo.join()

fin_2 = time.time()
print(f"Tiempo total: {fin_2 - inicio_2:.2f} segundos")

diff_1 = fin - inicio
diff_2 = fin_2 - inicio_2

print(f"Secuencial: {diff_1} \n Hilos: {diff_2}")

