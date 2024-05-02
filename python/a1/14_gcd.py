# 14) Write a python program to find gcd.?
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

num1 = 54
num2 = 24
val = gcd(num1, num2)

print(val)

'''
6
'''