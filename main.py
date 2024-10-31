from time import localtime
print("Exercise 8")
print()

print("This program give your age")
print()
print("Enter your birthday date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
print()
birthday = (day, month, year)
t = localtime()
age = localtime().tm_year - birthday[2]
if (month, day) > (t.tm_mon, t.tm_mday):
    age -= 1
print(f"You are {age} years old.")