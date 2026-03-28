# Comparativa de Rendimiento: Peticiones Secuenciales vs. Concurrencia (Threads) 

# Descripción del Proyecto
El script realiza consultas a la API de para obtener el clima actual de cuatro ciudades distintas (CDMX, Nueva York, Londres y Tokio). El objetivo principal no es el procesamiento de los datos climáticos en sí, sino medir y comparar el tiempo entre:

1. **Ejecución Secuencial:** El programa espera a que la petición de una ciudad termine para comenzar con la siguiente.
2. **Ejecución Concurrente:** El programa utiliza la biblioteca **threading** para lanzar todas las peticiones de red simultáneamente.

## Tecnologías y Requisitos
 1. Python 3.x
 2. Módulo `requests` (para las peticiones HTTP)
 3. Módulos nativos de Python: `time`, `threading`

Para instalar las dependencias necesarias, utilice:
```bash
pip install -r requirements.txt