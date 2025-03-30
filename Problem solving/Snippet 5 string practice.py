#Write a function that takes two strings as input and returns a single string that is the concatenation of the two strings, with a space in between.
#Example: concatenate_strings("Hello","World") should return "Hello World"

# # take user input of two strings
# a = input("Enter your string1: ")
# b = input("Enter your string1: ")
# print(a+" "+b)

# Write a function that takes a string as input and returns the reversed string.
c = input("Enter the string: ")
print(c[::-1])

"""Count Vowels:
Write a function that counts the number of vowels (a, e, i, o, u) in a given string.
Example: count_vowels("programming") should return 3."""

d = input("Enter the string: ")
count = 0
for i in d:
    if i in "aeiouAEIOU":
        count += 1
print(count)