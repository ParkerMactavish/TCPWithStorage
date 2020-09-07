import socket
import time

target_host = "127.0.0.1"
target_port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(("%f"%(time.time()*1000)).encode())

response = client.recv(4096)

print(response)

client.close()
