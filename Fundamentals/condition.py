# input() function
num = int(input("Enter your number: "))

# if-else statement
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Example-1
if 4 != 4.0:
    print("Not equal")
else:
    print("Equal")

# Multiple condition: if-elif-else statement
age = int(input("Enter your age: "))
if age >= 1 and age <= 10:
    print("You are under 10")
elif age >= 10 and age <= 18:
    print("You are under 18")
else:
    print("Your are 18+")

# Example
indianDish = ["naan", "samosa", "rajma", "daal"]
chineseDish = ["egg role", "fried rice", "pot sticker"]
italianDish = ["pasta", "pizza", "risotto"]

dish = input("Enter a dish name: ")

if dish in indianDish:
    print("Indian")
elif dish in chineseDish:
    print("Chinese")
else:
    print("Italian")
