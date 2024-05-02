# 4. Write a Python function to check if a given string is a palindrome.
def is_palindrome(s = ""):
    return s == s[::-1]

print("Palindrome: ", is_palindrome(input("Enter string: ")))

'''
Enter string: hi
Palindrome:  False
__________________________
Enter string: racecar
Palindrome:  True
'''