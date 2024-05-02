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