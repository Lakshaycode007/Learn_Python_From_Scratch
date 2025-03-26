# Validate user input Exercise
# Username not longer than 12 characters.
# doesn't contain any digit and any spaces in between.


#1 Take input from user in a string format/
username = input("Enter the username For login ")
#2 use if-else conditions and string methods to validate the string.
#3 Condition 1 len(input) >= 12: print(some message)
if len(username) > 12:
    print(f"username {username} is too long \nRe-enter it please. ")
#4 condition 2 input.isdigit == False: follow command 2
elif not username.isalpha():
    print(f"Username {username} doesn't support numericals \nRe-enter it please.")
#5 condition 3 input.find != Ture: follow my another instruction.
elif not username.find(" "):
    print(f"Username {username} doesn't support any special characters.")
else:
    print(f" Hello,\n How are you? Mr.{username}")