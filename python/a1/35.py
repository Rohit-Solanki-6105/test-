# 35) Write a python program to display reverse pattern of digits from 10

def reverse_pattern_digits():
    num = 10
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(num, end=' ')
            num -= 1
        print()

# Example usage
reverse_pattern_digits()

'''
10 9 8 7 
6 5 4
3 2
1
'''