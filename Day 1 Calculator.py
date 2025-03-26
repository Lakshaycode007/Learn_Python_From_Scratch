# in this exercise lets try to create a calculator application

num1 = float(input("Enter number 1 "))
num2 = float(input("enter number 2 "))
operator = input("Enter the input (+ - * /) ")

if operator == '+': print(num1 + num2)
elif operator == '-': print(num1 - num2)
elif operator == '*': print(num1 * num2)
else: print(num1 / num2)