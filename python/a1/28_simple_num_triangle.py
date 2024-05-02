# 28) Write a python program to display Simple Number Triangle Pattern

def num_triangle(num):
    len = 1
    for i in range(1,num+1):
        s = str(i)
        print(" "*(num-i),s*(len))
        len = 2*i+1

num_triangle(5)

'''
     1
    222
   33333
  4444444
 555555555
 '''