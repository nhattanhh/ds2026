import xmlrpc.client
import sys
import os

HOST = '127.0.0.1'
PORT = 8080

def send_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    server_url = f'http://{HOST}:{PORT}'
    proxy = xmlrpc.client.ServerProxy(server_url)
    
    print(f"Connected to RPC server at {server_url}")
    
    try:
       
        with open(filename, 'rb') as f:
            file_content = f.read()
            
        result = proxy.save_file(os.path.basename(filename), xmlrpc.client.Binary(file_content))
        
        if result:
            print(f"File '{filename}' sent successfully.")
        else:
            print(f"Failed to send file '{filename}'.")
            
    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Make sure it is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <filename>")
    else:
        send_file(sys.argv[1])
