import socket

host='localhost'
port=4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print('Server listening on port:',port)
s.listen()

c,addr = s.accept()

print("Connection from:",str(addr))

c.send(b"Hello, how are you? ")
c.send("Bye".encode())
c.close()
