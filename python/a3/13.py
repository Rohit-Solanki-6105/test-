# 13. Write a Python function to extract a sublist from a given list using slicing.
def sublist(lst, start = 0, end = 0):
    end+=1
    return lst[start:end]

l1 = [1, 2, 3, 4, 10]

print(sublist(l1, 1, 2))

'''
[2, 3]
'''