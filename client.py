#import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

#Main function
def main():

    #Creating a socket  object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the server
    try:
        client.connect((HOST, PORT))
    except:
        print(f"unable to connectto server {HOST} {PORT}")

if __name__=='__main__':
    main() 