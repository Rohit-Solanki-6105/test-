# 44) Write a python program to display hourglass pattern program

def HourGlass(num):
    
    for i in range(num+1, 1, -1):
        print(" "*(num-i+1), "*"*(2*i-1))
        
    for i in range(num+1):
        print(" "*(num-i), "*"*(2*i+1))
        # print(" "*(num-i),f"{i}"*(i))
    
HourGlass(5)

'''
 ***********
  *********
   *******
    *****
     ***
      *
     ***
    *****
   *******
  *********
 ***********
 '''
