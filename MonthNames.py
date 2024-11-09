# Exercise 1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
# An example run of the program (numbers in bold are typed in by the user)
# Enter the month: 3
# Month 3 is March


month_number = int(input("Enter the month: "))

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Please enter a number between 1 and 12.")


# Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)
# Enter your age: 63
# Your ticket costs £2.00

age = int(input("Enter your age: "))
full_price = 6

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price:.2f}")


# Exercise 3
# Name your file: BodyMassIndex.py
# Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
# BMI= weight(kg)/height2(m2)
# BMI Weight Status Categories table
# BMI range - kg/m2   Category
# Below 18.5                    Underweight
# 18.5 -24.9         Normal
# 25 - 29.9          Overweight
# 30 & Above     Obese
# An example run of the program (numbers in bold are typed in by the user)
# Enter your weight in (kg): 75
# Enter your height in (m): 1.70
# Your BMI is: 25.95
# You are in the “overweight” range.

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are in the underweight range.")
elif 18.5 <= bmi < 25:
    print("You are in the normal range.")
elif 25 <= bmi < 30:
    print("You are in the overweight range.")
else:
    print("You are in the obese range.")


# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest number is: {greatest}")


# Exercise 5
# Find the factorial of a given number using loops(note the number is received from the user)

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")


# Exercise 6
# Reverse a number using while loop

# Solution to Exercise 6
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"Reversed number is: {reversed_num}")


# Exercise 7
# Finding the multiples of a number using loop

num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {num} up to {limit}:")

for i in range(1, limit + 1):
    if i % num == 0:
        print(i)


# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program
# :hello there
# hello there
# :finished
# finished
# :done
# Done

while True:
    user_input = input(":")
    if user_input.lower() == 'done':
        print("Done")
        break
    else:
        print(user_input)

#
# Exercise 9
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 10
# Write a program to print the following pattern:
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

