import socket 
from threading import Thread

name = input("ENTER YOUR NAME")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address, port))

print("CONNECTED TO SERVER")


def recieve():
    while(True):
        try:
            answer = client.recv(2048).decode("utf-8")
            if(answer == "NAME"):
                client.send(name.encode("utf-8"))
            else:
                print(answer)
        except:
            print("AN ERROR OCCURED")
            print("Closing Client....")
            client.close()
            break


def write():
    while(True):
        answer = "{}:{}".format(name,input(" "))
        client.send(answer.encode("utf-8"))


recieve_thread = Thread(target=recieve)
recieve_thread.start()

write_thread = Thread(target=write)
write_thread.start()
