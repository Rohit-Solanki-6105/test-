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