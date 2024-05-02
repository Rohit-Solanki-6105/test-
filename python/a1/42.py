# 42) Write a python program to display downward triangle pattern of stars

def downward_triangle(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

# Input number of rows
rows = int(input("Enter the number of rows: "))
downward_triangle(rows)

'''
Enter the number of rows: 5
* * * * *
* * * *
* * *
* *
*
'''