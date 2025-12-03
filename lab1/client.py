import socket
import sys
import os

HOST = '127.0.0.1' 
PORT = 8080       

def send_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")
            
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    s.sendall(data)
            print(f"File '{filename}' sent successfully.")
            
        except ConnectionRefusedError:
            print("Error: Could not connect to the server. Make sure it is running.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <filename>")
    else:
        send_file(sys.argv[1])
