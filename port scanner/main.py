import socket
import threading


target = input("Enter the target IP address: ")

start_port = input("Enter starting port: ")
end_port = input("Enter ending port: ")


def scan(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(int(start_port), int(end_port)):
        try:
            s.connect((ip, port))
            print(f"Port {port} is open.")
        except socket.error:
            print(f"Port {port} is closed.")

    s.close()


thread = threading.Thread(target=scan(target))
thread.start()
thread.join()


thread_2 = threading.Thread(target=scan(target))
thread_2.start()
thread_2.join()