# Basic types
a = 5
print(a)
print(type(a))

b = 0.1
print(b)
print(type(b))

c = float(2)
print(c)
print(type(c))

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

# Strings
hello = "Hello"
print(hello)

world = "world"
hello_world = hello + ", " + world + "!"
print(hello_world)

hello_hello = 2 * hello
print(hello_hello)

n_days = 7
print(f"There are {n_days} days in a week")

# Lists
numbers = [3, 4, 5]
print(numbers[0])
print(numbers[2])
print(numbers[0:1])
print(numbers[0:3])
print(len(numbers))
print(sum(numbers))

numbers[0] = 6
print(numbers)

numbers[0:2] = [7, 8]
print(numbers)

print(numbers + numbers)
print(numbers * 3)

big_numbers = [x for x in numbers if x > 6]
print(big_numbers)

big_square_numbers = [x*x for x in numbers if x > 6]
print(big_square_numbers)

# If statements and for loops
if numbers[2] > 3:
    print(numbers)

for i in range(4):
    print(i)

for i in range(2, 4):
    print(i)

for x in numbers:
    if x > 5:
        print(f"{x} is more than five")

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
import numpy as np
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
