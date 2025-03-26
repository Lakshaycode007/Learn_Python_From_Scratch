# STRING FUNCTIONS
name = input('Enter your name: ')

# to find the length of a string
print(len(name))

# Find the first occurance of given character
print(name.find('a'))


# Find the last occurance of given character
print(name.rfind('a'))

# To capitalize first letter of string
print(name.capitalize())

# To capitalize whole string.
print(name.upper())

# To write whole string in small letter.
print(name.lower())

# It is True if string contains only digit as a string else False.
print(name.isdigit()) #Lakshay132 == False  354651324 == True

# Returns True if strings contains space in a string else returns False.
print(name.isspace())

# This function returns True if string contains only alphabets else returns False.
print(name.isalpha())

# To count how many times a specific Substring is repeated in a string.
print(name.count('a'))

# To replace a character from a string.
print(name.replace('l', 'D'))

