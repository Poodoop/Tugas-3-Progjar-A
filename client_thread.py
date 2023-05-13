import sys
import socket
import logging
import threading
import time  # Import time

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
        sock.sendall(message.encode())
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[FROM SERVER] got {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return

def thread():
    t = threading.Thread(target=kirim_data)
    t.start()
    t.join()

if __name__ == '__main__':
    thread_counter = 0 
    start_time = time.time()  
    while time.time() - start_time < 30:  
        thread()
        thread_counter += 1  
    logging.warning(f"Total threads created: {thread_counter}")
