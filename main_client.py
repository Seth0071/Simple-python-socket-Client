#Author: Seth007
#Last changes: Tuesday 14.Nov 2023
#Only works if you know the Server IP and the Server is up!
#Check if Firewall is blocking requests before using
#####################################################################

import socket 
import time 

server_ip = input("Please input the Server IP:  ")
port = 9999 #default

aut_conn = True

#input the port and host to communicate with


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the socket

client_ip = socket.gethostname() 

def client_conn():
    seconds = time.time() 
    current_time = time.ctime(seconds)
    current_time2 = current_time + " > "
  
    print(current_time2, "Connecting to Server...")
    connection = client_socket.connect((server_ip, port)) #connect to server
  
    print(current_time2, "Connection established with Server.")

    while (aut_conn == True):
      msg_from_server = client_socket.recv(1024).decode() # receive message from server
      print('Msg received from server: ' + msg_from_server)
        
      msg = input("Message for Server:")
      if (msg == "end_connection"):
        client_socket.close()  # close the connection with server
      else:
        client_socket.send(msg.encode()) #send message to server
client_conn()
