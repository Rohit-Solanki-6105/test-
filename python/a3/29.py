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