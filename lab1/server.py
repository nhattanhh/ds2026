import socket
import os

HOST = '0.0.0.0'  
PORT = 8080   

def start_server():
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      
        s.bind((HOST, PORT))
     
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            with open('received_file.txt', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print("File received successfully and saved as 'received_file.txt'")

if __name__ == "__main__":
    start_server()
