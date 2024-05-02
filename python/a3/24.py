# 24. Write a Python function to generate a list of squares of numbers from 1 to N using list comprehension.

def generate_squares(n):
    return [i**2 for i in range(1, n+1)]

print(generate_squares(3))
print(generate_squares(7))

'''
[1, 4, 9]
[1, 4, 9, 16, 25, 36, 49]
'''