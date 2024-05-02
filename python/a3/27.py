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