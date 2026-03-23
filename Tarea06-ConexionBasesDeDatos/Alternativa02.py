## Alternativa 2. Dos fases 
    ## Fase 1. Todos los hilos scrapean
    ## Fase 2. Todos los hilos insertan

import time
import random
import requests
import threading
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import queue
from sqlalchemy import create_engine, text

semaforo = threading.Semaphore(8)

cola_datos = queue.Queue()

def conexionBD():
    user = "postgres"
    password = "supersecret"
    host = "localhost"
    port = "5432"
    database = "db_alternativa2"
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)

## FASE 1
def obtener_precio(symbol):
    with semaforo:
        URL = f"https://finance.yahoo.com/quote/{symbol}"
        headers = {"User-Agent":"MiProyecto/1.0"}

        precio = "N/A"

        while True:
            time.sleep(5 * random.random())
            response = requests.get(URL, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                valor = soup.find("span", {"data-testid":"qsp-price"})
                if valor:
                    precio = valor.text.strip()
                break
            else:
                break
    
        cola_datos.put({"s": symbol, "p": precio})
        print(f"En cola: {symbol} cuesta {precio}")

## Fase 2
def guardar_precio(engine):
    while not cola_datos.empty():
        dato = cola_datos.get()    
        try:
            with engine.connect() as conector:
                fecha_actual = datetime.now()
                query = text("INSERT INTO inversiones (symbol, price, register_date) VALUES (:s, :p, :f)")
                conector.execute(query,{"s": dato["s"], "p":dato["p"], "f":fecha_actual})
                conector.commit()
        except Exception as e:  
            print(f"Error al guardar {dato["s"]}: {e}")
        finally:
            cola_datos.task_done()

if __name__ == "__main__":
    engine = conexionBD()

    with open("Tarea 6/data/lista_sp500.txt", "r") as f:
        lista_symbolos = eval(f.read())
    
    ## Recolección de datos 
    thareads_scrape = []

    for symbol in lista_symbolos:
        t = threading.Thread(target = obtener_precio, args = (symbol, ))
        thareads_scrape.append(t)
        t.start()

    for t in thareads_scrape:
        t.join()

    print("Recolección de datos terminada")

    ## Inserción en Base de datos
    threads_db = []

    for _ in range(3):
        t = threading.Thread(target = guardar_precio, args = (engine, ))
        threads_db.append(t)
        t.start()
    
    for t in threads_db:
        t.join()
    
    df = pd.read_sql("SELECT *  FROM inversiones", engine)
    print(df)

    print("Proceso finalizado")
