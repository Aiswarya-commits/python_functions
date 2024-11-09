# Function and Code Examples

# 1. len() function in Python
# The len() function in Python returns the number of items in an object.
# Here, we use it to find the length of a list.

my_list = [10, 20, 30, 40, 50]
length_of_list = len(my_list)
print("Length of list:", length_of_list)

# 2. greet(name) function
# This function takes a name as input and prints a greeting message.
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# 3. find_maximum(numbers) function
# This function takes a list of integers and returns the maximum value without using the max() function.
def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
numbers = [10, 45, 2, 30, 78]
print("Maximum value:", find_maximum(numbers))

# 4. Local vs Global Variables
# Local variables are defined within a function and can only be accessed within that function.
# Global variables are defined outside of any function and can be accessed throughout the program.

x = 10

def demo_scope():
    x = 5
    print("Inside function, x =", x)

demo_scope()
print("Outside function, x =", x)

# 5. calculate_area(length, width=5) function
# This function calculates the area of a rectangle. If the width is not provided, it defaults to 5.
def calculate_area(length, width=5):
    return length * width

print("Area with length 10 and width 4:", calculate_area(10, 4))

print("Area with length 10:", calculate_area(10))

