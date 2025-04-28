# Import - requried modules
import socket
import threading 

HOST = '127.0.0.1'
PORT = 1234 #you can use any port between 0 to 65535
LISTENER_LIMIT = 5

# Main Function 
def main():

    #Creating the socket class object 
    # AF_INET: we are going to use IPv4 address
    # SOCK_STREAM: we are using  TCp packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # creating a try catch block 
    try:
        # provide the server  with an address in the form of 
        # host IP and port 
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host (HOST) and port (PORT)")

        # Set server  limit
        server.listen(LISTENER_LIMIT)

        #This While loop will keep listening to client  connections 
        while 1:

            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]})")

if __name__=='__main__':
    main()