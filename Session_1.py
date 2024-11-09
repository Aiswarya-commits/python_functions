# # welcome to the world of python
# # alt+shift+. increase
# # alt+shift+, decrease
# # ctrl+/
#
# print("hi")
# print(1)
# print(5+10)
# print(10/5)
# # print(10/0)
# print(5//2)
#
# """hi
# i am
# Aiswarya"""
#
# """
# A=10
# B=20
# Swaping Algorithm
# A=A+B
# # A=30
# B=A-B
# # B=10
# A=A-B
# # A=20
#
# """
#
# print("""hi
# i am
# Aiswarya"""
#
# """
# A=10
# B=20
# Swaping Algorithm
# A=A+B
# # A=30
# B=A-B
# # B=10
# A=A-B
# # A=20
# """)
#
# print("""
# *
# **
# ***
# ****
# *****
# """)
#
# # Escape sequence
# print('Hi "Anu" welcome')
# print('Hi , \"Anu\" it\'s Your car')
#
# # Variables
# # x=10
# # print(type(x))
#
#
# # Hello Learners, Please find the 'To Do List' for next live core session.
# # 1) Write a Python program that assigns the values 10 to a variable called x and 20 to a variable called y. Then print the value of x and y on separate lines.
# # 2) Create a Python program that declares a variable name and assigns your name to it. Then print the variable name.
# # 3) Write a Python program that prints the following pattern using escape sequences (\n and \t):
# #      *
# #    ***
# #   *****
# #  *******
#
# # x=10
# # y=20
# # print(x,"\n",y)
#


# Format Method

# 1st Method
# name1="Ramu"
# Age=25
# print("This is",name1,"who's age is",Age)

# 2nd Method
# print("This is {} who's age is {}".format(name1,Age))
# Yob=2000
# print("This is {} who's age is {}".format(name1,2024-Yob))
# print("This is {1} who's age is {0}".format(name1,Age))
# print("This is kerala,God's own country.")
# print(f'{name1} who\'s age is {2024-(Yob)}')

# input statements
# name2=input("Enter Your Name:")
# Age2=int(input("Enter Your Age"))
# # print("Name of the candidate is",name2)
# print(f'Name of the candidate is {name2}.His age is {Age2}')
# print("Data types of the values are",type(name2),type(Age2))


# simple calculator
# value1=int(input("Enter the first value:"))
# value2=int(input("Enter the Second value:"))
# print("Calculator")
# print("The mathematical operations are {} , {} , {} & {}".format(value1+value2,value1-value2,value1*value2,value1/value2))


# Data structures
# A=1,2,3,4,5
# print(A)
# print(type(A))
#
# B=[10,11,12,13,"hi",True,99]
# print(B,type(B))


# Arithmetic operators
# ceil Division
# import math
# x=5/2
# print(math.ceil(x))

# Logical Operators: and or not



# Cpmparison/Relational operators: < > <= >= == !=
# a=10
# b=20
# c=30
# print(a>b)
# print(a>b and a>c)

# Data structures
# String
# name2="Alibaba"
# name3="A"
# print(type(name3),type(name2))
#
# print(id(name2))
# name2=name2+"A"
# print(name2)
# print(id(name2))
#
# # string slicing
# print(name2[1:5])

# num=int(input("Enter The number:"))
# if(num%2==0):
#     print(num,"is an even number")
# else:
#     print(num,"is an odd number")

# num2=int(input("Enter the number"))
# if(num2%5==0):
#     print(num2,"multiple of 5")
# else:
#     print(num2,"is not multiple of 5")

# num1=int(input("Enter your age:"))
# if num1<18:
#     print("You are Minor")
# elif num1>=18 and num1< 60:
#         print("You are Adult")
# else:
#         print("You are a senior citizen")

# Looping statements

# for i in range(1,10):
#     print(i,"Aiswarya")

# for i in range(1,6,2):
#     print(i,"Aiswarya")

# for i in range(1,20,3):
#     print(i*"*")

# for i in range(1,5,1):
#     print(i*"*")

# for i in range(1,8,3):
#     print(i,i+1,i+2)

# Nested loop


# for i in range(1,3):
#     print("Outer loop",i)
#     for j in range(0,i):
#         print("inner loop",j)
#         print("Eit from inner loop and going to outer loop")
#         print("loop over")

# prime numbers from 1 to 30
for num in range(2,31):
    prime_or_not=True

    for denominator in range(2, num):
        if num % denominator ==0:
            prime_or_not=False
            break

        if prime_or_not:
            print(num, end=' ')




