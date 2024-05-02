# 15. Write a Python function to replace a sublist within a list with another sublist using slicing.
def replace_sublist(list_item, start, end, new_list):
    list_item[start:end] = new_list
    return list_item

list_item = [1, 2, 3, 4, 5, 6]
new_list = [7, 8, 9]
updated_list = replace_sublist(list_item, 2, 5, new_list)

print(updated_list)

'''
[1, 2, 7, 8, 9, 6]
'''