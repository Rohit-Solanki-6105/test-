# 11) Write a python program to find factorial.

def fectorial(num):
    # print(num)
    fect = 1
    for i in range(1, num + 1):
        fect *= i

    return fect

print(fectorial(int(input("Enter num for fectorial: "))))

'''
Enter num for fectorial: 6
720
'''