import time
import requests
import threading

ciudades = [
    {"lat": 19.43, "lon": -99.13}, ## CDMX
    {"lat": 40.71, "lon": -74.00}, ## NY
    {"lat": 51.50, "lon": -0.12}, ## Londres
    {"lat": 35.68, "lon": 139.69} ## Tokio
]

def obtener_clima(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = f"?latitude={lat}&longitude={lon}&current_weather=true"
    url = base_url + params
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()['current_weather']
    return None


if __name__ == "__main__":
    ## SECUENCIAL
    inicio = time.time()
    for ciudad in ciudades:
        obtener_clima(ciudad['lat'], ciudad['lon'])
    
    tiempo_sec = time.time() - inicio
    print(f"Tiempo secuenciales: {tiempo_sec: .4f} segundos")

    ## CON THREADS
    inicio = 0
    inicio = time.time()
    threads = []

    for thread in ciudades:
        t = threading.Thread(target = obtener_clima, args = (ciudad['lat'], ['lon']))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

    tiempo_thread = time.time() - inicio
    print(f"Tiempo con THREADS: {tiempo_thread: .4f} segundos")
    print(f"""Diferencia de tiempo entre secuencial y concurrencia: 
          {max(tiempo_sec, tiempo_thread) - min(tiempo_sec, tiempo_thread): .4f} segundo""")