# 21. Write a Python function to calculate the sum of all elements in a list.
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

l1 = [ 1, 2, 3, 4, 5]
print(sum_list(l1))

'''
15
'''