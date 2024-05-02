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