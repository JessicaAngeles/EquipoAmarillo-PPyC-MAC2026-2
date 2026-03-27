import requests
from PIL import Image
import numpy as np
import io
import threading

url_img = (
    "https://images.unsplash.com/"
    "photo-1506748686214-e9df14d4d9d0?w=1080"
)

response = requests.get(url_img)
img = Image.open(io.BytesIO(response.content))
matriz = np.array(img)

def procesar_bloque(matriz, inicio, fin):
    for i in range(inicio, fin):
        for j in range(matriz.shape[1]):
            r, g, b = matriz[i, j]
            gris = int(0.299*r + 0.587*g + 0.114*b)
            matriz[i, j] = [gris, gris, gris]

def escala_grises_threads(matriz, num_hilos):
    alto = matriz.shape[0]
    threads = []
    bloque = alto // num_hilos

    for i in range(num_hilos):
        inicio = i * bloque
        if i != num_hilos - 1:
            fin = (i + 1) * bloque
        else:
            fin = alto
        threads.append( 
            threading.Thread(target=procesar_bloque, args=(matriz, inicio, fin))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return matriz

if __name__ == "__main__" :

    matriz_gris2 = escala_grises_threads(matriz, 8)
    Image.fromarray(matriz_gris2.astype('uint8')).save("./imagen_threads.jpg")