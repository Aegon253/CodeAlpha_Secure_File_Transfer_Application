import socket
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

key = b"MySecureKey12345"  # any 16-byte key
nonce = b"abcdefs090078601"  # any 16-byte nonce

cipher = AES.new(key, AES.MODE_EAX, nonce)

users = {"admin": "password1"}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen()
print("Server listening on port 8000...")

client, addr = server.accept()
username = client.recv(1024).decode()
password = client.recv(1024).decode()
if username not in users or users[username] != password:
    client.send("AUTH_FAIL".encode())
    client.close()
    print(f"Authentication failed for user: {username}")
    server.close()
    exit()
else:
    client.send("AUTH_SUCCESS".encode())
    print(f"Authentication successful for user: {username}")

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


encrypted_data = file_bytes[:-33]  
received_hmac = file_bytes[-33:-1]  


#integrity checks
hmac = HMAC.new(key, encrypted_data, SHA256).digest()
if hmac != received_hmac:
    print("Integrity check failed.")
    client.close()
    server.close()
    exit()
else:
    print("Integrity check passed")


file.write(cipher.decrypt(encrypted_data))
file.close()
print("File received and decrypted successfully")
print(file_bytes)
client.close()
server.close()
