## Alternativa 1. 
    ## Escritura inmedianta, cada uno de hilos hacen una conexión
import time
import random
import requests
import threading
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text

semaforo = threading.Semaphore(8)

def conexionBD():
    user = "postgres"
    password = "supersecret"
    host = "localhost"
    port = "5432"
    database = "db_alternativa1"
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)

def obtener_guardar_precio(symbol, engine):
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

        try:
            with engine.connect() as connector:
                fecha_actual = datetime.now()
                query = text("INSERT INTO inversiones (symbol, price, register_date) VALUES (:s, :p, :f)")
                connector.execute(query, {"s": symbol, "p": precio, "f": fecha_actual})
                connector.commit()
                print(f"Guardado: {symbol} cuesta {precio}")
        except Exception as e:
            print(f"Error al guardar {symbol}: {e}")
    

if __name__ == "__main__":
    engine = conexionBD()

    with open("Tarea 6/data/lista_sp500.txt", "r") as f:
        lista_symbolos = eval(f.read())
    
    thareads = []
    for symbol in lista_symbolos:
        t = threading.Thread(target = obtener_guardar_precio, args = (symbol, engine))
        thareads.append(t)
        t.start()

    for t in thareads:
        t.join()

    df = pd.read_sql("SELECT *  FROM inversiones", engine)
    print(df)

    print("Proceso finalizado")