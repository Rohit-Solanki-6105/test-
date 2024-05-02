# 15) Write a python program to find lcm.
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def lcm(x, y):
   lcm = (x*y)/gcd(x,y)
   return lcm

n1 = 20
n2 = 25

l = lcm(n1, n2)
print(l)

'''
575.0
'''