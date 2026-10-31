import socket

# Convert a dotted-decimal IPv4 address into its packed byte representation.
ip = "192.168.1.1"

ip_bytes = socket.inet_aton(ip)

print(ip_bytes)
print(type(ip_bytes))