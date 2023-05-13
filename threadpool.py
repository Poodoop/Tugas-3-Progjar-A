import sys
import socket
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time 

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[FROM SERVER] got {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return

if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        start_time = time.time() 
        request_counter = 0  
        futures = set()  

        while time.time() - start_time < 60:  
            future = executor.submit(kirim_data)
            futures.add(future)

            completed_futures = {f for f in futures if f.done()}
            request_counter += len(completed_futures)
            futures -= completed_futures

        for future in futures:
            future.result()

        logging.warning(f"Total requests sent: {request_counter}")
