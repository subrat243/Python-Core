# Inspect the current directory and host name with standard-library modules.
import os
import socket
import random
import requests

print(os.getcwd())

hostname = socket.gethostname()
print(hostname)

num = random.randint(1, 100)
print(f"Generated random number: {num}")

response = requests.get("https://rootbysubrat.vercel.app")
print(response.status_code)