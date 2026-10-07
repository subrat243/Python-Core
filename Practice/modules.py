# Inspect the current directory and host name with standard-library modules.
import os
import socket

print(os.getcwd())

hostname = socket.gethostname()
print(hostname)
