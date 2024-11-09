# Data structures in python
#
# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("List of 5 random numbers:", random_numbers)

# Q2. Insert 3 new values to the list and print the updated list.
random_numbers.extend([101, 102, 103])
print("Updated list with 3 new values:", random_numbers)

# Q3. Try to use a for loop to print each element in the list.
for number in random_numbers:
    print(number)


# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
person = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print("Dictionary:", person)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
person['phone'] = '1234567890'
print("Updated dictionary:", person)

# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Q2. Add the value 6 to the set created in Q1.
my_set.add(6)
print("Updated set:", my_set)

# Q3. Remove the value 3 from the set created in Q1.
my_set.discard(3)
print("Set after removing 3:", my_set)


# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)

# Q2. Print the length of the tuple created in Q1.
print("Length of the tuple:", len(my_tuple))



