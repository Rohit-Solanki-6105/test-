# 9. Write a Python function to swap the case of each character in a given string.
def swap_case(s):
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

print("Case Swapped: ", swap_case(input("Enter String: "))) 

'''
Enter String: hiHeLo
Case Swapped:  HIhElO
'''