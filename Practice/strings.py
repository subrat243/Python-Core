a = 'hello'
b = "world"
c = '''This is a multi-line string. 
It can span multiple lines.'''

word = "Python"

print(a)
print(b)
print(c)
print(word)

print(a[0])  # Accessing the first character of the string 'a'
print(a[2])
print(a[-1])  # Accessing the last character of the string 'a'

print(word[0:3])  # Slicing the string 'word' to get the first three characters
print(word[2:5])  # Slicing the string 'word' to get characters from index 2 to 5
print(word[:4])   # Slicing the string 'word' to get the first four characters
print(word[2:]) # Slicing the string 'word' to get characters from index 2 to the end
print(word[:])  # Slicing the string 'word' to get every character
print(word[:-1])  # Slicing the string 'word' to reverse it
print(word[::-1])  # Slicing the string 'word' to reverse it
print(word[::2])  # Slicing the string 'word' to get every second character
print(word[1::2])  # Slicing the string 'word' to get every second character starting from index 1
print(word[2:5:1]) # Slicing the string 'word' to get characters from index 2 to 5 with a step of 1
print(word[2:5:2]) # Slicing the string 'word' to get characters from index 2 to 5 with a step of 2

print(len(word))  # Getting the length of the string 'word'
print(word.count('o'))  # Counting the occurrences of 'o' in the string 'word'
print(word.find('t'))  # Finding the index of the first occurrence of 't'
print(word.replace('P', 'J'))  # Replacing 'P' with 'J' in the string 'word'
print(word.upper())  # Converting the string 'word' to uppercase
print(word.lower())  # Converting the string 'word' to lowercase

print("Hello\nWorld")
print("Hello\tWorld")
print('It\'s Python')
print("C:\\Users\\Harry")
