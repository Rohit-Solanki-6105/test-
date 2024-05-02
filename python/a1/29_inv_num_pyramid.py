# 29) Write a python program to display inverted pyramid of numbers

def num_triangle(num):
  len = num*2-1
  for i in range(1, num+1):  
    s = str(i)
    print(" "*(i), s*(len))
    # print(s)
    len-=2


num_triangle(5)

'''
  111111111
   2222222
    33333
     444
      5
'''