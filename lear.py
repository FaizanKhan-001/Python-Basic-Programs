# 1. Print Hello World
print("Hello World")

# 2. Add Two Numbers
a = 10
b = 20
print(a + b)

# 3. Calculate the Area of a Triangle
B = int(input("Enter base: "))
H = int(input("Enter height: "))
Area = 0.5 * B * H
print("Area of triangle is:", Area)

# 4. Area of a Square
side = int(input("Enter side of square: "))
Area = side * side
print("Area of square is:", Area)

# 5. Average of Two Floating Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("Average of the two numbers is:", average)

# 6. Compare Two Integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a >= b)

# 7. Length of First Name
first_name = input("Enter your first name: ")
length = len(first_name)
print("Length of your first name is:", length)

# 8. Occurrence of '$' in a String
string = input("Enter a string: ")
count = string.count('$')
print("Occurrence of '$' in the string is:", count)

# 9. Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 10. Greatest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)

# 11. Multiple of 7
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")

# 12. Square Root
number = float(input("Enter a number: "))
square_root = number ** 0.5
print("The square root of the number is:", square_root)

# 13. Solve Quadratic Equation
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are real and different.")
    print("Root 1 is:", root1)
    print("Root 2 is:", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root is:", root)
else:
    print("The roots are complex.")

# 14. Swap Two Variables
x = 5
y = 10
print("Before swapping: x =", x, "and y =", y)
x, y = y, x
print("After swapping: x =", x, "and y =", y)

# 15. Kilometers to Miles
x = float(input("Enter distance in kilometers: "))
miles = x * 0.621371
print("Distance in miles is:", miles)

# 16. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit is:", fahrenheit)

# 17. Positive, Negative or Zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 18. Leap Year
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

# 19. Prime Number Check
number = int(input("Enter a number: "))
is_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False
if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")

# 20. Prime Numbers in Interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print("Prime numbers in the interval are:")
for number in range(start, end + 1):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        print(number)

# 21. Factorial
number = int(input("Enter a number: "))
factorial = 1
if number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of the number is:", factorial)

# 22. Multiplication Table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 23. Fibonacci Sequence
number = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if number <= 0:
    print("Please enter a positive integer.")
elif number == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < number:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# 24. Armstrong Number Check
number = int(input("Enter a number: "))
num_str = str(number)
sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
if sum_of_cubes == number:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

# 25. Armstrong Numbers in Interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print("Armstrong numbers in the interval are:")
for number in range(start, end + 1):
    num_str = str(number)
    sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
    if sum_of_cubes == number:
        print(number)

# 26. Sum of Natural Numbers
number = int(input("Enter a number: "))
sum_of_natural_numbers = sum(range(1, number + 1))
print("The sum of natural numbers up to", number, "is:", sum_of_natural_numbers)

# 27. Powers of 2 (Lambda)
powers_of_2 = lambda x: 2 ** x
number = int(input("Enter a number: "))
print("Powers of 2 up to", number, "are:")
for i in range(1, number + 1):
    print(powers_of_2(i))

# 28. Divisible Check
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
if divisor == 0:
    print("Error: Divisor cannot be zero.")
else:
    if dividend % divisor == 0:
        print(dividend, "is divisible by", divisor)
    else:
        print(dividend, "is not divisible by", divisor)

# 29. ASCII Value
character = input("Enter a character: ")
ascii_value = ord(character)
print("The ASCII value of", character, "is", ascii_value)

# 30. HCF
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("The HCF of", num1, "and", num2, "is", hcf)

# 31. LCM
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = 54
num2 = 24
print

#list sliciing 

my_list = [1, 2, 3, 4, 5]

print(my_list[:])


#program for sort the values of dictonaries

dt = {5:4, 1:6, 6:3}

sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dt)


#python program to join two lists

list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2
print(list_joined)


#python program to get a substring of a string
my_string = "I love python."

# prints "love"
print(my_string[2:6])

# prints "love python."
print(my_string[2:])

# prints "I love python"
print(my_string[:-1])


#program for count the occurance of a item in a list
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)


#program to reverse a number

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


#program to captailze first lettter

my_string = "programiz is Lit"

print(my_string[0].upper() + my_string[1:])


#Python program to remove dupblicates in a list

list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))