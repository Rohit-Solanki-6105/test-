Name  = Solanki Rohit Hareshbhai
Roll = 106
Subject = Python Assignment
Course = Msc CS sem 4 - batch 2

----------------------------------------------------

# 1) Write a python program to add two numbers.
# 2) Write a python program to find quotient and remainder.
# 17) Write a python program to calculate power of a number.
#27) Write a python program to make a simple calculator to add, subtract, multiply or divide

while True: print(eval(input("Expression: ")))

'''
Expression: 1+2
3
Expression: 4%3
1
Expression: 3**2
9
Expression: 2**3
8
Expression: 5//2
2
Expression: 2/3
0.6666666666666666
Expression: 2-5
-3
Expression: exit()
'''
-------------------------------------------------------

# 10) Write a python program to check leap year.
def is_leap(year):
    if year % 4 == 0:
        return True

    return False

print(is_leap(2020))
print(is_leap(2001))

'''
True
False
'''
-------------------------------------------------------

# 11) Write a python program to find factorial.

def fectorial(num):
    # print(num)
    fect = 1
    for i in range(1, num + 1):
        fect *= i

    return fect

print(fectorial(int(input("Enter num for fectorial: "))))

'''
Enter num for fectorial: 6
720
'''
-------------------------------------------------------

# 12) Write a python program to generate multiplication table.
def multiply_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
multiply_table(float(input("Enter number to generate multiplication table: ")))

'''
Enter number to generate multiplication table: 3
3.0 X 1 = 3.0
3.0 X 2 = 6.0
3.0 X 3 = 9.0
3.0 X 4 = 12.0
3.0 X 5 = 15.0
3.0 X 6 = 18.0
3.0 X 7 = 21.0
3.0 X 8 = 24.0
3.0 X 9 = 27.0
3.0 X 10 = 30.0
'''
-------------------------------------------------------

# 13) Write a python program to display fibonacci series. (eg. 0, 1, 1, 2, 3, 5, 8, 13, …)?

def fibonacci(num):
    series = []
    n1 = 0
    n2 = 1
    next_num = n2
    for i in range(num):
        series.append(next_num)
        n1 = n2
        n2 = next_num
        next_num = n1+n2

    return series

print(fibonacci(10))

'''
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''
-------------------------------------------------------

# 14) Write a python program to find gcd.?
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

num1 = 54
num2 = 24
val = gcd(num1, num2)

print(val)

'''
6
'''
-------------------------------------------------------

# 15) Write a python program to find lcm.
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def lcm(x, y):
   lcm = (x*y)/gcd(x,y)
   return lcm

n1 = 20
n2 = 25

l = lcm(n1, n2)
print(l)

'''
575.0
'''
-------------------------------------------------------

# 16) Write a python program to reverse a number.
def reverse_num(num):
    num = str(num)
    return num[::-1]

print(reverse_num(123.12))
print(reverse_num(2345689))

'''
21.321
9865432
'''
-------------------------------------------------------

# 18) Write a python program to find binary value of a character.
# bin_val = bin(ord(input("Enter a Character: ")))
# bin_value = str(bin_val)
# print(bin_value)

def Print_Binary_Values(num): 
    # base condition 
    if(num > 1): 
        Print_Binary_Values(num // 2) 
    print(num % 2, end="") 

# Rohit
Print_Binary_Values(ord('R'))
print(end=" ")
Print_Binary_Values(ord('o'))
print(end=" ")
Print_Binary_Values(ord('h'))
print(end=" ")
Print_Binary_Values(ord('i'))
print(end=" ")
Print_Binary_Values(ord('t'))

'''
1010010 1101111 1101000 1101001 1110100
'''
-------------------------------------------------------

# 19) Write a python program to display two separate strings in single line continuously.
a = input("s1: ")
b = input("s2: ")

print(a, b)

print(a, end=" ")
print(b)

'''
s1: 2
s2: 3
2 3
2 3
'''
-------------------------------------------------------

# 20) Write a python program to check whether a number is palindrome or not.?
def is_palindrome(n):
    return eval(f"{n} == {int(str(n)[::-1])}")

print(is_palindrome(12321))
print(is_palindrome(123))

'''
True
False
'''
-------------------------------------------------------

# 21) Write a python program to check whether a number is prime or not.
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(21))
print(is_prime(22))
print(is_prime(23))

'''
False
False
True
'''
-------------------------------------------------------

# 22) Write a python program to display prime numbers between two intervals.?
def prime_numbers(start, end):
    prime_numbers = []
    for possiblePrime in range(start, end + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            prime_numbers.append(possiblePrime)
    return prime_numbers

# Get user input for the interval
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Print the prime numbers in the interval
print("Prime numbers between {} and {} are:".format(start, end))
print(prime_numbers(start, end))

'''
Enter the starting range: 32
Enter the ending range: 56
Prime numbers between 32 and 56 are:
[37, 41, 43, 47, 53]
'''
-------------------------------------------------------

# 23) Write a python program to check armstrong number.
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

lenth_num = len(str(num))
print(lenth_num)

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += (digit ** lenth_num)
   print(digit, "^", lenth_num, "+= sum = ", sum)
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

'''
Enter a number: 153
153 is an Armstrong number
'''
# 1, 1296, 81, 1694, 256

-------------------------------------------------------

# 24) Write a python program to display armstrong number between two intervals.?
# Function to find Armstrong numbers in a given interval
def find_Armstrong(lower, upper):
    # Iterate over numbers from lower to upper
    for num in range(lower, upper+1):
        # Calculate the sum of the cubes of the digits
        sum = 0
        temp = num
        order = len(str(num))
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        # Check if the number is an Armstrong number
        if num == sum:
            print(num)

# Replace these values with the desired interval
lower = 100
upper = 2000

# Call the function to find Armstrong numbers
find_Armstrong(lower, upper)

'''
153
370
371
407
1634
'''
-------------------------------------------------------

# 25) Write a python program to display factors of a number.?
def factors(x):
   for i in range(1, x):
       if x % i == 0:
           print(i)


factors(10)

'''
1
2
5
'''
-------------------------------------------------------

# 26) Write a python programs to create pyramid and pattern.
def pyramid(num):
    for i in range(1,num+1):
        print("*"*(i))

pyramid(int(input("Enter height: ")))

'''
Enter height: 5
*
**
***
****
*****
'''
-------------------------------------------------------

# 28) Write a python program to display Simple Number Triangle Pattern

def num_triangle(num):
    len = 1
    for i in range(1,num+1):
        s = str(i)
        print(" "*(num-i),s*(len))
        len = 2*i+1

num_triangle(5)

'''
     1
    222
   33333
  4444444
 555555555
 '''
-------------------------------------------------------

# 29) Write a python program to display inverted pyramid of numbers

def num_triangle(num):
  len = num*2-1
  for i in range(1, num+1):  
    s = str(i)
    print(" "*(i), s*(len))
    # print(s)
    len-=2


num_triangle(5)

'''
  111111111
   2222222
    33333
     444
      5
'''
-------------------------------------------------------

# 3) Write a python program to find type of objects in your system.
a = 1
print(type(a))
'''
<class 'int'>
'''
-------------------------------------------------------

# 30) Write a python program to display inverted pyramid of descending numbers

def num_triangle(num):
  spaces = 0
  for i in range(num, 0, -1):  
    s = str(i)
    print(" " * spaces, s*(i*2-1))
    spaces += 1

num_triangle(5)

'''
 555555555
  4444444
   33333
    222
     1
     
'''
-------------------------------------------------------

# 31) Write a python program to display inverted pyramid of the same digit
def pyramid(num, rows):
    for i in range(rows, 0, -1):
        print(" "*(rows-i),str(num)*(2*i-1))
pyramid(int(input("Number: ")), int(input("Rows: ")))

'''
Number: 5
Rows: 6
 55555555555
  555555555
   5555555
    55555
     555
      5
      '''
-------------------------------------------------------

# 32) Write a python program to display reverse pyramid of numbers
def reverse_pyramid_numbers(rows):
    num = 1
    for i in range(rows, 0, -1):
        print(' '*(rows - i), end='')
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
reverse_pyramid_numbers(rows)

'''
Enter the number of rows: 6
1 2 3 4 5 6
 7 8 9 10 11
  12 13 14 15
   16 17 18
    19 20
     21
     '''

-------------------------------------------------------

# 33) Write a python program to display inverted half pyramid number pattern

def pyramid(rows):
    for i in range(rows, 0, -1):
        # print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
pyramid(rows)

'''
Enter the number of rows: 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
-------------------------------------------------------

# 34) Write a python program to display pyramid of natural numbers less than 10

def pyramid_natural_numbers():
    num = 1
    for i in range(1, 5):
        print(" "*(5-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()

# Example usage
pyramid_natural_numbers()

'''
    1 
   2 3
  4 5 6
 7 8 9 10
'''

-------------------------------------------------------

# 35) Write a python program to display reverse pattern of digits from 10

def reverse_pattern_digits():
    num = 10
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(num, end=' ')
            num -= 1
        print()

# Example usage
reverse_pattern_digits()

'''
10 9 8 7 
6 5 4
3 2
1
'''
-------------------------------------------------------


# 36) Write a python program to display connected inverted pyramid pattern of numbers

def connected_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for k in range(i, 0, -1):
            print(k, end='')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
connected_inverted_pyramid(rows)

'''
Enter the number of rows: 5
1234554321
 12344321
  123321
   1221
    11
    '''

-------------------------------------------------------


# 37) Write a python program to display even number pyramid pattern

def even_number_pyramid(rows):
    num = 2
    for i in range(1, rows + 1):
        print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 2
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
even_number_pyramid(rows)

'''
Enter the number of rows: 5
    2
   4 6
  8 10 12
 14 16 18 20
22 24 26 28 30
'''
-------------------------------------------------------

# 38) Write a python program to display pyramid of horizontal tables

def horizontal_table_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i),end="")
        for j in range(1, i + 1):
            print(f"{i*j:4}", end=' ')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
horizontal_table_pyramid(rows)

'''
Enter the number of rows: 5
       1
      2    4
     3    6    9
    4    8   12   16
   5   10   15   20   25
'''

-------------------------------------------------------

# 39) Write a python program to display pyramid pattern of alternate numbers

def alternate_number_pyramid(start, rows):
    num = start
    for i in range(1, rows + 1):
        print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 2
        print()

# Example usage
start_num = int(input("Enter the starting number: "))
rows = int(input("Enter the number of rows: "))
alternate_number_pyramid(start_num, rows)

'''
Enter the number of rows: 5
    1
   3 5
  7 9 11
 13 15 17 19
21 23 25 27 29
'''
-------------------------------------------------------

# 4) Write a python program to read two numbers and display the greatest number.
# 7) Write a python program to find largest number among three numbers
a = [1,4,2]
print(max(a))

'''
4
'''
-------------------------------------------------------

# 40) Write a python program to display mirrored pyramid (right-angled triangle) pattern of numbers

def mirrored_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(i, 0, -1):
            print(j, end='')
        for k in range(2, i + 1):
            print(k, end='')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
mirrored_pyramid(rows)

'''
Enter the number of rows: 5
    1
   212
  32123
 4321234
543212345
'''

-------------------------------------------------------

# 41) Write a python program to display equilateral triangle with stars (asterisk symbol)

def equilateral_triangle_boundary(rows):
    for i in range(rows):
        if i == 0:
            print(' ' * (rows - 1) + '*')
        elif i == rows - 1:
            print(' ' * (rows - i - 1) + '* ' * (i + 1))
        else:
            print(' ' * (rows - i - 1) + '*' + ' ' * (2 * i - 1) + '*')


def equilateral_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)


# Input number of rows
rows = int(input("Enter the number of rows: "))


equilateral_triangle_boundary(rows)
equilateral_triangle(rows)

'''
Enter the number of rows: 5
    *
   * *
  *   *
 *     *
* * * * *
    *
   * *
  * * *
 * * * *
* * * * *
'''
-------------------------------------------------------

# 42) Write a python program to display downward triangle pattern of stars

def downward_triangle(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

# Input number of rows
rows = int(input("Enter the number of rows: "))
downward_triangle(rows)

'''
Enter the number of rows: 5
* * * * *
* * * *
* * *
* *
*
'''
-------------------------------------------------------

# 43) Write a python program to display pyramid pattern of stars

def pyramid(rows):
    for i in range(1, rows + 1):
        print(' '*(rows - i),'* '*i)

# Input number of rows
rows = int(input("Enter the number of rows: "))
pyramid(rows)

'''
Enter the number of rows: 5
    *
   * *
  * * *
 * * * *
* * * * *
'''
-------------------------------------------------------

# 44) Write a python program to display hourglass pattern program

def HourGlass(num):
    
    for i in range(num+1, 1, -1):
        print(" "*(num-i+1), "*"*(2*i-1))
        
    for i in range(num+1):
        print(" "*(num-i), "*"*(2*i+1))
        # print(" "*(num-i),f"{i}"*(i))
    
HourGlass(5)

'''
 ***********
  *********
   *******
    *****
     ***
      *
     ***
    *****
   *******
  *********
 ***********
 '''

-------------------------------------------------------

from math import factorial

n = 5
for i in range(n):
    # print(" "*(n-i+1), end="")
    for j in range(n-i+1):

        # for left spacing
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line
    print()
-------------------------------------------------------

# 5) Write a python program to check whether number is even or odd.
def check_even(num):
    if num%2 == 0: 
        print("Even")
        # return True
    print("Odd")
    # return False
check_even(int(input("Enter int: ")))
# print(check_even(int(input("Enter number: "))))

'''
Enter int: 3
Odd

Enter int: 4
Even
'''
-------------------------------------------------------

# 6) Write a python program to check whether a character is vowel or consonant.
def Vowel_or_Consonent(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        print("Vowel")
    else:
        print("Consonent")

Vowel_or_Consonent('a')
Vowel_or_Consonent('c')

'''
Vowel
Consonent
'''
-------------------------------------------------------

# 8) Write a python program to find all roots of a quadratic equation.

import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "Complex roots"

# Example usage
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

roots = quadratic_roots(a, b, c)
print("Roots:", roots)

'''
Enter the coefficient of x^2 (a): 1
Enter the coefficient of x (b): 5
Enter the constant term (c): 2
Roots: (-0.4384471871911697, -4.561552812808831)
'''
-------------------------------------------------------

# 9) Write a python program to calculate sum of natural numbers.

def nat_sum(n):
    sum = 0
    for i in range(n):
        sum+=i
    return sum
    
n = int(input("Enter num: "))
print(f"Sum: {nat_sum(n)}")

'''
Enter num: 34
Sum: 561
'''
-------------------------------------------------------


# def pyramid(num):
#     for i in range(0,num):
#         # print(i, end=" = ")
#         print("*"*(num-i), " "*(2*i), "*"*(num-i))
#         # print(f"i: {i},  num - i: {num - i}, 2*i : {2*i}")
    
#     # print("----------------------------")
#     for i in range(num, -1, -1):
#         # print(i, end=" = ")
#         print("*"*(num-i), " "*(2*i), "*"*(num-i))

# pyramid(10)

# def pyramid(num):
#     for i in range(num):
#         print(" "*(num-i), "*"*(2*i-1))

#     for i in range(num, -1, -1):
#         print(" "*(num-i), "*"*(2*i-1))

# def pyramid(num):
#     for i in range(num, 0, -1):
#         print('*'*(i), " ", "*"*(num-i), end="")
#         print("*"*(num-i), " ", "*"*(i))

#     for i in range(num+1):
#         print('*'*(i), " ", "*"*(num-i), end="")
#         print("*"*(num-i), " ", "*"*(i))

# def pyramid(num):
#     for i in range(num):
#         print(" "*(num-i),  "*"*(2*i+1))

#     for i in range(3):
#         print(" "*(num),  "*")

# def pyramid(num):


# pyramid(10)

# def calc(n1, op, n2):
#     match(op):
#         case  "+": return n1 + n2
#         case "-": return n1 - n2
#         case "*": return n1 * n2
#         case "/": return n1 / n2

# n1 = float(input("Enter first number: "))
# op = input("Enter operator (+,-,*,/): ")
# n2 = float(input("Enter second number: "))

# # print(f"{n1} {op} {n2} = ", end="")
# # print(calc(n1, op, n2))   # Output: 1
# print(f"{n1} {op} {n2} = ",calc(n1, op, n2), sep="")

# def is_palindrome(num):
#     num = str(num)
#     rev = num[::-1]
#     print(f"Num: {num}, Rev: {rev}")
#     print(num == rev)

# is_palindrome(12321)

# def is_armstrong(num):
#     # 153 = 1^3 + 5^3 + 3^3
#     sum = 0
#     temp = num
#     length_num = len(str(num))

#     while temp > 0: 
#         digit = temp % 10
#         sum += digit ** length_num
#         temp //= 10
#     print(sum)
#     return num == sum

# print(is_armstrong(92727))
    
# def pyramid(num):
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
#     for i in range(num, 0, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
'''
      *
     ***
    *****
   *******
  *********
 ***********
  *********
   *******
    *****
     ***
      *
      
      '''

# def pyramid(num):
    
#     for i in range(num+1, 1, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
        
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
# '''
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#  '''

# pyramid(5)

def box(num):
    print("*"*(2*num+3))
    
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
#     for i in range(num, 0, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
    for i in range(num):
        print("*"," "*(num-i),"*"*(2*i+1), " "*(num-i), "*", sep="")
    for i in range(num-1, 0, -1):
        print("*"," "*(num-i+1),"*"*(2*i-1), " "*(num-i+1), "*", sep="")
    print("*"*(2*num+3))

'''
*************
*     *     *
*    ***    *
*   *****   *
*  *******  *
* ********* *
*  *******  *
*   *****   *
*    ***    *
*     *     *
*************
'''

# box(50)
def box(num):
    
    print("*"*(2*num+3))
    for i in range(num):
        print("*"*(num-i)," ","*"*(2*i+1), " ", "*"*(num-i), sep="")
    for i in range(num-1, 0, -1):
        print("*"*(num-i+1)," ","*"*(2*i-1), " ", "*"*(num-i+1), sep="")
    
    print("*"*(2*num+3))
'''
***********************
********** * **********
********* *** *********
******** ***** ********
******* ******* *******
****** ********* ******
***** *********** *****
**** ************* ****
*** *************** ***
** ***************** **
* ******************* *
** ***************** **
*** *************** ***
**** ************* ****
***** *********** *****
****** ********* ******
******* ******* *******
******** ***** ********
********* *** *********
********** * **********
***********************
'''
box(10)
-------------------------------------------------------

'''
1. Define a Book class with attributes like title, author, and no_of_pages (all strings). 
Implement constructor(s) to initialize these attributes when creating a new Book object. 
Add a method called describe_book() that prints a summary of the book's information.
'''

class BOOK:
    def  __init__(self, title, author, pages, price):
        self.__title = title
        self.__author = author
        self._no_of_pages = pages
        self.price = price
    
    def describe_book(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Number of Pages: {self._no_of_pages}")
        print(f"Price: ${self.price}")

b1 = BOOK("hi", "helo", 420, 1200)
b1.describe_book()

'''
Title: hi
Author: helo
Number of Pages: 420
Price: $1200
'''

-------------------------------------------------------

'''
2. Define class student with attributes like First_name, Last_name, Course, batch_year, result). 
Apply constructor (s) to initialize the attributes while creating new student object. Here, 
batch_year must be passing year and result must be PASS or FAIL. Add a method to calculate 
total number of FAIL students. (static method).
'''
class Student:
    def __init__(self, First_name, Last_name, Course, batch_year, result):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Course = Course
        self.batch_year = batch_year
        self.result = result

    @staticmethod
    def count_fail_students(students):
        return len([student for student in students if student.result == 'FAIL'])
    

# Example usage:
students = [
    Student('hi', 'helo', 'CS', 2020, 'PASS'),
    Student('just', 'kidding', 'CS', 2020, 'FAIL'),
    Student('no', 'never', 'CS', 2020, 'PASS'),
    Student('workin', 'progress', 'CS', 2020, 'FAIL'),
]

num_fail_students = Student.count_fail_students(students)
print(f'Number of FAIL students: {num_fail_students}')

'''
Number of FAIL students: 2
'''
