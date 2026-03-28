import threading
import time

boletos_disponibles = 1000

def vender_boletos(cantidad):
    global boletos_disponibles
    temp = boletos_disponibles
    time.sleep(0.0001)
    boletos_disponibles = temp - cantidad
    
# Lista para almacenar los hilos
hilos = []

#Tarea Instanciar multiples hilos que ejecuten esta funcion de forma concurrente .
for _ in range(100):
    t = threading.Thread(target=vender_boletos, args=(1,))
    hilos.append(t)
    t.start()

# Espera a que todos los hilos terminen
for t in hilos:
    t.join()


print(f"--- RESULTADOS SIN LOCK ---")
print("Boletos disponibles:", boletos_disponibles)