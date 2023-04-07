#!/usr/bin/env python
# coding: utf-8

# ### 1. Variables and Data types

# In[1]:


# Assigning integer value 11 to variable 'a'
a = 11

# Assigning integer value 14 to variable 'c'
b = 14

# Assigning string value "Vighnesh" to variable 'c'
c = "Vighnesh"

# Assigning boolean value True to variable d
d = True

# Printing the value of variable 'a'
print(a)

# Printing the value of variable 'b'
print(b)

# Printing the value of variable 'c'
print(c)

# Printing the value of variable 'd'
print(d)


# In[2]:


# Print the type of variables a, b, c and d
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[3]:


# Declare two variables var1 and var2 with values of different data types
var1 = 321
var2 = "321"

# Print the data types of the variables using the type() function
print("Datatype of var1 : ",type(var1))
print("Datatype of var2 : ", type(var2))

# Convert the var2 string variable to an integer and multiply it by 10 and store it in var3 variable
var3 = int(var2) * 10

# Print the value and data type of var3 variable
print("Value of var3 : ",var3)
print("Datatype of var3 : ", type(var3))

# Declare a float variable var4
var4 = 91.22

# Print the data type of var4 variable
print("Datatype of var4 : ", type(var4))

# Convert the var4 float variable to an integer and store it in var5 variable
var5 = int(var4)

# Print the value and data type of var5 variable
print("Value of var5 : ", var5)
print("Datatype of var5 : ",type(var5))


# ### 2. Operators

# In[4]:


# Declare two variables a and b with initial values
a = 15
b = 4

# Print the values of a and b
print("Value of a : ", a)
print("Value of b : ", b)

# Perform arithmetic operations on a and b and print the results
print("Addition of a + b: ", a+b)
print("Subtraction of a - b: ", a-b)
print("Multiplication a * b: ", a*b)
print("Normal Division of a / b: ", a/b)
print("Integer Division of a // b: ", a//b)
print("Remainder of a % b: ", a%b)
print("Power of a for exponent 2: ", a**2)

# Perform comparison operations on a and b and print the results
print("Equal of a == b: ", a==b)
print("Not Equal of a != b: ", a!=b)
print("Less Than Equal a <= b: ", a<=b)
print("Greater Than Equal a >= b: ", a>=b)
print("Less Than a < b: ", a<b)
print("Greater Than a > b: ", a>b)


# ### 3. Input/output

# In[5]:


# Prompt the user to enter their name and favorite number
name = input("Enter your name (Must be a string) : ")
favorite_number = input("Enter your favorite number (Must be an integer) : ")

# Convert the favorite_number variable from string to integer using the int() function
favorite_number = int(favorite_number)

# Print the name and favorite number values, and their data types using the type() function
print("Value of name : ",name)
print("Value of favorite number : ",favorite_number)
print("Type of name : ",type(name))
print("Type of favorite number : ",type(favorite_number))


# ### 4. Command line arguments

# In[6]:


# Importing the sys module to access the command line arguments
import sys

# Using the len() function to get the number of command line arguments passed
n = len(sys.argv)

# Storing the command line arguments in a list
command_line_args = sys.argv

# Printing the number and list of command line arguments
print("Total number of command line arguments : ", n)
print("What are the input command line arguments? ", command_line_args)

# Accessing and printing individual command line arguments
print("First Command Line Argument : ", sys.argv[0])
print("Second Command Line Argument : ", sys.argv[1])
print("Third Command Line Argument : ", sys.argv[2])
# print("Fourth Command Line Argument : ", sys.argv[3])


# ### 5. If-else

# In[7]:


# Python If-Else with logical operators

# Declare two variables a and b with some values
a = 4
b = 5

# Check if a is greater than b using if-else statement and print respective messages
if a>b :
    print("True Condition - a is greater than b !!")
else:
    print("False Condition - a is not greater than b !!")

# Take user input for name and favorite_number
name = input("Enter your name (Must be a string) : ")
favorite_number = input("Enter your favorite number (Must be an integer) : ")
favorite_number = int(favorite_number)

# Check if name is "Vighnesh" and favorite_number is 17 using logical AND operator and print respective messages
if (name == "Vighnesh") and (favorite_number == 17):
    print("Vighnesh's Data Matched !!")
else:
    print("Vighnesh's Data Mis-Matched !!")


# ###  6. Nested If-else

# In[8]:


# Prompt the user to enter the student's final score as an integer
scores = input("Enter student's final scores (Must be an integer): ")

# Convert the input to an integer
scores = int(scores)

# Use a set of conditional statements to assign a grade based on the score
if scores >= 95:
    print("A+ Grade !!")
elif scores < 95 and scores >= 85:
    print("A Grade !!")
elif scores < 85 and scores >= 75:
    print("B+ Grade !!")
elif scores < 75 and scores >= 70:
    print("B Grade !!")
else:
    print("C Grade !!")


# ### 7. For loop

# In[9]:


# Execute a for loop with a start and end value
# The loop variable `i` will take on values from 1 to 10
for i in range(1, 11):
    print(i)

# Execute a for loop without specifying the start value
# The loop variable `i` will take on values from 0 to 9
for i in range(10):
    print("vighnesh")

# Execute a for loop to print all odd numbers between 1 and 99
# The loop variable `i` will take on odd values from 1 to 99
for i in range(1, 100, 2):
    print(i)


# ### 8. While loop

# In[10]:


# Set the initial value of the loop variable to 1
num = 1

# Execute a while loop while `num` is less than or equal to 50
while num <= 50:
    # Print the value of `num` to the console
    print(num)
    # Increment the value of `num` by 1
    num = num + 1
    # Alternatively, you could use the shorthand `num += 1`


# ### 8. Break and continue

# In[11]:


# Example using the `break` keyword
print("Example for Break Keyword")

# Execute a for loop that iterates over the values from 1 to 19 (inclusive)
# The loop will terminate early if the value of `i` becomes greater than 10
for i in range(1, 20):
    # If `i` is greater than 10, break out of the loop
    if i > 10:
        break
    # Otherwise, print the value of `i`
    print(i)

# Example using the `continue` keyword
print("Example for Continue Keyword")

# Execute a for loop that iterates over the values from 1 to 19 (inclusive)
# The loop will skip over any values of `i` that are less than 10
for i in range(1, 20):
    # If `i` is less than 10, skip to the next iteration of the loop
    if i < 10:
        continue
    # Otherwise, print the value of `i`
    print(i)



