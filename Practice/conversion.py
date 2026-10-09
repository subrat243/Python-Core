payload = "GET /index.html HTTP/1.1"

encoded = payload.encode('utf-8')

print(encoded)
print(type(encoded))

decoded = encoded.decode('utf-8')

print(decoded)
print(type(decoded))
