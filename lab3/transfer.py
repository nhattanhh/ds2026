from mpi4py import MPI
import sys
import os

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if comm.Get_size() < 2:
        print("This program requires at least 2 MPI processes.")
        return

    if rank == 0:
        
        filename = sys.argv[1] if len(sys.argv) > 1 else "test_mpi.txt"
        
        if not os.path.exists(filename):
            print(f"Rank 0: File '{filename}' not found. Creating a dummy file.")
            with open(filename, 'w') as f:
                f.write("This is a dummy file for MPI transfer.")
        
        print(f"Rank 0: Sending file '{filename}'...")
        
        # Read file content
        with open(filename, 'rb') as f:
            file_content = f.read()
            
        comm.send(filename, dest=1, tag=0)
        comm.send(file_content, dest=1, tag=1)
        print("Rank 0: File sent successfully.")
        
    elif rank == 1:
        print("Rank 1: Waiting for file...")
        filename = comm.recv(source=0, tag=0)
        file_content = comm.recv(source=0, tag=1)
        print(f"Rank 1: Received file '{filename}'. Saving...")
        save_name = "received_" + filename
        with open(save_name, 'wb') as f:
            f.write(file_content)
        print(f"Rank 1: File saved as '{save_name}'.")

if __name__ == "__main__":
    main()
