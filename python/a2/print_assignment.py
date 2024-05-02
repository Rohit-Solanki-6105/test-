Name  = Solanki Rohit Hareshbhai
Roll = 106
Subject = Python Assignment
Course = Msc CS sem 4 - batch 2


#_____________________________________________________________
# Assignment 1
#____________________________________________________________

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


#_____________________________________________________________
# Assignment 2
#____________________________________________________________
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
10. Write a python program to handle the ZeroDivisionError exception.
'''

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


divide_numbers(10, 0)

divide_numbers(20, 5)

'''
Error: Division by zero is not allowed.
Result of division: 4.0
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
-------------------------------------------------------

'''
3. Define class Surface_Area which includes three methods with the name Calculate_area() 
(Function Overloading). Each method accepts parameter(s) to calculate area of circle, 
rectangle and triangle. Display the result from calling of respective Calculate_area() as per 
the user’s request. Design the menu-driven program.
'''

# class Surface_Area:

#     def Calculate_area(self, length, breadth):
#         return length * breadth

#     def Calculate_area(self, base, height, default=1):
#         return 0.5 * base * height
    
#     def Calculate_area(self, radius):
#         return 3.14 * radius ** 2


class Surface_Area:

    def Calculate_area(self, *args):
        if len(args) == 1:
            # Calculate area of circle (args[0] = radius)
            radius = args[0]
            return 3.14 * radius ** 2
        elif len(args) == 2:
            # Calculate area of rectangle (args[0] = length, args[1] = breadth)
            length, breadth = args
            return length * breadth
        elif len(args) == 3:
            # Calculate area of triangle (args[0] = base, args[1] = height, args[2] = default)
            base, height, _ = args  # Ignore the third argument (default)
            return 0.5 * base * height
        else:
            raise ValueError("Invalid number of arguments")

def main():
    surface_area = Surface_Area()
    while True:
        print("-----------------------------------")
        print("1. Calculate area of circle")
        print("2. Calculate area of rectangle")
        print("3. Calculate area of triangle")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        print("-----------------------------------")
        if choice == 1:
            radius = float(input("Enter radius: "))
            print("Area of circle:", surface_area.Calculate_area(radius))
        elif choice == 2:
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            print("Area of rectangle:", surface_area.Calculate_area(length, breadth))
        elif choice == 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area of triangle:", surface_area.Calculate_area(base, height, 1))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

main()

'''
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 1
-----------------------------------
Enter radius: 2
Area of circle: 12.56
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 2
-----------------------------------
Enter length: 2
Enter breadth: 3
Area of rectangle: 6.0
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 3
-----------------------------------
Enter base: 5
Enter height: 6
Area of triangle: 15.0
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 4
-----------------------------------
'''
-------------------------------------------------------

'''
4. Write a python program to create employee class that has employee details (id, name, 
salary) and design a function that reads the employee id from the user and display employee 
details along with the Net salary after adding DA(15%), MA(5%), HRA(20%) and deducting 
PA(12%) from the basic salary.
'''

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_net_salary(self):
        # Constants for percentage values
        da_percent = 15
        ma_percent = 5
        hra_percent = 20
        pa_percent = 12

        # Calculate allowances and deductions
        da_amount = (da_percent / 100) * self.salary
        ma_amount = (ma_percent / 100) * self.salary
        hra_amount = (hra_percent / 100) * self.salary
        pa_amount = (pa_percent / 100) * self.salary

        # Calculate net salary
        net_salary = self.salary + da_amount + ma_amount + hra_amount - pa_amount

        # Display employee details and net salary
        print("\nEmployee Details:")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.salary)
        print("DA (15%):", da_amount)
        print("MA (5%):", ma_amount)
        print("HRA (20%):", hra_amount)
        print("PA (12%):", pa_amount)
        print("Net Salary:", net_salary)



# Create an employee object
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))

employee = Employee(emp_id, name, salary)

# Calculate and display net salary
employee.calculate_net_salary()

'''
Enter Employee ID: 1
Enter Employee Name: hi
Enter Basic Salary: 100

Employee Details:
Employee ID: 1
Name: hi
Basic Salary: 100.0
DA (15%): 15.0
MA (5%): 5.0
HRA (20%): 20.0
PA (12%): 12.0
Net Salary: 128.0
'''
-------------------------------------------------------

'''
5. Write a python program to overload the multiplication (*) operator that can act on objects 
of NUM class having two members as no1 and no2.
'''
class Num:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def __mul__(self, other):
        # Define the behavior of the multiplication operator (*) with Num objects
        if isinstance(other, Num):
            # If 'other' is also an instance of Num, perform element-wise multiplication
            return Num(self.no1 * other.no1, self.no2 * other.no2)
        elif isinstance(other, (int, float)):
            # If 'other' is a scalar (int or float), multiply each element by the scalar
            return Num(self.no1 * other, self.no2 * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Num' and '{type(other).__name__}'")

    def __rmul__(self, other):
        # Define the behavior when the left-hand operand is a scalar and the right-hand operand is a Num object
        if isinstance(other, (int, float)):
            return Num(self.no1 * other, self.no2 * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: '{type(other).__name__}' and 'Num'")

    def __str__(self):
        # Define how the object should be represented as a string
        return f"Num({self.no1 * self.no2})"


num1 = Num(2, 3)
num2 = Num(4, 5)

result1 = num1 * num2
print("Multiplication of num1 and num2:", result1)

result2 = num1 * 2
print("Multiplication of num1 with scalar:", result2)

result3 = 3 * num2
print("Multiplication of scalar with num2:", result3)

'''
Multiplication of num1 and num2: Num(120)
Multiplication of num1 with scalar: Num(24)
Multiplication of scalar with num2: Num(180)
'''
-------------------------------------------------------

'''
6. Write a python program to create class time with attributes hour and minutes. Add 
constructor(s) to initialize the attributes. Overload '+' operator to add two time (hh:mm) 
type objects to show new added time.
'''

class Time:
    def __init__(self, hour=0, minutes=0):
        self.hour = hour
        self.minutes = minutes

    def __add__(self, other):
        # Check if 'other' is also a Time object
        if isinstance(other, Time):
            # Calculate total minutes
            total_minutes = self.minutes + other.minutes
            carry_hour = total_minutes // 60  # Calculate hours to carry over
            final_minutes = total_minutes % 60  # Calculate final minutes after carrying over

            # Calculate total hours
            total_hours = self.hour + other.hour + carry_hour

            return Time(total_hours, final_minutes)
        else:
            # Raise TypeError if 'other' is not a Time object
            raise TypeError("Unsupported operand type(s) for +: 'Time' and '{}'".format(type(other).__name__))

    def __str__(self):
        # Format the time as hh:mm
        return f"{self.hour:02}:{self.minutes:02}"


time1 = Time(3, 45)
time2 = Time(1, 30)

# Adding two Time objects using the '+' operator
result_time = time1 + time2
print("Sum of time1 and time2:", result_time)

'''
Sum of time1 and time2: 05:15
'''

-------------------------------------------------------

'''
7. Creating a Bank Account Class with Inheritance
    >   Define a base class Account with attributes like account_no (string) and balance 
        (float). Implement constructor method in Account to initialize these attributes.
    >   Create a subclass BankAccount that inherits from Account. 
    >   Add a method called deposit(amount) to BankAccount to add funds to the balance.
    >   Optionally, you can add a withdraw(amount) method that subtracts funds from the 
        balance while considering overdraft protection (if applicable).
'''

class Account:
    def __init__(self, account_no, balance=0.0):
        self.account_no = account_no
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_no}, Balance: Rs.{self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount:.2f} into account {self.account_no}. New balance: Rs.{self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew Rs.{amount:.2f} from account {self.account_no}. New balance: Rs.{self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal amount exceeds available balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


class BankAccount(Account):
    def __init__(self, account_no, balance=0.0):
        super().__init__(account_no, balance)

    # Override the withdraw method to include overdraft protection
    def withdraw(self, amount):
        overdraft_limit = 100.0  # Define overdraft protection limit

        if amount > 0:
            if self.balance + overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrew Rs.{amount:.2f} from account {self.account_no}. New balance: Rs.{self.balance:.2f}")
            else:
                print("Withdrawal amount exceeds available balance including overdraft protection.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


bank_account = BankAccount("123456789", 100.0)

print(bank_account)

bank_account.deposit(500.0)

bank_account.withdraw(300.0)

bank_account.withdraw(500.0)

bank_account.withdraw(-50.0)

'''
Account Number: 123456789, Balance: Rs.100.00
Deposited Rs.500.00 into account 123456789. New balance: Rs.600.00
Withdrew Rs.300.00 from account 123456789. New balance: Rs.300.00
Withdrawal amount exceeds available balance including overdraft protection.
Invalid withdrawal amount. Please enter a positive value.
'''
-------------------------------------------------------

'''
8. Write a python program to create a CAR abstract class that contains an instance variable, a 
concrete method and two abstract methods. Also derive Maruti sub class from the CAR 
class and show implementation of abstract methods of CAR in subclass.
'''

from abc import ABC, abstractmethod

# Define abstract base class Car
class Car(ABC):
    def __init__(self, model):
        self.model = model

    # Concrete method
    def show_model(self):
        print(f"Car Model: {self.model}")

    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Define subclass Maruti that inherits from Car
class Maruti(Car):
    def __init__(self, model):
        super().__init__(model)

    # Implementation of abstract method start
    def start(self):
        print(f"{self.model} car started.")

    # Implementation of abstract method stop
    def stop(self):
        print(f"{self.model} car stopped.")


maruti_car = Maruti("Swift")

maruti_car.show_model()

maruti_car.start()
maruti_car.stop()

'''
Car Model: Swift
Swift car started.
Swift car stopped.
'''
-------------------------------------------------------

'''
9. Create an interface Shape with methods area() and perimeter().
'''
from abc import ABC, abstractmethod

# Define abstract base class Shape with abstract methods area() and perimeter()
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Example usage with a concrete subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2  # Calculate area of circle

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Calculate perimeter (circumference) of circle

# Example usage with a concrete subclass Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Calculate area of rectangle

    def perimeter(self):
        return 2 * (self.length + self.width)  # Calculate perimeter of rectangle

circle = Circle(5)
print("Circle - Area:", circle.area())
print("Circle - Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.area())
print("Rectangle - Perimeter:", rectangle.perimeter())

'''
Circle - Area: 78.5
Circle - Perimeter: 31.400000000000002
Rectangle - Area: 24
Rectangle - Perimeter: 20
'''
-------------------------------------------------------


#_____________________________________________________________
# Assignment 3
#____________________________________________________________
# 1. Write a Python function to read and reverse a string.

def reverse_str(s):
    return s[::-1]
string = input("Enter string: ")
print(reverse_str(string))

'''
Enter string: hihelo
olehih
'''
-------------------------------------------------------

# 2. Write a Python function to count the number of vowels in a given string

def vowel_counter(string):
    counter = 0
    for c in string:
        for vowel in "aeiouAEIOU":
            if c == vowel: 
                counter+=1
    
    return counter

string = input("Enter string: ")

print(f"Total vowels: {vowel_counter(string)}")

'''
Enter string: hihElo
Total vowels: 3
'''
-------------------------------------------------------

# 3. Write a Python function to remove duplicate characters from a string.
def remove_duplicates(input_string):
    return ''.join(set(input_string))

# Test the function
print("Non Duplicates: ", remove_duplicates(input("Enter String: ")))

'''
Enter String: hihi
Non Duplicates:  hi
'''
-------------------------------------------------------

# 4. Write a Python function to check if a given string is a palindrome.
def is_palindrome(s = ""):
    return s == s[::-1]

print("Palindrome: ", is_palindrome(input("Enter string: ")))

'''
Enter string: hi
Palindrome:  False
__________________________
Enter string: racecar
Palindrome:  True
'''
-------------------------------------------------------

# 5. Write a Python function to count the number of words in a given string.

def count_words(s):
    return len(s.split())

print("Total words: ", count_words(input("Enter String: ")))

'''
Enter String: hi helo
Total words:  2
'''
-------------------------------------------------------

# 6. Write a Python function to convert a CamelCase string to snake_case.

def camel_to_snake(camel_case_string):
   snake_case_string = ""
   for i, c in enumerate(camel_case_string):
      if i == 0:
         snake_case_string += c.lower()
      elif c.isupper():
         snake_case_string += "_" + c.lower()
      else:
         snake_case_string += c

   return snake_case_string


print("snake_case: ", camel_to_snake(input("Enter CamelCase: ")))

'''
Enter CamelCase: hiHelo
snake_case:  hi_helo
'''
-------------------------------------------------------

# 7. Write a Python function to convert the first letter of each word to uppercase in a given string.
def convert_to_title_case(s):
    return s.title()

print(convert_to_title_case(input("Enter a sentence: ")))

'''
Enter a sentence: hi helo
Hi Helo
'''
-------------------------------------------------------

# 8. Write a Python function to count the frequency of a substring within a string.

def freq_sub(sub, string):
    counter = 0
    for i in range(len(string) - len(sub)):
        if sub == string[i:i+len(sub)]:
            counter += 1

    return counter

string = input("Enter String: ")
substr = input("Enter substring: ")

print("Total frequency: ", freq_sub(substr, string))

'''
Enter String: hi hihelo whatsup
Enter substring: hi
Total frequency:  2
'''
-------------------------------------------------------

# 9. Write a Python function to swap the case of each character in a given string.
def swap_case(s):
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

print("Case Swapped: ", swap_case(input("Enter String: "))) 

'''
Enter String: hiHeLo
Case Swapped:  HIhElO
'''

-------------------------------------------------------

# 10. Write a Python function to remove all whitespace characters from a given string.

def remove_whitespace(input_string):
    return ''.join(input_string.split())

print("space removed: ", remove_whitespace(input("Enter String: ")))

'''
Enter String: hi helo     whatsup
space removed:  hihelowhatsup
'''
-------------------------------------------------------

# 11. Write a Python function to extract even and odd indexed elements from a given list using slicing.

def extract_even_odd_index(lst):
    return  lst[::2], lst[1::2]

l = [1, 2, 4, 6, 8, 10]
print(extract_even_odd_index(l))

'''
([1, 4, 8], [2, 6, 10])
'''
-------------------------------------------------------

# 12. Write a Python function to reverse a given list using slicing.

def reverse_list(lst):
    return lst[::-1]

l = [1, 2, 3]
print(reverse_list(l))
-------------------------------------------------------

# 13. Write a Python function to extract a sublist from a given list using slicing.
def sublist(lst, start = 0, end = 0):
    end+=1
    return lst[start:end]

l1 = [1, 2, 3, 4, 10]

print(sublist(l1, 1, 2))

'''
[2, 3]
'''
-------------------------------------------------------

# 14. Write a Python function to extract alternate elements from a given list using slicing.

def alter(lst, start = 0):
    return lst[start::2]

l1 = [1, 2, 3, 56, 12]

print(alter(l1, 1))
print(alter(l1, 0))

'''
[2, 56]
[1, 3, 12]
'''
-------------------------------------------------------

# 15. Write a Python function to replace a sublist within a list with another sublist using slicing.
def replace_sublist(list_item, start, end, new_list):
    list_item[start:end] = new_list
    return list_item

list_item = [1, 2, 3, 4, 5, 6]
new_list = [7, 8, 9]
updated_list = replace_sublist(list_item, 2, 5, new_list)

print(updated_list)

'''
[1, 2, 7, 8, 9, 6]
'''
-------------------------------------------------------

# 16. Write a Python function to compute the factorial of a given number recursively.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(6))

'''
120
720
'''
-------------------------------------------------------

# 19. Write a Python function to generate the Fibonacci sequence up to a specified number of terms
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Test the function
print(fibonacci(10))
print(fibonacci(12))

'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''
-------------------------------------------------------

# 20. Write a Python function to convert temperature from Celsius to Fahrenheit and vice versa.
def convert_temperature(temperature, from_scale, to_scale):
    if from_scale == "C" and to_scale == "F":
        return (temperature * 9/5) + 32
    elif from_scale == "F" and to_scale == "C":
        return (temperature - 32) * 5/9
    else:
        return "Invalid scale. Please use 'Celsius' or 'Fahrenheit'."

# Example usage:
print(convert_temperature(43, "C", "F"))
print(convert_temperature(68, "F", "C"))

'''
109.4
20.0
'''
-------------------------------------------------------

# 21. Write a Python function to calculate the sum of all elements in a list.
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

l1 = [ 1, 2, 3, 4, 5]
print(sum_list(l1))

'''
15
'''
-------------------------------------------------------

# 22. Write a Python function to remove duplicates from a list.
# 23. Write a Python function to remove duplicates from a list.

def remove_duplicates(input_list):
    result = []
    for element in input_list:
        if element not in result:
            result.append(element)
    return result

l1 = [1, 1, 2, 3, 4, 5, 5, 5]

print(remove_duplicates(l1))

'''
[1, 2, 3, 4, 5]
'''
-------------------------------------------------------

# 24. Write a Python function to generate a list of squares of numbers from 1 to N using list comprehension.

def generate_squares(n):
    return [i**2 for i in range(1, n+1)]

print(generate_squares(3))
print(generate_squares(7))

'''
[1, 4, 9]
[1, 4, 9, 16, 25, 36, 49]
'''
-------------------------------------------------------

# 25. Write a Python function to sort a list of strings in alphabetical order.

def sort_strings(mylist):
    mylist.sort()
    return mylist

# Example usage:
mylist = ["whatsup", "hi", "Runner", "run"]

print(sort_strings(mylist))

'''
['Runner', 'hi', 'run', 'whatsup']
'''
-------------------------------------------------------

# 26. Write a Python function to merge two dictionaries.
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

# Example usage:
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(merge_dictionaries(d1, d2))

'''
{'a': 1, 'b': 3, 'c': 4}
'''
-------------------------------------------------------

# 27. Write a Python function to access the value associated with a given key in a dictionary.

def get_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return "Key not found in the dictionary"
    
d = {'key1': 1, 'key2': 2, 'key3': 3}
print(get_value(d, 'key1')) 
print(get_value(d, 'key4')) 

'''
1
Key not found in the dictionary
'''
-------------------------------------------------------

# 28. Write a Python function to get all keys from a dictionary.
def get_all_keys(dictionary):
    return list(dictionary.keys())

# Example usage:
d = {'name': 'Rohit', 'age': 19, 'city': 'Ahmedabad'}

print(get_all_keys(d))

'''
['name', 'age', 'city']
'''
-------------------------------------------------------

# 29. Write a Python function to update a dictionary with key-value pairs from another dictionary
def update_dictionary(d1, d2):
    for key, value in d2.items():
        d1[key] = value

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
update_dictionary(d1, d2)
print(d1)

'''
{'a': 1, 'b': 3, 'c': 4}
'''

-------------------------------------------------------

# 30. Write a Python function to create a dictionary with keys as numbers from 1 to N and values as squares of the keys

def create_dictionary(n):
    return {i: i**2 for i in range(1, n+1)}

# Test the function
print(create_dictionary(5))

'''
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
