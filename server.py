import socket

from Crypto.Cipher import AES 

key = b"MySecureKey12345" #  any 16 byte key
nonce = b"abcdefs090078601"  #any 16 byte nonce

cipher = AES.new(key, AES.MODE_EAX, nonce)

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",8000))
server.listen()
print("Server listening on port 8000....")

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)



file = open(file_name, "wb")
done = False
file_bytes = b""
while not done:
    data = client.recv(1024)
    if file_bytes[-1:] == b"\n":
        done = True
    else:
        file_bytes += data
    

file.write(cipher.decrypt(file_bytes[:-1]))
print(file_bytes)
file.close()
client.close()
server.close()

