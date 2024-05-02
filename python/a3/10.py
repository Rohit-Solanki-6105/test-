# 10. Write a Python function to remove all whitespace characters from a given string.

def remove_whitespace(input_string):
    return ''.join(input_string.split())

print("space removed: ", remove_whitespace(input("Enter String: ")))

'''
Enter String: hi helo     whatsup
space removed:  hihelowhatsup
'''