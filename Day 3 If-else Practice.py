# Q1 Even or Odd:
Num = int(input("Enter the number to check even or odd  "))
if Num % 2 == 0:
    print(f"number is even {Num}")
else:
    print(f"number is odd {Num}")

# Q2 Determine the number is +ve, -ve or zero
n = int(input("Enter the number  "))
if n == 0:
    print("Zero")
elif n > 0:
    print("Positive")
else: print("Negative")

# Q3 Find vowel and consonant
letter = input("Enter the alphabet ").lower()
if letter in "aeiou": print("vowel")
elif 'a' <= letter <= 'z' : print("consonant")
else: print("Not an alphabet")

#Largest of Two:
a = float(input("Enter the digit "))
b = float(input("Enter the digit "))
if a > b: print(f"a is greater {a}")
elif a == b: print(f"Both are equal {a} and {b}")
else: print(f"b is greater {b}")