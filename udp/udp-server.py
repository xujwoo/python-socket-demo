import socket
import binascii

HOST = '0.0.0.0'
PORT = 50018

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    request, client_address = s.recvfrom(1024)
    print('connected by', client_address,
          'received ', binascii.hexlify(request))
    if request:
        s.sendto(request, client_address)

