from xmlrpc.server import SimpleXMLRPCServer
import os

HOST = '0.0.0.0'
PORT = 8080

def save_file(filename, data):
    
    print(f"Receiving file: {filename}")
    try:
        with open(filename, 'wb') as f:
            f.write(data.data)
        print(f"File '{filename}' saved successfully.")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def start_server():
   
    with SimpleXMLRPCServer((HOST, PORT), allow_none=True) as server:
        server.register_introspection_functions()
        
        server.register_function(save_file, 'save_file')
        
        print(f"RPC Server listening on {HOST}:{PORT}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopping...")

if __name__ == "__main__":
    start_server()
