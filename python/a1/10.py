# 10) Write a python program to check leap year.
def is_leap(year):
    if year % 4 == 0:
        return True

    return False

print(is_leap(2020))
print(is_leap(2001))

'''
True
False
'''