# Task: Write a python program to find remainder when a number is divided by z.

# Read two numbers as text, then convert them to integers for division.
a = input("Enter a number: ")
b = input("Enter another number: ")

# Calculate the remainder after dividing the first number by the second.
c = int(a) % int(b)

print("The remainder of", a, "divided by", b, "is:", c)
