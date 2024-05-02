# 30. Write a Python function to create a dictionary with keys as numbers from 1 to N and values as squares of the keys

def create_dictionary(n):
    return {i: i**2 for i in range(1, n+1)}

# Test the function
print(create_dictionary(5))

'''
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''