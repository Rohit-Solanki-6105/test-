# 20) Write a python program to check whether a number is palindrome or not.?
def is_palindrome(n):
    return eval(f"{n} == {int(str(n)[::-1])}")

print(is_palindrome(12321))
print(is_palindrome(123))

'''
True
False
'''