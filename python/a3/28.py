# 28. Write a Python function to get all keys from a dictionary.
def get_all_keys(dictionary):
    return list(dictionary.keys())

# Example usage:
d = {'name': 'Rohit', 'age': 19, 'city': 'Ahmedabad'}

print(get_all_keys(d))

'''
['name', 'age', 'city']
'''