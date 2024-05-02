# 30) Write a python program to display inverted pyramid of descending numbers

def num_triangle(num):
  spaces = 0
  for i in range(num, 0, -1):  
    s = str(i)
    print(" " * spaces, s*(i*2-1))
    spaces += 1

num_triangle(5)

'''
 555555555
  4444444
   33333
    222
     1
     
'''