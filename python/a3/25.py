# 25. Write a Python function to sort a list of strings in alphabetical order.

def sort_strings(mylist):
    mylist.sort()
    return mylist

# Example usage:
mylist = ["whatsup", "hi", "Runner", "run"]

print(sort_strings(mylist))

'''
['Runner', 'hi', 'run', 'whatsup']
'''