list = [7, 9, "Hello", 3.14, True, None]
list[0] = 10

print(list)

print(list[2])
print(list[-1]) 

# print(list[10])  # This will raise an IndexError since the index is out of range

l1 = [10, 20, 30, 40, 50]

print(l1[0:2])  # Output: [10, 20]
print(l1[1:4])  # Output: [20, 30, 40]
print(l1[:3])   # Output: [10, 20, 30]
print(l1[2:])   # Output: [30, 40, 50]
print(l1[::-1]) # Output: [50, 40, 30, 20, 10]

