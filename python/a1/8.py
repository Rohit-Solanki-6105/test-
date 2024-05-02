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