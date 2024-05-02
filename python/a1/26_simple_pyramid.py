# 26) Write a python programs to create pyramid and pattern.
def pyramid(num):
    for i in range(1,num+1):
        print("*"*(i))

pyramid(int(input("Enter height: ")))

'''
Enter height: 5
*
**
***
****
*****
'''