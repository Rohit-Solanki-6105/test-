# 9) Write a python program to calculate sum of natural numbers.

def nat_sum(n):
    sum = 0
    for i in range(n):
        sum+=i
    return sum
    
n = int(input("Enter num: "))
print(f"Sum: {nat_sum(n)}")

'''
Enter num: 34
Sum: 561
'''