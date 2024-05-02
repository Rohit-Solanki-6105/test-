# 22. Write a Python function to remove duplicates from a list.
# 23. Write a Python function to remove duplicates from a list.

def remove_duplicates(input_list):
    result = []
    for element in input_list:
        if element not in result:
            result.append(element)
    return result

l1 = [1, 1, 2, 3, 4, 5, 5, 5]

print(remove_duplicates(l1))

'''
[1, 2, 3, 4, 5]
'''