import requests
from PIL import Image
import numpy as np
import io
import threading
import time
import multiprocessing

# Descarga de imagen pública en alta resolución desde Unsplash
# Repositorio : images.unsplash.com

url_img = (
    "https://images.unsplash.com/"
    "photo-1506748686214-e9df14d4d9d0?w=1080"
)

response = requests.get(url_img)
img = Image.open (io. BytesIO (response.content))
matriz = np.array(img) # Matriz de pixeles (Hight, Width, Channels)

def escala_grises_secuencial(matriz):
    alto, ancho, canales = matriz.shape
    for i in range(alto):
        for j in range(ancho):
            r, g, b = matriz [i, j]
            # Ecuación de luminancia CIE 1931
            gris = int(0.299*r + 0.587*g + 0.114*b)
            matriz [i, j] = [gris, gris, gris]
    return matriz

# Tarea: Dividir el rango de filas en N segmentos y distribuir entre N hilos

def escala_grises_threads(matriz, inicio, fin):
    ancho = matriz.shape[1]
    for i in range(inicio, fin):
        for j in range(ancho):
            r, g, b = matriz [i, j]
            # Ecuación de luminancia CIE 1931
            gris = int(0.299*r + 0.587*g + 0.114*b)
            matriz [i, j] = [gris, gris, gris]


# Funcion para multiprocessing
def escala_grises_multiprocessing(segmento):
    alto, ancho, canales = segmento.shape
    for i in range(alto):
        for j in range(ancho):
            r, g, b = segmento [i, j]
            # Ecuación de luminancia CIE 1931
            gris = int(0.299*r + 0.587*g + 0.114*b)
            segmento [i, j] = [gris, gris, gris]
    return segmento

if __name__ == "__main__":
    ###### Versión Secuencial
    start = time.time()
    print("Inicia versión secuencial")
    matriz_gris = escala_grises_secuencial(matriz.copy())

    # Convierte a imagen
    img_gris_sec = Image.fromarray(matriz_gris.astype('uint8'))
    img_gris_sec.save("imagen_grises_secuencial.jpg")
    
    print("Tiempo de versión secuencial fue de ", time.time() - start)
    
    ########## Inicia versión con threading
    print("\nInicia versión con threads")
    threads = []
    matriz_threads = matriz.copy()
    alto, ancho, canales  = matriz.shape

    N = 8
    bloque = alto // N

    for i in range(N):
        inicio = i * bloque
        if i != N-1:
            fin = (i + 1) * bloque
        else:
            fin = alto  # El bloque final se ajusta a 'alto', para no perder las ultimas filas

        threads.append(
            threading.Thread(target=escala_grises_threads, args=(matriz_threads, inicio, fin,))
        )

    start = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    img_gris_thre = Image.fromarray(matriz_threads.astype('uint8'))
    img_gris_thre.save("imagen_grises_threads.jpg")
    print("Tiempo de versión con threads fue de ", time.time() - start)

    ########### Con multiprocessing
    print("\nInicia versión con multiprocessing.Pool()")

    start = time.time()

    matriz_m = matriz.copy()

    num_procesos = multiprocessing.cpu_count()
    bloque_m = alto // num_procesos

    segmentos = []

    # Dividimos imagen entre num_procesos
    for i in range(num_procesos):
        inicio = i * bloque
        if i != N-1:
            fin = (i + 1) * bloque
        else:
            fin = alto

        segmentos.append(matriz_m[inicio:fin])

    # Con Pool
    with multiprocessing.Pool() as pool:
        resultados = pool.map(escala_grises_multiprocessing, segmentos)

    matriz_mp = np.vstack(resultados)
    
    img_gris_mp = Image.fromarray(matriz_mp.astype('uint8'))
    img_gris_mp.save("imagen_grises_mp.jpg")
    print("Tiempo de versión con multiprocessing.Pool() fue de ", time.time() - start)

    print(num_procesos)