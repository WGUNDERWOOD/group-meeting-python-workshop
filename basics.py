# Intro
# General purpose programming language
# Become very popular for data science and scientific computing

# Why Python?
# Python is easy: simple syntax
# Free and open-source
# Well maintained: good documentation, bugs fixed quickly
# Huge ecosystem of packages, backed by corporations (500k+)
# Multi-paradigm: functional, OOP, etc
# Dynamic typing and automatic memory management (GIL, RC, GC)
# Compared to R, Python is better for
#   Handling large data sets
#   Deep learning models
#   General-purpose programming (scripting, web dev, databasing)
# However
#   R has more classical statistical packages
#   R can be easier to use for visualisation

# Overview of the workshop
# Basics: arithmetic, strings, lists, control flow, functions
# Then Numpy, OOP, example application with visualisation
# Min will do second half, show some statistical examples
# Stop me any time with questions
# Feel free to follow along on your own machine

# Basic types
# Int
a = 5
print(a)
print(type(a))

# Float
b = 0.1
print(b)
print(type(b))

# Type conversion
c = float(2)
print(c)
print(type(c))

# Boolean
t = True
f = False
print(t or f)
print(t and f)
print(t and (not f))
# comments look like this

# Numeric operations
a = 4
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
# Note "^" is bitwise XOR

# Strings
hello = "Hello"
print(hello)

# Concatenation
world = "world"
hello_world = hello + ", " + world + "!"
print(hello_world)

# Repetition
hello_hello = 2 * hello
print(hello_hello)

# Formatting
n_days = 7
print(f"There are {n_days} days in a week")

# Lists
# Note zero-indexing and [...) ranges
# Length of slice is end - start
numbers = [3, 4, 5]
print(numbers[0])
print(numbers[2])
print(numbers[0:1])
print(numbers[0:3])
print(len(numbers))
print(sum(numbers))

# Mutation
numbers[0] = 6
print(numbers)
numbers[0:2] = [7, 8]
print(numbers)

# Concatenation and repetition
print(numbers + numbers)
print(numbers * 3)

# List comprehension
# Learn this! Very useful, not in R
# This is also often faster than making a loop
big_numbers = [x for x in numbers if x > 6]
print(big_numbers)
big_square_numbers = [x*x for x in numbers if x > 6]
print(big_square_numbers)
cube_even_square_odd_numbers = [x**3 if x % 2 == 0 else x**2 for x in numbers]
print(cube_even_square_odd_numbers)

# If statements and for loops
# Note the conciseness and similarity with English
# Be very careful with white space, as no braces
# Usual convention is 4 spaces per indentation level
if numbers[2] > 3:
    print(numbers)

for i in range(4):
    print(i)

for i in range(2, 4):
    print(i)

for x in numbers:
    if x > 5:
        print(f"{x} is more than five")

# If and else
fruit = ["apple", "banana"]
fruit_and_veg = ["apple", "cabbage", "carrot", "banana"]
vegetables = [x for x in fruit_and_veg if x not in fruit]
print(vegetables)

for x in fruit_and_veg:
    if x not in fruit:
        print(f"{x} is a vegetable")
    else:
        print(f"{x} is a fruit")

# Functions
# The main purpose of functions is to name an operation
def add_and_square(x, y):
    z = x + y
    return z * z

print(add_and_square(2, 3))

# Example program
# Find the 100th Fibonacci number
def slow_fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return slow_fibonacci(n-1) + slow_fibonacci(n-2)

f = slow_fibonacci(5)
print(f)

# Default arguments and tail recursion
def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1, b, a+b)

f = fibonacci(100)
print(f)

# Numpy
# Very important package for scientific computing
# Provides multidimensional arrays with associated functions
# Typically much faster than native Python lists
# Recall how list + list does concatenation; often not very helpful
import numpy as np # note alias here
one_dim = np.array([1, 2, 3, 4, 5, 6])
print(one_dim)
two_dim = np.array([[2, 4, 6], [8, 10, 12]])
print(two_dim)
print(two_dim[1,2])
print(two_dim.shape)
print(two_dim.size)
print(two_dim[two_dim < 10])
reshaped = np.reshape(two_dim, (6))
print(reshaped)

linear_array = np.linspace(1, 2, num=5)
print(linear_array)
zeros_array = np.zeros((2, 3))
print(zeros_array)
ones_array = np.ones((2, 3))
print(ones_array)

a = np.array([[2, 4, 6], [8, 10, 12]])
b = np.array([[1, 3, 5], [7, 9, 11]])
print(a + b)
print(a * b)
print(a + 1)
print(a * 4)
print(a.max())
print(a.T)
ab = a @ b.T
print(ab)
print(np.linalg.inv(ab))
print(np.linalg.eig(ab))

# Importing modules
# Typically do this at the top of your file/notebook
# Similar to R "source"
import functions
three = functions.add_one(2)
print(3)

# Basic OOP
# objects allow us to store information in a structured way
# methods allow us to do things with objects
class Person:

  # Initialise the object with basic information
  def __init__(self, first_name, surname, age):
    self.first_name = first_name
    self.surname = surname
    self.age = age

  # Use attributes in a method
  def get_full_name(self):
      return f"{self.first_name} {self.surname}"

  # Use external parameter in a method
  def get_age_in_year(self, year):
      return self.age + year - 2024

  # Mutating method
  def make_older(self):
      self.age = self.age + 1

p1 = Person("Will", "Underwood", 27)

print(p1.first_name)
print(p1.surname)
print(p1.age)
print(p1.get_full_name())
print(p1.get_age_in_year(2020))
print(p1.make_older())
print(p1.age)
print(p1.make_older())
print(p1.age)
