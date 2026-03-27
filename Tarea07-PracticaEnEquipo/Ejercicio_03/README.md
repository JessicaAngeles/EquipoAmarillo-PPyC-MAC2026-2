# Tarea 7 - Ejercicio 3
## Particionamiento de Espacios: Procesamiento de Imágenes Digitales

En el código se muestran tres enfoques para realizar el ejercicio:

- Forma secuencial
- Uso de hilos (`threading`)  
- Uso de multiprocessing (`multiprocessing.Pool`) 

Cada enfoque tiene su propia función.

## Enfoque secuencual
***El tiempo que dura este enfoque es de aproximadamente 9 segundos***

## Enfoque con threads

En la versión con threads, todos los hilos comparten el mismo espacio de memoria.  
Cada hilo procesa un segmento distinto de la matriz por filas, modificando directamente la matriz original.

***El tiempo que dura este enfoque es de aproximadamente 9 segundos***

## Enfoque con multiprocessing

En la versión con multiprocessing, la matriz se divide en varios segmentos independientes.

Cada segmento se almacena en una lista y se envía a distintos procesos mediante `multiprocessing.Pool`.

Cada proceso:
- Recibe un segmento de la imagen
- Aplica la conversión a escala de grises
- Devuelve el segmento procesado

Posteriormente, los segmentos se reconstruyen en una sola matriz utilizando `np.vstack`.

No es necesario preocuparse por el orden de los segmentos, ya que Pool.map conserva el orden de entrada y `np.vstack` los une respetando ese mismo orden.

***El tiempo que dura este enfoque es de aproximadamente 5 segundos***


## requiremets.txt

> pip install -r requirements.txt

requests==2.32.5
Pillow==11.3.0
numpy==2.2.5
