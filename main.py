print("Exercise 6")

char = input("Enter a character: ")
if char.isdigit():
    print("The character is a number.")
elif char.isalpha():
    print("The character is a letter.")
else:
    print("The character is a special character.")

