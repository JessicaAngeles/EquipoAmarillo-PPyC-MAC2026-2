import threading
import queue
import socket

cola_puertos = queue.Queue()

def revisar_puerto():
    while not cola_puertos.empty():
        try:
            pagina, puerto = cola_puertos.get_nowait()
        except queue.Empty:
            break

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((pagina, puerto)) == 0:
                print(f"{pagina} puerto {puerto} abierto")
        
        cola_puertos.task_done()



if __name__ == "__main__":
    paginas = ["scanme.nmap.org", "testphp.vulnweb.com","example.com","google.com"]


    for pagina in paginas:
        for puerto in range(1, 1000):
            cola_puertos.put((pagina, puerto, ))

    threads = []

    for _ in range(8):
        t = threading.Thread(target = revisar_puerto)
        t.start()
        threads.append(t)

    # Para que el programa no termine antes de tiempo
    for t in threads:
        t.join()