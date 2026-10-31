list = [7, 9, "Hello", 3.14, True, None]
list[0] = 10

print(list)

print(list[2])
print(list[-1]) 

print(list[10])  # This will raise an IndexError since the index is out of range