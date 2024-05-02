# 21) Write a python program to check whether a number is prime or not.
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(21))
print(is_prime(22))
print(is_prime(23))

'''
False
False
True
'''