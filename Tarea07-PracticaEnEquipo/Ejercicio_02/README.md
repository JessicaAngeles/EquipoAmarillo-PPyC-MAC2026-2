# Tarea 7 - Ejercicio 2
# Condiciones de Carrera y Sincronización: Exclusión Mutua

## Descripción

Este ejercicio demuestra el problema de las **condiciones de carrera** en programación concurrente y cómo solucionarlo utilizando mecanismos de **sincronización** como `threading.Lock()`.

---

## ¿Qué es una condición de carrera?

Una condición de carrera ocurre cuando múltiples hilos acceden y modifican una misma variable al mismo tiempo sin control.

Esto puede provocar:

* Resultados incorrectos
* Datos inconsistentes
* Comportamiento impredecible

---

## Solución: Exclusión Mutua

Se utiliza un `Lock` para asegurar que **solo un hilo a la vez** pueda ejecutar una sección crítica del código.

---

## Objetivo de la práctica

* Ejecutar múltiples hilos sin sincronización
* Observar resultados incorrectos
* Implementar un `Lock`
* Verificar que el resultado sea correcto

---

## Archivos del proyecto

* `Ejercicio2_sinlock.py` → Simulación con condición de carrera
* `Ejercicio2_conlock.py` → Solución usando `threading.Lock()`


## Resultados esperados

### Sin Lock

* Valores inconsistentes
* Diferencias entre conteos
* Resultado distinto en cada ejecución

### Con Lock

* Resultados correctos
* Datos consistentes

---

## Ejemplo de salida

### Sin Lock

```bash
--- RESULTADOS SIN LOCK ---
Boletos Disponibles: 928
```

### Con Lock

```bash
--- RESULTADOS CON LOCK --
Boletos Disponibles: 900
```

---

## ⏱️ Rendimiento

El uso de `Lock` garantiza consistencia, aunque puede aumentar ligeramente el tiempo de ejecución debido a la sincronización.

---

## Requeriments.txt

* No se requieren librerías externas

---

## Conclusión

* Las condiciones de carrera generan errores difíciles de detectar
* La exclusión mutua es esencial en programación concurrente
* `threading.Lock()` permite proteger secciones críticas y asegurar resultados correctos

---
