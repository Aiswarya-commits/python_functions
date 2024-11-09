# 1. len() function

#  Using len() to find the length of a list
my_list = [1, 2, 3, 4, 5]
print("Length of the list:", len(my_list))


# 2. Function to greet a person by name
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")


# 3. Function to find the maximum value in a list without using max()
def find_maximum(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
print("Maximum value:", find_maximum([3, 5, 1, 7, 4]))


# 4. Explanation and demonstration of local vs. global variables

x = 10  # Global variable

def example_function():
    x = 5  # Local variable with the same name as the global variable
    print("Inside function, x =", x)

example_function()
print("Outside function, x =", x)


# 5. Function to calculate the area of a rectangle with a default width value
def calculate_area(length, width=5):
    return length * width


print("Area with length 10 and default width:", calculate_area(10))
print("Area with length 10 and width 4:", calculate_area(10, 4))
