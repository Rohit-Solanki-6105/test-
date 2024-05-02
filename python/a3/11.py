# 11. Write a Python function to extract even and odd indexed elements from a given list using slicing.

def extract_even_odd_index(lst):
    return  lst[::2], lst[1::2]

l = [1, 2, 4, 6, 8, 10]
print(extract_even_odd_index(l))

'''
([1, 4, 8], [2, 6, 10])
'''