# 3. Write a Python function to remove duplicate characters from a string.
def remove_duplicates(input_string):
    return ''.join(set(input_string))

# Test the function
print("Non Duplicates: ", remove_duplicates(input("Enter String: ")))

'''
Enter String: hihi
Non Duplicates:  hi
'''