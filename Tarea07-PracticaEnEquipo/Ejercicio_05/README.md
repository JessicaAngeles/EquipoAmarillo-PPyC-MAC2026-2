# Generador y Procesador de Chistes con Hilos 

##  Descripción

Este programa implementa un sistema concurrente en Python utilizando **hilos (threads)**, donde:

* **Generadores** obtienen chistes desde una API pública.
* **Procesadores** consumen esos chistes y los guardan en archivos de texto.
* Se usa un **buffer compartido (cola)** para coordinar la comunicación entre hilos.

El programa se detiene cuando:

* Se alcanza un número máximo de chistes, o
* Se cumple un tiempo límite de ejecución.

---

## Tecnologías utilizadas

* Python 3
* Programación concurrente con:

  * `threading`
  * `queue`
* Consumo de APIs con:

  * `requests`

---

## Librerías necesarias

Instala las dependencias con:

```bash
pip install requests
```

> Las demás librerías (`threading`, `queue`, `time`) ya vienen incluidas en Python.

---

##  Cómo ejecutar

```bash
python nombre_del_archivo.py
```

---

## Funcionamiento

### Generadores (`generar`)

* Realizan peticiones a la API:

  ```
  https://api.chucknorris.io/jokes/random
  ```
* Insertan los chistes en un buffer compartido.
* Incrementan un contador global protegido por un `lock`.
* Detienen la ejecución al alcanzar el límite de chistes.

---

###  Procesadores (`procesar`)

* Extraen chistes del buffer.
* Los escriben en archivos:

  ```
  salida_0.txt
  salida_1.txt
  salida_2.txt
  ```
* Finalizan cuando reciben un valor `None` (señal de parada).

---

###  Control de ejecución

* `LIMITE_CHISTES`: número máximo de chistes a generar (50).
* `TIEMPO_EJECUCION`: tiempo máximo en segundos (5).
* `evento_fin`: evento que indica cuándo detener todos los hilos.

---

## Flujo del programa

1. Se crean:

   * 2 hilos generadores
   * 3 hilos procesadores

2. Los generadores producen chistes y los colocan en el buffer.

3. Los procesadores consumen y escriben los chistes en archivos.

4. El programa termina cuando:

   * Se alcanza el límite de chistes, o
   * Se cumple el tiempo máximo.

5. Se envían señales (`None`) para detener a los procesadores.

---

##  Salida

Se generan archivos de texto:

```
salida_0.txt
salida_1.txt
salida_2.txt
```

Cada archivo contiene múltiples chistes separados por líneas en blanco.

---

##  Consideraciones

* El buffer tiene tamaño limitado (`maxsize=20`), lo que evita sobrecarga.
* Se usa `lock` para evitar condiciones de carrera.
* Se usa `Event` para coordinar el final de ejecución.
* Maneja errores de red en las peticiones HTTP.


