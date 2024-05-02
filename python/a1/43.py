# 43) Write a python program to display pyramid pattern of stars

def pyramid(rows):
    for i in range(1, rows + 1):
        print(' '*(rows - i),'* '*i)

# Input number of rows
rows = int(input("Enter the number of rows: "))
pyramid(rows)

'''
Enter the number of rows: 5
    *
   * *
  * * *
 * * * *
* * * * *
'''