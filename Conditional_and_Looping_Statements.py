# Exercise 1: Month Names

month_num = int(input("Enter the month (1-12): "))
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

if 1 <= month_num <= 12:
    print(f"Month {month_num} is {months[month_num - 1]}")
else:
    print("Please enter a number between 1 and 12.")

# Exercise 2: Cinema Ticket Pricing

age = int(input("Enter your age: "))
full_price = 6

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price:.2f}")

# Exercise 3: BMI Calculator

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are in the 'Underweight' range.")
elif 18.5 <= bmi < 25:
    print("You are in the 'Normal' range.")
elif 25 <= bmi < 30:
    print("You are in the 'Overweight' range.")
else:
    print("You are in the 'Obese' range.")

# Exercise 4: Find the Greatest of Three Numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

# Exercise 5: Factorial Calculation using Loops

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

# Exercise 6: Reverse a Number using While Loop

num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"The reversed number is {reversed_num}")

# Exercise 7: Finding Multiples of a Number

num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {num} up to {limit}:")
for i in range(1, limit + 1):
    print(num * i)

# Exercise 8: Print Input and Break on 'done'

while True:
    value = input(":")
    if value.lower() == "done":
        print("Done")
        break
    else:
        print(value)

# Exercise 9: FizzBuzz

for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 10: Print Pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()









