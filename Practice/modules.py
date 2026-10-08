# Inspect the current directory and host name with standard-library modules.
import os
import socket
import random
import requests

print(os.getcwd())

hostname = socket.gethostname()
print(hostname)

# Generate and display a random integer from 1 through 100.
num = random.randint(1, 100)
print(f"Generated random number: {num}")

# Request the website and print the HTTP status code.
response = requests.get("https://rootbysubrat.vercel.app")
print(response.status_code)