#!/usr/bin/env python
# coding: utf-8

# ### 9. Lists

# In[1]:


# Create two lists with different data types
arr_list1 = [1,2,3,4,7]
arr_list2 = [3,4,"Hola",87.21,"Namaste",[4,9,13]]

# Print the contents of the two lists
print(arr_list1)
print(arr_list2)

# Create an empty list and use a for loop to add integers from 1 to 20 to the list
arr_list3 = []
for i in range(1,21):
    arr_list3.append(i)

# Print the contents of the list and its length
print(arr_list3)
list_len = len(arr_list3)
print("Length of the list : ",list_len)

# Create two lists and concatenate them using the + operator
arr_list4 = [33,45,88,34]
arr_list5 = [112,89,90,95,90]
result = arr_list4 + arr_list5
print(result)

# Create two lists and append one list to the other using the append() method
# Also, create two lists and extend one list with the other using the extend() method
arr_list4.append(arr_list5)
arr_list6 = [88,56,77,45]
arr_list7 = [68,89,58,55,30]
arr_list6.extend(arr_list7)
print("Append Output : ",arr_list4)
print("Extend Output : ",arr_list6)
print("Append Output Length: ",len(arr_list4))
print("Extend Output Length: ",len(arr_list6))

# Iterate through a list using a for loop without using an index
arr_list8 = [112,35,258,566,865]
for i in arr_list8:
    print(i)

# Iterate through a list using a for loop with an index
for idx in range(0,len(arr_list8)):
    print("Element at ",idx," index is : ",arr_list8[idx])


# ### 10. Tuple

# In[2]:


# This program demonstrates the usage of tuples in Python.
# Define a tuple with some values
arr_tuple = (11,33,34,23,45)

# Print the tuple
print("Tuple Output : ", arr_tuple)

# Iterate over the elements of the tuple without using an index
for i in arr_tuple:
    print(i)

# Iterate over the elements of the tuple using an index
for idx in range(0, len(arr_tuple)):
    print("Element at index ", idx, " is : ", arr_tuple[idx])


# ### 11. Dictionary

# In[3]:


# Python program for dictionaries
# Define a dictionary with key-value pairs
dict_exp = {"Vighnesh": 24, "Sakshi": 25, "Shweta": 23}
print("Dictionary Output: ", dict_exp)

# Get the length of the dictionary
print("Dictionary Length: ", len(dict_exp))

# Modify a value in the dictionary
dict_exp["Vighnesh"] = 26
print("Dictionary Output after value change: ", dict_exp)

# Iterate through the keys and values of the dictionary
for key, val in dict_exp.items():
    print("Key is", key, "and Value is", val)

# Get all the keys and values of the dictionary
print("Total Keys: ", dict_exp.keys())
print("Total Values: ", dict_exp.values())

# Access a specific value in the dictionary
print(dict_exp["Vighnesh"])


# ### 12. Set

# In[4]:


# Python program for Set
# create an empty set
set_var = set()

# adding elements to the set using add() method
set_var.add(4)
set_var.add(6)
set_var.add(3)
set_var.add(2)
set_var.add(8)
set_var.add(7)
set_var.add(4) # duplicate elements are ignored in a set
set_var.add(9)
set_var.add(11)

# print the content and length of the set
print("Content of Set : ", set_var)
print("Length of Set : ", len(set_var))

# convert the set to a list
set_list = list(set_var)

# print the content of the set after list conversion
print("Content of Set after List conversion: ", set_list)

# iterate elements with index
for idx in range(0, len(set_list)):
    print("Element at ", idx, " index is : ", set_list[idx])


# ### 13. Strings

# In[5]:


# Python Program Strings
tmp_str = "PythonSessions"

print("Input Str : ",tmp_str)
print("Length Of Input Str : ",len(tmp_str))

# Iterate elements without index
print("Without Index Iteration")
for char in tmp_str:
    print(char)

# Iterate elements with index
print("With Index Iteration")
for idx in range(0,len(tmp_str)):
    print("Character at ",idx," index is : ",tmp_str[idx])

print("Input Str in Upper Case : ",tmp_str.upper())
print("Input Str in Lower Case : ",tmp_str.lower())


# ### 14. List sorting

# In[6]:


# This program sorts a list of integers in ascending and descending order.
# Define the list
arr_list = [5, 6, 1, 2, 3, 9]

# Print the original list
print("Original List: ", arr_list)

# Sort the list in ascending order
arr_list.sort()
print("List After Sorting in Ascending Order: ", arr_list)

# Sort the list in descending order
arr_list.sort(reverse=True)
print("List After Sorting in Descending Order: ", arr_list)


# ### 15. List comprehension

# In[7]:


# Program for List Comprehension

arr_list = [3,6,7,4,1,2,15,10,12,11]

# Create another list which will have only even values
even_element_list = []

for num in arr_list:
    if num%2 == 0:
        even_element_list.append(num)

print("Even Elements List : ",even_element_list)

even_element_list = [ num for num in arr_list if num%2 == 0 ]
print("Even Elements List : ",even_element_list)



# Create another list which will have even values before odd values
result = [ num for num in arr_list if num%2 == 0 ] + [ num for num in arr_list if num%2 != 0 ]
print("Even-Odd Elements List : ",result)


# ### 16. Functions

# In[8]:


# Python program for functions
# A function without any argument
def print_func():
    print("Hello I'm Vighnesh")

# Calling the function
print_func()

# A function with 2 arguments
def power_func(num,exp):
    result = num**exp
    return result

# Calling the power function with 2 arguments
n = 3
e = 7
output = power_func(n,e)
print("Output of Power Function : ",output)

# A function that performs some mathematical operations
def math_ops(num1,num2):
    addition = num1 + num2
    subs = num1 - num2
    mul = num1 * num2
    div = num1/num2
    return addition, subs, mul, div
# Calling the math_ops function with 2 arguments and unpacking the result tuple
n1 = 18
n2 = 4
add, subs, mul, div = math_ops(n1,n2)
print("Addition of {}, {}: {}".format(n1, n2, add))
print("Substraction of {}, {}: {}".format(n1, n2, subs))
print("Multiplication of {}, {}: {}".format(n1, n2, mul))
print("Division of {}, {}: {}".format(n1, n2, div))

# A function that implements power function with key value inputs
def power_func(**kwargs):
    result = kwargs['num'] ** kwargs['exp']
    return result

# Calling the power function with keyword arguments
output1 = power_func(num=3,exp=4)
output2 = power_func(exp=4,num=3)
print("Output1 of Power Function : ",output1)
print("Output2 of Power Function : ",output2)


# ### 17. Lambda function

# In[9]:


# This is a program for lambda functions in Python.
# Here, we define two lambda functions using the lambda keyword.
# The first lambda function, add_lambda_exm, takes two arguments and returns their sum.
add_lambda_exm = lambda x,y : x+y

# The second lambda function, square_lambda_exm, takes one argument and returns its square.
square_lambda_exm = lambda x : x * x

# We then define two variables, num1 and num2, and assign them values.
num1 = 4
num2 = 7

# We use the first lambda function to add the values of num1 and num2, and store the result in add_result.
add_result = add_lambda_exm(num1,num2)

# We use the second lambda function to find the square of the value of num2, and store the result in square_result.
square_result = square_lambda_exm(num2)

# Finally, we print out the values of add_result and square_result.
print("Sum of ",num1," and ",num2," is = ",add_result)
print("Square of ",num2," is = ",square_result)


# ### 18. Map reduce

# In[10]:


# Program for map(), reduce(), filter()
# define a list
arr_list = [9,6,3,22]

# define lambda functions to add 5 and square the elements of the list
add_five_lambda = lambda x : x + 5
square_lambda = lambda x : x * x

# apply map() on lambda functions to transform the list
result_add_five = list(map(add_five_lambda, arr_list))
result_square = list(map(square_lambda, arr_list))

# print the transformed lists
print("Result for Add Five Map : ",result_add_five)
print("Result for Square Map : ",result_square)

# define two lists and a lambda function to sum their elements
arr_list1 = [2,4,6,8]
arr_list2 = [11,2,10,20]
sum_list_lambda = lambda x,y : x+y

# apply map() on lambda function to sum the corresponding elements of two lists
sum_list_result = list(map(sum_list_lambda, arr_list1, arr_list2))
print("Sum List Result : ",sum_list_result)

# define a list and lambda function to sum its elements using reduce()
from functools import reduce
arr_list3 = [1,2,4,9]
sum_ele = lambda x,y : x+y
result_reduce = reduce(sum_ele,arr_list3)
print("Result of Reduce : ", result_reduce)

# define a list and lambda function to filter even numbers
seq_num = [0, 1, 2, 4, 8, 11, 15]
filter_logic = lambda x : x%2 == 0
even_num_list = filter(filter_logic, seq_num)

# print the filtered list
print("Filter even number result : ",list(even_num_list))


# ### 19. Try & Except

# In[11]:


# Python program for try & except

a = 10

# Normal exception capturing
try:
    result = a/0
except:
    print("Some error occurred !!")

# Capture all exceptions
try:
    print("Before division")
    result = a/0
    print("After division")
except Exception as err:
    print("Failed Execution - ",str(err))

# Capture specific exception
try:
    print("Before division")
    result = a/0
    print("After division")
except ZeroDivisionError as err:
    print("Failed Execution - ",str(err))

arr_list = [1,2,3,4,5]

try:
    print("10th Element - ",arr_list[9])
except Exception as err:
    print("Failed Execution - ",str(err))

name = input("Enter your name : ")
age = int(input("Enter your age : "))

try:
    if (age<18):
        raise Exception("Cannot register for this application, Age must be greater than 18 !!")
    print("Valid User !!")
except Exception as err:
    print("Failed Execution - ",str(err))

# Multiple exceptions
a = 0
inp_dict = {'Vighnesh' : 10, 'Robin' : 15}
arr_list = [1,2,5,8]

try:
    print("Before Core Logic")
    result = a/0
    get_jimmy = inp_dict['Jimmy']
    tenth_element = arr_list[9]
    print("After Core Logic")
except ZeroDivisionError as err:
    print("Failed Execution - ",str(err))
except KeyError as err:
    print("Failed Execution - ",str(err))
except IndexError as err:
    print("Failed Execution - ",str(err))

# Use of else block
a = 10
inp_dict = {'Vighnesh' : 10, 'Robin' : 15, 'Jimmy' : 20}
arr_list = [1,2,5,8]

try:
    print("Before Core Logic")
    result = a/10
    get_jimmy = inp_dict['Jimmy']
    tenth_element = arr_list[2]
    print("After Core Logic")
except ZeroDivisionError as err:
    print("Failed Execution - ",str(err))
except KeyError as err:
    print("Failed Execution - ",str(err))
except IndexError as err:
    print("Failed Execution - ",str(err))
else:
    print("If there is no exception the this code block will be executed")

# Use of finally block
a = 10
inp_dict = {'Vighnesh' : 10, 'Robin' : 15, 'Jimmy' : 20}
arr_list = [1,2,5,8]

try:
    print("Before Core Logic")
    result = a/10
    get_jimmy = inp_dict['Jimmy']
    tenth_element = arr_list[9]
    print("After Core Logic")
except ZeroDivisionError as err:
    print("Failed Execution - ",str(err))
except KeyError as err:
    print("Failed Execution - ",str(err))
except IndexError as err:
    print("Failed Execution - ",str(err))
else:
    print("If there is no exception the this code block will be executed")
finally:
    print("This block will always execute doesn't matter exception occurred or not")


# ### 20. OOP in Python

# 1. Class & Object

# In[12]:


class Car:
    pass

# Creating an instance of the Car class
car1 = Car()

# Setting attributes for car1
car1.name = "Enzo"
car1.price = 5000000
car1.quantity = 5

# Printing the types of car1 and its attributes
print(type(car1))          # <class '__main__.Car'>
print(type(car1.name))     # <class 'str'>
print(type(car1.price))    # <class 'int'>
print(type(car1.quantity)) # <class 'int'>


# In[1]:


class Hotel:
    def __init__(self):
        # Initialize empty lists for guests and a dictionary of rooms
        self.guests = []
        self.rooms = {'Single': {'available': 10,'price': 1000},
                      'Double': {'available': 20,'price': 2000},'Suite':
                      {'available': 5,'price': 5000}}

    def menu(self):
        # Display the menu options and get user input
        user_input = input("""Hi, welcome to our hotel!
        1. Press 1 to check availability
        2. Press 2 to book a room
        3. Press 3 to cancel a booking
        4. Press 4 to check guest details
        5. Press 5 to exit""")

        # Based on the user input, call the appropriate method or display an error message
        if user_input == '1':
            self.check_availability()
        elif user_input == '2':
            self.book_room()
        elif user_input == '3':
            self.cancel_booking()
        elif user_input == '4':
            self.check_guest_details()
        elif user_input == '5':
            exit()
        else:
            print('Invalid input!')
            self.menu()

    def check_availability(self):
        # Display the available rooms and their prices
        for room_type, room_info in self.rooms.items():
            print(room_type, 'Rooms Available:', room_info['available'], 'Price:', room_info['price'])
        self.menu()

    def book_room(self):
        # Get the desired room type from the user and check availability
        room_type = input('Enter Room Type (Single/Double/Suite): ')
        if room_type not in self.rooms:
            print('Invalid Room Type')
            self.menu()
        elif self.rooms[room_type]['available'] == 0:
            print('Sorry, no', room_type, 'Rooms available')
            self.menu()
        else:
            # If the room is available, ask for guest details and add the guest and room to the appropriate lists
            self.rooms[room_type]['available'] -= 1
            guest_name = input('Enter Guest Name: ')
            guest_age = input('Enter Guest Age: ')
            guest = {'Name': guest_name, 'Age': guest_age, 'Room Type': room_type}
            self.guests.append(guest)
            print('Booking Successful!')
            self.menu()

    def cancel_booking(self):
        # Get the name of the guest whose booking needs to be cancelled and remove the guest from the list
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in self.guests:
            if guest['Name'] == guest_name:
                self.rooms[guest['Room Type']]['available'] += 1
                self.guests.remove(guest)
                guest_found = True
                print('Booking Cancelled Successfully!')
                break
        # If no matching guest is found, display an error message
        if not guest_found:
            print('Guest Not Found')
        self.menu()

    def check_guest_details(self):
        # Get the name of the guest whose details need to be checked and display the details if the guest is found
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in self.guests:
            if guest['Name'] == guest_name:
                print('Name:', guest['Name'])
                print('Age:', guest['Age'])
                print('Room Type:', guest['Room Type'])
                guest_found = True
                break


# In[2]:


hotel = Hotel()
hotel.menu()


# In[9]:


class Fraction:
  
    # Constructor to initialize numerator and denominator
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    # Method to return the fraction in the form of a string
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    # Method to add two fractions
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    # Method to subtract two fractions
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    # Method to multiply two fractions
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    # Method to divide two fractions
    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    # Method to convert fraction to decimal
    def convert_to_decimal(self):
        return self.num / self.den


# In[10]:


frac1 = Fraction(4,8)
frac2 = Fraction(9,8)


# In[11]:


print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)


# In[16]:


class Point:

    # constructor to initialize coordinates of point
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method to return a string representation of the point
    def __str__(self):
        return '<{},{}>'.format(self.x, self.y)

    # method to calculate euclidean distance between two points
    def euclidean_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    # method to calculate distance of point from origin
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Line:

    # constructor to initialize coefficients of line equation
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    # method to return a string representation of the line equation
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    # method to check if a given point lies on the line or not
    def point_on_line(self, point):
        if self.A * point.x + self.B * point.y + self.C == 0:
            return "The point lies on the line"
        else:
            return "The point does not lie on the line"

    # method to calculate shortest distance between line and point
    def shortest_distance(self, point):
        return abs(self.A * point.x + self.B * point.y + self.C) / (self.A ** 2 + self.B ** 2) ** 0.5


# In[17]:


line1 = Line(1,7,-2)
point1 = Point(3,8)
print(line1)
print(point1)

line1.shortest_distance(point1)


# 2. Encapsulation & Static variables

# In[18]:


class Hotel:
    def __init__(self):
        # Initialize empty lists for guests and a dictionary of rooms
        self.__guests = []
        self.__rooms = {'Single': {'available': 10, 'price': 1000},
                      'Double': {'available': 20, 'price': 2000},'Suite':
                      {'available': 5, 'price': 5000}}

    def menu(self):
        # Display the menu options and get user input
        user_input = input("""Hi, welcome to our hotel!
        1. Press 1 to check availability
        2. Press 2 to book a room
        3. Press 3 to cancel a booking
        4. Press 4 to check guest details
        5. Press 5 to exit""")

        # Based on the user input, call the appropriate method or display an error message
        if user_input == '1':
            self.__check_availability()
        elif user_input == '2':
            self.__book_room()
        elif user_input == '3':
            self.__cancel_booking()
        elif user_input == '4':
            self.__check_guest_details()
        elif user_input == '5':
            exit()
        else:
            print('Invalid input!')
            self.menu()

    def __check_availability(self):
        # Display the available rooms and their prices
        for room_type, room_info in self.__rooms.items():
            print(room_type, 'Rooms Available:', room_info['available'], 'Price:', room_info['price'])
        self.menu()

    def __book_room(self):
        # Get the desired room type from the user and check availability
        room_type = input('Enter Room Type (Single/Double/Suite): ')
        if room_type not in self.__rooms:
            print('Invalid Room Type')
            self.menu()
        elif self.__rooms[room_type]['available'] == 0:
            print('Sorry, no', room_type, 'Rooms available')
            self.menu()
        else:
            # If the room is available, ask for guest details and add the guest and room to the appropriate lists
            self.__rooms[room_type]['available'] -= 1
            guest_name = input('Enter Guest Name: ')
            guest_age = input('Enter Guest Age: ')
            guest = {'Name': guest_name, 'Age': guest_age, 'Room Type': room_type}
            self.__guests.append(guest)
            print('Booking Successful!')
            self.menu()

    def __cancel_booking(self):
        # Get the name of the guest whose booking needs to be cancelled and remove the guest from the list
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in self.__guests:
            if guest['Name'] == guest_name:
                self.__rooms[guest['Room Type']]['available'] += 1
                self.__guests.remove(guest)
                guest_found = True
                print('Booking Cancelled Successfully!')
                break
        # If no matching guest is found, display an error message
        if not guest_found:
            print('Guest Not Found')
        self.menu()

    def __check_guest_details(self):
        # Get the name of the guest whose details need to be checked and display the details if the guest is found
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in self.__guests:
            if guest['Name'] == guest_name:
                print('Name:', guest['Name'])
                print('Age:', guest['Age'])
                print('Room Type:', guest['Room Type'])
                guest_found = True
                break


# In[20]:


hotel = Hotel()
hotel.menu()


# In[21]:


class Hotel:
    guests = []
    rooms = {'Single': {'available': 10, 'price': 1000},
             'Double': {'available': 20, 'price': 2000},
             'Suite': {'available': 5, 'price': 5000}}

    @staticmethod
    def menu():
        # Display the menu options and get user input
        user_input = input("""Hi, welcome to our hotel!
        1. Press 1 to check availability
        2. Press 2 to book a room
        3. Press 3 to cancel a booking
        4. Press 4 to check guest details
        5. Press 5 to exit""")

        # Based on the user input, call the appropriate method or display an error message
        if user_input == '1':
            Hotel.check_availability()
        elif user_input == '2':
            Hotel.book_room()
        elif user_input == '3':
            Hotel.cancel_booking()
        elif user_input == '4':
            Hotel.check_guest_details()
        elif user_input == '5':
            exit()
        else:
            print('Invalid input!')
            Hotel.menu()

    @staticmethod
    def check_availability():
        # Display the available rooms and their prices
        for room_type, room_info in Hotel.rooms.items():
            print(room_type, 'Rooms Available:', room_info['available'], 'Price:', room_info['price'])
        Hotel.menu()

    @staticmethod
    def book_room():
        # Get the desired room type from the user and check availability
        room_type = input('Enter Room Type (Single/Double/Suite): ')
        if room_type not in Hotel.rooms:
            print('Invalid Room Type')
            Hotel.menu()
        elif Hotel.rooms[room_type]['available'] == 0:
            print('Sorry, no', room_type, 'Rooms available')
            Hotel.menu()
        else:
            # If the room is available, ask for guest details and add the guest and room to the appropriate lists
            Hotel.rooms[room_type]['available'] -= 1
            guest_name = input('Enter Guest Name: ')
            guest_age = input('Enter Guest Age: ')
            guest = {'Name': guest_name, 'Age': guest_age, 'Room Type': room_type}
            Hotel.guests.append(guest)
            print('Booking Successful!')
            Hotel.menu()

    @staticmethod
    def cancel_booking():
        # Get the name of the guest whose booking needs to be cancelled and remove the guest from the list
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in Hotel.guests:
            if guest['Name'] == guest_name:
                Hotel.rooms[guest['Room Type']]['available'] += 1
                Hotel.guests.remove(guest)
                guest_found = True
                print('Booking Cancelled Successfully!')
                break
        # If no matching guest is found, display an error message
        if not guest_found:
            print('Guest Not Found')
        Hotel.menu()

    @staticmethod
    def check_guest_details():
        # Get the name of the guest whose details need to be checked and display the details if the guest is found
        guest_name = input('Enter Guest Name: ')
        guest_found = False
        for guest in Hotel.guests:
            if guest['Name'] == guest_name:
                print('Name:', guest['Name'])
                print('Age:', guest['Age'])
                print('Room Type:', guest['Room Type'])
                guest_found = True
                break


# In[22]:


hotel = Hotel()
hotel.menu()


# 3. Aggregation, inheritance & polymorphism

# In[2]:


# aggregation
class Car:
    def __init__(self, make, model, year, price_per_day):
        self.make = make
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.is_available = True  # Initialize the car as available

    def book(self):
        if not self.is_available:  # If car is already booked, return False
            return False
        self.is_available = False  # Mark the car as unavailable
        return True


class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.booked_cars = []  # Initialize the list of booked cars for the customer

    def book_car(self, car):
        if not car.book():  # If the car is not available, return False
            return False
        self.booked_cars.append(car)  # Add the booked car to the list of booked cars for the customer
        return True

    def return_car(self, car):
        if car not in self.booked_cars:  # If the car was not booked by the customer, return False
            return False
        self.booked_cars.remove(car)  # Remove the returned car from the list of booked cars for the customer
        car.is_available = True  # Mark the car as available
        return True


car1 = Car('Toyota', 'Camry', 2020, 50)
car2 = Car('Honda', 'Accord', 2021, 60)

cust1 = Customer('John', 'john@example.com', '555-5555')
cust2 = Customer('Jane', 'jane@example.com', '555-5556')

print(car1.is_available)  # True
print(cust1.book_car(car1))  # True
print(car1.is_available)  # False
print(cust2.book_car(car1))  # False
print(cust2.book_car(car2))  # True
print(cust1.return_car(car1))  # True
print(car1.is_available)  # True


# In[6]:


# Inheritance
# Parent class
class Vehicle:
    # Initialize vehicle attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to get vehicle description
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# Child class that inherits from Vehicle
class Car(Vehicle):
    # Initialize car attributes
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    # Method to get car description including fuel type
    def get_description(self):
        return f"{super().get_description()} ({self.fuel_type})"

# Create instances of Vehicle and Car
vehicle = Vehicle('Honda', 'Accord', 2021)
car = Car('Toyota', 'Camry', 2020, 'Gasoline')

# Call get_description method for each instance
print(vehicle.get_description()) # Output: 2021 Honda Accord
print(car.get_description()) # Output: 2020 Toyota Camry (Gasoline)


# In[9]:


# Single Inheritance Example

# Defining the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating")

# Defining the child class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canine")
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")
# Create a Dog object
my_dog = Dog("Max", "Labrador")

# Call the eat() and bark() methods
my_dog.eat()
my_dog.bark()


# In[12]:


# Multilevel Inheritance
# Defining the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating")

# Defining a derived class from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canine")
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")

# Defining a derived class from Dog
class Bulldog(Dog):
    def __init__(self, name):
        super().__init__(name, breed="Bulldog")
    
    def guard(self):
        print(f"{self.name} is guarding the house")

bulldog1 = Bulldog("Tommy")
print(bulldog1.name)
print(bulldog1.species)
print(bulldog1.breed)
bulldog1.eat()
bulldog1.bark()
bulldog1.guard()


# In[15]:


# Hierarchical in heritance
# Defining the parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"Driving a {self.make} {self.model}")

# Defining two derived classes from Vehicle
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def park(self):
        print(f"Parking the {self.make} {self.model}")

class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def haul(self):
        print(f"Hauling cargo in the {self.make} {self.model}")

# Create a car object
my_car = Car("Toyota", "Camry")
# Call the drive method of the Vehicle class
my_car.drive()
# Call the park method of the Car class
my_car.park()

# Create a truck object
my_truck = Truck("Ford", "F-150")
# Call the drive method of the Vehicle class
my_truck.drive()
# Call the haul method of the Truck class
my_truck.haul()


# In[17]:


# Multiple Inheritance(Diamond Problem)
# Define a parent class A
class A:
    def foo(self):
        print("A's foo() called")
        
# Define two child classes B and C that inherit from A
class B(A):
    def foo(self):
        print("B's foo() called")

class C(A):
    def foo(self):
        print("C's foo() called")
        
# Define a child class D that inherits from both B and C
class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the foo() method on the object of class D
d.foo()


# In[18]:


# Hybrid Inheritance
# Define the base class A
class A:
    def method_A(self):
        print("Method A called")

# Define two classes B and C that derive from A
class B(A):
    def method_B(self):
        print("Method B called")

class C(A):
    def method_C(self):
        print("Method C called")

# Define a class D that derives from both B and C
class D(B, C):
    def method_D(self):
        print("Method D called")

# Create an object of class D and call its methods
obj = D()
obj.method_A()  # Call the method_A() method of class A
obj.method_B()  # Call the method_B() method of class B
obj.method_C()  # Call the method_C() method of class C
obj.method_D()  # Call the method_D() method of class D


# 

# In[19]:


# polymorphism
# Define a class Shape
class Shape:
  # Define a method area() to calculate the area of different shapes
  def area(self, a, b=None):
    raise NotImplementedError("Subclass must implement abstract method")

# Define a class Circle that derives from Shape
class Circle(Shape):
  # Define a method area() to calculate the area of a circle
  def area(self, r, *args):
    return 3.14*r*r

# Define a class Rectangle that derives from Shape
class Rectangle(Shape):
  # Define a method area() to calculate the area of a rectangle
  def area(self, l, w, *args):
    return l*w

# Create instances of the Circle and Rectangle classes
c = Circle()
r = Rectangle()

# Call the area() method on the Circle object to calculate the area of a circle
print("Area of Circle:", c.area(2)) # Output: Area of Circle: 12.56 (approximately)

# Call the area() method on the Rectangle object to calculate the area of a rectangle
print("Area of Rectangle:", r.area(3, 4)) # Output: Area of Rectangle: 12


# In[ ]:




