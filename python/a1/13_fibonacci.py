# 13) Write a python program to display fibonacci series. (eg. 0, 1, 1, 2, 3, 5, 8, 13, …)?

def fibonacci(num):
    series = []
    n1 = 0
    n2 = 1
    next_num = n2
    for i in range(num):
        series.append(next_num)
        n1 = n2
        n2 = next_num
        next_num = n1+n2

    return series

print(fibonacci(10))

'''
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''