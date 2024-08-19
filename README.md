# Secure File Transfer Application
### This project is a secure file transfer application that allows you to send and receive files over a network. The application uses AES encryption to ensure the confidentiality of the files being transferred and HMAC for integrity checks. It also includes a simple access control mechanism using a username and password.

## Features
- **AES Encryption**: Files are encrypted using the AES algorithm in EAX mode, providing secure and authenticated data transfer.
- **HMAC Integrity Check**: The application employs HMAC with SHA-256 to ensure the integrity of the transferred files.
- **Access Control**: Requires a valid username and password to initiate a file transfer.
- **Socket Programming**: Utilizes TCP sockets for reliable file transmission.


### Prerequisites
Python 3.x
pycryptodome library for AES encryption and HMAC
You can install the pycryptodome library using pip:

    pip install pycryptodome

## Usage
### Server

      python server.py

### Client
You will be prompted to enter the username and password for authentication.

      python client.py <input_file> <output_file>

- **<input_file>:** The path to the file you want to send.
- **<output_file>:** The name of the file to save on the server.

      python client.py secret.txt received_secret.txt

You will be prompted to enter the username and password. If the authentication is successful, the file secret.txt will be encrypted and sent to the server, which will save it as received_secret.txt.


## Logging
- The client logs important events to client.log:
- Successful connection to the server.
- Authentication results.
- Reading and encrypting of the input file.
- Sending of encrypted data and HMAC to the server.
- Any errors encountered during the process.

## Security Considerations
- Ensurance of Confidentiality and Integrity of file during transfer.
- The AES key, nonce, and user credentials are hardcoded in the script. 
- The HMAC ensures that any tampering with the encrypted data during transmission will be detected.
