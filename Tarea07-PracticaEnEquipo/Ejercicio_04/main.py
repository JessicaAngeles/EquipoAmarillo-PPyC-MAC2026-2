import urllib.request
from collections import Counter
import re
import threading
libros = [
    ("https://www.gutenberg.org/cache/epub/1342/pg1342.txt", "Orgullo y Prejuicio"),
    ("https://www.gutenberg.org/cache/epub/84/pg84.txt", "Frankenstein"),
    ("https://www.gutenberg.org/cache/epub/11/pg11.txt", "Alicia en el pais de las maravillas")
]
resultados = []
lock = threading.Lock()
def contar_palabras(url):
    respuesta = urllib.request.urlopen(url)
    texto = respuesta.read().decode('utf-8').lower()
    lista_palabras = re.findall(r'\b\w+\b', texto)
    return Counter(lista_palabras)
def contar_palabras_libro(url, nombre):
    print(f"Procesando: {nombre}")
    contador = contar_palabras(url)
    with lock:
        resultados.append(contador)

if __name__ == "__main__":
    threads = []
    for url, nombre in libros:
        thread = threading.Thread(target=contar_palabras_libro, args=(url, nombre))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    resultado_final = Counter()
    for parcial in resultados:
        resultado_final.update(parcial)

    print("\nTop 20 palabras más frecuentes:\n")
    for palabra, freq in resultado_final.most_common(20):
        print(f"{palabra}: {freq}")
