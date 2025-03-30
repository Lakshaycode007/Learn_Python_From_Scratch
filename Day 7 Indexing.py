# # Indexing = Accessing string's elements in sequence using []
# #             [start: End :Steps]
credit_number = "1235654265466841"
# fetch the first element.
# Index starts from 0 means first element from the string and so on.
print(credit_number[0]) # output: 1
#fetch 2nd elements
print(credit_number[1]) # output: 2
# Access 1st elements to 4th element
print(credit_number[0:4]) # output: 1235
# start is 0 and end is excluded so end - 1 will be accessed
# Another way to do access the same elements
print(credit_number[:4]) # output: 1235
# Accessing center elements from strings
print(credit_number[5:9]) # output: 6542
# Accessing elements from in between to last
print(credit_number[5:]) # output: 6542-6546-6841

"""REVERSE INDEXING"""
# Access last element of string
print(credit_number[-1]) # output: 1 last element
# Accessing second last element
print(credit_number[-2]) # output: 4 second last element
#negetive indexing starts from -1 and keep increasing like -2, -3, -3 etc.
# Accessing last 4 elements from string
print(credit_number[-1:-5:-1]) # must give values for steps to print it from reverse order.
# Accessing all the elements of string from reverse
print(credit_number[::-1])

"""Argument STEP in string indexing"""
# Accessing every second element of string
print(credit_number[::2])

"""
Excersice 1
print only even digits from a given numerical string
"""
num_str = input("Enter a numerical string: ")
for i in num_str:
    if int(i) % 2 == 0:
        print(i, end="")
