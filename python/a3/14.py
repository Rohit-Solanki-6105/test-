# 14. Write a Python function to extract alternate elements from a given list using slicing.

def alter(lst, start = 0):
    return lst[start::2]

l1 = [1, 2, 3, 56, 12]

print(alter(l1, 1))
print(alter(l1, 0))

'''
[2, 56]
[1, 3, 12]
'''