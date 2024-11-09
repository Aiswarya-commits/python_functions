# #comments
#
# """
# hi
# this is
# multiple line commenting
# """
# print("""This is
# multiple line
#  commenting""")
#
# print("""
# *
# **
# ***
# ****
# *****
# ******
# """)
#
# # Escape sequence
# # Escape sequence is done with \
# print('Hi "Anu" welcome')
# print("Hi 'Anu' welcome")
#
# print('Hi \"Anu\", it\'s your car')
#
# # types of esc.seq..
# #\t tab
# #\n nextline
# #\b backspace
# #\x hexademical
#
# #\t tab
# print('\tHi \"Anu\", it\'s your car')
#
# #\n naextline
# print('Hi \"Anu\", it\'s \nyour car')
#
# #\b backspace
# print('Hi \"Anu\", it\'s your car\b')
#
# #\x hexadecimal
# print("\x75")
#
# print("""\n*\n**\n***\n****\n*****\n******""")

# variables
# x=10 # = assignment operator
# print(type(x))
#
# y="Name"
# print(type(y))
#
# Divakar=10.5
# print(type(Divakar))

# Variable naming rules
# 1. start with letter or underscore
# 2. Numbers can be used but not at the beginning
# 3. sum of numbers there should be spacing between words
# 4. special characters except  _ are not allowed
# 5. Variables are case-sensitive


# A=10
# print(id(A)) # variable refferance number
# a=20
# print(id(a))

# Age !=AGE !=age

# _num1=15
# _num2=15
# print(id(_num1),id(_num2))

# Data types
#int
#float
#string
#boolean (True or false)
#complex (imaginary number 5+6j)
#none

# img=(5+6j)
# print(type(img))
#
# A="His"
# print(7*A)

# camelcasing and pascalcasing
#pythonFileTwo camel casing
#pascal casing PythonFileTwo
#Python_File_Two

# concatenation
# a="Hey"
# b="Helooo"
# c=10
# d=a+" "+b
# print(d)

#Type casting
# f=str(c) #order of assignmnet will be from left to right
# print(type(f))
# e = a+f
# c=str(c)
# g=a+c
# print(g)

# Formar Method
# 1st Method
name1="Ramu"
Age=25
print("This is",name1,"who's age is",Age)
print("This is {} who's age is {}".format(name1,Age))
print("This is {} who's age is {}".format(Age,name1))
yob=2000
print("This is {} who's age is {}".format(name1,2024-yob))
print("This is {1} who's age is {0}".format(name1,Age))
print("This kerala, God's own country")
print(f'{name1} who\'s age is {2024-int(yob)}')
# input statement
name2=input("Enter your name:")
age2=input("Enter your age")
print("Name of the candidate is",name2)
print(f"name of the candidate is {name2}. his age is")














