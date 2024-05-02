# 25) Write a python program to display factors of a number.?
def factors(x):
   for i in range(1, x):
       if x % i == 0:
           print(i)


factors(10)

'''
1
2
5
'''