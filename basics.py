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
#f = slow_fibonacci(35)
#print(f)

def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1, b, a+b)

f = fibonacci(100)
print(f)
