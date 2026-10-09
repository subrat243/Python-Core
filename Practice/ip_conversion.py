import socket

ip = "192.168.1.1"

ip_bytes = socket.inet_aton(ip)

print(ip_bytes)
print(type(ip_bytes))