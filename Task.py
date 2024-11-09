# Exercise 1
# Printing name, student number, and email address
print("Bob")
print("ST1001")
print("bob@gmail.com")

# Exercise 2
# Printing name, student number, and email address using escape sequences
print("Bob\nST1001\nbob@gmail.com")

# Exercise 3
# Add, subtract, multiply, and divide two numbers
num1 = 14
num2 = 7

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Exercise 4
# Display numbers from 1 to 5 in steps
for i in range(1, 6):
    print(i)

# Exercise 5
# Printing a sentence with quotation marks and line break
print("\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\".")

# Exercise 6
# Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
# Define variables and print their types and sum
num = 23
textnum = "57"
decimal = 98.3

print(type(num))
print(type(textnum))
print(type(decimal))

sum_value = num + int(textnum) + decimal
print("Sum:", sum_value)

print(type(sum_value))

# Exercise 8
# Calculate the number of minutes in a year
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

total_minutes = days_in_year * hours_in_day * minutes_in_hour

print("The total number of minutes in a year is:", total_minutes)

# Exercise 9
# Asking the user for their name and printing a greeting
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10
# Program to convert pounds to dollars
pounds = float(input("Please enter amount in pounds: "))
conversion_rate = 1.38  # Example conversion rate
dollars = pounds * conversion_rate

print(f"£{pounds} are ${dollars:.2f}")





